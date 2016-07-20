#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This first exercise will give brief orientation to SimpleITK 
# This exercise is based on the SimpleITK notebooks
# Your task is to document the different operations

import SimpleITK as sitk

print ( 'SimpleITK Image Basics')

##1- Image Construction
image = sitk.Image(256, 128, 64, sitk.sitkInt16)
image_2D = sitk.Image(64, 64, sitk.sitkFloat32)
image_2D = sitk.Image([32,32], sitk.sitkUInt32)
image_RGB = sitk.Image([128,128], sitk.sitkVectorUInt8, 3)

help ( image )

# 2- Image properties
# Explain the difference between these methods
print ( image.GetDimension() )
print ( image.GetSize() )
print ( image_2D.GetSize() )
print ( image_RGB.GetSize() )

print ( image.GetWidth() )
print ( image.GetHeight() )
print ( image.GetDepth() )

print ( image.GetOrigin() )
print ( image.GetSpacing() )

# 3- Image access
# Explain the difference between the two procedures
# Procedure 1
print ( image.GetPixel ( 0, 0, 0 ) )
image.SetPixel ( 0, 0, 0, 1 )
print ( image.GetPixel ( 0, 0, 0 ) )

# Procedure 2
print ( image[0,0,0])
image[0,0,0] = 10
print ( image[0,0,0])

# 4- I/O operations
# Explain the different steps
# You need to replace these paths with a valid one
in_image="/home/mzuluaga/Dropbox/Summer_School/MR/subject101_ed.nii"
out_image="/home/mzuluaga/Data/dummy_img.nii"
image = sitk.ReadImage( in_image )

print ( image )
sitk.Show ( image )
sitk.WriteImage ( image, out_image)

#5- Operators
#Change the path accordingly to where you have the images
in_image="/home/mzuluaga/Dropbox/Summer_School/2D/cthead1.png"
image = sitk.ReadImage ( in_image )
sitk.Show ( image, "Slice" )

sitk.Show ( 100 + image, "SlicePlus100" )


# 6- Explain each of the steps here executed.
# What is it obtained as an image in anImg?
xImg = sitk.Image( 256, 256, sitk.sitkFloat32 )
yImg = sitk.Image( 256, 256, sitk.sitkFloat32 )

for y in range( 0, xImg.GetSize()[1] ):
    for x in range( 0, xImg.GetSize()[0] ):
        xImg.SetPixel( x, y, x )
        yImg[x, y] = y

sitk.Show ( xImg, "XImage" )
sitk.Show ( yImg, "YImage" )

sigma = 50
xImg = xImg - xImg.GetSize()[0] / 2
yImg = yImg - yImg.GetSize()[1] / 2

anImg = sitk.Exp( -1 * (xImg**2 + yImg**2) / (2.0 * sigma**2) )
sitk.Show ( anImg, "What is this Image?" )


