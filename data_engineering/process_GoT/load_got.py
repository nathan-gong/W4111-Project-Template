import pymongo
# import mysecrets
import utils.file_utils as file_utils

mongo_db_name = "F24_GoT"
data_path = "/Users/donald.ferguson/Dropbox/000/000-Data/GoT/"

data_file_load_info = [
    {
        "file_name": "characters-gender-all.json",
        "top_level_element": None,
        "collection": "characters_gender",
        "is_list": False
    },
    {
        "file_name": "characters-groups.json",
        "top_level_element": "groups",
        "collection": "characters_groups",
        "is_list": True
    },
    {
        "file_name": "characters.json",
        "top_level_element": "characters",
        "collection": "characters",
        "is_list": True
    },
    {
        "file_name": "episodes.json",
        "top_level_element": "episodes",
        "collection": "episodes",
        "is_list": True
    },
    {
        "file_name": "locations.json",
        "top_level_element": "regions",
        "collection": "locations",
        "is_list": True
    }
]


def get_connection():
    client = pymongo.MongoClient(
        # mysecrets.mongodb_url
    )
    return client


def test_connection(con=None):
    if not con:
        con = get_connection()

    print("Databases = ", list(con.list_databases()))


def load_and_save_file(file_path, collection_name, top_level_element=None, is_list=True):

    j_data = file_utils.load_json_file(file_path)

    if top_level_element:
        j_data = j_data[top_level_element]

    if not is_list:
        j_data = [j_data]

    con = get_connection()
    con[mongo_db_name][collection_name].insert_many(j_data)


def load_and_save_all_files():

    for f in data_file_load_info:
        load_and_save_file(
            file_path=data_path + f['file_name'],
            collection_name=f['collection'],
            top_level_element=f['top_level_element'],
            is_list=f["is_list"]
        )


if __name__ == "__main__":
    test_connection()
    load_and_save_all_files()




