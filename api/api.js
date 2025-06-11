const get_list_file = async () => {
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

const get_link_download = async () => {
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