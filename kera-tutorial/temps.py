from imutils import paths
import os

imagePaths = sorted(list(paths.list_images('/home/jesse/Downloads/kera-tutorial/animals')))
random.seed(42)
random.shuffle(imagePaths)
labels=[]
data=[]
# loop over the input images
for imagePath in imagePaths:
	# load the image, resize the image to be 32x32 pixels (ignoring
	# aspect ratio), flatten the image into 32x32x3=3072 pixel image
	# into a list, and store the image in the data list
	image = cv2.imread(imagePath)
	image = cv2.resize(image, (32, 32)).flatten()
	data.append(image)
        #t=imagePath.split(os.path.sep)
        #print("Sums: ",t,"\n")
        label = imagePath.split(os.path.sep)[-2]
        print("label: ",label,"\n")
        labels.append(label)
print("\n",labels,"\n")
