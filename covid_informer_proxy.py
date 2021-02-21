import requests
import os
from datetime import datetime, timedelta
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

POPULATION = 2_795_175
URL = "https://services3.arcgis.com/MF53hRPmwfLccHCj/arcgis/rest/services/COVID19_statistika_dashboards/FeatureServer/0/query"
MY_NUMBER = '+37062634021'
TWILIO_NUMBER = '+18473805948'

account_sid = 'AC15b1124223f4dd6d898e08b1e08f4b23'
auth_token = os.environ.get('AUTH_TOKEN')

parameters = {
    'where': "municipality_code = '00'",
    'outFields': 'date,cumulative_totals',
    'f': 'json'
}

response = requests.get(URL, params=parameters)
day_0 = response.json()['features'][0]['attributes']
day_14 = response.json()['features'][14]['attributes']

cases_14_days = day_0['cumulative_totals'] - day_14['cumulative_totals']
rate = round((cases_14_days / (POPULATION / 100_000)), 2)
date = datetime.utcfromtimestamp(day_0['date'] / 1000) + timedelta(days=1)

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}
client = Client(account_sid, auth_token, http_client=proxy_client)
message = client.messages.create(
    body=f"On {date.date()} rate is {rate}",
    from_=TWILIO_NUMBER,
    to=MY_NUMBER
)
