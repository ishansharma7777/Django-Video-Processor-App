import subprocess

def extract_subtitles(video_path, output_path):
    command = [
        'ffmpeg', '-i', video_path, '-map', '0:s:0', '-c:s', 'srt', output_path
    ]
    subprocess.run(command, check=True)
