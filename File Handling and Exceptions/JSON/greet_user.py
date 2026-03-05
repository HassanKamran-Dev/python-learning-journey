import json

filename = "username.json"

with open(filename,"r") as f_obj:
    username = json.load(f_obj)

print("Hello",username,"welcome back!")