##
## REMARK: Use for Demonstration Purpose *ONLY*
## FUNCTION:
## - Create bulk/multiple objects using one api call 
## - Delete bulk objects
##

import csv
import json
import sys
import requests
import os
# Suppress HTTPS insecure warning message
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def createobj(obj, url):
    global r
    global headers
    global server
    global username
    global password
    global log

    try:
        result = None

        ## print url
        print ("-"*15 + "\nurl\n" + "-"*15)
        print ("url = " + url)

        post_data = obj
        r = requests.post(url, data=json.dumps(post_data), headers=headers, verify=False)
        status_code = r.status_code
        resp = r.text
        log = open('POST_Create-FMC-Objects.log', 'a')   
        print("Status code: "+str(status_code))
        json_resp = json.loads(resp)
        log.write('\n---------------------------------------------------------------------\n')
        log.write(json.dumps(json_resp,sort_keys=True,indent=4, separators=(',', ': ')))  
        
        if status_code == 201 or status_code == 202:
            print ("bulk objects was successfully created\n")
            result = []
            for item in json_resp["items"]:
                result.append(item["links"]["self"])
        elif status_code == 400:
            print ("bulk objects already exists!\n")
        else:
            r.raise_for_status()
            print ("bulk objects encountered an error during POST --> "+ resp +'\n')
            
    except requests.exceptions.HTTPError as err:
        print ("Error in connection --> "+str(err))
    finally:
        if r: r.close()
    
    return result

def delobj(obj):
    global r
    global headers
    global server
    global username
    global password
    global log

    result = []
    for url in obj:
        try:     
            ## print url
            print ("-"*15 + "\nurl\n" + "-"*15)
            print ("url = " + url)

            r = requests.delete(url, headers=headers, verify=False)
            status_code = r.status_code
            resp = r.text
            log = open('POST_Create-FMC-Objects.log', 'a')   
            print("Status code: "+str(status_code))
            json_resp = json.loads(resp)
            log.write('\n---------------------------------------------------------------------\n')
            log.write(json.dumps(json_resp,sort_keys=True,indent=4, separators=(',', ': ')))  
        
            if status_code == 200 or status_code == 201 or status_code == 202:
                print (" was successfully deleted\n")
                result.append(json_resp)
            elif status_code == 400:
                print (" already exists!\n")
            else:
                r.raise_for_status()
                print (" encountered an error during POST --> "+ resp +'\n')
            
        except requests.exceptions.HTTPError as err:
            print ("Error in connection --> "+str(err))
        finally:
            if r: r.close()
    return result

server = "https://fmcrestapisandbox.cisco.com"

username = "username"
if len(sys.argv) > 1:
    username = sys.argv[1]
password = "password"
if len(sys.argv) > 2:
    password = sys.argv[2]
objects_filename = "objects.csv"
if len(sys.argv) > 3:
    objects_filename = sys.argv[3]

r = None
headers = {'Content-Type': 'application/json'}
api_auth_path = "/api/fmc_platform/v1/auth/generatetoken"
auth_url = server + api_auth_path

print('\nAttempting connection to FMC...')
try:
    requests.packages.urllib3.disable_warnings()
    r = requests.post(auth_url, headers=headers, 
    auth=requests.auth.HTTPBasicAuth(username,password), verify=False)
    auth_headers = r.headers
    auth_token = auth_headers.get('X-auth-access-token', default=None)
    if auth_token == None:
        print("auth_token not found. Exiting...")
        sys.exit()
except Exception as err:
    print ("Error in generating auth token --> "+str(err))
    sys.exit()

headers['X-auth-access-token'] = auth_token

## print auth_token
print ("-"*15 + "\nauth_token\n" + "-"*15)
print ("auth_token = " + auth_token)
## print r
print ("-"*15 + "\nr\n" + "-"*15)
print (r.headers)

# DOMAIN_UUID
domain_uuid = auth_headers.get('DOMAIN_UUID', default=None)
print ("-"*15 + "\nDomain UUID\n" + "-"*15)
print ("Domain UUID = " + domain_uuid)

print('...Connected! Auth token collected successfully (' + auth_token + (')\n'))

api_path_object = "/api/fmc_config/v1/domain/" + domain_uuid + "/object/"
api_path_networks = api_path_object + "networks?bulk=true"
api_path_hosts = api_path_object + "hosts?bulk=true"
api_path_ranges = api_path_object + "ranges?bulk=true"
api_path_fqdns = api_path_object + "fqdns?bulk=true"

try:
    f = open(objects_filename)
    objectsfile = csv.DictReader(f)
