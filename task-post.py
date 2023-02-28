#print(f'Hello, {req.encoding}!{req.status_code} How are you?')
#SELECT * FROM lampdb2.Telemetry ORDER BY id DESC;
import requests
import mysql.connector
from mysql.connector import Error
import time
import configparser

index='72'

#Read from .ini file
config = configparser.ConfigParser()
config.read('credentials.ini')

host = config['mysql']['host']
user = config['mysql']['user']
password = config['mysql']['password']
database = config['mysql']['database']

# Define new data to create
new_data = {
    "musicbox_id": 284,
    "telemetry": index
}

# The API endpoint to communicate with
url_post = "http://google.com"

get_response = requests.get(url_post)
if get_response.status_code == 200:
    print('POST success!')
elif get_response.status_code != 200:
    print('Error!')
    print(get_response.status_code)

# A POST request to the API
post_response = requests.post(url_post, json=new_data)
# Print the response
post_response_json = post_response.json()
print(post_response_json)

####################################################
#Working with DB
####################################################

print('Whait for process post request!')
time.sleep(10)
print('Go again!')

try:
    connection = mysql.connector.connect(host=host,
                                         database=database,
                                         user=user,
                                         password=password)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        #cursor.execute("select database();")
        #record = cursor.fetchone()
        #print("You're connected to database: ", record)

        #Select
        cursor.execute(f"SELECT telemetry FROM lampdb2.Telemetry WHERE musicbox_id = '284' AND telemetry = '\"{index}\"' ORDER BY id DESC LIMIT 1;")
        myresult = cursor.fetchall()
        y=0
        for x in myresult:
            y+=1
            print(f"y={y} value: {x}")
        if y == 1:
            print("DB filled. Post query work.")
        else:
            print(f"The data has not been recorded in the database. Post query did not work. y={y}")
        #Delite
        cursor.execute("DELETE FROM lampdb2.Telemetry WHERE musicbox_id = '284' AND telemetry = '\"72\"';")
        connection.commit()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
