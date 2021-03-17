import multiprocessing as mp
from flask import Flask, request
from EatBuilder import EatBuilder
from config.Hpara import *
import requests
import time

queue = mp.Queue(20)

app = Flask(__name__)


@app.route("/eat")
def horizontal_build():
    try:
        videoid = request.args.get('videoId')
        queue.put_nowait(videoid)
        requests.get(statue_url.format(videoid,statue['doing']))
        return 'OK'
    except Exception as e:
        print(e)
        if 'videoid' in locals():
            requests.get(statue_url.format(videoid, statue['error']))
        else:
            requests.get(statue_url.format(0,statue['error']))
        return 'QueueFull'


def real_build():
    video_builder = EatBuilder()
    while True:
        if queue.empty():
            time.sleep(5)
        else:
            videoid = queue.get()
            try:
                inner_message = requests.get(inner_url.format(videoid)).content.decode('utf-8')
                video_builder.message_process(inner_message)
                video_builder.gen_video()
            except Exception as e:
                requests.get(statue_url.format(videoid,statue['error']))
                print(e)


if __name__ == '__main__':
    p0 = mp.Process(target=app.run, args=('0.0.0.0', 5001, True))
    p1 = mp.Process(target=real_build)
    if __name__ == "__main__":
        p0.start()
        p1.start()
