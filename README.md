# Welcome to YouTube Comments

**Why do we use this?**

 **Ans**: This Wrapper is capable to posts comments on youtube videos of any channel

**Only posts comment?**

 **Ans** : No, it   also replies to a random comment


# Examples

```from ytcomment import Comment

comment=Comment(client_id="your google client id",
client_secret="your google client secret",
channel_id='channel id',
numberOfVideosToComment = 1
)

# Channel id is optional

# bydefault if channel id is not provided comment will be posted on channels subscribed by you

comment.insert_comment(text=text to comment,numberofCommentsToPost=1)
```


**Reply to a random comment**

```comment=Comment(client_id="your google auth client id",
client_secret="your google auth client secret",
channel_id="channel id")

comment.insert_comment(is_reply=True,apiKey=your google api key,number,numberOfCommentsToReply=1)
```



