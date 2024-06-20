import Data.TarManager.np_to_slices.image_mask_slices_generator as tar
import Data.ImagesManager.image_mask_generator as local_images


def image_mask_aggregator():
    for img_np, mask_np, provenience in tar.image_mask_slices_iterator():
        yield img_np, mask_np, provenience

    for img_np, mask_np, provenience in local_images.image_mask_iterator():
        yield img_np, mask_np, provenience
