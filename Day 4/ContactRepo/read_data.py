def read_data(sheet):
	if sheet is None:
		return []

	return list(sheet.iter_rows(values_only=True))