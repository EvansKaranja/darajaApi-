import base64
from datetime import datetime
import requests
from keys import get_access_token
import keys


def get_formatted_time():
    unformated_time = datetime.now()
    formatted_time = unformated_time.strftime("%Y%m%d%H%M%S")
    return formatted_time


def get_decoded_password(*args):
    data_to_encode = keys.business_shortCode + \
        keys.lina_na_mpesa_passkey+get_formatted_time()
    encoded_string = base64.b64encode(data_to_encode.encode())
    decoded_password = encoded_string.decode('utf-8')
    return decoded_password
# print(decoded_password)


def lipa_na_mpesa(*args):
    access_token = get_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": keys.business_shortCode,
        "Password": get_decoded_password(),
        "Timestamp": get_formatted_time(),
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
