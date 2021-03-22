import json
import traceback

def message_processor(message):
    try:
        message_dict = json.loads(message)
        id=message_dict['articleId']
        print("Message is:", message_dict)
        op={}
        op['pic']= message_dict["cover"]
        op['title'] = message_dict["title"]
        op['text']=message_dict['text'] if 'text' in message_dict else message_dict['summary']
        source=[]
        for eachdict in message_dict['scenes']:
            source.append({})
            source[-1]['pic'] = eachdict["items"][0]['source']
            source[-1]['text'] = eachdict["text"]
            source[-1]['title']= eachdict['title']
        return True,(id,op,source)
    except Exception:
        traceback.print_exc()
        return False,()