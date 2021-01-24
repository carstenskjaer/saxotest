from saxo_openapi import API
import saxo_openapi.endpoints.rootservices as rs
import saxo_openapi.endpoints.chart as chart
from pprint import pprint
import json

token = "eyJhbGciOiJFUzI1NiIsIng1dCI6IjhGQzE5Qjc0MzFCNjNFNTVCNjc0M0QwQTc5MjMzNjZCREZGOEI4NTAifQ.eyJvYWEiOiI3Nzc3NSIsImlzcyI6Im9hIiwiYWlkIjoiMTA5IiwidWlkIjoiVnFRemJCSGVvTjQ4UXNPalNTZ1Bldz09IiwiY2lkIjoiVnFRemJCSGVvTjQ4UXNPalNTZ1Bldz09IiwiaXNhIjoiRmFsc2UiLCJ0aWQiOiIyMDAyIiwic2lkIjoiNTk4ZjUyNjAxZDRiNGU4OTgwODk2ZWFjNjA0NWM3YTAiLCJkZ2kiOiI4NCIsImV4cCI6IjE2MTE1NTY5ODEifQ.3IKHbaLnF1I-PirYcuKN3qB00wYeBAb4SAKuQhvGUPZf6eTBmAGSFi_rruiUfPStg90m87cKF-j71h6OWJ47oQ"
client = API(access_token=token)


# lets make a diagnostics request, it should return '' with a state 200
r = rs.diagnostics.Get()
print("request is: ", r)
rv = client.request(r)
assert rv is None and r.status_code == 200
print('diagnostics passed')

# request available rootservices-features
r = rs.features.Availability()
rv = client.request(r)
print("request is: ", r)
print("response: ")
pprint(rv, indent=2)
print(r.status_code)

params = {
    "AssetType": "FxSpot",
    "Horizon": 1,
    "Count": 1000,
    "Uic": 23
}


r = chart.charts.GetChartData(params=params)
rv = client.request(r)
print(json.dumps(rv, indent=2))