except FileNotFoundError:
    print("File '" + objects_filename + "' does not exist")
    sys.exit()

try:
    log = open('POST_Create-FMC-Objects.log', 'a')
except Exception:
    print ("Erorr: Open log file")
    sys.exit()

list_networks = []
list_hosts = []
list_ranges = []
list_fqdns = []

for object in objectsfile:
    post_data = {
        "name": object["name"],
        "type": object["type"],
        "value": object["value"],
        "description": object["description"],
    }
    print('Creating object ' + object["name"])
    try:
        object_type = object["type"].lower()
        if object_type in ["network","networks"]:
            url = server + api_path_networks
            list_networks.append(post_data)
        elif object_type in ["host","hosts"]:
            url = server + api_path_hosts
            list_hosts.append(post_data)
        elif object_type in ["range","ranges"]:
            url = server + api_path_ranges
            list_ranges.append(post_data)
        elif object_type in ["fqdn","fqdns"]:
            url = server + api_path_fqdns
            list_fqdns.append(post_data)
        else:
            # url = server + api_path_object + object["type"]
            print ("-"*15+"\nUnknown object type\n"+"-"*15)
            print (post_data)
            continue
        if (url[-1] == '/'):
            url = url[:-1]
            
        # r = requests.post(url, data=json.dumps(post_data), headers=headers, verify=False)
        # status_code = r.status_code
        # resp = r.text
        # log = open('POST_Create-FMC-Objects.log', 'a')   
        # print("Status code: "+str(status_code))
        # json_resp = json.loads(resp)
        # log.write('\n---------------------------------------------------------------------\n')
        # log.write(json.dumps(json_resp,sort_keys=True,indent=4, separators=(',', ': ')))  
        
        # if status_code == 201 or status_code == 202:
        #     print (object["name"] + " was successfully created\n")
        # elif status_code == 400:
        #     print (object["name"] + " already exists!\n")
        # else:
        #     r.raise_for_status()
        #     print (object["name"] + " encountered an error during POST --> "+ resp +'\n')
            
    except requests.exceptions.HTTPError as err:
        print ("Error in connection --> "+str(err))
    finally:
        if r: r.close()

## print count
print ("-"*15 + "\ncount\n" + "-"*15)
print ("count of list_networks" + str(len(list_networks)))
print ("count of list_hosts" + str(len(list_hosts)))
print ("count of list_ranges" + str(len(list_ranges)))
print ("count of list_fqdns" + str(len(list_fqdns)))

## print list_networks
print ("-"*15 + "\nlist_networks\n" + "-"*15)
print (json.dumps(list_networks))

## print list_hosts
print ("-"*15 + "\nlist_hosts\n" + "-"*15)
print (json.dumps(list_hosts))

## print list_ranges
print ("-"*15 + "\nlist_ranges\n" + "-"*15)
print (json.dumps(list_ranges))

## print list_fqdns
print ("-"*15 + "\nlist_fqdns\n" + "-"*15)
print (json.dumps(list_fqdns))

# create bulk objects for each type
result_networks = createobj(list_networks, server + api_path_networks)
result_hosts = createobj(list_hosts, server + api_path_hosts)
result_ranges = createobj(list_ranges, server + api_path_ranges)
result_fqdns = createobj(list_fqdns, server + api_path_fqdns)

## print result_networks
print ("-"*15 + "\nresult_networks\n" + "-"*15)
print (result_networks)

## print result_hosts
print ("-"*15 + "\nresult_hosts\n" + "-"*15)
print (result_hosts)

## print result_ranges
print ("-"*15 + "\nresult_ranges\n" + "-"*15)
print (result_ranges)

## print result_fqdns
print ("-"*15 + "\nresult_fqdns\n" + "-"*15)
print (result_fqdns)

os.system('pause')

result_del_networks = delobj(result_networks)
result_del_hosts = delobj(result_hosts)
result_del_ranges = delobj(result_ranges)
result_del_fqdns = delobj(result_fqdns)

## print result_del_networks
print ("-"*15 + "\nresult_del_networks\n" + "-"*15)
print (result_del_networks)

## print result_del_hosts
print ("-"*15 + "\nresult_del_hosts\n" + "-"*15)
print (result_del_hosts)

## print result_del_ranges
print ("-"*15 + "\nresult_del_ranges\n" + "-"*15)
print (result_del_ranges)

## print result_del_fqdns
print ("-"*15 + "\nresult_del_fqdns\n" + "-"*15)
print (result_del_fqdns)


if f != None:
    f.close()
if log != None:
    log.close()
print('Log file "POST_Create-FMC-Objects.log" updated\n')
os.system('pause')
