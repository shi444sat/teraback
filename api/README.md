# API Documentation

**`Domain`** : [`teradl-api.dapuntaratya.com`](https://teradl-api.dapuntaratya.com)  
**`Endpoint`** : [`/generate_file`](https://teradl-api.dapuntaratya.com/generate_file) [`/generate_link`](https://teradl-api.dapuntaratya.com/generate_link)

Konten
- [Mendapatkan Semua Daftar File](#mendapatkan-semua-daftar-file)
- [Mendapatkan Link Download/Stream Dari Tiap File](#mendapatkan-link-downloadstream-dari-tiap-file)
- [Catatan](#catatan)

<br><br><br>

## Mendapatkan Semua Daftar File

Untuk mendapat semua daftar file, kirim permintaan `POST` ke endpoint [`/generate_file`](https://teradl-api.dapuntaratya.com/generate_file) dengan parameter berikut :
- `url` adalah target link terabox yang akan diunduh

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

Setelah berhasil, anda akan menerima tanggapan JSON berikut :

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

## Mendapatkan Link Download/Stream Dari Tiap File

Untuk mendapat link download/stream dari suatu file, kirim permintaan `POST` ke endpoint [`/generate_link`](https://teradl-api.dapuntaratya.com/generate_link) dengan parameter berikut :
- `uk` adalah user ID dari pemilik file *(didapat dari permintaan sebelumnya)*
- `shareid` adalah ID dari folder yang dibagikan *(didapat dari permintaan sebelumnya)*
- `timestamp` merupakan penanda waktu *(didapat dari permintaan sebelumnya)*
- `sign` adalah signature hash untuk autentikasi akses ke file *(didapat dari permintaan sebelumnya)*
- `fs_id` adalah ID unik dari file yang ingin diunduh *(didapat dari permintaan sebelumnya)*

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

Setelah berhasil, anda akan menerima tanggapan JSON berikut :

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

## Catatan

> [!TIP]  
> Jika ingin menjalankan di local, pastikan `flask_app.py` sudah di-run  
> Lalu jalankan *live-server* atau *localhost* pada `index.html`

> [!WARNING]  
> Platform ini hanya berfungsi untuk link yang berkaitan dengan Terabox  
> Contoh : `1024terabox`, `freeterabox`, `nephobox`, dan lainnya

> [!CAUTION]  
> Jangan abuse, gunakan sewajarnya !  
> Segala tindakan adalah tanggung jawab pengguna  