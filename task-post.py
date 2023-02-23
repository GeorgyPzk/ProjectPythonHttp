#print(f'Hello, {req.encoding}!{req.status_code} How are you?')
#SELECT * FROM lampdb2.Telemetry ORDER BY id DESC;

import requests

# Define new data to create
new_data = {
    "musicbox_id": 284,
    "telemetry": {"dt":"2023-02-12 12:48:08","system":"android","cpu_temperature":"51.0","device_os":"7.1.1","mac":"02:00:00:44:55:66"}
}

# The API endpoint to communicate with
url_post = "http://lampvideo.ru/api/v1/telemetry.php"

# A POST request to tthe API
post_response = requests.post(url_post, json=new_data)

# Print the response
post_response_json = post_response.json()
print(post_response_json)
