# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd
import time
import datetime

## Configuration

baseURL = "https://your-domain.atlassian.com/rest/"
#baseURL = "https://jira-project.atlassian.com/rest/"

createissueAPI = "api/2/issue/"
dashboardAPI = "api/2/dashboard"
userAPI = "api/2/user"
groupAPI = "api/2/group"
projectAPI = "api/2/project"
metaissueAPI = "api/2/issue/createmeta"


auth = HTTPBasicAuth("mail@example.com", "<api-token>")
#eg:  auth = HTTPBasicAuth("abcd@gmail.com", "DFethf673824") create your own api token from jira site

## Create user

def createuser ( password , email , name ):
   url = baseURL + userAPI

   headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
   }

   payload = json.dumps( {
      "password": password,
      "emailAddress": email,
      "displayName": name,
      "name": ""
   } )

   response = requests.request(
      "POST",
      url,
      data=payload,
      headers=headers,
      auth=auth
   )

   print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

   return

## Get user by ID

def getuserbyId ( Id ):
   url = baseURL + userAPI

   headers = {
      "Accept": "application/json"
   }
   query = {
      "accountId" : Id
   }

   response = requests.request(
      "GET",
      url,
      headers=headers,
      params=query,
      auth=auth
   )

   print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
   return

## Create Group

def creategroup (gname):
   url = baseURL + groupAPI
   headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
   }
   payload = json.dumps( {
   "name": gname
   } )

   response = requests.request(
      "POST",
      url,
      data=payload,
      headers=headers,
      auth=auth
   )
   print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
   return

## Get all dashboard

def getdashboard ():
   url = baseURL + dashboardAPI
   headers = {
      "Accept": "application/json"
   }

   response = requests.request(
      "GET",
      url,
      headers=headers,
      auth=auth
   )

   print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
   return

## Get single dashboard by id 

def getdashboardbyId ():
   url = baseURL + dashboardAPI +"/10002"
   headers = {
      "Accept": "application/json"
   }

   response = requests.request(
      "GET",
      url,
      headers=headers,
      auth=auth
   )

   print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
   return

## Create dashboard
def createdashboard (dname , desc):
   url = baseURL + dashboardAPI

   headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
   }

   payload = json.dumps( {
      "name": dname,
      "description": desc,
      "sharePermissions": []
   } )

   response = requests.request(
      "POST",
      url,
      data=payload,
      headers=headers,
      auth=auth
   )

   print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
   return

## Delete dashboard by Id

def deletedash():

   url = baseURL + dashboardAPI +"/10005"
   response = requests.request(
      "DELETE",
      url,
      auth=auth
   )

   print(response.text)
   print ("Deleted Successfully !!!")
   return

## Create issue 

def createissue(sum , desc ):
   url = baseURL + createissueAPI
   headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
   }

   payload = json.dumps( {
      "fields": {
         "project":
         { 
            "key" : "CJ"
         },
         "summary": sum,
         "description": desc,
         "issuetype": {
            "name": "Bug"
         }
      }
   } )


   response = requests.request(
      "POST",
      url,
      data=payload,
      headers=headers,
      auth=auth
   )

   print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
   return

## Get Issue by Id

def getissuebyId ():
   url = baseURL + createissueAPI + "/10004"
   headers = {
      "Accept": "application/json"
   }

   response = requests.request(
      "GET",
      url,
      headers=headers,
      auth=auth
   )

   print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
   return


## Get create issue meta data

def getissuemeta ():
   url = baseURL + metaissueAPI
   headers = {
      "Accept": "application/json"
   }

   response = requests.request(
      "GET",
      url,
      headers=headers,
      auth=auth
   )

   print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
   return


## Delete Issue by Id 

def deleteissuebyID ():
   url = baseURL + createissueAPI + "/10004"
   response = requests.request(
      "DELETE",
      url,
      auth=auth
   )

   print(response.text)
   print ("Deleted Successfully !!!")
   return


## Get all Projects

def getprojects ():
   url = baseURL + projectAPI

   headers = {
      "Accept": "application/json"
   }

   response = requests.request(
      "GET",
      url,
      headers=headers,
      auth=auth
   )

   print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
   return


#Call above functions using the 

#createuser (password ="abcd" , email ="abcd@xyz.com", name = "Mr AB")
#getuserbyId (Id = "557058:84f7ce7c-91a6-4ad0-b420-4ea26758341d" )
#creategroup (gname = "My Group")
#getdashboard ()
#getdashboardbyId ()
#createdashboard(dname = "Dashboard" , desc="checking whether working or not")
#deletedash()
#createissue (sum = "issue" , desc = " checking whether works")
#getissuebyId()
#getissuemeta()
#deleteissuebyID()
# getprojects()


print (" 0: To Create User\n\n 1: To get user by Id\n\n 2: Create a group  \n\n 3: Get all dashboards ")
print ("\n 4: Get dashboard by Id \n\n 5: Create Dashboard \n\n 6: Delete Dashboard by Id \n\n 7: Create issue ")
print ("\n 8: Get issue by Id \n\n 9: Get issues\n\n 10: Delete issue by Id \n\n11: Get all projects")

x = input ("Please enter your Choice: ")
x= int(x)
if x == 0:
   createuser (password ="amazo" , email ="amazon@aws.com", name = "Mr BOBO")
elif x == 1:
   getuserbyId (Id = "557058:84f7ce7c-91a6-4ad0-b420-4ea26758341d" )
elif x == 2:
   creategroup (gname = "My Group")
elif x == 3:
   getdashboard ()
elif x == 4:
   getdashboardbyId ()
elif x == 5:
   createdashboard(dname = "Dashboard" , desc="checking whether working or not")
elif x == 6:
   deletedash()
elif x == 7:
   createissue (sum = "issue" , desc = " checking whether works")
elif x == 8:
   getissuebyId()
elif x == 9:
   getissuemeta()
elif x == 10:
   deleteissuebyID()
elif x == 11:
   getprojects()
else:
    print("wrong Choice !!!\nEnter a value in between 0 to 11")

