import os
import shutil

imagesPath = "./images" 
outputPath = "./output/" 

if not os.path.exists(outputPath):
    os.makedirs(outputPath)

if not os.path.exists(imagesPath):
    os.makedirs(imagesPath)

files = os.listdir(imagesPath)
# print (files)
for i, file in enumerate(files):
    filePath = os.path.join(imagesPath, file)
    fileName = file.split('.')[0].lower()
    extension = file.split('.')[1].lower()
    # filename, extension = os.path.splitext(file)
    extension = str(extension).lower()
    
    if str(extension).lower() in ["jpg", "jpeg", "png"]:
        # filename, extension = os.path.splitext(file)
        newFilename = f"nude hanz{i + 1}.{extension}"
        copiedFilePath = f"{outputPath}{fileName}"
        renamed = f"{outputPath}{newFilename}"
        shutil.copy(filePath, copiedFilePath)
        os.replace(copiedFilePath, renamed)
        print(f"Renamed {file} to {newFilename}")