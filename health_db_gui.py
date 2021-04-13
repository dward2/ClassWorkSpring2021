import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, simpledialog, messagebox
from health_db_client import make_post_request_to_add_patient
from image_handler import send_image_to_server


from PIL import Image, ImageTk


def design_window():

    def cancel_command():
        print("Cancel")
        root.destroy()
        return

    def ok_command():
        # Get Data From GUI
        p_name = donor_name.get()
        p_id = patient_id.get()
        p_blood = blood_letter.get()
        p_rh = rh_factor.get()
        # Call an outside function to do the work on that data
        result = make_post_request_to_add_patient(p_name, p_id, p_blood, p_rh)
        # Modify GUI in response to function result
        status.configure(text=result)
        return

    def change_picture_cmd():
        filename = filedialog.askopenfilename(initialdir="C:/")
        if filename == "":
            return
        pil_image = Image.open(filename)
        tk_image = ImageTk.PhotoImage(pil_image)
        image_label.configure(image=tk_image)
        image_label.image = tk_image
        send_image_to_server(filename)
        messagebox.showinfo("My Program", "Picture changed")

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

    pil_image = Image.open("acl1.jpg")
    image_size = pil_image.size
    adj_factor = 1
    new_width = round(image_size[0] * adj_factor)
    new_height = round(image_size[1] * adj_factor)
    new_size_image = pil_image.resize((new_width, new_height))
    tk_image = ImageTk.PhotoImage(new_size_image)
    image_label = ttk.Label(root, image=tk_image)
    image_label.image = tk_image
    image_label.grid(column=1, row=7)

    change_picture_btn = ttk.Button(root, text="Change Picture",
                                    command=change_picture_cmd)
    change_picture_btn.grid(column=2, row=7)

    root.mainloop()


if __name__ == "__main__":
    design_window()
