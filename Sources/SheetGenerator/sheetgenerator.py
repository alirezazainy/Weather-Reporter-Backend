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
    workbook = xlsxwriter.Workbook(f'Files/{name}.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.set_column('A:D', 20)
    worksheet.write('A1', 'نام شهر')
    worksheet.write('B1', 'دما')
    worksheet.write('C1', 'رطوبت')
    worksheet.write('D1', 'سرعت باد')
    r = 2
    for city in cities:
        worksheet.write(f"A{r}", f'{city.persianname}')
        worksheet.write(f"B{r}", f'{city.temperature}')
        worksheet.write(f"C{r}", f'{city.humidity}')
        worksheet.write(f"D{r}", f'{city.windspeed}')
        r += 1

    workbook.close()
    return name +'.xlsx'


