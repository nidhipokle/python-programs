import os
import shutil

folder = r"C:\Users\Nidhi\Downloads"

text_folder = os.path.join(folder, "Text")
pdf_folder = os.path.join(folder, "PDF")
image_folder = os.path.join(folder, "Images")

os.makedirs(text_folder, exist_ok=True)
os.makedirs(pdf_folder, exist_ok=True)
os.makedirs(image_folder, exist_ok=True)

for file in os.listdir(folder):

    old_path = os.path.join(folder, file)

    if os.path.isfile(old_path):

        if file.endswith(".txt"):
            shutil.move(old_path, text_folder)
            print(file, "-> Text")

        elif file.endswith(".pdf"):
            shutil.move(old_path, pdf_folder)
            print(file, "-> PDF")

        elif file.endswith(".jpg") or file.endswith(".png"):
            shutil.move(old_path, image_folder)
            print(file, "-> Images")

print("Files organized successfully!")
