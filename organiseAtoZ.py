# To organizes images in a folder into subfolders alphabetically.

import os
import shutil

def organize_images(source_folder):
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        folder_path = os.path.join(source_folder, letter)
        os.makedirs(folder_path, exist_ok=True)

    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    for file in files:
        first_letter = file[0].upper()

        if 'A' <= first_letter <= 'Z':
            destination_folder = os.path.join(source_folder, first_letter)
            shutil.move(os.path.join(source_folder, file), os.path.join(destination_folder, file))

if __name__ == "__main__":
    source_folder = ""  # Replace with your actual source folder
    organize_images(source_folder)
    print("Images organized successfully.")

