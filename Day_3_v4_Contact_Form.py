import tkinter as tk


def submit_form():
	name = name_entry.get().strip()
	email = email_entry.get().strip()
	country_code = country_code_entry.get().strip()
	phone_number = phone_number_entry.get().strip()

	if name == "":
		message_label.config(text="Full name is required.", fg="red")
	elif email == "":
		message_label.config(text="Email is required.", fg="red")
	elif phone_number == "":
		message_label.config(text="Contact number is required.", fg="red")
	elif "@" not in email or "." not in email:
		message_label.config(text="Enter a valid email address.", fg="red")
	elif country_code != "" and not country_code.isdigit():
		message_label.config(text="Country code must contain only digits.", fg="red")
	elif not phone_number.isdigit():
		message_label.config(text="Phone number must contain only digits.", fg="red")
	elif len(phone_number) < 7:
		message_label.config(text="Phone number is too short.", fg="red")
	else:
		message_label.config(
			text=f"Saved: {name} | {email} | +{country_code} {phone_number}",
			fg="green",
		)


root = tk.Tk()
root.title("Contact Form")
root.geometry("500x320")
root.resizable(False, False)

title_label = tk.Label(root, text="Contact Form", font=("Arial", 20, "bold"))
title_label.pack(pady=15)

form_frame = tk.Frame(root)
form_frame.pack(pady=10)

tk.Label(form_frame, text="Full Name").grid(row=0, column=0, sticky="w", padx=10, pady=8)
name_entry = tk.Entry(form_frame, width=35)
name_entry.grid(row=0, column=1, padx=10, pady=8)

tk.Label(form_frame, text="Email").grid(row=1, column=0, sticky="w", padx=10, pady=8)
email_entry = tk.Entry(form_frame, width=35)
email_entry.grid(row=1, column=1, padx=10, pady=8)

tk.Label(form_frame, text="Contact Number").grid(row=2, column=0, sticky="w", padx=10, pady=8)
country_code_entry = tk.Entry(form_frame, width=6)
country_code_entry.grid(row=2, column=1, sticky="w", padx=(10, 0), pady=8)
country_code_entry.insert(0, "91")

phone_number_entry = tk.Entry(form_frame, width=25)
phone_number_entry.grid(row=2, column=1, padx=(70, 10), pady=8, sticky="w")

submit_button = tk.Button(root, text="Submit", command=submit_form, width=12)
submit_button.pack(pady=10)

message_label = tk.Label(root, text="", font=("Arial", 10))
message_label.pack(pady=5)

root.mainloop()
