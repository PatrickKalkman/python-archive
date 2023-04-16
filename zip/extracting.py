import zipfile


def extract_zip_archive(input_file, output_folder):
    with zipfile.ZipFile(input_file, 'r') as zip_file:
        zip_file.extractall(output_folder)


def main():
    input_file = 'example_archive.zip'
    output_folder = 'extracted_files'

    extract_zip_archive(input_file, output_folder)


if __name__ == "__main__":
    main()
