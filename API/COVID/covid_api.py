import requests

# url = "https://covid-193.p.rapidapi.com/countries"

# headers = {
# 	"X-RapidAPI-Key": "aa24d1a197msh7c322f1111480c2p16c025jsn35b22e6582d6",
# 	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# print(response.json())


url2 = "https://covid-193.p.rapidapi.com/history"

querystring2 = {"country":"portugal","day":"2021-06-02"}

headers2 = {
	"X-RapidAPI-Key": "aa24d1a197msh7c322f1111480c2p16c025jsn35b22e6582d6",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response2 = requests.get(url2, headers=headers2, params=querystring2)

print(response2.json())