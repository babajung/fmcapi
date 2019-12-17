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