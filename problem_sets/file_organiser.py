import os
import shutil

downloads_path = "../../../../downloads"
file_extensions = {
    "Text Files": [".txt", ".md", ".doc", ".docx"],
    "Video Files": [".mov", ".mp4", ".avi", ".mkv"],
    "Image Files": [".jpeg", ".jpg", ".png", ".gif"],
}

extension_to_folder = {
    ext: folder for folder, exts in file_extensions.items() for ext in exts
}


def move_file(src, dest):
    try:
        shutil.move(src, dest)
        return True
    except Exception as e:
        print(f"Error moving {src}: {e}")
        return False


def run():
    files_moved_count = 0

    # Pre-create directories
    for folder in file_extensions.keys():
        os.makedirs(os.path.join(downloads_path, folder), exist_ok=True)

    for root, _, files in os.walk(downloads_path):
        for filename in files:
            file_extension = os.path.splitext(filename)[1]
            folder_name = extension_to_folder.get(file_extension)

            if folder_name:
                old_path = os.path.join(root, filename)
                new_path = os.path.join(downloads_path, folder_name, filename)

                if move_file(old_path, new_path):
                    files_moved_count += 1
                    print(f"Moved file: {filename} to {folder_name}/")

    print(
        f"Moved {files_moved_count} file(s)!"
        if files_moved_count
        else "No files found to move!"
    )


run()
