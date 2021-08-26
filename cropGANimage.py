from PIL import Image
import os

path = "/Users/jerrypan/Desktop/Research & Internship Project/A-scalable-NFT-Art-Project-by-Indorse/pytorch-CycleGAN-and-pix2pix/results/"
styleTextPath = "/Users/jerrypan/Desktop/Research & Internship Project/A-scalable-NFT-Art-Project-by-Indorse/pytorch-CycleGAN-and-pix2pix/image-data/styleText/"
print(os.listdir(path))
modelOutputs = os.listdir(path)
styles = ["style_cezanne", "style_monet", "style_ukiyoe"]
count = 0
outputPath = "/Users/jerrypan/Desktop/Research & Internship Project/A-scalable-NFT-Art-Project-by-Indorse/image-data/GANCroppedBackground/"
for modelOutput in modelOutputs:
    if modelOutput not in styles:
        continue
    inputPath = path + modelOutput + "/test_latest/images/"
    allImages = os.listdir(inputPath)
    for image in allImages:
        img = Image.open(inputPath + image)
        count += 1
        # imgCropped = img.crop((150, 0, 1230, 1380))
        imgCropped = img.resize((1080, 1380))
        styleText = Image.open(styleTextPath + modelOutput + ".png")
        imgCropped.paste(styleText, (0, 0), styleText)
        imgCropped.save(outputPath + modelOutput + str(count) + ".png")
        print(count)

print("DONE")
