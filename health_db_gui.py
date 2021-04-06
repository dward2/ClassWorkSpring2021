import tkinter as tk
from tkinter import ttk
import requests


def design_window():

    def cancel_command():
        print("Cancel")
        root.destroy()
        return

    def ok_command():
        p_id = patient_id.get()
        p_name = donor_name.get()
        p_blood_letter = blood_letter.get()
        p_rh = rh_factor.get()
        answer = make_new_patient_post_request(p_name, p_id, p_blood_letter,
                                               p_rh)
        status.configure(text=answer)
        return

    root = tk.Tk()
    root.title("Blood Donor Database")
    # root.geometry("500x300")

    top_label = ttk.Label(root, text="Blood Donor Database")
    top_label.grid(column=0, row=0, columnspan=2, sticky='w')
    print(type(top_label))

    ttk.Label(root, text="Name:").grid(column=0, row=1, sticky=tk.E)
    donor_name = tk.StringVar()
    donor_name.set("Enter your name here...")
    name_entry_box = tk.Entry(root, textvariable=donor_name, width=50)
    name_entry_box.grid(column=1, row=1, sticky=tk.W)

    ttk.Label(root, text="Id:").grid(column=0, row=2, sticky=tk.E)
    patient_id = tk.StringVar()
    id_entry_box = tk.Entry(root, textvariable=patient_id)
    id_entry_box.grid(column=1, row=2, sticky=tk.W)

    blood_letter = tk.StringVar()
    ttk.Radiobutton(root, text="A", variable=blood_letter,
                    value="A").grid(column=0, row=3, sticky=tk.W)
    ttk.Radiobutton(root, text="B", variable=blood_letter,
                    value="B").grid(column=0, row=4, sticky=tk.W)
    ttk.Radiobutton(root, text="AB", variable=blood_letter,
                    value="AB").grid(column=0, row=5, sticky=tk.W)
    ttk.Radiobutton(root, text="O", variable=blood_letter,
                    value="O").grid(column=0, row=6, sticky=tk.W)

    rh_factor = tk.StringVar()
    rh_check = ttk.Checkbutton(root, text='Rh Positive', variable=rh_factor,
                               onvalue='+', offvalue='-')
    rh_check.grid(column=1, row=4, sticky=tk.W)
    rh_factor.set("-")

    ttk.Label(root, text="Closest Donation Center").grid(column=2, row=0)
    donor_center = tk.StringVar()
    donor_center_combo = ttk.Combobox(root, textvariable=donor_center)
    donor_center_combo.grid(column=2, row=1)
    donor_center_combo["values"] = ("Durham", "Raleigh", "Cary", "Apex")
    donor_center_combo.state(["readonly"])

    cancel_button = ttk.Button(root, text="Cancel", command=cancel_command)
    cancel_button.grid(column=2, row=6)
    ok_button = ttk.Button(root, text="Ok", command=ok_command)
    ok_button.grid(column=1, row=6)

    status = ttk.Label(root, text="Status")
    status.grid(column=2, row=4)

    root.mainloop()


def make_new_patient_post_request(patient_name, patient_id, blood_letter,
                                  rh_factor):
    patient_id = int(patient_id)
    patient = {"name": patient_name,
               "id": patient_id,
               "blood_type": "{}{}".format(blood_letter, rh_factor)}

    r = requests.post("http://127.0.0.1:5000/new_patient", json=patient)
    print(r.status_code)
    print(r.text)
    return r.text


if __name__ == "__main__":
    design_window()
