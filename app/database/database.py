import json


class Directory():
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def all_contacts(self):
        contacs_database = self.load_contacts_file()

        return contacs_database

    def load_contacts_file(self):
        with open(self.path_to_file, "r") as open_file:
            return json.load(open_file)

    def contact_by_id(self, contact_id):
        contact = filter(lambda contact: contact["id"] ==
                         contact_id, self.all_contacts())

        return list(contact)

    def contacts_by_phrase(self, phrase):
        matching_contacts = filter(
            lambda contact: phrase.lower() in contact["name"].lower(), self.all_contacts())

        return list(matching_contacts)

    def delete_contact(self, contact_id):
        if self.contact_exist(contact_id):
            filtered_contacts = list(
                filter(lambda contact: contact["id"] != contact_id, self.all_contacts()))
            self.update_contacts(filtered_contacts)

    def update_contacts(self, updated_contacts):
        with open(self.path_to_file, "w") as open_file:
            json.dump(updated_contacts, open_file)

    def contact_exist(self, contact_id):
        return len(list(filter(lambda contact: contact["id"] ==
                               contact_id, self.all_contacts())))
