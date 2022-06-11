import requests
import json

def get_waifu_list():
    response = requests.get("https://api.waifu.pics/nsfw/waifu")
    waifu_list = response.json()
    return get_waifu_url(waifu_list)


def get_waifu_url(json_waifu):
    return json_waifu["url"]