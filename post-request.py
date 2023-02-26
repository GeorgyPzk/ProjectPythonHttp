import requests

# Define new data to create
new_data = {
    "userID": 1,
    "id": 1,
    "title": "Making a POST request",
    "body": "This is the data we created."
}

# The API endpoint to communicate with
url_post = "https://jsonplaceholder.typicode.com/posts"

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

"""
{'userID': 1, 'id': 101, 'title': 'Making a POST request', 'body': 'This is the data we created.'}
"""