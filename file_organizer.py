import os

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder not found!")
        return

    extensions = {
        "Images": [".jpg", ".png", ".gif", ".jpeg"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".avi", ".mkv"],
        "Music": [".mp3", ".wav"],
        "Others": []
    }

    for category, exts in extensions.items():
        category_path = os.path.join(folder_path, category)
        os.makedirs(category_path, exist_ok=True)

        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path) and any(file.endswith(ext) for ext in exts):
                shutil.move(file_path, os.path.join(category_path, file))

folder_path = input("Enter folder path: ")
organize_files(folder_path)
print("Files organized successfully!")
