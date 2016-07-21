import SimpleITK as sitk
import numpy as np

image = sitk.ReadImage('data/MR/subject101_ed.nii')
labels = sitk.ReadImage('data/MR/subject101_ed_label.nii')
labels = sitk.GetArrayFromImage(labels)
#help(sitk.IsolatedWatershed)

shed = sitk.IsolatedWatershed(image, [70, 134, 139], [126, 162, 153])

#shed = sitk.ReadImage('shed.nii')

shed_data = sitk.GetArrayFromImage(shed)



true_volume = labels == 34
segmented_volume = shed_data == 1

score = 2.0*np.sum(np.logical_and(true_volume, segmented_volume)) / \
    np.sum(np.logical_or(true_volume, segmented_volume))

print('Dice: %.4f' % score)

shed = shed_data.astype(float) / shed_data.max() * 255

shed = sitk.GetImageFromArray(shed)


sitk.WriteImage(shed, 'shed.nii')
sitk.Show(shed)
