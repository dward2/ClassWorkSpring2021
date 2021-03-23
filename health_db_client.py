import requests

patient = {"name": "Keith",
            "id": 8,
            "blood_type": "AX+"}

r = requests.post("http://127.0.0.1:5000/new_patient", json=patient)
print(r.status_code)
print(r.text)