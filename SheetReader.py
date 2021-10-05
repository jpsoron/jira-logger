import pandas
from WeeklyHours import WorkedHours

def sheet_reader(excelpath):
    workedhours = WorkedHours()
    data = pandas.read_excel(excelpath, "NO EDITAR")


    return workedhours

