import os
import shutil

source_folder = r"D:\downloads"

files_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"]
}

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file)[1].lower()

        moved = False

        for folder_name, extension in files_types.items():
            if file_ext in extension:
                folder_path = os.path.join(source_folder, folder_name)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(file_path, os.path.join(folder_path, file))
                moved = True
                break

        if not moved:
            other_folder = os.path.join(source_folder, "other")
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)

            shutil.move(file_path, os.path.join(other_folder, file))

print("File organized successfully")
