import requests

def make_post_request_to_add_patient(p_name, p_id, p_blood, p_rh):

    id_int = convert_id_to_int(p_id)
    # if id_int is not int:
    #     return id_int

    patient = {"name": p_name,
                "id": id_int,
                "blood_type": "{}{}".format(p_blood, p_rh)}

    r = requests.post("http://127.0.0.1:5000/new_patient", json=patient)
    print(r.status_code)
    print(r.text)
    return r.text

def convert_id_to_int(p_id):
    try:
        id_int = int(p_id)
    except ValueError:
        return "id was not an integer"
    return id_int

# new_test = {"id": 8,
#             "test_name": "HDL",
#             "test_result": 77}
# r = requests.post("http://127.0.0.1:5000/add_test", json=new_test)
# print(r.status_code)
# print(r.text)
#
# r = requests.get("http://127.0.0.1:5000/get_results/8")
# print(r.status_code)
# print(r.text)

