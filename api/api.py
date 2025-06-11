import requests

get_list_file = requests.post(
    url = "https://teradl-api.dapuntaratya.com/generate_file",
    headers = {"Content-Type":"application/json"},
    json = {"url":"https://1024terabox.com/s/1eBHBOzcEI-VpUGA_xIcGQg"}
).json()

get_link_download = requests.post(
    url     = "https://teradl-api.dapuntaratya.com/generate_link",
    headers = {"Content-Type":"application/json"},
    json    = {
        "uk"        : 4399535305786,
        "shareid"   : 4095377511,
        "timestamp" : 1744294847,
        "sign"      : "0f7aa2dc4d7373e307241b7eb1e5c8f55a58dd21",
        "fs_id"     : 56206195934797
    }
).json()