from PIL import Image
import os

path = "/Users/jerrypan/Desktop/Research & Internship Project/A-scalable-NFT-Art-Project-by-Indorse/pytorch-CycleGAN-and-pix2pix/results/"

print(os.listdir(path))
modelOutputs = os.listdir(path)

count = 0
outputPath = "/Users/jerrypan/Desktop/Research & Internship Project/A-scalable-NFT-Art-Project-by-Indorse/image-data/GANCroppedBackground/"
for modelOutput in modelOutputs:
    inputPath = path + modelOutput + "/test_latest/images/"
    allImages = os.listdir(inputPath)
    for image in allImages:
        img = Image.open(inputPath + image)
        count += 1
        imgCropped = img.crop((150, 0, 1230, 1380))
        imgCropped.save(outputPath + str(count) + ".png")
        print(count)

print("DONE")
