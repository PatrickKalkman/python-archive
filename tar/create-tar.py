import tarfile


def create_gzipped_tar_archive(tar_path, file_paths):
    with tarfile.open(tar_path, 'w:gz') as tar_file:
        for file_path in file_paths:
            tar_file.add(file_path, arcname=file_path)


def main():
    tar_path = 'example.tgz'
    file_paths = ['./example_folder/file1.txt',
                  './example_folder/file2.txt',
                  './example_folder/file3.txt']

    create_gzipped_tar_archive(tar_path, file_paths)
    print(f"{tar_path} created with the files: {', '.join(file_paths)}")


if __name__ == '__main__':
    main()
