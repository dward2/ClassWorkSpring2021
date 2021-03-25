def test_add_patient_to_db():
    from health_db_server import add_patient_to_db
    from health_db_server import db
    name = "David Ward"
    id = 100
    blood_type = "O+"
    add_patient_to_db(name, id, blood_type)
    last_patient_in_db = db[-1]
    expected = {"name": name,
                "id": id,
                "blood_type": blood_type,
                "test": []}
    assert last_patient_in_db == expected
