from urllib.error import URLError
from urllib.request import Request, urlopen
from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)

input_url = input("Enter the URL\n(Eg - www.google.com)\n")
url = "https://" + input_url

m_reason = ''
m_code = ''
m_message = ''

req = Request(url)

try:
    response = urlopen(req)
except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
        m_reason = e.reason
    if hasattr(e, 'code'):
        print('The server could not fulfill the request.')
        print('Error code: ', e.code)
        print("The above information is being send to registered number")
        m_code = e.code
        m_message = 'We failed to reach a server. Reason:' + e.reason +\
                    '\nThe server could not fulfill the request. Error Code:' + str(m_code)
        message = client.messages.create(body=m_message,
                                         to=my_cell,
                                         from_=my_twilio)
else:
    print("The server can be reached and the request is fulfilled. Code: 200"
          "\nThe above information is being send to registered number")
    m_message = "The server can be reached and the request is fulfilled. Code: 200"
    message = client.messages.create(body=m_message,
                                     to=my_cell,
                                     from_=my_twilio)


