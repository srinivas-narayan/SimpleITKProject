import SimpleITK as sitk
import numpy as np

image = sitk.ReadImage('data/MR/subject101_ed.nii')
labels = sitk.ReadImage('data/MR/subject101_ed_label.nii')
labels = sitk.GetArrayFromImage(labels)
#help(sitk.IsolatedWatershed)

region = sitk.ConfidenceConnected(image, [[70, 134, 139]], multiplier=2)
region_data = sitk.GetArrayFromImage(region)
region_upscaled = region_data.astype(float) / region_data.max() * 255
region_upscaled = sitk.GetImageFromArray(region_upscaled)
region_upscaled.CopyInformation(region)


true_volume = labels == 34
segmented_volume = region_data == 1

score = 2.0*np.sum(np.logical_and(true_volume, segmented_volume)) / \
    np.sum(np.logical_or(true_volume, segmented_volume))

print('Dice: %.4f' % score)



sitk.WriteImage(region_upscaled, 'region.nii')
sitk.Show(region_upscaled)
