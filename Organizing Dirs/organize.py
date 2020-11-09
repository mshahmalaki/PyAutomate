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


print(pick_directory('.docx'))
