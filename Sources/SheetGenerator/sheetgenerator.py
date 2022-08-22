import xlsxwriter
from hashlib import md5
from time import localtime
from schemas import CityDisplay
from typing import List


def add_prefix(username: str):
    prefix = md5(str(localtime()).encode('utf-8')).hexdigest()
    return f"{prefix}_{username}"


# Create an new Excel file and add a worksheet.
def newExcel(username: str, cities: List[CityDisplay]):

    name = add_prefix(username)
    workbook = xlsxwriter.Workbook(f'{name}.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})
    worksheet.set_column('A:D', 20)
    worksheet.write('A1', 'نام شهر', bold)
    worksheet.write('B1', 'دما', bold)
    worksheet.write('C1', 'رطوبت', bold)
    worksheet.write('D1', 'سرعت باد', bold)
    i = 2
    for city in cities:
        worksheet.write(f'A{i}', f'{city.persianname}')
        worksheet.write(f'B{i}', f'{city.temperature}')
        worksheet.write(f'C{i}', f'{city.humidity}')
        worksheet.write(f'D{i}', f'{city.windspeed}')
        i =+ 1

    workbook.close()
    return name +'.xlsx'


