import os
from glob import glob

def split_video(input_file, output_prefix, duration):
    os.system(f"ffmpeg -i {input_file} -f segment -vcodec copy -reset_timestamps 1 -segment_time {duration} {output_prefix}%03d.mp4")
    
filenames = glob("/data/public/BrightEyes.mp4")

for container in filenames:
    split_video(f"{container}", f"/data/public/videowatermark-dct-dwt-java_jar/videos/{container[13:-4]}_", 10)