#!/usr/bin/python 
import os;
import cx_Oracle;
import openpyxl;
#print 'here is output :';
#ot=os.system('ls -lrt /opt/home/netx/backups/pa | tail -n 1');

#os.system('y | sh /opt/home/netx/backups/pa/Master-GWA-SNMP.2019-02-19.0/PA/GWA-SNMP.sh')


#Establishing DB connection
connstr='h3ghscqa/h3ghscqa@10.32.0.158:1521/h3g12cr'
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()
curs.arraysize=100

#######################################

def Test_result(status, cellno):
    print 'This is to check the values of status n cellno : ',status, cellno
    xfile = openpyxl.load_workbook('TestReport-fm_sams_enodeb_snmp_nr7.0.0.xlsx')

    sheet = xfile.get_sheet_by_name('Scorecard')
    sheet[cellno] = status
    xfile.save('TestReport-fm_sams_enodeb_snmp_nr7.0.0.xlsx')
##################################################

print "\n                            Excectuing TC-001:: \n" 


#curs.execute("select MOID,STRVALUE from MOATT where STRVALUE in ('fm_sams_enodeb_snmp_nr7.0.0-samsung-mib','GWA-SNMP-TRAP-162')")
curs.execute("select MO,CLASS,NAME from MO where NAME like '%fm_sams_enodeb_snmp_nr7.0.0-samsung-mib%' or Name like '%GWA-SNMP-TRAP-162%'")
for column_1, column_2, column_3 in curs.fetchall():
        print column_1, "\t", column_2, "\t",column_3 

        if column_3=='PMO-fm_sams_enodeb_snmp_nr7.0.0-samsung-mib': 
           MOID=column_1
           print 'This MO is going to be your MOID',MOID
DATA = curs.rowcount
print 'This is row count of the executed query:',DATA


if DATA>2:
   print 'TC-001 :: PAAS'
   Test_result( status="PASS",cellno='G30' );
else:
   print 'TC-001:: FAIL'
   Test_result(status ="FAIL", cellno='G30');
#curs.close()


print "\n                             Excectuing TC-002:: \n"

#curs.execute("select MOID,STRVALUE from MOATT where MOID='6134' and STRVALUE in ('fm_sams_enodeb_snmp_nr7.0.0-samsung-mib') and strvalue!='null' ")
curs.execute("select MOID,STRVALUE from MOATT where MOID='29280' and strvalue!='null' and strvalue like '%1.3.6.1.4.1.236%' or strvalue like '%1\.3\.6\.1\.4\.1\.236\.%'")

print "MOID\tSTRVALUE\n"
for column_1, column_2 in curs.fetchall():
        print column_1, "\t", column_2
DATA = curs.rowcount
print '\n This is number of alarms as per CMT:',DATA -2 


if DATA -2 ==11:
   print 'TC-002 :: PAAS'
   Test_result( status="PASS",cellno='G36' );
else:
   print 'TC-002:: FAIL'
   Test_result(status ="FAIL", cellno='G36');


print "\n                         Excectuing TC-003::...... \n"

curs.execute("select MOID,STRVALUE from MOATT where MOID='29280' and strvalue != 'null' and compid='-1'")


DATA1 = curs.rowcount
print '\n These are attributes of plugins in NetExpert:',DATA1

print "MOID\tSTRVALUE\n"
for column_1, column_2 in curs.fetchall():
       # print column_1, "\t", column_2
        if column_2 == 'vsaTempObjects_fm_sams_enodeb_snmp_nr7.0.0-samsung-mib' : 
            Test_result( status="PASS",cellno='G32' );
        if column_2 == 'PMO-fm_sams_enodeb_snmp_nr7.0.0-samsung-mib' :
            Test_result( status="PASS",cellno='G31' );
 
        print column_1, "\t", column_2


curs.close()

conn.close()









