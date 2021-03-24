#!/usr/bin/python
import sys
import json
import requests 
## getting this when calling with Montgomery in response of URL "http://api.bart.gov/api/etd.aspx?cmd=etd&orig=Montgomery&key=MW9S-E7SL-26DU-VV8V&json=y".   reposnse -->  <details>The orig station parameter MONTGOMERY is missing or invalid.</details> 
def UP_comingTrains(source):
 conn="http://api.bart.gov/api/etd.aspx?cmd=etd&orig="+source+"&key=MW9S-E7SL-26DU-VV8V&json=y"
#print ("This is str",source)
 r1 = requests.get(conn)
 if (r1.status_code == 200 ):
    print (" All set Response is  OK:",r1.status_code,"\n") 
 else:
    sys.exit ("Seems something wrong Pls chk!!")
    


 with open(r'result.json','wb') as f:
     f.write(r1.content)
     
 
 info_dict = json.loads(r1.content)
 print (info_dict.items() ,"\n ")

 print ("----------------------------------------------------")
#print (info_dict['root']['time'])
 print (info_dict['root']['station'][0]['name'],"\t" ,info_dict['root'] ['time'])

 print ("----------------------------------------------------")
 #for i in range(0,2):
  #print ("ETD  is : ",info_dict['root']['station'][0]['etd'][0]['estimate'][i]['minutes'])
        
 cnt=0
 new_dict={}
 while (cnt<5):
  #print (info_dict['root']['station'][0]['etd'][0]['destination'] ," \t :ETD  is : ",info_dict['root']['station'][0]['etd'][0]['estimate'][0]['minutes'] ,"(in min)")
  
  r=info_dict['root']['station'][0]['etd'][cnt]['destination']
  #if (r==""): break
    
  t=info_dict['root']['station'][0]['etd'][cnt]['estimate'][0]['minutes']
    
  new_dict.update({t:r})
  cnt+=1
    #print ("final is ", new_dict.items())
 for i in sorted (new_dict):    
    print ( i ,"min", "\t", new_dict[i])
  

UP_comingTrains(source="ALL")
