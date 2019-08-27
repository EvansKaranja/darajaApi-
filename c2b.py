import requests
import keys
from keys import get_access_token


def register_url():
    access_token = get_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "ShortCode": keys.shortcode,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://fullstackdjango.com/confirmation_url",
        "ValidationURL": "https://fullstackdjango.com/validation_url",
    }

    response = requests.post(api_url, json=request, headers=headers)
    print(response.text)


# register_url()
def simulate_c2b_transaction():
    access_token = get_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "ShortCode": keys.shortcode,
        "CommandID": "CustomerPayBillOnline",
        "Amount": "2",
        "Msisdn": keys.test_msisdn,
        "BillRefNumber": "12345678",
    }

    response = requests.post(api_url, json=request, headers=headers)
    print(response.text)


simulate_c2b_transaction()
