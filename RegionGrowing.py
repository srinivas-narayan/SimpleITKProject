##############################################
#Region growing segmentation example
##############################################

from matplotlib import pyplot as plt
import SimpleITK as sitk
import numpy as np
import math




###################################
#Main program starts here
##################################

#Read the files
image = sitk.ReadImage('D:\\Ubuntu_VB\\MR\\subject101_ed.nii')
#maskImage = sitk.ReadImage('D:\\Ubuntu_VB\\MR\\subject101_ed_label.nii')

#see image....
sitk.Show(image)


#now smoothen image - using Curvature Flow algorithm
print('starting smoothing....')
imageSmooth = sitk.CurvatureFlow(image1=image,timeStep=0.125,numberOfIterations=5)
print ('Finished Smoothing....')

# sitk_show(sitk.Tile(imageSmooth[:,:,100], image[:,:,100], (2, 1, 0))) #not sure why this does not work!!

# Define segmentation labels
lblLeftVentricle = 255
lblRightVentricle = 128


# now define seeds
# seedThresholdSlices = [(1000, 1443, 140), (1000,1445, 150), (800,1380, 160),(700,1050,180),(740,800,200) ]
# lstSeedLV = [(174,190,50), (174,174,75), (174,200,32)]
# lstSeedRV = [(174,228,64),(174,214,90),(174,230,78)]

lstSeedLV = [(50,135,128), (75,128,128), (32,150,128)]
lstSeedRV = [(64,168,128),(90,160,128),(78,164,128)]

#create a copy of smooth image
imgSeeds = sitk.Image(imageSmooth)
#put seeds on
for s in lstSeedLV:
    imgSeeds[s] = 5000
#end for - this makes seeds really bright!!
for s in lstSeedRV:
    imgSeeds[s] = 5000
#end for - this makes seeds really bright!!
#See the seeds,,,
sitk.Show(imgSeeds[:,:,128])

#now apply the region growing filter
imgLV = sitk.ConnectedThreshold(image1 = imageSmooth, seedList=lstSeedLV, lower=950, upper = 1400, replaceValue=lblLeftVentricle )
imgRV = sitk.ConnectedThreshold(image1 = imageSmooth, seedList=lstSeedRV, lower=800, upper= 1200, replaceValue=lblRightVentricle )

sitk.Show(imgLV)
sitk.Show(imgRV)

#TODO: To write a comparison function....
