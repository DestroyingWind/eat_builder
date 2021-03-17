import requests
import json
import random

def message_processor(message,direct_inner_message=False):
    try:
        if not direct_inner_message:
            outermessage_dict = json.loads(message)
            print("outer message:\n", outermessage_dict)
            callback_url = outermessage_dict["callbackurl"]
            id = outermessage_dict["id"]
            message_dict = bytes(requests.get(outermessage_dict["dataurl"]).content)
            message_dict = json.loads(message_dict)
        else:
            callback_url=""
            id=0
            message_dict = json.loads(message)
        print("inner message:\n", message_dict)
        op={}
        op['pic']= message_dict["cover"]
        op['title'] = message_dict["title"]
        op['text']=message_dict['text']
        source=[]
        for eachdict in message_dict['source']:
            source.append({})
            source[-1]['pic'] = eachdict["pic"]
            source[-1]['text'] = eachdict["text"]
            source[-1]['title']= eachdict['title']
        return True,(callback_url,id,op,source)
    except Exception as e:
        print(e)
        print(message)
        return False,()