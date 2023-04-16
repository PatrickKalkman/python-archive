import zipfile
import os

def add_file_to_zip_archive(input_file, archive_file):
    with zipfile.ZipFile(archive_file, 'a', zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.write(input_file, os.path.basename(input_file))

def main():
    input_file = 'new_file.txt'
    archive_file = 'example_archive.zip'

    add_file_to_zip_archive(input_file, archive_file)

if __name__ == "__main__":
    main()
