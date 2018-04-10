

## filetype and mimety
AUTHORIZED_FILETYPES = [

	('csv', 	'data', 	'text/csv'),
	('json', 	'data', 	'application/json'),
	('ods', 	'data', 	'application/vnd.oasis.opendocument.spreadsheet'),
	('xls', 	'data', 	'application/vnd.ms-excel'),
	('xlsx', 	'data', 	'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),

	('jpg', 	'images', 	'image/jpeg'),
	('jpeg', 	'images', 	'image/jpeg'),
	('png', 	'images', 	'image/png'),

	('pdf', 	'files', 	'application/pdf'),
	('odt', 	'files', 	'application/vnd.oasis.opendocument.text'),
	('doc', 	'files', 	'application/msword'),
	('docx', 	'files', 	'application/vnd.openxmlformats-officedocument.wordprocessingml.document'),
]

AUTHORIZED_FILETYPES_LIST = [ i[0] for i in AUTHORIZED_FILETYPES ]

AUTHORIZED_FILETYPES_DICT = { i[0] : { 
										"folder" 	: i[1], 
										"mimetype"	: i[2] 
									} for i in AUTHORIZED_FILETYPES 
							}

