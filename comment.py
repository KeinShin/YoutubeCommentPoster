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

from uploads import Videoids

from auth import build

class Comment(Videoids):
    def __init__(self,client_id,client_secret,commentLimit=4,channelId=None,numberOfVideosToComment: int=1):
    
     super().__init__(channelId=channelId,client_secret=client_secret,client_id=client_id,videosNumber=numberOfVideosToComment)
    #  self.limit=limit
     self.commentLimit=commentLimit
     
     
    def insert_comment(self,text,is_reply: bool =False,apiKey=None,numberOfCommentsToReply: int =1,numberofCommentsToPost: int =1):
      self.getVideos(limit=1)
      a=[]
      parentIds={}
      for i in self.videos:

        channel_id=self.auth.videos().list(part='snippet',
                                           id=i).execute()
        channel_id=channel_id['items'][0].get('snippet').get("channelId")
        x=0
        
        if is_reply:
            if not apiKey:

             raise ValueError("Provide Your Google Developer Api Key!")
            else:
              self.auth2=build('youtube',"v3",developerKey=apiKey)
              results=self.auth2.commentThreads().list(
            part='replies',
            videoId=i,
        ).execute() 
              for n in results['items'] :
                 if 'replies' in n.keys():
                  for z in n['replies']['comments']:
                   if x== numberOfCommentsToReply:
                       break
                   for z in  z.keys():
                       
                    if z=="snippet":
                     reply=n['replies']['comments'][0][z]
                     a.append(reply['parentId'])
                     x+=1
              parentIds.update({reply['videoId']: a})
              for i in parentIds:
                 for k in parentIds[i]:
                  self.auth.comments().insert(part='snippet',body=
                                                     {
  "snippet": {
    "videoId": i,
    "textOriginal": text,
    "parentId":k
    
  }
}
                                                     ).execute()
            print("{} Comments replied with message '{}' on video".format(numberOfCommentsToReply,text), i)
        else:
         x=0
         if x ==      numberofCommentsToPost:
             break
         self.auth.commentThreads().insert(
            part='snippet',
            body=dict(
                snippet=dict(channelId=channel_id,
                             videoId=i,
                             topLevelComment=dict(
                                 snippet=dict(
                                     textOriginal=text
                                 )
                             ))
            )
        ).execute()
         x+=1
         print("Commented On Video : ",i)
        
