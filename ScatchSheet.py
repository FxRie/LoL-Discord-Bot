import json

root = {}
root1 = {"champions": []}

with open("ChampionAttributes.json", "r", encoding='utf-8-sig') as read_file:
    root = json.load(read_file)

for entry in root["data"]:
    championName = root["data"][entry]["name"]
    championId = root["data"][entry]["key"]
    root1["champions"].append({"championId": int(championId), "championName": championName})

with open("Champions.json", "w") as write_file:
    json.dump(root1, write_file, indent=5)
