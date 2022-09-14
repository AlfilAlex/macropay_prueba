import pytest
import json

from app import create_app
# from requests import Response


@pytest.fixture()
def contact_id():
    return "3bf6353d-9142-4f32-bbe0-edc52b8a4eb0"


@pytest.fixture()
def mock_contact(contact_id):
    return [
        {
            "addressLines": [
                "516 Liliana Haven",
                "Reneeshire",
                "Iceland"
            ],
            "id": contact_id,
            "name": "Abbigail Wunsch",
                    "phone": "1-603-530-1253 x9180"
        }
    ]


@pytest.fixture()
def mock_contacts():
    return [
        {
            "addressLines": [
                "2776 Skiles Pass",
                "West Doylehaven",
                "Samoa"
            ],
            "id": "781a0de5-be80-4500-8600-7e3fd0995ba3",
            "name": "Elsa Kunze I",
                    "phone": "(747) 171-6131"
        },
        {
            "addressLines": [
                "8136 Breanne Rue",
                "Lake Kirstinmouth",
                "Maldives"
            ],
            "id": "b45b38b1-ef55-42c6-8a1d-3ec7da091880",
            "name": "Enid Kunze",
                    "phone": "1-631-156-2885 x96519"
        },
        {
            "addressLines": [
                "96435 Zemlak Bridge",
                "Ambrosehaven",
                "Tajikistan"
            ],
            "id": "160faacc-6ca9-4b29-85fe-ec4019b129cc",
            "name": "Jennifer Kunze",
                    "phone": "365-947-7215 x04765"
        }
    ]


@ pytest.fixture()
def test_client():
    app = create_app()
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client
