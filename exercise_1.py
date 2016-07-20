#!/usr/bin/env python
# -*- coding: utf-8 -*-

import SimpleITK as sitk
import numpy as np

import argparse
import math

def compute_mean( arr_one ):
    mean = 0
    all_voxels = arr_one.size

    for voxel in np.nditer(arr_one):
        mean += voxel

    mean /= float(all_voxels)

    return mean

def compute_std( arr_one ):
    variance = 0
    std = 0
    #=================== YOUR CODE HERE ==============================
    # Based on the example to compute the mean, compute the standard
    # deviation of the image intensities

   
    #=================================================================
    std = math.sqrt(variance)
    return std

def compute_mode( arr_one ):
    mode = 0

    # Investigate the role of histogram function
    h, bins = np.histogram( arr_one, bins=255, range=(0,arr_one.max()) )

    #=================== YOUR CODE HERE ==============================
    # Compute the mode by inspecting the image histogram computed in
    # the previous line. Investigate the role of the numpy function
    # histogram.
    
    #=================================================================
    return mode

def compute_volume_per_label( arr_one ):
    volumes = []
    max_label = arr_one.max()

    #Initialise in zero
    for i in range (max_label):
        volumes.append(0)
    #=================== YOUR CODE HERE ==============================
    # Count the number of voxels associated to each of the labels
    # in the image and return these numbers in the array volumes.
    # Do not compute the volume for the background (value=0).
    
    #=================================================================
    return volumes

def compute_mean_max_volume( arr_one, arr_two, val ):
    mean = 0
    count = 0

    for voxels, labels in np.nditer([arr_one,arr_two]):
    #=================== YOUR CODE HERE ====================
        
    #=================================================================

    return mean

def convert_to_binary_mask( arr_one ):
    new_arr = arr_one
    #=================== YOUR CODE HERE ==============================
    # Assign 1 to every voxel in the image that is different from 0.
    
    #=================================================================
    return new_arr

#************************* main section **********************************
print 'SimpleITK: Interaction with numpy'

# This lines of code allow to read arguments from the command line
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--img", required=True, help="Input image")
parser.add_argument("-m", "--mask", required=True, help="Mask image")
parser.add_argument("-o", "--out", required=True, help="Output image")
args = parser.parse_args()

#1- Image reading
image=sitk.ReadImage(args.img)

#=================== YOUR CODE HERE ==============================
# Complete code here to read the mask image.
# Hint: The mask image name is stored in args.mask

#=================================================================

#2- Converting a SimpleITK image object to an array
img_npy = sitk.GetArrayFromImage( image )
help( sitk.GetArrayFromImage )

#=================== YOUR CODE HERE ==============================
# Convert the mask image you read into a numpy array

#================================================================

#3- Compute image statistics - Complete code for std and mode
mean_val=compute_mean( img_npy )
std_val=compute_std( img_npy )
mode_val=compute_mode( img_npy )

#=================== YOUR CODE HERE ==============================
# Compute the volume for each label of the mask image by invoking
# compute_volume_per_label. Note: You should also implement this
# function. Save the result in vol

#================================================================

#=================== YOUR CODE HERE ==============================
# Find the label with the largest volume. Then, implement
# compute_mean_max_volume so that the mean of the region with the
# largest volume is computed.

#================================================================

#=================== IMPLEMENT FUNCTION ==========================
# Implement the function convert_to_binary_mask, to binarise the
# voxels of the mask image, i.e. assign a value of 1 to every
# voxel different from zero.
new_arr = convert_to_binary_mask( mask_npy )
#================================================================

help( sitk.GetImageFromArray )

#=================== YOUR CODE HERE ==============================
# Convert new_arr numpy array to a SimpleITK image and write to disk.
# Hint: The filename of the image to be saved is stored in args.out

#================================================================

#==================== Print out your results =====================
# Print values of mean, std, volumes per label and mean over a
# regio and image info of the new mask. Compare with others to
# validate your results



