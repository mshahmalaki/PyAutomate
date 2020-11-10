from os import scandir
from pathlib import Path


SUBDIRECTORIES = {
    "Document": ['.pdf', '.doc', '.docx', '.rtf', '.txt'],
    "Audio": ['.m4a', '.m4b', '.mp3', '.wma'],
    "Video": ['.mov', '.avi', '.mp4', '.mkv'],
    "Image": ['.jpg', '.jpeg', '.png']
}


def pick_directory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'Miscellaneous'


def organize_directory():
    for item in scandir():
        if item.is_dir():
            continue
        file_path = Path(item)
        file_type = file_path.suffix.lower()
        directory = pick_directory(file_type)
        directory_path = Path(directory)
        if not directory_path.is_dir():
            if file_type == '.py' or file_type == '.md':
                continue
            directory_path.mkdir()
        file_path.rename(directory_path.joinpath(file_path))


organize_directory()
