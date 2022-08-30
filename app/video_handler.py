from pytube import YouTube

def download_youtube_video(url, video_name):
    video = YouTube(url)
    try:
        video.streams.filter(res='720p', file_extension='mp4', fps=30).first().download(filename=f'./files/videos/{video_name}.mp4')
        return True
    except:
        return False

#OG Vid: https://www.youtube.com/watch?v=zFViSKSOgs0