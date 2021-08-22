import hashlib
from PIL import Image
import os
from os import listdir
from os.path import isfile, join
import random
##################### TO CHANGE ###################################################
path = "/Users/jerrypan/Desktop/Research & Internship Project/A-scalable-NFT-Art-Project-by-Indorse/pytorch-CycleGAN-and-pix2pix/image-data/"
##################### TO CHANGE ###################################################

string = "n"
encoded = string.encode()
hashObject = hashlib.sha256(encoded)
hexDigits = hashObject.hexdigest()
hexDigitsInDecimal = int(hexDigits, 16)
print(hexDigits)  # ce76c835a3668e99f680f1b043f09b6bbbb71905e6f2b2079f0dd59daba5002e

img = Image.open(path + "Background/1.png")

width, height = img.size
# print(width, height)

# for x in range(width):
#     for y in range(height):
#         (r, g, b, a) = img.getpixel((x,y))
        # print(r, g, b, a)
        ####################################################################
        # Do your logic here and create a new (R,G,B) tuple called new_color
        ####################################################################
        # img.putpixel( (x,y), (r + 100, g + 100, b + 100))

# encoding
for x in range(0, 64, 8):
    r, g, b, a = int(hexDigits[x:x+2], 16), int(hexDigits[x+2:x+4], 16), int(hexDigits[x+4:x+6], 16), int(hexDigits[x+6:x+8], 16)
    img.putpixel((x, 0), (r, g, b, a))

img.save("/Users/jerrypan/Desktop/Research & Internship Project/A-scalable-NFT-Art-Project-by-Indorse/pytorch-CycleGAN-and-pix2pix/image-data/Background/1_processed.png")


#############################################################################################
# decoding
encoded_img = Image.open("/Users/jerrypan/Desktop/Research & Internship Project/A-scalable-NFT-Art-Project-by-Indorse/pytorch-CycleGAN-and-pix2pix/image-data/Background/1_processed.png")
code = ""
for x in range(0, 64, 8):
    r, g, b, a = encoded_img.getpixel((x, 0))
    hexR = hex(r)[2:] 
    hexG = hex(g)[2:] 
    hexB = hex(b)[2:] 
    hexA = hex(a)[2:]
    if len(hexR) == 1:
        hexR = "0" + hexR 
    if len(hexG) == 1:
        hexG = "0" + hexG
    if len(hexB) == 1:
        hexB = "0" + hexB 
    if len(hexA) == 1:
        hexA = "0" + hexA
    code = code + hexR + hexG + hexB + hexA
# print(code)
#############################################################################################
pathBackgrounds = os.listdir(path + "Background/")
pathFrames = os.listdir(path + "Frames/")
pathProducts = os.listdir(path + "Product/")

backgroundNum = random.choice(pathBackgrounds)
productNum = random.choice(pathProducts)
######################################################################
# Common/Rare/Epic/LegendaryLegendary
ledendaryProb = 0.03
epicProb = 0.10 + ledendaryProb
rareProb = 0.30 + epicProb

if (hexDigitsInDecimal % 100) / 100 <= ledendaryProb:
    frameNum = "4-Legendary.png"
elif (hexDigitsInDecimal % 100) / 100 <= epicProb:
    frameNum = "3-Epic.png"
elif (hexDigitsInDecimal % 100) / 100 <= rareProb:
    frameNum = "2-Rare.png"
else:
    frameNum = "1-Common.png"
######################################################################
backgroundImg = Image.open(path + "Background/" + str(backgroundNum))
frameImg = Image.open(path + "Frames/" + frameNum)
productImg = Image.open(path + "Product/" + productNum + "/product.png")
textImg = Image.open(path + "Product/" + productNum + "/" + frameNum[0] + ".png")


area = (0, 0, 1080, 1380)
backgroundImg.paste(productImg, (0, 0), productImg)
backgroundImg.paste(frameImg, (0, 0), frameImg)
backgroundImg.paste(textImg, (0, 0), textImg)

backgroundImg.save(path + "Outputs/" + str(hexDigits) + ".png")