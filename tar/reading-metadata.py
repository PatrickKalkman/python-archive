import tarfile
import time


def print_metadata(file_info):
    file_name = file_info.name
    file_size = file_info.size
    last_modified = file_info.mtime

    last_modified_str = time.strftime('%Y-%m-%d %H:%M:%S',
                                      time.localtime(last_modified))

    print(f"File Name: {file_name}")
    print(f"File Size: {file_size} bytes")
    print(f"Last Modified: {last_modified_str}\n")


def read_tar_metadata(tar_path):
    with tarfile.open(tar_path, 'r') as tar_file:
        for file_info in tar_file.getmembers():
            print_metadata(file_info)


def main():
    tar_path = 'meta.tgz'
    read_tar_metadata(tar_path)


if __name__ == '__main__':
    main()
