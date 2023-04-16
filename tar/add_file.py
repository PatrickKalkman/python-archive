import tarfile


def add_file_to_tar_archive(tar_path, file_path):
    with tarfile.open(tar_path, 'a') as tar_file:
        tar_file.add(file_path, arcname=file_path)


def main():
    tar_path = 'example.tar'
    file_path = 'file4.txt'

    add_file_to_tar_archive(tar_path, file_path)
    print(f"{file_path} added to {tar_path}")


if __name__ == '__main__':
    main()
