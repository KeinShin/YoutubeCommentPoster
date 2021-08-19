
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


import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

from auth import Auth

   
class Videoids(Auth):
 def __init__(self,client_secret,client_id,channelId=None,videosNumber: int=1):
     super().__init__(client_id=client_id,client_secret=client_secret)
     self.auth=self.auth
     self.channelid=channelId
     self.videoLen = videosNumber
 def getSubscriptions(self):
   auth=self.auth
   limit=self.videoLen
   subs=[]
   r=auth.subscriptions().list(
    part="snippet",
    mine=True,
    maxResults=1,
)
   if self.channelid:
         subs.append(self.channelid)
   else:
         
     for i in r.execute()['items']:
         if "snippet" in i.keys():
              subs.append(i['snippet'].get('resourceId').get("channelId"))
   videos=[]
   uploads=[]
   for i in subs:
     r=auth.channels().list(
      part="contentDetails",
      id=i,
      ).execute()
      
     for i in r['items']:
        if "contentDetails" in i.keys():
            uploads.append(i['contentDetails'].get('relatedPlaylists').get("uploads"))
   
   self.uploads=uploads
   
 def getVideos(self):
     self.getSubscriptions()
     auth=self.auth
     videoids=[]
     a=0
     for  i in self.uploads:
      r=auth.playlistItems().list(part="contentDetails",playlistId=i,maxResults=self.videoLen).execute()
      for i in r['items']:
          for z in i['contentDetails']:
                
           if z  == "videoId":
             videoids.append(i['contentDetails'].get(z))
     self.videos=videoids
  
