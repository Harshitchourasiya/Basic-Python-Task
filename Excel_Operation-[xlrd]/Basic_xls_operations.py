#to write and read from xls file syntax

import xlwt
import xlrd
from xlutlis.copy import copy

workbookforreading = xlrd.open_workbook('mname.xls')

sheetforreading = workbookforreading.sheet_by_index(indextoread)

wb = copy(workbookforreading)

sheettowrite = wb.get_sheet(indextoread)

sheettowrite.write(row_number.column_number,"your data")
sheettowrite.save("nameofsheet.xls)
