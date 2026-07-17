def update_data(sheet, target, updated_data=[]):
	if sheet is None or not target or not updated_data:
		return False

	for row in sheet.iter_rows(min_row=2):
		if row[0].value == target:
			for cell, value in zip(row, updated_data):
				cell.value = value
			sheet.parent.save(sheet.parent.filename)
			return True

	return False