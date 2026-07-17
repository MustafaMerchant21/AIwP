def delete_data(sheet, id):
	if sheet is None or id is None:
		return False

	target_id = id
	for row in sheet.iter_rows(min_row=2):
		if row[0].value == target_id:
			sheet.delete_rows(row[0].row, amount=1)
			sheet.parent.save(sheet.parent.filename)
			return True

	return False
