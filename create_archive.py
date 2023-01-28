import os
from os.path import basename
from zipfile import ZipFile
import zipfile
import pytest
import glob


@pytest.fixture()
def clear_dir():
    path_archive = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')
    precondition_directory(path_archive)


def create_archive(path_with_files, path_save_archive):
    file_directory = os.listdir(path_with_files)
    with zipfile.ZipFile(path_save_archive, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in file_directory:
            add_file = os.path.join(path_with_files, file)
            zf.write(add_file, basename(add_file))
    contains_zip = ZipFile(path_save_archive).namelist()
    assert file_directory == contains_zip, 'Содержимое архива не совпадает с исходными файлами'

# test

def precondition_directory(path_save_archive):
    path_file = os.path.join(path_save_archive, '*.*')
    for file in glob.glob(path_file):
        os.remove(file)
