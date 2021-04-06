from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def starting_form():
    my_data = ""
    warning = True
    patients = ["Dave", "Luca", "Keshav"]
    if request.method == "POST":
        patient_name = request.form["name"]
        patient_id = request.form["patient_id"]
        blood_letter = request.form["Blood_Letter"]
        rh_positive = request.form.get("rh_positive")
        donation_center = request.form["donation_center"]
        print("Patient name is {}".format(patient_name))
        print("Patient id is {}".format(patient_id))
        print("Patient blood type is {}".format(blood_letter))
        print("Patient rh factor is {}".format(rh_positive))
        print("Patient donation center is {}".format(donation_center))
        my_data = "Patient id {} information entered".format(patient_id)
        if rh_positive == "+":
            warning = False
        return redirect(url_for("success_function"))

    query_string = request.query_string.decode()
    print(query_string)

    return render_template("health_db_web_gui.html",
                           my_data=my_data,
                           warning=warning,
                           patients=patients)


@app.route("/success", methods=["GET"])
def success_function():
    return render_template("success.html")



if __name__ == '__main__':
    app.run()
