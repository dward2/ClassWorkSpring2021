def test_add_patient_to_db():
    from health_db_server import add_patient_to_db
    name = "David Ward"
    id = 100
    blood_type = "O+"
    add_patient_to_db(name, id, blood_type)
