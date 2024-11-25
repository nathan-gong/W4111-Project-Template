import gzip
import shutil
import json


def unzip_file_to_file(in_file, out_file):

    with gzip.open(in_file, 'rb') as f_in:
        with open(out_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def load_json_file(file_path):

    with open(file_path, "r") as in_file:
        result = json.load(in_file)

    return result




