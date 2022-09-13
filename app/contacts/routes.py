
from flask import Blueprint, make_response, request
from flask import current_app as app
from .. import contact_directory
# from flask_cors import cross_origin

api_prefix = app.config['PREFIX']
contacts = Blueprint('contacts', __name__,
                     url_prefix=api_prefix)


@contacts.route('/contacts', methods=['GET'])
def contacs():
    if "phrase" in request.args:
        if not request.args["phrase"]:
            return make_response({"status": "fail", "data": {"phrase": "Empty phrases are not allowed"}}, 400)

        dir_contacts = contact_directory.contacts_by_phrase(
            request.args["phrase"])
    else:
        dir_contacts = contact_directory.all_contacts

    dir_contacts.sort(key=lambda contact: contact["name"])
    response = make_response({"status": "success",
                              "data": {"contacts": dir_contacts}}, 200)
    return response
