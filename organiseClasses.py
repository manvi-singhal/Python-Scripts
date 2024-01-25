#To organize the dataset into folders based on the class names

import os
import json
import shutil

def create_class_folders(classes, dataset_folder):
    for class_name in classes:
        folder_path = os.path.join(dataset_folder, class_name)
        os.makedirs(folder_path, exist_ok=True)

def organize_dataset(images_data, dataset_folder):
    for image_info in images_data:
        image_name = image_info["image"]
        annotations = image_info["annotations"]

        if annotations:
            label = annotations[0]["label"]

            if label in classes:
                source_path = os.path.join(dataset_folder, image_name)
                destination_folder = os.path.join(dataset_folder, label)
                destination_path = os.path.join(destination_folder, image_name)
                shutil.move(source_path, destination_path)

if __name__ == "__main__":
    dataset_folder = "" # Replace with your actual dataset folder
    json_file_path = "" # Replace with your actual JSON file path

    classes = [""] # Replace with your actual classes eg. ["cat", "dog", "bird"]

    with open(json_file_path, 'r') as json_file:
        images_data = json.load(json_file)

    create_class_folders(classes, dataset_folder)
    organize_dataset(images_data, dataset_folder)
    print("Dataset organized successfully.")
