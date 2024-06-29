from Repository import organs_stats_repository, images_stats_repository


def get_overview_data():
    heart_stats = organs_stats_repository.get_entry('heart')
    prostate_stats = organs_stats_repository.get_entry('prostate')
    endometriosis_stats = organs_stats_repository.get_entry('endometriosis')
    overview = {
        'pairs': heart_stats['slices'] + prostate_stats['slices'] + endometriosis_stats['slices'],
        'diseased_slices': heart_stats['diseased'] + prostate_stats['diseased'] + endometriosis_stats['diseased'],
        'healthy_slices': heart_stats['healthy'] + prostate_stats['healthy'] + endometriosis_stats['healthy'],
        'hearts': heart_stats['slices'],
        'prostates': prostate_stats['slices'],
        'endometriosis': endometriosis_stats['slices']
    }

    return overview


def get_organ_stats(organ):
    organ_stats = organs_stats_repository.get_entry(organ)
    return {
        'provenience': organ,
        'slices': organ_stats['slices'],
        'healthy_slices': organ_stats['healthy'],
        'diseased_slices': organ_stats['diseased']
    }


def get_images_statistics(_type, modified):
    img_stats = images_stats_repository.get_entry(_type, modified)
    return __parse_images_stats(img_stats)


def __parse_images_stats(img_stats):
    return {
        'max_np_value': img_stats['max_np_value'],
        'min_np_value': img_stats['min_np_value'],
        'unique_np_values_count': img_stats['unique_np_values_count'],
        'unique_sizes_count': img_stats['unique_sizes_count']
    }


def get_images_unique_sizes(_type, modified):
    img_stats = images_stats_repository.get_entry(_type, modified)

    return img_stats['unique_sizes']


def get_images_weighted_average_np_value(_type, modified):
    img_stats = images_stats_repository.get_entry(_type, modified)
    weighted_average_np_value = img_stats['weighted_average_np_value']
    return {
        'weighted_average_np_value': weighted_average_np_value
    }
