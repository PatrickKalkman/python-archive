import zipfile
import os


def create_zip_archive(input_folder, output_file):
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(input_folder):
            for file in files:
                file_path = os.path.join(root, file)
                print(f"Adding {file_path} to {output_file}")
                zip_file.write(file_path,
                               os.path.relpath(file_path, input_folder))


def main():
    input_folder = 'example_folder'
    output_file = 'example_archive.zip'

    create_zip_archive(input_folder, output_file)


if __name__ == "__main__":
    main()
