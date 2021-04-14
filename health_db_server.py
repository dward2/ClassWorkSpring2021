from flask import Flask, request, jsonify
import logging
from pymodm import connect
from pymodm import errors as pymodm_errors
from patient_class import Patient
# ***** Added for Image Handling Routes *****
from image_record_class import ImageRecord


logging.basicConfig(filename="server.log", level=logging.INFO)

app = Flask(__name__)


def init_server():
    print("Connecting to MongoDB...")
    connect("mongodb+srv://spring2021:OAqFeWjqw0FWZucD@"
            "bme547.ba348.mongodb.net/health_db?retryWrites=true&w=majority")
    print("Connected.")


def add_patient_to_db(name_in, id, blood_type):
    new_patient = Patient(name=name_in,
                          id_no=id,
                          blood_type=blood_type)
    saved_patient = new_patient.save()
    logging.info("Added new patient id {} to database"
                 .format(saved_patient.id_no))
    return saved_patient


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    # get input data from requests
    in_data = request.get_json()

    # validate input & process patient
    answer, server_status = process_new_patient(in_data)

    # Return/display results
    return answer, server_status


def validate_blood_type(in_data):
    blood_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    if in_data["blood_type"] not in blood_types:
        return "{} is not a valid blood type".format(in_data["blood_type"])
    return True


def validate_new_patient_info(in_dict):
    expected_keys = ("name", "id", "blood_type")
    expected_types = (str, int, str)
    for key, ty in zip(expected_keys, expected_types):
        if key not in in_dict.keys():
            return "{} key not found".format(key), 400
        if type(in_dict[key]) != ty:
            return "{} key has the wrong value type".format(key), 400
    return True, 200


def process_new_patient(in_data):
    validate_input, server_status = validate_new_patient_info(in_data)
    if validate_input is not True:
        return validate_input, server_status
    valid_blood_type = validate_blood_type(in_data)
    if valid_blood_type is not True:
        return valid_blood_type, 400

    # define new patient dictionary
    add_patient_to_db(in_data["name"],
                      in_data["id"],
                      in_data["blood_type"])
    return "Patient successfully added", 200


@app.route("/add_test", methods=["POST"])
def post_add_test():
    in_data = request.get_json()
    result, server_status = process_add_test(in_data)
    return result, server_status


def process_add_test(in_data):
    validate_input, server_status = validate_add_test_info(in_data)
    if validate_input is not True:
        return validate_input, server_status
    valid_patient_id = validate_patient_id(in_data["id"])
    if valid_patient_id is False:
        return "Patient id {} does not exist".format(in_data["id"]), 400
    add_patient_test_data(in_data)
    return "Test data successfully added", 200


def validate_add_test_info(in_dict):
    expected_keys = ("id", "test_name", "test_result")
    expected_types = (int, str, int)
    for key, ty in zip(expected_keys, expected_types):
        if key not in in_dict.keys():
            return "{} key not found".format(key), 400
        if type(in_dict[key]) != ty:
            return "{} key has the wrong value type".format(key), 400
    return True, 200


def validate_patient_id(patient_id):
    try:
        db_item = Patient.objects.raw({"_id": patient_id}).first()
    except pymodm_errors.DoesNotExist:
        return False
    return True


def add_patient_test_data(in_data):
    try:
        db_item = Patient.objects.raw({"_id": in_data["id"]}).first()
    except pymodm_errors.DoesNotExist:
        return False
    new_test = (in_data["test_name"], in_data["test_result"])
    db_item.test.append(new_test)
    updated_patient = db_item.save()
    return updated_patient


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_results(patient_id):
    validation_info, server_status = \
        validate_variable_url_patient_id(patient_id)
    if server_status != 200:
        return validation_info, server_status
    patient = get_patient_from_db(validation_info)
    patient_info = {"name": patient.name,
                    "id": patient.id_no,
                    "blood_type": patient.blood_type,
                    "tests": patient.test}
    return jsonify(patient_info), 200


def validate_variable_url_patient_id(patient_id):
    try:
        id_int = int(patient_id)
    except ValueError:
        return "{} is not a valid patient id".format(patient_id), 400
    valid_patient_id = validate_patient_id(id_int)
    if valid_patient_id is False:
        return "Patient id {} does not exist in database".format(id_int), 400
    return id_int, 200


def get_patient_from_db(patient_id):
    try:
        db_item = Patient.objects.raw({"_id": patient_id}).first()
    except pymodm_errors.DoesNotExist:
        return False
    return db_item


"""
************* Image Handling Routes ***************
"""


@app.route("/add_image", methods=["POST"])
def add_image():
    in_data = request.get_json()
    result, status = process_add_image(in_data)
    return result, status


def process_add_image(in_data):
    validate_message, status = validate_input(in_data,
                                              ["image", "net_id", "id_no"],
                                              [str, str, int])
    if status != 200:
        return validate_message, status
    if get_image_from_database(in_data) is not False:
        return "Image id {} already exists for net_id {}"\
                   .format(in_data["id_no"], in_data["net_id"]), 400
    reply = add_image_to_database(in_data)
    try:
        return_string = "Image successfully added as id_no {}"\
            .format(reply.id_no)
    except AttributeError:
        return "Problem with save to database", 400
    return return_string, 200


def validate_input(in_data, keys, types):
    for key, in_type in zip(keys, types):
        if key not in in_data:
            return "Missing key {} in post".format(key), 400
        if type(in_data[key]) is not in_type:
            return "Key {} is of incorrect type".format(key), 400
    return True, 200


def get_image_from_database(in_data):
    try:
        record = ImageRecord.objects.raw({"$and":
                                          [{"net_id": in_data["net_id"]},
                                           {"id_no": in_data["id_no"]}
                                           ]
                                          }).first()
    except pymodm_errors.DoesNotExist:
        return False
    return record


def add_image_to_database(in_data):
    record = ImageRecord(net_id=in_data["net_id"],
                         id_no=in_data["id_no"],
                         image=in_data["image"])
    reply = record.save()
    return reply


@app.route("/get_image/<net_id>/<id_no>", methods=["GET"])
def get_image(net_id, id_no):
    b64_string, status = process_get_image(net_id, id_no)
    return b64_string, status


def process_get_image(net_id, id_no):
    validate_result, status = validate_id_no(id_no)
    if status == 200:
        id_no = validate_result
    else:
        return validate_result, status
    search_data = {"net_id": net_id, "id_no": id_no}
    image_record = get_image_from_database(search_data)
    if image_record is False:
        return "No image with id {} found for net id {}"\
                   .format(id_no, net_id), 400
    return image_record.image, 200


def validate_id_no(id_no):
    try:
        id_int = int(id_no)
    except ValueError:
        return "id_no given is not a valid integer", 400
    return id_int, 200


if __name__ == '__main__':
    init_server()
    app.run()
