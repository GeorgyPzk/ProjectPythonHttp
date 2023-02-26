#print(f'Hello, {req.encoding}!{req.status_code} How are you?')
#SELECT * FROM lampdb2.Telemetry ORDER BY id DESC;

import requests
import mysql.connector
from mysql.connector import Error

# Define new data to create
new_data = {
    "musicbox_id": 284,
    "telemetry": {"dt":"2023-02-12 12:48:08","system":"android","cpu_temperature":"51.0","device_os":"7.1.1","mac":"02:00:00:44:55:66"}
}

# The API endpoint to communicate with
url_post = "http://lampvideo.ru/api/v1/telemetry.php"

get_response = requests.get(url_post)
if get_response.status_code == 200:
    print('Success!')
elif get_response.status_code != 200:
    print('Error!')
    print(get_response.status_code)

# A POST request to tthe API
post_response = requests.post(url_post, json=new_data)

# Print the response
post_response_json = post_response.json()
print(post_response_json)

########################################################################

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
