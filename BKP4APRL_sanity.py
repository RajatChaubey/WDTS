#!/usr/bin/python 
import os,shutil;
import cx_Oracle;
import openpyxl;
import sys;
import ReadCMT;
#print 'here is output :';
#ot=os.system('ls -lrt /opt/home/netx/backups/pa | tail -n 1');

#os.system('y | sh /opt/home/netx/backups/pa/Master-GWA-SNMP.2019-02-19.0/PA/GWA-SNMP.sh')

pname = sys.argv[1]
#alarm_count = sys.argv[2]
varb= "PMO-"+pname
print "\n This is passed plugin name on commandline:",pname , "\n This will be PMO: - ",varb

v,w,Plugin_name=ReadCMT.CMTvalues()
line=ReadCMT.Class_values()
print "These values are fetched from ReadCMT module-->called function CMTvalues:",v,w,Plugin_name
print "These values are fetched from ReadCMT module-->called function Class_values:",line

#Establishing DB connection
connstr='h3ghscqa/h3ghscqa@10.32.0.158:1521/h3g12cr'
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()
curs.arraysize=100

#######################################

def Test_result(status, cellno):
    print 'This is to check the values of status n cellno:',status, cellno,"\n"
    #xfile = openpyxl.load_workbook('TestReport-fm_sams_enodeb_snmp_nr7.0.0.xlsx')
    xfile = openpyxl.load_workbook('TestReport_Format.xlsx')

    sheet = xfile.get_sheet_by_name('Scorecard')
    sheet[cellno] = status
    xfile.save('TestReport_Format.xlsx')
##################################################

print "\n                            Excectuing TC-001:: \n" 

#named_params = {'pn':"%fm_sams_enodeb_snmp_nr7.0.0-samsung-mib%"}
named_params = {}
named_params['pn'] = varb 
#named_params['ac'] = sys.argv[2]
#curs.execute("select MO,CLASS,NAME from MO where NAME=?",varb)
curs.execute('select MO,CLASS,NAME from MO where NAME like :pn',named_params)
#print curs.fetchall() 
for column_1, column_2, column_3 in curs.fetchall():
        print column_1, "\t", column_2, "\t",column_3
        if column_3==varb:
           ID=column_1
           print '\nThis MO is going to be your MOID',ID

#print curs.bindnames() 
#curs.execute("select MOID,STRVALUE from MOATT where STRVALUE in ('fm_sams_enodeb_snmp_nr7.0.0-samsung-mib','GWA-SNMP-TRAP-162')")
curs.execute("select MO,CLASS,NAME from MO where Name like '%GWA-SNMP-TRAP-162%'")
for column_1, column_2, column_3 in curs.fetchall():
        print column_1, "\t", column_2, "\t",column_3 
#DATA = curs.rowcount
#print 'This is row count of the executed query:',DATA
        if column_3=='GWA-SNMP-TRAP-162':
                  print 'TC-001 :: PAAS'
                  Test_result( status="PASS",cellno='G30' );


print "\n                             Excectuing TC-002:: \n"


named_param = {}
named_param['ac'] = ID
named_param['od'] = "%"+v+"%"
print "Printing Dictionary value to test :",named_param['ac']
print "Printing Dictionary value to test :",named_param['od']
curs.execute("select MOID,STRVALUE from MOATT where MOID=:ac  and strvalue!='null' and strvalue like :od ",named_param)
#curs.execute('select MOID,STRVALUE from MOATT where MOID=:ac  and strvalue!='null' and strvalue like :od or strvalue like '%1\.3\.6\.1\.4\.1\.236\.%'',named_param)

#curs.execute("select MOID,STRVALUE from MOATT where MOID=:ac  and strvalue!='null' and strvalue like :oid or strvalue like '%1\.3\.6\.1\.4\.1\.236\.%'",named_param)
#curs.execute('select MOID,STRVALUE from MOATT where strvalue like :od',named_param)


print "MOID\tSTRVALUE\n"
for column_1, column_2 in curs.fetchall():
        print column_1, "\t", column_2
DATA = curs.rowcount
print '\n This is number of alarms as of Now in ORACLE DB for particular Plugin name:',DATA 


if DATA  == w:
   print 'TC-002 :: PAAS'
   Test_result( status="PASS",cellno='G36' );
else:
   print 'TC-002:: FAIL'
   Test_result(status ="FAIL", cellno='G36');


print "\n                         Excectuing TC-003::...... \n"

curs.execute("select MOID,STRVALUE from MOATT where MOID='29280' and strvalue != 'null' and compid='-1'")

print "MOID\tSTRVALUE\n"
for column_1, column_2 in curs.fetchall():
       # print column_1, "\t", column_2
        if column_2 == 'vsaTempObjects_fm_sams_enodeb_snmp_nr7.0.0-samsung-mib' : 
            Test_result( status="PASS",cellno='G32' );
        if column_2 == 'PMO-fm_sams_enodeb_snmp_nr7.0.0-samsung-mib' :
            Test_result( status="PASS",cellno='G31' );
 
        print column_1, "\t", column_2
DATA1 = curs.rowcount
print '\n These are attributes of plugins in NetExpert:',DATA1

curs.close()
conn.close()

os.rename("TestReport_Format.xlsx", "TestReport_"+Plugin_name+"."+"xlsx")
execfile("Email.py")
#shutil.copy( "/opt/home/netx/RAJAT_AUTOMATION//CMT_Folder/TestReport_Format.xlsx", "/opt/home/netx/RAJAT_AUTOMATION/TestReport_Format.xlsx") 







