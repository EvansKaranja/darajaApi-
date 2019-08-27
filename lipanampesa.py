import requests
from requests.auth import HTTPBasicAuth
import keys
import base64
from datetime import datetime

unformated_time = datetime.now()
formatted_time = unformated_time.strftime("%Y%m%d%H%M%S")


def get_decoded_password(*args):
    data_to_encode = keys.business_shortCode + \
        keys.lina_na_mpesa_passkey+formatted_time
    encoded_string = base64.b64encode(data_to_encode.encode())
    decoded_password = encoded_string.decode('utf-8')
    return decoded_password
# print(decoded_password)


def get_access_token():
    consumer_key = keys.consumer_key
    consumer_secret = keys.consumer_secret
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(api_url, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    json_response = r.json()
    return json_response['access_token']


def lipa_na_mpesa(*args):
    access_token = get_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": keys.business_shortCode,
        "Password": get_decoded_password(),
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": keys.phone_number,
        "PartyB": keys.business_shortCode,
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://fullstackdjango.com/lipanampesa",
        "AccountReference": "KAW 324Z",
        "TransactionDesc": "pay parking fee"
    }
    response = requests.post(api_url, json=request, headers=headers)
    print(response.text)


lipa_na_mpesa()
print(keys.phone_number)
