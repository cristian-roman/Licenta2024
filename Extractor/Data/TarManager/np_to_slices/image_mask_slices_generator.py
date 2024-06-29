from Data.TarManager.refs_to_np.image_mask_np_generator import image_mask_np_iterator


def image_mask_slices_iterator():
    for np_image_pair in image_mask_np_iterator(10):
        img_np, mask_np, provenience = np_image_pair
        img_slices = img_np.shape[2]
        for slice_number in range(img_slices):
            mask_np_slice = mask_np[:, :, slice_number]

            if len(img_np.shape) == 3:
                img_np_slice = img_np[:, :, slice_number]
            elif len(img_np.shape) == 4:
                img_np_slice = img_np[:, :, slice_number, 0]
            else:
                raise ValueError('Invalid image shape')

            yield img_np_slice, mask_np_slice, provenience
