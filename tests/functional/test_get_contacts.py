import pytest
from json import dumps, loads
from unittest.mock import patch
# import requests
# from requests import Response


def test_contacts(test_client):
    response = test_client.get("/api/v1/contacts")
    assert response.status_code == 200

    response = test_client.post("/api/v1/contacts")
    assert response.status_code == 405

    response = test_client.put("/api/v1/contacts")
    assert response.status_code == 405

    response = test_client.patch("/api/v1/contacts")
    assert response.status_code == 405

    response = test_client.delete("/api/v1/contacts")
    assert response.status_code == 405


@patch('app.contacts.routes.contact_directory.all_contacts')
def test_get_all_contacts(mock_get, test_client, mock_contacts):
    mock_get.return_value = mock_contacts
    response = test_client.get("/api/v1/contacts")

    assert response.status_code == 200


@patch('app.contacts.routes.contact_directory.all_contacts')
def test_get_contacts_by_phrase(mock_get, test_client, mock_contacts):
    mock_get.return_value = mock_contacts
    response = test_client.get("/api/v1/contacts?phrase=as")

    assert response.status_code == 200


@patch('app.contacts.routes.contact_directory.all_contacts')
def test_get_contacts_by_empty_phrase(mock_get, test_client, mock_contacts):
    mock_get.return_value = mock_contacts
    response = test_client.get("/api/v1/contacts?phrase=")

    assert response.status_code == 400


@patch('app.contacts.routes.contact_directory.contact_by_id')
def test_get_contact_by_id(mock_get, test_client, mock_contact, contact_id):
    mock_get.return_value = mock_contact
    response = test_client.get(f"/api/v1/contacts/{contact_id}")
    contact_data = loads(response.data)

    assert response.status_code == 200
    assert len(contact_data) > 0


@patch('app.contacts.routes.contact_directory.contact_by_id')
def test_get_contact_by_id_notfound(mock_get, test_client):
    mock_get.return_value = []
    contact_id = "asdfasdfasdfasd"

    response = test_client.get(f"/api/v1/contacts/{contact_id}")

    assert response.status_code == 404


@patch('app.contacts.routes.contact_directory.delete_contact')
@patch('app.contacts.routes.contact_directory.contact_exist')
def test_del_contact_by_id(mock_contact_exist, mock_del, test_client, mock_contact, contact_id):
    mock_contact_exist.return_value = True
    mock_del.return_value = mock_contact

    response = test_client.delete(f"/api/v1/contacts/{contact_id}")

    assert response.status_code == 204


@patch('app.contacts.routes.contact_directory.contact_exist')
def test_del_contact_by_id_notfound(mock_contact_exist, test_client):
    mock_contact_exist.return_value = False
    contact_id = "asdfasdfasdfasd"

    response = test_client.delete(f"/api/v1/contacts/{contact_id}")

    assert response.status_code == 404
