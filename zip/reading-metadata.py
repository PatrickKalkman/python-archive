import zipfile

def print_metadata(file_info):
    file_name = file_info.filename
    file_size = file_info.file_size
    compressed_size = file_info.compress_size
    l_mod = file_info.date_time
    l_mod_date = f"{l_mod[0]:02d}-{l_mod[1]:02d}-{l_mod[2]:02d}"
    l_mod_time = f"{l_mod[3]:02d}:{l_mod[4]:02d}:{l_mod[5]:02d}"

    compression_ratio = compressed_size / file_size if file_size > 0 else 0

    print(f"File Name: {file_name}")
    print(f"File Size: {file_size} bytes")
    print(f"Compressed Size: {compressed_size} bytes")
    print(f"Last Modified: {l_mod_date} {l_mod_time}")
    print(f"Compression Ratio: {compression_ratio:.2%}\n")

def main():
    # Open the ZIP archive in read mode
    with zipfile.ZipFile('meta.zip', 'r') as zip_file:
        # Iterate through the files in the archive
        for file_info in zip_file.infolist():
            print_metadata(file_info)

if __name__ == "__main__":
    main()
