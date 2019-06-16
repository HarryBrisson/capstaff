

import youtube_dl


def download_youtube_video(vid_id):
	ydl_opts = {
	    'format': 'bestvideo[tbr<1000][ext=mp4][vcodec*=avc]',
	    'outtmpl': r'videos/%(id)s.%(ext)s'
	}

	url = f'https://www.youtube.com/watch?v={vid_id}'

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		    ydl.download([url])


