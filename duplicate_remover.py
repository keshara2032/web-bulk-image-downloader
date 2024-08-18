import os
import imagehash
from PIL import Image

def find_duplicate_images(folder_path):
    hashes = {}
    duplicates = []

    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            file_path = os.path.join(folder_path, filename)
            try:
                with Image.open(file_path) as img:
                    img_hash = imagehash.average_hash(img)

                if img_hash in hashes:
                    duplicates.append(file_path)
                else:
                    hashes[img_hash] = file_path

            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

    return duplicates

def move_duplicates(duplicate_files, folder_path):

    duplicate_folder = os.path.join(folder_path, "duplicates")
    # create a folder to move the duplicates
    if not os.path.exists(duplicate_folder):
        os.makedirs(duplicate_folder)

    
    for file_path in duplicate_files:
        #move the duplicate file to the duplicates folder
        file_name = os.path.basename(file_path)
        new_file_path = os.path.join(duplicate_folder, file_name)
        os.rename(file_path, new_file_path)
        print(f"Moved duplicate: {file_path}")

if __name__ == "__main__":
    folder_path = "./dataset/kelly"
    duplicates = find_duplicate_images(folder_path)
    if duplicates:
        move_duplicates(duplicates, folder_path)
    else:
        print("No duplicates found.")
