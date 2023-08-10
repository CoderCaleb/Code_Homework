import os
import shutil

from_dir = "/Users/caleb/myFolder"
to_dir = "/Users/caleb/sortedFolder"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    
    if not extension:
        continue
    
    allowed_extensions = ['.txt', '.doc', '.docx', '.pdf']
    
    if extension in allowed_extensions:
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "Document_Files")
        path3 = os.path.join(path2, file_name)
        
        if not os.path.exists(path2):
            os.makedirs(path2)
        
        shutil.move(path1, path3)

print("Files moved successfully!")
