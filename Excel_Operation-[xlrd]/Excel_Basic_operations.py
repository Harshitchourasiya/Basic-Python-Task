import xlrd
import xlwt
from xlutils.copy import copy

def write_xl(row,fields):
    rb = xlrd.open_workbook('student.xls',formating_info=True)
    r_sheet = rb.sheet_by_index(0)
   
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    sheet.write(r,0,fields["attendance"])
    wb.save("student.xls")
    print('wrote student.xls')

def read_xl(loc):
    workbook = xlrd.open_workbook("student.xls")
    sheet1 = workbook.sheet_by_index(0)
    cell = sheet1.cell(loc[0],loc[1])
    return str(cell.value)


def create_xl(name):
    workbook = xlwt.workbook()
    sheet = workbook.add_sheet(name)
    workbook.save(name+"xls")

if __name__=="__main__":
    fields =  {}
    print ("spreadsheet check : ")
    

loc = [0,0]
loc[0] = int (raw_input("1:"))
loc[1] = int (raw_input("2:"))
a=raw_input("Enter file name : ")
create_xl(a)
value = read_xl(loc)
print value
