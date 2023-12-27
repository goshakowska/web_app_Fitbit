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


def get_clients(gym_id):
    api_url = "http://localhost:8000/simulation/all_clients/"
    headers = {"Content-Type": "application/json"}
    body = {"gym_id": gym_id}
    try:
        response = requests.post(api_url, json=body, headers=headers)
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

def get_equipments(gym_id, exercise_id):
    api_url = "http://localhost:8000/simulation/all_equipments/"
    headers = {"Content-Type": "application/json"}
    body = {"gym_id": gym_id, "exercise_id": exercise_id}
    try:
        response = requests.post(api_url, json=body, headers=headers)
        if response.status_code == 200:
            return response.json().get('equipments', [])
        else:
            print(f"Error response {response.status_code}  {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")

def insert_exercise_history(exercise_date, duration, repetitions_number, gym_id, exercise_id, equipment_id, client_id, calories, params):
    api_url = "http://localhost:8000/simulation/insert_exercise_history/"
    headers = {"Content-Type": "application/json"}

    body = {
        "exercise_date": exercise_date,
        "duration": duration,
        "repetitions_number": repetitions_number,
        "gym_id": gym_id,
        "exercise_id": exercise_id,
        "equipment_id": equipment_id,
        "client_id": client_id,
        "calories": calories,
        "params": params
        }

    try:
        response = requests.post(api_url, json=body, headers=headers)

        if response.status_code == 200:
            pass
        else:
            print(f"Error response {response.status_code}  {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")

