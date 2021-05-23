import requests

url = "https://discord.com/api/v8/applications/588076611329589254/commands"

json = {
    "name": "white",
    "description": "Set nickname color to white",
}

headers = {
    "Authorization": "Bot NTg4MDc2NjExMzI5NTg5MjU0.XP_3Bg.TSmV3jkAvkGCfZshmPiD7-IWWrA"
}

r = requests.post(url, headers=headers, json=json) # , json=json
print(r.text)