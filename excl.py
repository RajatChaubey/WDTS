#!/usr/bin/python
import openpyxl
xfile = openpyxl.load_workbook('TestReport-fm_sams_enodeb_snmp_nr7.0.0.xlsx')

sheet = xfile.get_sheet_by_name('Scorecard')
sheet['G30'] = 'PASS  RAJAT'
xfile.save('OUTPUT.xlsx')
