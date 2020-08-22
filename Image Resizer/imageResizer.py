import cv2
import glob
import os


def resizeImage(inputPath, outputPath, height, width, channel = 3, fileExtension = ".jpg"):
	path = inputPath + "*" + fileExtension
	outputPath = outputPath
	s = 0
	f = 0
	for i in glob.glob(path):
		temp = i.split(os.path.sep)[-1]
		fileName = outputPath+temp
		try:
			x = cv2.imread(i,1)
			x = cv2.resize(x,(width,height))
			cv2.imwrite(f'{fileName}',x)
			s+=1
		except:
			f+=1
			print(f"Failed for image -- {temp}")

	print(f"Completed\nTotal: {s}\nFailed: {f}")


if __name__ == "__main__":

	#sample input
	resizeImage(inputPath = "iFolder/", outputPath = "oFolder/", height = 180, width = 100, fileExtension = '.png')

