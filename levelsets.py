import SimpleITK as sitk
import numpy as np

image = sitk.ReadImage('data/MR/subject101_ed.nii')
image_data = sitk.GetArrayFromImage(image)
labels_org = sitk.ReadImage('data/MR/subject101_ed_label.nii')
labels = sitk.GetArrayFromImage(labels_org)

label_left = sitk.GetImageFromArray((labels == 34) * 1)
#label_left.SetSpacing(image.GetSpacing())

#stats = sitk.LabelStatisticsImageFilter()
#stats.Execute(image, label_left)

idx = [70, 134, 139]
pt = image.TransformIndexToPhysicalPoint(idx)

seg = sitk.Image(image.GetSize(), sitk.sitkUInt8)
seg.CopyInformation(image)
seg[idx] = 1
seg = sitk.BinaryDilate(seg, 10)

mean = np.mean(image_data[labels == 34])
sigma = np.std(image_data[labels == 34])

lower_threshold = mean - 6 * sigma
upper_threshold = mean + 6 * sigma

init_ls = sitk.SignedMaurerDistanceMap(seg, insideIsPositive=True, useImageSpacing=True)

lsFilter = sitk.ThresholdSegmentationLevelSetImageFilter()
lsFilter.SetLowerThreshold(lower_threshold)
lsFilter.SetUpperThreshold(upper_threshold)
lsFilter.SetMaximumRMSError(0.02)
lsFilter.SetNumberOfIterations(100)
lsFilter.SetCurvatureScaling(1)
lsFilter.SetPropagationScaling(1)
lsFilter.ReverseExpansionDirectionOn()

levels = lsFilter.Execute(init_ls, sitk.Cast(image, sitk.sitkFloat32))
#sitk.Show(levels)


levels_data = sitk.GetArrayFromImage(levels)



true_volume = labels == 34
segmented_volume = levels_data > levels_data.min()

score = 2.0*np.sum(np.logical_and(true_volume, segmented_volume)) / \
    np.sum(np.logical_or(true_volume, segmented_volume))

print('Dice: %.4f' % score)

sitk.Show(levels)
sitk.WriteImage(levels, 'levels.nii')
