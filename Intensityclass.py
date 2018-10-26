import xlrd
from xlwt import Workbook


def classif( a, b, c):
    if b >= 5.0 and b < 6.0:
        if a >= 0.0 and a <= 25.0:
            if c >= 0 and c <= 100:
                return 1
        if a > 25 and a <= 50:
            if c >= 0 and c <= 100:
                return 1
        if a > 50 and a <= 100 :
            if c >= 0 and c <= 100:
                return 1
        if a > 100 and a <= 1000:
            if c >= 0 and c <= 100:
                return 1

        if a >= 0 and a <= 25:
            if c > 100 and c <= 500:
                return 1
        if a > 25 and a <= 50:
            if c > 100 and c <= 500:
                return 1
        if a > 50 and a <= 100:
            if c > 100 and c <= 500:
                return 1
        if a > 100 and a <= 1000:
            if c > 100 and c <= 500:
                return 0

        if a >= 0 and a <= 25:
            if c > 500 and c <= 1000:
                return 1
        if a > 25 and a <= 50:
            if c > 500 and c <= 1000:
                return 0
        if a > 50 and a <= 100:
            if c > 500 and c <= 1000:
                return 0
        if a > 100 and a <= 1000:
            if c > 500 and c <= 1000:
                return 0

        if a >= 0 and a <= 25:
            if c > 1000 and c <= 44000:
                return 0
        if a > 25 and a <= 50:
            if c > 1000 and c <= 44000:
                return 0
        if a > 50 and a <= 100:
            if c > 1000 and c <= 44000:
                return 0
        if a > 100 and a <= 1000:
            if c > 1000 and c <= 44000:
                return 0

    if b >= 6.0 and b < 7.0:
        if a >= 0.0 and a <= 25.0:
            if c >= 0 and c <= 100:
                return 2
        if a > 25 and a <= 50:
            if c >= 0 and c <= 100:
                return 2
        if a > 50 and a <= 100 :
            if c >= 0 and c <= 100:
                return 2
        if a > 100 and a <= 1000:
            if c >= 0 and c <= 100:
                return 2

        if a >= 0 and a <= 25:
            if c > 100 and c <= 500:
                return 2
        if a > 25 and a <= 50:
            if c > 100 and c <= 500:
                return 2
        if a > 50 and a <= 100:
            if c > 100 and c <= 500:
                return 1
        if a > 100 and a <= 1000:
            if c > 100 and c <= 500:
                return 1

        if a >= 0 and a <= 25:
            if c > 500 and c <= 1000:
                return 1
        if a > 25 and a <= 50:
            if c > 500 and c <= 1000:
                return 1
        if a > 50 and a <= 100:
            if c > 500 and c <= 1000:
                return 1
        if a > 100 and a <= 1000:
            if c > 500 and c <= 1000:
                return 0

        if a >= 0 and a <= 25:
            if c > 1000 and c <= 44000:
                return 0
        if a > 25 and a <= 50:
            if c > 1000 and c <= 44000:
                return 0
        if a > 50 and a <= 100:
            if c > 1000 and c <= 44000:
                return 0
        if a > 100 and a <= 1000:
            if c > 1000 and c <= 44000:
                return 0

    if b >= 7.0 and b < 8.0:
        if a >= 0.0 and a <= 25.0:
            if c >= 0 and c <= 100:
                return 2
        if a > 25 and a <= 50:
            if c >= 0 and c <= 100:
                return 2
        if a > 50 and a <= 100 :
            if c >= 0 and c <= 100:
                return 2
        if a > 100 and a <= 1000:
            if c >= 0 and c <= 100:
                return 2

        if a >= 0 and a <= 25:
            if c > 100 and c <= 500:
                return 2
        if a > 25 and a <= 50:
            if c > 100 and c <= 500:
                return 2
        if a > 50 and a <= 100:
            if c > 100 and c <= 500:
                return 2
        if a > 100 and a <= 1000:
            if c > 100 and c <= 500:
                return 2

        if a >= 0 and a <= 25:
            if c > 500 and c <= 1000:
                return 2
        if a > 25 and a <= 50:
            if c > 500 and c <= 1000:
                return 1
        if a > 50 and a <= 100:
            if c > 500 and c <= 1000:
                return 1
        if a > 100 and a <= 1000:
            if c > 500 and c <= 1000:
                return 1

        if a >= 0 and a <= 25:
            if c > 1000 and c <= 44000:
                return 0
        if a > 25 and a <= 50:
            if c > 1000 and c <= 44000:
                return 0
        if a > 50 and a <= 100:
            if c > 1000 and c <= 44000:
                return 0
        if a > 100 and a <= 1000:
            if c > 1000 and c <= 44000:
                return 0

    if b >= 8.0 and b < 9.0:
        if a >= 0.0 and a <= 25.0:
            if c >= 0 and c <= 100:
                return 2
        if a > 25 and a <= 50:
            if c >= 0 and c <= 100:
                return 2
        if a > 50 and a <= 100 :
            if c >= 0 and c <= 100:
                return 2
        if a > 100 and a <= 1000:
            if c >= 0 and c <= 100:
                return 2

        if a >= 0 and a <= 25:
            if c > 100 and c <= 500:
                return 2
        if a > 25 and a <= 50:
            if c > 100 and c <= 500:
                return 2
        if a > 50 and a <= 100:
            if c > 100 and c <= 500:
                return 2
        if a > 100 and a <= 1000:
            if c > 100 and c <= 500:
                return 2

        if a >= 0 and a <= 25:
            if c > 500 and c <= 1000:
                return 2
        if a > 25 and a <= 50:
            if c > 500 and c <= 1000:
                return 2
        if a > 50 and a <= 100:
            if c > 500 and c <= 1000:
                return 1
        if a > 100 and a <= 1000:
            if c > 500 and c <= 1000:
                return 1

        if a >= 0 and a <= 25:
            if c > 1000 and c <= 44000:
                return 1
        if a > 25 and a <= 50:
            if c > 1000 and c <= 44000:
                return 1
        if a > 50 and a <= 100:
            if c > 1000 and c <= 44000:
                return 1
        if a > 100 and a <= 1000:
            if c > 1000 and c <= 44000:
                return 0

    if b >= 9.0 and b < 10.0:
        if a >= 0.0 and a <= 25.0:
            if c >= 0 and c <= 100:
                return 2
        if a > 25 and a <= 50:
            if c >= 0 and c <= 100:
                return 2
        if a > 50 and a <= 100 :
            if c >= 0 and c <= 100:
                return 2
        if a > 100 and a <= 1000:
            if c >= 0 and c <= 100:
                return 2

        if a >= 0 and a <= 25:
            if c > 100 and c <= 500:
                return 2
        if a > 25 and a <= 50:
            if c > 100 and c <= 500:
                return 2
        if a > 50 and a <= 100:
            if c > 100 and c <= 500:
                return 2
        if a > 100 and a <= 1000:
            if c > 100 and c <= 500:
                return 2

        if a >= 0 and a <= 25:
            if c > 500 and c <= 1000:
                return 2
        if a > 25 and a <= 50:
            if c > 500 and c <= 1000:
                return 2
        if a > 50 and a <= 100:
            if c > 500 and c <= 1000:
                return 2
        if a > 100 and a <= 1000:
            if c > 500 and c <= 1000:
                return 2

        if a >= 0 and a <= 25:
            if c > 1000 and c <= 4400:
                return 1
        if a > 25 and a <= 50:
            if c >1000 and c <= 44000:
                return 1
        if a > 50 and a <= 100:
            if c > 1000 and c <= 44000:
                return 1
        if a > 100 and a <= 1000:
            if c > 1000 and c <= 44000:
                return 0


loc = "E:\Workspace\Codefundoo\database1.xlsx"
wb = xlrd.open_workbook(loc)
sh = wb.sheet_by_index(0)

wb = Workbook()
sheet1 = wb.add_sheet('sheet1')

for i in range (60000, 117060):
    intensity = classif(sh.cell_value(i, 2), sh.cell_value(i, 3), sh.cell_value(i, 4))
    sheet1.write(i-60000,0,intensity)

wb.save('op1.xls')