import json


class Directory():
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def load_json_file(self):
        return json.load(self.path_to_file)

    @property
    def contacts(self):
        return self.load_json_file()


if __name__ == '__main__':
    directory = Directory("./fakedatabase.json")
