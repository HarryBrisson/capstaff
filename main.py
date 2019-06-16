

import os

from functions.capstaff import *
from functions.youtube_downloads import *



def create_palette_viz_for_video(vid_id):
	vpath = f'videos/{vid_id}.mp4'
	ipath = f'images/{vid_id}.png'
	download_youtube_video(vid_id)
	create_palette_over_time_visual(vpath, ipath)
	os.remove(vpath)




if __name__ == "__main__":
	vid_id = 'L_jWHffIx5E'
	create_palette_viz_for_video(vid_id)