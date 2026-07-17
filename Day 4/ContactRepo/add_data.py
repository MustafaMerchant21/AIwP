from . import create_or_load_workbook as clw
from . import delete_data as dlt
from . import config
def add_data(name, email, country_code, phone_number):
	wb = clw.create_or_load_workbook(config.FILE_NAME)
	sheet = wb.active

	config.COUNT += 1
	sheet.append([config.COUNT, name, email, country_code, phone_number])
	wb.save(config.FILE_NAME)
	dlt.delete_data(sheet, id)