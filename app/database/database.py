import json

# from contacts_app.app.contacts.routes import contacs


class Directory():
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def load_json_file(self):
        with open(self.path_to_file, "r") as open_file:
            return json.load(open_file)

    @property
    def all_contacts(self):
        contacs_database = self.load_json_file()

        return contacs_database

    def contact_by_id(self, contact_id):
        contact = filter(lambda contact: contact["id"] ==
                         contact_id, self.all_contacts)

        return list(contact)

    def contacts_by_phrase(self, phrase):
        matching_contacts = filter(
            lambda contact: phrase.lower() in contact["name"].lower(), self.all_contacts)

        return list(matching_contacts)


if __name__ == '__main__':
    directory = Directory("./fakedatabase.json")
    # {'id': 'f88e54c5-eec8-4c6a-acd4-1177fd07abf5', 'name': 'Rusty Medhurst', 'phone': '1-259-626-1422', 'addressLines': ['762 Greenholt Lake', 'New Alekside', 'Djibouti']}
