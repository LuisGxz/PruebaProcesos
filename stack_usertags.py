import requests
import json

def obtener_tags(user_id):
    url = f"https://api.stackexchange.com/2.2/users/{user_id}/top-tags?site=stackoverflow"
    r = requests.get(url)
    r_json = r.json()

    tags = ""

    if "error_id" in r_json: 
        return None
    else:
        for tag in r_json["items"]:
            tags += tag["tag_name"] + " "
        return tags
