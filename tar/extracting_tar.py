import tarfile


def extract_tar_archive(tar_path, output_path):
    with tarfile.open(tar_path, 'r') as tar_file:
        tar_file.extractall(output_path)


def main():
    tar_path = 'example.tgz'
    output_path = 'extracted_files'

    extract_tar_archive(tar_path, output_path)
    print(f"Files from {tar_path} have been extracted to {output_path}")


if __name__ == '__main__':
    main()
