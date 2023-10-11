Sure, I can help with that. Here is a Python script that should do the job. This script will search for all image files in a specified directory and its sub-directories, and move them to a new location.

```python
import os
import shutil

def move_images(source_dir, dest_dir):
    # Image file extensions
    img_extensions = ['.jpg', '.png', '.jpeg', '.gif', '.bmp']

    for subdir, dirs, files in os.walk(source_dir):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if ext in img_extensions:
                file_path = os.path.join(subdir, file)
                shutil.move(file_path, dest_dir)

# Specify source and destination directories
source_dir = '/path/to/source/directory'
dest_dir = '/path/to/destination/directory'

move_images(source_dir, dest_dir)
```

Please replace `'/path/to/source/directory'` and `'/path/to/destination/directory'` with your actual directories. This script uses the `os` and `shutil` modules in Python. The `os.walk()` function generates the file names in a directory tree by walking the tree either top-down or bottom-up, and for each directory in the tree it yields a 3-tuple containing the directory path, the directory names in that directory, and the filenames in that directory. The `shutil.move()` function moves a file or directory (and its contents) to another location.

Please note that this script will move all images from the source directory and its sub-directories to the destination directory. If there are images with the same name in different sub-directories, this script will overwrite those images in the destination directory. If you want to keep all images even if they have the same name, you might need to modify this script to rename images before moving them.

Also, please be aware that moving files can be a destructive operation. If something goes wrong during the move, your files could be lost. I would recommend backing up your files before running this script.

Let me know if you need further assistance! 😊