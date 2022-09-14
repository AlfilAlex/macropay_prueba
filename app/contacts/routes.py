
from flask import Blueprint, make_response, request
from flask import current_app as app
from .. import contact_directory
# from flask_cors import cross_origin

api_prefix = app.config['PREFIX']
contacts = Blueprint('contacts', __name__,
                     url_prefix=api_prefix)


@contacts.route('/contacts', methods=['GET'])
def contacts_list():
    if "phrase" in request.args:
        if request.args["phrase"] == "":
            return make_response({"status": "fail", "data": {"phrase": "Empty phrases are not allowed"}}, 400)

        dir_contacts = contact_directory.contacts_by_phrase(
            request.args["phrase"])
    else:
        dir_contacts = contact_directory.all_contacts()

    dir_contacts.sort(key=lambda contact: contact["name"])
    response = make_response({"status": "success",
                              "data": {"contacts": dir_contacts}}, 200)
    response.headers['Content-type'] = 'application/json'

    return response


@contacts.route("contacts/<contact_id>", methods=["GET"])
def contact(contact_id):
    contact = contact_directory.contact_by_id(contact_id)
    if not contact:
        response = make_response(
            {"status": "fail", "data": {"phrase": f"Contact with ID value {contact_id} does not exist"}}, 404)
    else:
        response = make_response({"status": "success",
                                  "data": {"contact": contact}}, 200)

    response.headers['Content-type'] = 'application/json'
    return response


@contacts.route("contacts/<contact_id>", methods=["DELETE"])
def delete_contact(contact_id):
    try:
        contact_directory.delete_contact(contact_id)
        response = make_response(
            {"status": "success", "data": None}, 204)
    except ValueError:
        response = make_response({"status": "fail", "data": {
                                 "phrase": f"Contact with ID value {contact_id} does not exist"}}, 404)

    return response
