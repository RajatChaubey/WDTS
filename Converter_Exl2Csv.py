import subprocess
import xlrd
import csv

out = subprocess.Popen('ls -lrt *CMTBuilder*', shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

stdout,stderr = out.communicate()
print "This is CMT EXL which will be converted to CSV:",(stdout.split()[8])


def csv_from_excel():

    wb = xlrd.open_workbook(stdout.split()[8])
    sh = wb.sheet_by_name('ALARMS')
    your_csv_file = open('Alarms.csv', 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

csv_from_excel();
