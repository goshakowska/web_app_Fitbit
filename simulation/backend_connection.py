import requests


# CONNECTION
def connection():
    api_url = "http://localhost:8000/simulation/test_connection/"
    headers = {"Content-Type": "application/json"}

    body = {"message": "We are connected"}

    try:
        response = requests.post(api_url, json=body, headers=headers)

        if response.status_code == 200:
            print("Success")
        else:
            print(f"Error response {response.status_code}  {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")


def get_clients():
    api_url = "http://localhost:8000/simulation/all_clients/"
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(api_url, headers=headers)
        if response.status_code == 200:
            return response.json().get('clients', [])
        else:
            print(f"Error response {response.status_code}  {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")


def get_gyms():
    api_url = "http://localhost:8000/simulation/all_gyms/"
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(api_url, headers=headers)
        if response.status_code == 200:
            return response.json().get('gyms', [])
        else:
            print(f"Error response {response.status_code}  {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")

def get_exercises():
    api_url = "http://localhost:8000/simulation/all_exercises/"
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(api_url, headers=headers)
        if response.status_code == 200:
            return response.json().get('exercises', [])
        else:
            print(f"Error response {response.status_code}  {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")

def get_trainers(gym_id):
    api_url = "http://localhost:8000/simulation/all_trainers/"
    headers = {"Content-Type": "application/json"}

    body = {"gym_id": gym_id}

    try:
        response = requests.post(api_url, json=body, headers=headers)

        if response.status_code == 200:
            return response.json().get('trainers', [])
        else:
            print(f"Error response {response.status_code}  {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")
