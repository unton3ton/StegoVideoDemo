import os
from glob import glob

def rescale_video(input_file, output_prefix):
    os.system(f"ffmpeg -i {input_file} -vf scale=1280:720 {output_prefix}rescale.mp4")
    os.remove(input_file)
    
filenames = glob("/data/public/videowatermark-dct-dwt-java_jar/videos/*.mp4")

for container in filenames:
    rescale_video(f"{container}", f"/data/public/videowatermark-dct-dwt-java_jar/videos/{container[52:-4]}_")