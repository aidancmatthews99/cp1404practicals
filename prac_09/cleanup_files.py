"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # os.rename(filename, new_name)
        # shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = ''
    previous_letter = ''
    for letter in filename:
        if letter.isupper() and previous_letter != '_' and previous_letter != '':
            new_name += '_'
        if previous_letter == ' ' or previous_letter == '_' or previous_letter == '':
            letter = letter.upper()

        new_name += letter
        previous_letter = letter
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            old_name_path = os.path.join(directory_name, filename)
            new_name_path = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(old_name_path, new_name_path)
            print(get_fixed_filename(filename))
        print("Directory:", directory_name)
        print("\tContains subdirectories:", subdirectories)
        print("\tContains files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))



# main()
demo_walk()
# get_fixed_filename('AngelsWeHaveHeard.txt')