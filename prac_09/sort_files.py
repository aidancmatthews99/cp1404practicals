
import os
import shutil

word = '.txt'
excel = '.csv'
picture = '.jpg'
extensions = []
print("Starting directory is: ", os.getcwd())
os.chdir('FilesToSort')
for directory, subdirectory, files in os.walk(os.getcwd()):
    print(directory)
    print(subdirectory)
    print(files)

    for file in files:
        for i, letter in enumerate(file):
            if letter == '.' and file[i:]:
                try:
                    extensions.append(file[i:])
                    os.mkdir(extensions[-1])
                except FileExistsError:
                    pass
                shutil.move(file, file[i:])
                continue

print(extensions)
