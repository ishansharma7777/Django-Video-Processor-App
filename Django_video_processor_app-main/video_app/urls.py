from django.urls import path
from . import views
from .views import video_player, serve_subtitles
from .views import upload_video
from django.conf import settings
from django.conf.urls.static import static
from .views import video_detail
urlpatterns = [
    path('upload/', upload_video, name='upload_video'),
    
    path('video/<int:video_id>/', video_detail, name='video_detail'),
    path('homepage/',views.homepage,name='homepage' ),
    path('subtitles/<int:video_id>/', serve_subtitles, name='serve_subtitles'),
    path('<int:video_id>/', video_player, name='video_player'),
    path('subtitles/<str:subtitle_filename>/', serve_subtitles, name='serve_subtitles'),
    # path('upload/', views.video_upload, name='video_upload'),
    path('videos/', views.video_list, name='video_list'),
    path('delete/<int:video_id>/', views.delete_video, name='delete_video'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

