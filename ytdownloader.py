import yt_dlp
url=input("Enter video Url: ")
download_directory = '/home/edelicat3/Desktop/youtubedownloads'

ydl_opts = {
        'outtmpl' : f'{download_directory}/%(title)s.%(ext)s',
        'format' : 'best'
        }
with yt_dlp.YoutubeDL(ydl_opts)as ydl:
    ydl.download([url])

print("Downloaded  successfully!!!")
