from django import template

register = template.Library()

@register.filter(name='is_mp4')
def is_mp4(video_url):
    return video_url.endswith('.mp4')

@register.filter(name='is_mkv')
def is_mkv(video_url):
    return video_url.endswith('.mkv')
