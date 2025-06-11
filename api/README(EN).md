# API Documentation

**`Domain`** : [`teradl-api.dapuntaratya.com`](https://teradl-api.dapuntaratya.com)  
**`Endpoint`** : [`/generate_file`](https://teradl-api.dapuntaratya.com/generate_file) [`/generate_link`](https://teradl-api.dapuntaratya.com/generate_link)

Content
- [Get All File List](#get-all-file-list)
- [Get Download/Stream Links For Each File](#get-downloadstream-links-for-each-file)
- [Notes](#notes)

<br><br><br>

## Get All File List

To get the entire list of files, send a `POST` request to the [`/generate_file`](https://teradl-api.dapuntaratya.com/generate_file) endpoint with the following parameters :
- `url` is the target terabox link to be downloaded

<br>

**`linux (terminal)`**
```sh
curl -X POST "https://teradl-api.dapuntaratya.com/generate_file" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://1024terabox.com/s/1eBHBOzcEI-VpUGA_xIcGQg"}'
```

**`python`**
```py
import requests

response = requests.post(
    url     = "https://teradl-api.dapuntaratya.com/generate_file",
    headers = {"Content-Type":"application/json"},
    json    = {"url":"https://1024terabox.com/s/1eBHBOzcEI-VpUGA_xIcGQg"}
).json()
```

**`javascript`**
```js
const fetchData = async () => {
    const response = await fetch(
        "https://teradl-api.dapuntaratya.com/generate_file",
        {
            method  : "POST",
            headers : {"Content-Type":"application/json"},
            body    : JSON.stringify({"url":"https://1024terabox.com/s/1eBHBOzcEI-VpUGA_xIcGQg"})
        }
    );
    const data = await response.json();
};

fetchData();
```

<br>

Upon success, you will receive the following JSON response :

**`response`**
```json
{
    "status"    : "success",
    "sign"      : "0f7aa2dc4d7373e307241b7eb1e5c8f55a58dd21",
    "timestamp" : 1744294847,
    "shareid"   : 4095377511,
    "uk"        : 4399535305786,
    "list"      : [
        {
            "is_dir" : 1,
            "fs_id"  : "375456746849604",
            "name"   : "KUMPULANMOVIE",
            "type"   : "other",
            "size"   : "",
            "image"  : "",
            "list"   : [
                {
                    "is_dir" : 0,
                    "fs_id"  : 56206195934797,
                    "name"   : "The Bourne Ultimatum (2007).mp4",
                    "type"   : "video",
                    "size"   : 2732182029,
                    "image"  : "https://data.terabox.com/thumbnail/88841....",
                    "list"   : []
                },
                {
                    "is_dir" : 0,
                    "fs_id"  : 1074701728574105,
                    "name"   : "The Bourne Supremacy 1997.mp4",
                    "type"   : "video",
                    "size"   : 1087005586,
                    "image"  : "https://data.terabox.com/thumbnail/9b1a9....",
                    "list"   : []
                }
            ]
        }
    ]
}
```

<br><br><br><br>

## Get Download/Stream Links For Each File

To get a download/stream link for a file, send a `POST` request to the [`/generate_link`](https://teradl-api.dapuntaratya.com/generate_link) endpoint with the following parameters :
- `uk` is the user ID of the file owner *(obtained from the previous request)*
- `shareid` is the ID of the shared folder *(obtained from the previous request)*
- `timestamp` is the timestamp *(obtained from the previous request)*
- `sign` is the hash signature to authenticate access to the file *(obtained from the previous request)*
- `fs_id` is the unique ID of the file to be downloaded *(obtained from the previous request)*

<br>

**`linux (terminal)`**
```sh
curl -X POST "https://teradl-api.dapuntaratya.com/generate_link" \
  -H "Content-Type: application/json" \
  -d '{"uk":4399535305786,"shareid":4095377511,"timestamp":1744294847,"sign":"0f7aa2dc4d7373e307241b7eb1e5c8f55a58dd21","fs_id":56206195934797}'
```

**`python`**
```py
import requests

response = requests.post(
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
```

**`javascript`**
```js
const fetchData = async () => {
    const response = await fetch(
        "https://teradl-api.dapuntaratya.com/generate_link",
        {
            method  : "POST",
            headers : {"Content-Type":"application/json"},
            body    : JSON.stringify({
                "uk"        : 4399535305786,
                "shareid"   : 4095377511,
                "timestamp" : 1744294847,
                "sign"      : "0f7aa2dc4d7373e307241b7eb1e5c8f55a58dd21",
                "fs_id"     : 56206195934797,
            })
        }
    );
    const data = await response.json();
};

fetchData();
```

<br>

Upon success, you will receive the following JSON response :

**`response`**
```json
{
    "status": "success",
    "download_link": {
        "url_1": "https://d-jp02-zen.terabox.com/file/88841...",
        "url_2": "https://fragrant-term-0df9.elviraeducational.workers.dev/?url=aHR0cHMlM..."
    }
}
```

<br><br><br>

### Notes

> [!TIP]  
> If you want to run locally, make sure `flask_app.py` is run  
> Then run *live-server* or *localhost* on `index.html`  

> [!WARNING]  
> This platform only works for links related to Terabox  
> Example: `1024terabox`, `freeterabox`, `nephobox`, and others  

> [!CAUTION]  
> Do not abuse, use it wisely !  
> All actions are the responsibility of the user  