# https://github.com/mightymoogle/StegoVideoDemo

# python3 runjava.py -p embed -m base
# python3 runjava.py -p extract -m base
# python3 runjava.py -p psnr -m base

# python3 runjava.py -p embed -m random
 

'''
python3 runjava.py -h
usage: runjava.py [-h] -p PROCESS -m MODE

Пример использования консольного интерфейса

options:
  -h, --help            show this help message and exit
  -p PROCESS, --process PROCESS
                        embed , extract or psnr
  -m MODE, --mode MODE  base or random
'''

import os
import argparse
from glob import glob
from random import choice

parser = argparse.ArgumentParser(description="Пример использования консольного интерфейса")
parser.add_argument("-p", "--process", help="embed , extract or psnr", required=True)
parser.add_argument("-m", "--mode", help="base or random", required=True)

args = parser.parse_args()
 
process = args.process
mode = args.mode


if mode == "base":
    catalogin = catalogout = catalogwm = "samples"

    videoin = "riga.mp4"
    videoout = "riga_encoded.mp4"

    watermarkimg = "mark_logo.bmp"
    extractwatermark = "result.png"

    algorithms = [1, # Embedding strength - this controls how well the watermark is embedded during the DCT transformation. Larger number leads to a more robust watermark, but will most likely be more visible and may result in a lower PSNR. The value depends on the algorithm selected and on the video container used.
                  2, # Compression - this controls how much the image gets compressed. We recommend keeping it at 0 for minimum additional compression. 2 attacks support compression of the video stream.
                  3, # Block size - this controls the block size of the DCT transformation. We recommend keeping it at 8.
                  4] # Adaptive mode - this enables the Adaptive mode described in the article in the introduction. It embeds based on the movement in the video and ignores monotone images. Please note - implementation is very slow and basic. Only Kaur and Kothari algorithms supported.

    algorithm = algorithms[0]

    if process == "embed":
        os.system(f"java -jar StegoVideo.jar embed -c {videoin} -o {videoout} -w {watermarkimg} -a {algorithm}")
    elif process == "extract":
        os.system(f"java -jar StegoVideo.jar extract -s {videoout} -o extractwms/{extractwatermark} -width 90 -height 90 -a {algorithm}")
    else:
        os.system(f"java -jar StegoVideo.jar psnr -c {videoin} -s {videoout}")

elif mode == "random":
    catalogin = "videos"
    catalogout = "videoswithwm"
    catalogwm = "imageswatermarks"
    algorithms = [1, 2, 3, 4]
    watermarkimages = glob(f'{catalogwm}/*')
    videos = glob(f'{catalogin}/*'); print(videos)
    for videoin in videos:
        #print(videoin)
        videoout = f"{catalogout}/{videoin[len(catalogin)+1:-4]}_encoded.{videoin[-3:]}"; print(videoout)

        watermarkimg = choice(watermarkimages); print(watermarkimg)

        extractwatermark = f'{watermarkimg[len(catalogwm)+1:-4]}_from_{videoout[len(catalogout)+1:-4]}.bmp'; print(extractwatermark)

        algorithm = 1 # choice(algorithms); print(algorithm)

        if process == "embed":
            os.system(f"java -jar StegoVideo.jar embed -c {videoin} -o {videoout} -w {watermarkimg} -a {algorithm}")
            os.system(f"java -jar StegoVideo.jar extract -s {videoout} -o extractwms/{extractwatermark} -width 90 -height 90 -a {algorithm}")
        elif process == "extract":
            os.system(f"java -jar StegoVideo.jar extract -s {videoout} -o extractwms/{extractwatermark} -width 90 -height 90 -a {algorithm}")
        else:
            os.system(f"java -jar StegoVideo.jar psnr -c {videoin} -s {videoout}")

else:
    print("I need mode's parameter")