from pymodm import MongoModel, fields, connect

connect("mongodb+srv://spring2021:OAqFeWjqw0FWZucD@"
            "bme547.ba348.mongodb.net/health_db?retryWrites=true&w=majority")


# class Patient(MongoModel):
#     name = fields.CharField()
#     id_no = fields.IntegerField(primary_key=True)
#     blood_type = fields.CharField()
#     test = fields.ListField()
from patient_class import Patient

def get_all_patients():
    for patient in Patient.objects.raw({}):
        print(patient.name)


def add_patient():
    new_patient = Patient(name="Dave12", id_no=22)
    new_patient.save()
    new_patient.print_name()


if __name__ == '__main__':
    add_patient()
    get_all_patients()
