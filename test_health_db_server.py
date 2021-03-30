from health_db_server import init_server

init_server()


def test_add_patient_to_db():
    from health_db_server import add_patient_to_db
    name = "David Ward"
    id = 100
    blood_type = "O+"
    answer = add_patient_to_db(name, id, blood_type)
    answer.delete()
    assert answer.id_no == id


# def test_get_patient_from_db():
#     from health_db_server import get_patient_from_db
#     from health_db_server import db
#     test_patient = {"name": "Erica Emerson",
#                     "id": 200,
#                     "blood_type": "O-",
#                     "test": []}
#     db.append(test_patient)
#     answer = get_patient_from_db(200)
#     assert answer == test_patient
#
#
# def test_get_patient_from_db_missing():
#     from health_db_server import get_patient_from_db
#     from health_db_server import db
#     test_patient = {"name": "Erica Emerson",
#                     "id": 201,
#                     "blood_type": "O-",
#                     "test": []}
#     db.append(test_patient)
#     answer = get_patient_from_db(200)
#     assert answer is False
