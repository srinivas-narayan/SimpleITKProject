#!/usr/bin/env python
# -*- coding: utf-8 -*-

import SimpleITK as sitk
import argparse

def convert_to_binary_mask( image ):

    #=================== YOUR CODE HERE ==============================
    # Assign 1 to every voxel in the image that is different from 0.
    # Use a simpleITK filter
    
    #=================================================================
    return new_img

def dilate_mask( image ):
    filter = sitk.BinaryDilateImageFilter()
    filter.SetKernelRadius ( 1 ).SetForegroundValue ( 1 )
    dilated = filter.Execute ( image )
    return dilated

def erode_mask( image ):
    #=================== YOUR CODE HERE ==============================
    # Based on the code for dilate_mask, implement this function so
    # that the input image is eroded. Use the same kernel radius.
    
    #=================================================================
    return eroded

def obtain_border( image ):
    #=================== YOUR CODE HERE ==============================
    # Obtain a rough estimate of the border of the masked object
    # by sustracting the eroded mask from the dilated mask
    
    #=================================================================
    return border_img

print 'SimpleITK: Basic filters'

# This lines of code allow to read arguments from the command line
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--img", required=True, help="Input image")
parser.add_argument("-m", "--mask", required=True, help="Mask image")
parser.add_argument("-o", "--out", required=True, help="Output image")
parser.add_argument("-b", "--border", required=True, help="Border image")
args = parser.parse_args()

#1- Reading the original image and displaying it
image = sitk.ReadImage ( args.img )
sitk.Show ( image, "Original image" )

# Smooth filter: A Gaussian filter is applied to the input
# image and it is displayed. Sigma = 2.0
smooth = sitk.SmoothingRecursiveGaussian ( image, 2.0 )
sitk.Show ( smooth, "Gaussian smoothing, sigma 2.0" )

# An alternative way to use the SmoothingRecursiveGaussian
# The image is displayed. New sigma is 4.0
# Can you see any differences in the image?
Gaussian = sitk.SmoothingRecursiveGaussian
smooth = Gaussian ( image, 4. )
sitk.Show ( smooth, "Gaussian smoothing, sigma 4.0" )

#=================== YOUR CODE HERE ==============================
# We want to display the difference between the original
# image and the substracted one. The following piece of
# code tries to do so. However, as you will see when you
# run it, there is an error.
# Your task is towrite the necessary code to fix this
# problem.
# Hint: Run the program and check the displayed error.
# Hint 2: Invesigate the usage of sitk.Cast function

#=================================================================
sitk.Show ( sitk.Subtract ( image, smooth ), "DiffWithGaussian" )

#=================== YOUR CODE HERE ==============================
# In exercise_1, you coded the function convert_to_binary_mask
# through the use of numpy. SimpleITK has a BinaryThreshold
# filter that can do the same.
# Implement convert_to_binary_mask. Read the mask image passed as
# argument and apply convert_to_binary_mask function. Save the
# result to disk into args.out. The results should be the same
# you obtained in exercise_1.

#=================================================================

# =================== YOUR CODE HERE ==============================
# Implement obtain_border to get a rough estimation of the borders
# of the object contained in the previously computed mask.
# Rough borders of an object are usually obtained by sustracting the
# dilated and eroded versions of the original mask. See dilate_mask
# for an example on how to dilate/erode using simpleITK.
# Display the result border image. WARNING: You might need to
# adjust the window/level settings to see the image properly.

#=================================================================
