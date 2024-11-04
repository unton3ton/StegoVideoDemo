# https://pyimagesearch.com/2014/09/15/python-compare-two-images/
# https://habr.com/ru/articles/848990/

# import the necessary packages
from skimage.metrics import structural_similarity as ssim # pip install scikit-image
import matplotlib.pyplot as plt
import numpy as np
import cv2

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def psnr(mse):
	if mse == 0:
		psnr_val = float('inf')
	else:
		psnr_val = 20*np.log10(255/np.sqrt(mse))
	return psnr_val

def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)
	'''
	Алгоритм SSIM (Structural Similarity Index) — один из самых популярных методов для 
	измерения сходства между двумя изображениями. Он учитывает изменения яркости, контраста 
	и структуры. Изображения идентичны, если == 1
	'''
	p = psnr(m)
	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f, PSNR: %.2f" % (m, s, p))
	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")
	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")
	# show the images
	plt.show()

# load the images -- the original, the original + contrast,
# and the original + photoshop
original = cv2.imread("kikicut_wm_25fps/1.png")
contrast = cv2.imread("kikicut/1.png")

# convert the images to grayscale
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)

compare_images(original, original, "Original vs. Original")
compare_images(original, contrast, "Original vs. Contrast")
