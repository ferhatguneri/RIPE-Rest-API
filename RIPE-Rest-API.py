#Creted By Ferhat Guneri
#Mail: guneriferhat21@gmail.com

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import requests
from datetime import datetime
requests.packages.urllib3.disable_warnings()


def InsertPerson(PersonName,PersonAddress,PersonPhone,PersonEmail,PersonMaintaner):
        headers = {"Content-Type":"application/json", "Accept":"application/json"}
        payload = {
  "objects": {
    "object": [
      {
        "source": {
          "id": "RIPE"
        },
        "attributes": {
          "attribute": [
            {
              "name": "person",
              "value": PersonName
            },
            {
              "name": "address",
              "value": PersonAddress
            },
            {
              "name": "phone",
              "value": PersonPhone
            },
            {
              "name": "e-mail",
              "value": PersonEmail
            },
            {
              "name": "mnt-by",
              "value": PersonMaintaner
            },
            {
              "name": "nic-hdl",
              "value": "AUTO-1"
            },
            {
              "name": "remarks",
              "value": "remark"
            },
            {
              "name": "source",
              "value": "RIPE"
            }
          ]
        }
      }
    ]
  }
}

        url = ("https://rest.db.ripe.net/ripe/person?password=YourMntPassword")
        res = requests.post(url, json=payload, headers = headers, verify=False)
        print res
        res = res.json()
        res = json.dumps(res)
        res = json.loads(res)
        print res
        PersonID = res['objects']['object']['primary-key']['attribute']['value']


def DeletePerson(nic_hdl):

        url = ("https://rest.db.ripe.net/ripe/person/"+nic_hdl+"?password=YourMntPassword")
        res = requests.delete(url, verify=False)
        print res
        res = res.json()
        res = json.dumps(res)
        res = json.loads(res)
        print res


def InsertOrUpdateInetnum(inetnum,netname,descr,country,org,admin-c,tech-c,mnt-by):
        headers = {"Content-Type":"application/json", "Accept":"application/json"}
        payload = { "objects":{
      "object":[
        {
            "attributes":{
              "attribute":[
                  {
                    "name":"inetnum",
                    "value":inetnum
                  },
                  {
                    "name":"netname",
                    "value":netname
                  },
                  {
                    "name":"descr",
                    "value":descr
                  },
                  {
                    "name":"country",
                    "value":country
                  },
                  {
                    "link":{
                        "type":"locator",
                        "href":"http://rest.db.ripe.net/ripe/organisation/"+str(org)
                    },
                    "name":"org",
                    "referenced-type":"organisation",
                    "value":org
                  },
                  {
                    "link":{
                        "type":"locator",
                        "href":"http://rest-prepdev.db.ripe.net/ripe/person/"+str(admin-c)
                    },
                    "name":"admin-c",
                    "referenced-type":"person",
                    "value":admin-c
                  },
                  {
                    "link":{
                        "type":"locator",
                        "href":"http://rest-prepdev.db.ripe.net/ripe/person/"+str(tech-c)
                    },
                    "name":"tech-c",
                    "referenced-type":"person",
                    "value":tech-c
                  },
                  {
                    "name":"status",
                    "value":"ASSIGNED PA"
                  },
                  {
                    "link":{
                        "type":"locator",
                        "href":"http://rest-prepdev.db.ripe.net/ripe/mntner/"+str(mnt-by)
                    },
                    "name":"mnt-by",
                    "referenced-type":"mntner",
                    "value":mnt-by
                  },
                  {
                    "name":"created",
                    "value":datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                  },
                  {
                    "name":"source",
                    "value":"RIPE"
                  }
              ]
            }
        }
      ]
  }}
        inetnum2 = inetnum.replace(' - ', '%20-%20')
        url = ("https://rest.db.ripe.net/ripe/inetnum/"+inetnum2+"?password=YourMntPassword")
        res = requests.put(url, json=payload, headers = headers, verify=False)
        print res
        res = res.json()
        res = json.dumps(res)
        res = json.loads(res)
        print res
#InsertOrUpdateInetnum()


def DeleteInetnum(inetnum):
        inetnum2 = inetnum.replace(' - ', '%20-%20')
        url = ("https://rest.db.ripe.net/ripe/inetnum/"+inetnum2+"?password=YourMntPassword&reason=API Test")
        res = requests.delete(url, verify=False)
        print res
        res = res.json()
        res = json.dumps(res)
        res = json.loads(res)
        print res
#DeleteInetnum()
