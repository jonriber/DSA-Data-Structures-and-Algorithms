import requests

url = "https://google-news13.p.rapidapi.com/latest"

querystring = {"lr":"en-US"}

headers = {
	"X-RapidAPI-Key": "aa24d1a197msh7c322f1111480c2p16c025jsn35b22e6582d6",
	"X-RapidAPI-Host": "google-news13.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())