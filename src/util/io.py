def append_to_file(filename, data):
    with open(filename, mode='a') as f:
        f.write(f'{data}\n')


def read_metadata(filename):
    metadata_list = []
    with open(filename, mode='r') as f:
        metadata_list = f.readlines()

    return metadata_list
