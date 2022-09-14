import json
import boto3

region_name = 'us-east-1'
table_name = 'contacts'
client = boto3.client('dynamodb', region_name=region_name)


class Directory():
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def all_contacts(self):
        contacts = client.scan(
            TableName=table_name, Limit=3, ProjectionExpression="id,#n,phone,addressLines", ExpressionAttributeNames={"#n": "name"})
        formated_contacts = self.format_ddb_resp(
            contacts["Items"])
        return formated_contacts

    def contact_by_id(self, contact_id):
        key = self.format_contact_id(contact_id)
        contact = client.get_item(TableName=table_name,
                                  Key=key)
        formated_contact = self.format_ddb_resp([contact["Item"]])

        return formated_contact

    def contacts_by_phrase(self, phrase):
        contacts = client.scan(TableName=table_name,
                               Limit=20,
                               ExpressionAttributeNames={"#n": "name"},
                               ExpressionAttributeValues={
                                   ":nm": {"S": f"{phrase.lower()}"}},
                               FilterExpression="contains(#n, :nm )",)

        formated_contacs_database = self.format_ddb_resp(
            contacts["Items"])

        return formated_contacs_database

    def delete_contact(self, contact_id):
        key = self.format_contact_id(contact_id)
        result = client.delete_item(TableName=table_name, Key=key,
                                    ReturnValues="ALL_OLD")
        if "Attributes" not in result:
            raise ValueError

    def update_contacts(self, updated_contacts):
        with open(self.path_to_file, "w") as open_file:
            json.dump(updated_contacts, open_file)

    def contact_exist(self, contact_id):
        return True
    #     key = self.format_contact_id(contact_id)
    #     contact = client.get_item(TableName=table_name,
    #                               Key=key,
    #                               ProjectionExpression="placeholder")
    #     print(contact)

    #     return len(list(filter(lambda contact: contact["id"] ==
    #                            contact_id, self.all_contacts())))

    def format_contact_id(self, contact_id):
        return {
            "id": {"S": contact_id},
        }

    def format_ddb_resp(self, contacts_resp):
        formated_contact_resp = []
        for contact in contacts_resp:
            formated_contact_resp.append({"id": contact["id"]["S"],
                                          "name": contact["name"]["S"],
                                          "phone": contact["phone"]["S"],
                                          "addressLines": [address["S"] for address in contact["addressLines"]["L"]]})
        return formated_contact_resp


def main():
    client = boto3.client('dynamodb', region_name=region_name)


if __name__ == '__main__':
    main()
