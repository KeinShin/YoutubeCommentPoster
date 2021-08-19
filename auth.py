# MIT License

# Copyright (c) 2021 KeinShin

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from googleapiclient.discovery import build


import os
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from google.auth.transport.requests import Request
import json

credential = None
class BuildClient:
    def __init__(self,client_id,client_secret):
        
      import json
      
      a=open("client_secrets.json")
      a=json.load(a)
      b=a['web']
      b.pop('client_id')
      # b.pop('project_id')
      b.pop("client_secret")
      b
      b['client_id'] = client_id
      # b['project_id'] = project_id
      b['client_secret'] = client_secret
      b['redirect_urls'] = ["http://localhost:8080/"]
      
      z=open("client_secrets.json",'w')
      z.truncate(0)
      json.dump(a,z)


if os.path.exists("token.pickle"):
    with open("token.pickle",'rb') as token:
        credential=pickle.load(token)


if not credential or not credential.valid:
    if credential and credential.expired and credential.refresh_token:
        print("Refreshing your token...")
        credential.refresh(Request())
    else:
        
       flow=InstalledAppFlow.from_client_secrets_file(
           "client_secrets.json",
           scopes=['https://www.googleapis.com/auth/youtube',"https://www.googleapis.com/auth/youtube.force-ssl"]
       )
       
       flow.run_local_server(port=8080,prompt="consent")
       credential = flow.credentials
       if not os.path.exists("token.pickle"):
        open("token.pickle", "a")
       print("Saving credentials for future use..")
       with open("token.pickle",'wb') as f:
           pickle.dump(credential,f) 



class Auth(BuildClient):
 def __init__(self,client_id,client_secret):
  print("Setting up Client....")
  super().__init__(client_id=client_id,client_secret=client_secret)
     
  self.auth=build("youtube","v3",credentials=credential)
   
   