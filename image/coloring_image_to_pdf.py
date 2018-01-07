#!/usr/bin/python3
# encoding: utf-8

from PIL import Image, ImageOps

# create A4 page
widthA4, heightA4  = int(8.27 * 300), int(11.7 * 300) # A4 at 300dpi
page = Image.new('RGB', (widthA4, heightA4), 'white')

# open image
rawImage = Image.open('01.jpg')

# not working crop
imageBox = ImageOps.invert(rawImage).getbbox()
cropped  = rawImage.crop(imageBox)
widthCro, heightCro = cropped.size

# get aspect ratio
aspRate = min(widthA4/widthCro, heightA4/heightCro)

# get margins
leftOf = int((widthA4-int(aspRate*widthCro))/2)
topOf  = int((heightA4-int(aspRate*heightCro))/2)

# resize image
newImage = cropped.resize((int(aspRate*widthCro), int(aspRate*heightCro)), Image.ANTIALIAS)

# paste and save
page.paste(newImage, box = (leftOf, topOf))
page.save('01.pdf')
