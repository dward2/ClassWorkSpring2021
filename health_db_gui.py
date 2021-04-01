import tkinter as tk
from tkinter import ttk


def design_window():
    root = tk.Tk()
    root.title("Blood Donor Database")
    # root.geometry("500x300")

    top_label = ttk.Label(root, text="Blood Donor Database")
    top_label.grid(column=0, row=0, columnspan=2, sticky='w')
    print(type(top_label))

    ttk.Label(root, text="Name:").grid(column=0, row=1, sticky=tk.E)
    donor_name = tk.StringVar()
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


    root.mainloop()


if __name__ == "__main__":
    design_window()

