from django.shortcuts import render, redirect
import os
from django.http import FileResponse, Http404
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import VideoForm
from django.core.files.storage import FileSystemStorage
from .models import VideoUpload
import subprocess
import os
from django.conf import settings
import subprocess




def homepage(request):
    return render(request, 'homepage.html')

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video_instance = form.save()

            # Get the path of the uploaded video
            video_path = os.path.join(settings.MEDIA_ROOT, video_instance.video.name)

            # Define the output subtitle path (VTT format)
            subtitle_dir = os.path.join(settings.MEDIA_ROOT, 'subtitle')
            if not os.path.exists(subtitle_dir):
                os.makedirs(subtitle_dir)  # Create directory if it doesn't exist
            subtitle_path = os.path.join(subtitle_dir, f"{video_instance.title}.vtt")

            # Use ffmpeg to extract subtitles
            ffmpeg_command = f"ffmpeg -i {video_path} -map 0:s:0 {subtitle_path}"
            try:
                subprocess.run(ffmpeg_command, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error extracting subtitles: {e}")

            # Save the subtitle path in the model
            video_instance.subtitle = f"subtitle/{video_instance.title}.vtt"
            video_instance.save()

            return redirect('video_list')
    else:
        form = VideoForm()

    return render(request, 'upload_video.html', {'form': form})



def serve_subtitles(request, subtitle_filename):
    subtitle_path = os.path.join(settings.MEDIA_ROOT, 'subtitles', subtitle_filename)
    return FileResponse(open(subtitle_path, 'rb'), content_type='application/x-subrip')


# def video_detail(request, video_id):
#     video_instance = get_object_or_404(VideoUpload, id=video_id)
#     print(video_instance.subtitle.url)
#     return render(request, 'video_player.html', {'video_instance': video_instance})

def video_player(request, video_id):
    video_instance = VideoUpload.objects.get(id=video_id)
    return render(request, 'video_player.html', {'video_instance': video_instance})




# def video_upload(request):
#     if request.method == 'POST':
#         # handle the uploaded video here
#         pass
#     return render(request, 'upload_video.html')



def video_list(request):
    videos = VideoUpload.objects.exclude(video='')  # Only fetch entries with associated video files
    return render(request, 'video_list.html', {'videos': videos})

def parse_vtt(subtitle_path):
    transcript = []
    with open(subtitle_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        timestamp = None
        text = []

        for line in lines:
            line = line.strip()

            # Check for timestamps (e.g., 00:00:00.000 --> 00:00:02.000)
            if "-->" in line:
                if timestamp and text:
                    transcript.append({"timestamp": timestamp, "text": " ".join(text)})
                timestamp = line.split(" --> ")[0]  # Start time of the subtitle
                text = []
            elif line:
                text.append(line)

        if timestamp and text:
            transcript.append({"timestamp": timestamp, "text": " ".join(text)})
    
    return transcript

def video_detail(request, video_id):
    video_instance = get_object_or_404(VideoUpload, id=video_id)
    
    # Parse subtitles if available
    transcript = []
    if video_instance.subtitle and video_instance.subtitle.path.endswith('.vtt'):
        transcript = parse_vtt(video_instance.subtitle.path)

    return render(request, 'video_player.html', {
        'video_instance': video_instance,
        'transcript': transcript
    })


def delete_video(request, video_id):
    video_instance = get_object_or_404(VideoUpload, id=video_id)
    
    # Delete the video file from the server
    video_path = video_instance.video.path
    if os.path.exists(video_path):
        os.remove(video_path)
    
    # If there's a subtitle file, delete that too
    if video_instance.subtitle:
        subtitle_path = video_instance.subtitle.path
        if os.path.exists(subtitle_path):
            os.remove(subtitle_path)
    
    # Delete the video instance from the database
    video_instance.delete()

    # Redirect back to the video list after deletion
    return redirect('video_list')
