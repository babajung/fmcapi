Readme.txt

                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
    84454449888094527777          789       782  88888880 788888882 4888888887  
    84590052777                   5887      888 788024407 188414407 8887727888  
    8427                       77 7888     4888 788       288       882    884  
    7      7                  287 78082    8088  88       788       885    888  
     777    7             7 74447 78008   08088 788       288       885    747  
    2  7777           7  2  02247 789084  80088  88       788       885         
     77 77          7 7 4  457247 780088 580088 7887  77  7887  77  885         
    7 72    7    7 7 0  8  022747 7897888887788  88888888 788888885 885         
     57    7 77 2 2 72 24  427257 788 28888 788 7887      788       885         
    8  7  2 77 5 77 87 44  027747 788  8887 588  88       788       885     7   
      7 74  4 72 0  8  58  117247 788  788  488 788       288       885    888  
    77 78  8  8  8  87 207 742747 788   87  488  887      788       881    880  
   72 78  42  8  8  87 704  52247 788       088 788       288       882    884  
     787 787 28  8  88  882  0507 288       888 7887      58852114  8882152888  
     44  48  20  07 707 7247 7447 788       785  88       788888887 4888888887  
                                                                                
   72 2    77  77   7   2         7 7  77   7   7   7  57  7    7  777       8  
   74  477277 077770    8   8 725 27 272 877074 72721  97  572 8 87272 87727 8  
        77  77      7    77  77       727  77      8   777     7 7   7  7  777  
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
======================================== Objects csv file example ===================================

name,value,type,description
zTEMP01,1.1.1.0/24,network,test object network
zTEMP02,2.2.2.2,host,test object host
zTEMP03,3.3.3.1-3.3.3.254,range,test object range
zTEMP04,www.example.com,fqdn,test object fqdn

======================================== HELP COMMAND LINE ==========================================

(py3-venv) D:\>create_objects_v7.exe -h
usage: create_objects_v7.exe [-h] [-v] [-t]

create_object_v7 v7.0
Bancha Sae-Lao <bancha@mfec.co.th>

a tool for creating bulk objects for networks, hosts, ranges, and fqdns in FMC

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Enable log debugging, default is INFO
  -t, --test     Test Mode (Create then delete created objects), default is creating objects only


======================================== TEST MODE =================================================
Note: create bulk objects then clean up by deleting the created objects

(py3-venv) D:\>create_objects_v7.exe -v -t
Enter the device IP address: fmcrestapisandbox.cisco.com
Enter the username of the FMC(Please note it is always recommended to have a seperate API User):admin
Enter the password of the FMC:

Loggged in Domain UUID IS: e276abec-e0f2-11e3-8169-6d9ed49b625f
Number of Domain 1
Enter the objects filename (default=objects.csv) :
Read the objects file objects.csv

---Creating bulk objects------------------------------------------------------------------

Object zTEMP01 Type network Value 1.1.1.0/24
Object zTEMP11 Type network Value 1.1.1.0/24
Object zTEMP21 Type network Value 1.1.1.0/24

---Creating bulk objects------------------------------------------------------------------

Object zTEMP02 Type host Value 2.2.2.2
Object zTEMP12 Type host Value 2.2.2.2
Object zTEMP22 Type host Value 2.2.2.2

---Creating bulk objects------------------------------------------------------------------

Object zTEMP03 Type range Value 3.3.3.1-3.3.3.254
Object zTEMP13 Type range Value 3.3.3.1-3.3.3.254
Object zTEMP23 Type range Value 3.3.3.1-3.3.3.254

---Creating bulk objects------------------------------------------------------------------

Object zTEMP04 Type fqdn Value www.example.com
Object zTEMP14 Type fqdn Value www.example.com
Object zTEMP24 Type fqdn Value www.example.com
---------------Creating objects---------------
Press any key to continue . . .
bulk objects was successfully created

bulk objects was successfully created

bulk objects was successfully created

bulk objects was successfully created

---------------Deleting objects---------------
Press any key to continue . . .
zTEMP01 Network 1.1.1.0/24 was successfully deleted

zTEMP11 Network 1.1.1.0/24 was successfully deleted

zTEMP21 Network 1.1.1.0/24 was successfully deleted

zTEMP02 Host 2.2.2.2 was successfully deleted

zTEMP12 Host 2.2.2.2 was successfully deleted

zTEMP22 Host 2.2.2.2 was successfully deleted

zTEMP03 Range 3.3.3.1-3.3.3.254 was successfully deleted

zTEMP13 Range 3.3.3.1-3.3.3.254 was successfully deleted

zTEMP23 Range 3.3.3.1-3.3.3.254 was successfully deleted

zTEMP04 FQDN www.example.com was successfully deleted

zTEMP14 FQDN www.example.com was successfully deleted

zTEMP24 FQDN www.example.com was successfully deleted

---------------Exiting Program---------------
Press any key to continue . . .


======================================== NON-TEST (PRODUCTION) MODE==============================================
Note: create objects only

(py3-venv) D:\>create_objects_v7.exe -v
Enter the device IP address: fmcrestapisandbox.cisco.com
Enter the username of the FMC(Please note it is always recommended to have a seperate API User):admin
Enter the password of the FMC:

Loggged in Domain UUID IS: e276abec-e0f2-11e3-8169-6d9ed49b625f
Number of Domain 1
Enter the objects filename (default=objects.csv) :
Read the objects file objects.csv

---Creating bulk objects------------------------------------------------------------------

Object zTEMP01 Type network Value 1.1.1.0/24
Object zTEMP11 Type network Value 1.1.1.0/24
Object zTEMP21 Type network Value 1.1.1.0/24

---Creating bulk objects------------------------------------------------------------------

Object zTEMP02 Type host Value 2.2.2.2
Object zTEMP12 Type host Value 2.2.2.2
Object zTEMP22 Type host Value 2.2.2.2

---Creating bulk objects------------------------------------------------------------------

Object zTEMP03 Type range Value 3.3.3.1-3.3.3.254
Object zTEMP13 Type range Value 3.3.3.1-3.3.3.254
Object zTEMP23 Type range Value 3.3.3.1-3.3.3.254

---Creating bulk objects------------------------------------------------------------------

Object zTEMP04 Type fqdn Value www.example.com
Object zTEMP14 Type fqdn Value www.example.com
Object zTEMP24 Type fqdn Value www.example.com
---------------Creating objects---------------
Press any key to continue . . .
bulk objects was successfully created

bulk objects was successfully created

bulk objects was successfully created

bulk objects was successfully created

---------------Exiting Program---------------
Press any key to continue . . .
