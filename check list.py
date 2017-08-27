# test the logic of github
''' I need to try to code to load all sheet from my original Excel check list,
     it is seperated by different sheet.'''


import openpyxl

# define a function to print any sheet items
def print_check_point(sheet_name):
    ws=wb.get_sheet_by_name(sheet_name)
    i=ws.max_row
    for row in range(2,i+1):
        print(str(ws["A"+str(row)].value)," : " , str(ws["B"+str(row)].value))

#Start the main code
wb=openpyxl.load_workbook("database checking items.xlsx",data_only=True)
sheet_name=[]
for sheet_name in wb.get_sheet_names():
    print_check_point(sheet_name)
    print("----------------------------------------"+str(sheet_name) + "-----Finish---------------------------------------")
    print("")
