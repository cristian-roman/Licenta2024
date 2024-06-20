import json
import os


def unzip_file(tar_file_path, dest_folder):
    os.system(f'tar -xf {tar_file_path} -C {dest_folder}')


def delete_folder(folder_path):
    if os.path.exists(folder_path):
        os.system('rm -r ' + folder_path)


def delete_file(file_path):
    if os.path.exists(file_path):
        os.system('rm ' + file_path)


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def create_file(file_path):
    if not os.path.exists(file_path):
        os.system(f'touch {file_path}')


def save_json_document(json_document: dict, file_path: str):
    with open(file_path, 'w') as file:
        json.dump(json_document, file, indent=4)


def load_json_document(file_path: str):
    with open(file_path, 'r') as file:
        return json.load(file)


def rename_file(old_path, new_file_name):
    extension = old_path.split('.')[-1]
    new_path = old_path.replace(old_path.split('/')[-1], new_file_name + '.' + extension)
    os.rename(old_path, new_path)
