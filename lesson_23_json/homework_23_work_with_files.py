import json


def read_given_info(file_path):
    with open(file_path, encoding="utf-8") as file:
        some_list = file.read().splitlines()
        split_lines = [line.split(",") for line in some_list]
        return split_lines


def json_format_data():
    dict_a = {a[0]: a[1] for a in list_a}
    return dict_a


def write_json_file(file_path, some_dict):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(
            some_dict,
            file,
            sort_keys=True,
            ensure_ascii=False,
            indent=4,
        )


def homework_function():
    information_list = read_given_info('HW_Files.txt')
    information_dict = {a[0]: a[1] for a in information_list}
    write_json_file('HW_Files.json', information_dict)


if __name__ == "__main__":
    homework_function()
