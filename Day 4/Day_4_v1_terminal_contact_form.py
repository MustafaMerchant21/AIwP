import os

import ContactRepo.config as config
from ContactRepo.create_or_load_workbook import create_or_load_workbook as clw


def get_workbook_sheet():
	wb = clw(config.FILE_NAME)
	return wb, wb.active


def get_next_id(sheet):
	ids = [row[0].value for row in sheet.iter_rows(min_row=2) if isinstance(row[0].value, int)]
	return (max(ids) + 1) if ids else 1


def validate_data(name, email, country_code, phone_number):
	name = name.strip()
	email = email.strip()
	country_code = country_code.strip()
	phone_number = phone_number.strip()

	if not name or len(name) < 3 or not config.NAME_PATTERN.fullmatch(name):
		print("Invalid full name. Use 3+ letters with spaces, apostrophes, hyphens, or dots.")
		return False
	if not email or len(email) > 254 or not config.EMAIL_PATTERN.fullmatch(email):
		print("Invalid email address.")
		return False
	if country_code and not config.COUNTRY_CODE_PATTERN.fullmatch(country_code):
		print("Invalid country code. Use 1 to 4 digits and do not start with 0.")
		return False
	if not config.PHONE_PATTERN.fullmatch(phone_number):
		print("Invalid phone number. Use 10 to 15 digits.")
		return False
	return True


def load_rows():
	wb, sheet = get_workbook_sheet()
	return list(sheet.iter_rows(min_row=2, values_only=True))


def find_row_by_id(sheet, record_id):
	for row in sheet.iter_rows(min_row=2):
		if row[0].value == record_id:
			return row
	return None


def print_rows(rows):
	if not rows:
		print("No records found.")
		return

	header = f"{'ID':<6} {'Name':<24} {'Email':<30} {'Code':<8} {'Phone Number':<15}"
	print(header)
	print("-" * len(header))
	for row in rows:
		print(f"{row[0]:<6} {str(row[1])[:23]:<24} {str(row[2])[:29]:<30} {str(row[3]):<8} {str(row[4]):<15}")


def list_contacts():
	rows = load_rows()
	print_rows(rows)


def search_contacts():
	query = input("Search by name, email, or phone: ").strip().lower()
	rows = [
		row for row in load_rows()
		if query in str(row[1]).lower() or query in str(row[2]).lower() or query in str(row[4]).lower()
	]
	print_rows(rows)


def add_contact():
	name = input("Full name: ").strip()
	email = input("Email: ").strip()
	country_code = input("Country code (default 91): ").strip() or "91"
	phone_number = input("Phone number: ").strip()

	if not validate_data(name, email, country_code, phone_number):
		return

	wb, sheet = get_workbook_sheet()
	record_id = get_next_id(sheet)
	sheet.append([record_id, name, email, country_code, phone_number])
	wb.save(config.FILE_NAME)
	print(f"Saved record ID {record_id}.")


def update_contact():
	try:
		record_id = int(input("Record ID to update: ").strip())
	except ValueError:
		print("Record ID must be a positive whole number.")
		return

	wb, sheet = get_workbook_sheet()
	row = find_row_by_id(sheet, record_id)
	if row is None:
		print("Record ID not found.")
		return

	print("Press Enter to keep the current value.")
	name = input(f"Full name [{row[1].value}]: ").strip() or str(row[1].value)
	email = input(f"Email [{row[2].value}]: ").strip() or str(row[2].value)
	country_code = input(f"Country code [{row[3].value}]: ").strip() or str(row[3].value)
	phone_number = input(f"Phone number [{row[4].value}]: ").strip() or str(row[4].value)

	if not validate_data(name, email, country_code, phone_number):
		return

	row[1].value = name
	row[2].value = email
	row[3].value = country_code
	row[4].value = phone_number
	wb.save(config.FILE_NAME)
	print(f"Updated record ID {record_id}.")


def delete_contact():
	try:
		record_id = int(input("Record ID to delete: ").strip())
	except ValueError:
		print("Record ID must be a positive whole number.")
		return

	wb, sheet = get_workbook_sheet()
	row = find_row_by_id(sheet, record_id)
	if row is None:
		print("Record ID not found.")
		return

	sheet.delete_rows(row[0].row, amount=1)
	wb.save(config.FILE_NAME)
	print(f"Deleted record ID {record_id}.")


def pause():
	input("\nPress Enter to continue...")


def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")


def main():
	while True:
		clear_screen()
		print("CONTACT FORM MANAGER")
		print("1. Add contact")
		print("2. View all contacts")
		print("3. Search contacts")
		print("4. Update contact")
		print("5. Delete contact")
		print("6. Exit")

		choice = input("\nChoose an option: ").strip()
		clear_screen()

		if choice == "1":
			add_contact()
			pause()
		elif choice == "2":
			list_contacts()
			pause()
		elif choice == "3":
			search_contacts()
			pause()
		elif choice == "4":
			update_contact()
			pause()
		elif choice == "5":
			delete_contact()
			pause()
		elif choice == "6":
			print("Goodbye.")
			break
		else:
			print("Invalid choice.")
			pause()


if __name__ == "__main__":
	main()