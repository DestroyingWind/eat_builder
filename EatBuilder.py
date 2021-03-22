# coding:utf-8

import requests
import cv2
from utils import *
import numpy as np
import os
import time
import soundfile
import subprocess
import traceback

from message_processor import message_processor
from config.Hpara import callback_url


def get_shape(image):
    shape = image.shape
    shape = (shape[1], shape[0], shape[2])
    return shape


class EatBuilder(object):
    oss_dir = "eat_video"
    temp_store_dir = 'result'

    def __init__(self, test_flag=False):
        self.test_flag = test_flag
        self.resolution = (608, 1080)
        self.fps = 30
        self.id = 0
        self.subtitle_dict = {
            "alignment": 'center',
            "font": os.path.join('source', 'benmojinsong.ttf'),
            "size": 40,
            "position": (304, 730),
            "color": (255, 255, 255),
            "border_flag": False,
            "row_spacing": 10,
            "type": 'alllines'
        }
        self.title_dict = {
            "alignment": 'center',
            "font": os.path.join('source', 'benmojinsong.ttf'),
            "size": 60,
            "position": (304, 130),
            "color": (0, 0, 0),
            "border_flag": False,
            "row_spacing": 15,
            "type": 'alllines'
        }
        self.op = {}
        self.source = {}

    def message_process(self, message):
        success, items = message_processor(message)
        if success:
            self.id, self.op, self.source = items
        return success

    def build_mute_video(self):
        self.video = cv2.VideoWriter(self.change_to_temp_dir("eat_video.avi"), cv2.VideoWriter_fourcc("I", "4", "2", "0"), self.fps, self.resolution)
        opening = self.build_opening()
        self.opening_time = opening.__len__() / self.fps
        body = self.build_body()
        end = self.build_endding()
        mute_video = opening + body + end
        self.total_length = mute_video.__len__()
        for eachframe in mute_video:
            eachframe = cv2.resize(eachframe, self.resolution)
            self.video.write(eachframe)
        self.video.release()

    def build_opening(self):
        opframes = 90
        opening = []
        pic = get_img_from_url(self.op['pic'])
        shape = get_shape(pic)
        resx = (shape[0] - shape[1] / 16 * 9) / opframes
        resy = (shape[1] - shape[0] / 9 * 16) / opframes
        # pic=self.normalize_pic(pic,self.resolution)
        for i in range(opframes):
            thisframe = pic.copy()
            if resx > resy:
                thisframe = thisframe[:, int(resx * i):int(resx * i + shape[1] / 16 * 9), :]
            else:
                thisframe = thisframe[int(resy * i):int(resy * i + shape[0] / 9 * 16), :, :]
            thisframe = normalize_pic(thisframe, self.resolution)
            opening.append(thisframe)
        self.add_subtitle(opening, self.op['text'], self.subtitle_dict)
        self.add_subtitle(opening, self.op['title'], self.title_dict)
        return opening

    def build_body(self):
        timelength = 150
        picwindow = [(0, 369), (608, 711)]
        smallpicsize = (608, 342)
        frames = int(timelength // 2)
        # gen_speeds
        speedsy = []
        for i in range(frames):
            speedsy.append(1 / (i + 1))
        para = 711 / sum(speedsy)
        speedsy = [int(para * y) for y in speedsy]
        pixs = sum(speedsy)
        pic_start_y = 711 - pixs
        speedsx = []
        for i in range(frames, int(timelength)):
            speedsx.append(1 / abs(i - timelength))
        para = 304 / sum(speedsx)
        speedsx = [int(para * x) for x in speedsx]
        # gen_speeds fin
        body = []
        for i in range(self.source.__len__()):
            pic = get_img_from_url(self.source[i]['pic'])
            back = normalize_pic(pic, dsize=self.resolution)
            back = cv2.blur(back, (80, 80))
            front = normalize_pic(pic, smallpicsize)
            front = cv2.copyMakeBorder(front, 0, 0, 0, 400, cv2.BORDER_DEFAULT)
            position = [0, pic_start_y - 342]
            keyframe = []
            for j in range(timelength):
                thiframe = back.copy()
                if j < timelength // 2:
                    position[1] += speedsy[j]
                else:
                    position[0] -= speedsx[j - timelength // 2]
                thisframe = add_one_element(thiframe, front, position)
                keyframe.append(thisframe)
            self.add_subtitle(keyframe, self.source[i]['text'], self.subtitle_dict, True, True)
            self.add_subtitle(keyframe, self.source[i]['title'], self.title_dict, False, False)
            body += keyframe
        return body

    def build_endding(self):
        edframes = 0
        endding = []
        endding.append(np.zeros((1080, 608), dtype=np.uint8))
        return endding

    def add_bgm(self):
        bgm, sr = soundfile.read('source/newbgm0.wav')
        if bgm.shape.__len__ == 2:
            bgm = np.sum(bgm, axis=1) / 2
        soundframe = int(self.total_length / self.fps * sr)
        specify_bgm = [bgm.copy() for _ in range(soundframe // bgm.shape[0])]
        specify_bgm.append(bgm[:soundframe % bgm.shape[0]])
        soundfile.write(self.change_to_temp_dir('bgm.wav'), np.concatenate(specify_bgm), sr)
        subprocess.run(
            ["ffmpeg", "-y", "-i", self.change_to_temp_dir("eat_video.avi"), "-i", self.change_to_temp_dir("bgm.wav"),
             self.change_to_temp_dir("final.mp4")], stdout=-1, stderr=-1)

    def add_subtitle(self, frames: list, subtitle, subtitle_dict, fadein=True, bord=False):
        length = frames.__len__()
        if not length<=2*self.fps:
            length-=2*self.fps
        chars = subtitle.__len__()
        chars_per_frame = chars / length
        max_char_num = self.resolution[0] // subtitle_dict["size"] - 2
        subtitle = self.split_text(subtitle, max_char_num)
        lines = subtitle.__len__()
        new_subtitle = '\n'.join(subtitle)
        if fadein:
            if bord:
                textpic = get_subtitle_pic(new_subtitle, subtitle_dict['font'], subtitle_dict['size'], subtitle_dict['color'], subtitle_dict['row_spacing'], 5, (54, 46, 43))
            else:
                textpic = get_subtitle_pic(new_subtitle, subtitle_dict['font'], subtitle_dict['size'], subtitle_dict['color'], spacing=subtitle_dict['row_spacing'])
            shape = get_shape(textpic)
            line_height = shape[1] // lines
            mask = np.zeros([shape[1], shape[0]])
            horizon_speed = shape[0] / max([x.__len__() for x in subtitle]) * chars_per_frame
            count_list = [x.__len__() for x in subtitle]
            for i in range(1, count_list.__len__()):
                count_list[i] += count_list[i - 1]
            count_list.insert(0, 0)
            count = 0
            for i in range(frames.__len__()):
                char_num = chars_per_frame * i
                if char_num >= count_list[count]:
                    if count == count_list.__len__() - 1:
                        mask[:, :] = 1
                    else:
                        count = min(count_list.__len__() - 1, count + 1)
                        mask[:line_height * (count - 1), :] = 1
                else:
                    mask[line_height * (count - 1):line_height * count, :int((char_num - count_list[count - 1]) / chars_per_frame * horizon_speed)] = 1
                if subtitle_dict['alignment'] == 'left':
                    frames[i] = add_one_element(frames[i], mask_transparency(mask, textpic), subtitle_dict['position'])
                elif subtitle_dict['alignment'] == 'center':
                    frames[i] = add_one_element(frames[i], mask_transparency(mask, textpic), (subtitle_dict['position'][0] - textpic.shape[1] // 2, subtitle_dict['position'][1]))
                else:
                    frames[i] = add_one_element(frames[i], mask_transparency(mask, textpic), (subtitle_dict['position'][0] - textpic.shape[1], subtitle_dict['position'][1]))
        else:
            if bord:
                textpic = get_subtitle_pic(new_subtitle, subtitle_dict['font'], subtitle_dict['size'], subtitle_dict['color'], subtitle_dict['row_spacing'], 5, (54, 46, 43))
            else:
                textpic = get_subtitle_pic(new_subtitle, subtitle_dict['font'], subtitle_dict['size'], subtitle_dict['color'], spacing=subtitle_dict['row_spacing'])
            for i in range(frames.__len__()):
                if subtitle_dict['alignment'] == 'left':
                    frames[i] = add_one_element(frames[i], textpic, subtitle_dict['position'])
                elif subtitle_dict['alignment'] == 'center':
                    frames[i] = add_one_element(frames[i], textpic, (subtitle_dict['position'][0] - textpic.shape[1] // 2, subtitle_dict['position'][1]))
                else:
                    frames[i] = add_one_element(frames[i], textpic, (subtitle_dict['position'][0] - textpic.shape[1], subtitle_dict['position'][1]))
        return frames

    def split_text(self, text, max_char_num):
        if self.subtitle_dict["type"] == "alllines":
            text_list = [""]
            for i, char in enumerate(text):
                if char == '_':
                    text_list.append('')
                    continue
                if text_list[-1].__len__() >= max_char_num:
                    if char in [",", ".", "，", "。"]:
                        text_list[-1] += char
                    else:
                        text_list.append(char)
                else:
                    text_list[-1] += char
            if text_list[-1] == "":
                text_list.pop(-1)
            return text_list
        else:
            return [text]

    def uploads(self):
        platform = 'eat'
        final_filename = str(self.id) + "_" + platform + ".mp4"
        now = time.localtime()
        time_dir = "%04d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
        dir_file = time_dir + "/" + final_filename
        try:
            post_to_oss(self.change_to_temp_dir("final.mp4"), dir_file, direc=self.oss_dir)
            requests.get(callback_url.split("?")[0] + "?id={}&videoUrl={}".format(self.id, "https://video-ydianzx.oss-cn-beijing.aliyuncs.com/" + self.oss_dir + '/' + dir_file))
        except:
            print("upload failed!")
            raise AssertionError

    def change_to_temp_dir(self, fpath):
        return os.path.join(self.temp_store_dir, fpath)

    def reset(self):
        del self.source
        del self.op
        del self.video

    def gen_video(self):
        if self.test_flag:
            self.build_mute_video()
            print("mute video built")
            self.add_bgm()
            print("successfully built the video finished!!!")
        else:
            print("voices is ready!")
            try:
                print("building ", 'eat', " start")
                self.build_mute_video()
                print("mute video built")
                self.add_bgm()
                print("successfully built the video finished!!!")
                self.uploads()
                print("video uploaded!")
            except Exception:
                print("ERROR HAPPENDED!!!!!!\n")
                traceback.print_exc()
                requests.get(
                    "http://manager.media.yidianzx.com/api/article/getMessage.do?id={}&message=err".format(
                        self.id))
            self.reset()


if __name__ == "__main__":
    a = EatBuilder(test_flag=False)
    # a.message_process(
    #     message='{"articleId": 1275, "cover": "http://api.photochina.china.cn/oss/media/images/20201109/15/img_019c7d8459a998f1993361560cf5429a-640_360.jpg", "lastModify": 1604906747548, "scenes": [{"items": [{"action": "-", "source": "http://api.photochina.china.cn/oss/media/images/20201109/15/img_019c7d8459a998f1993361560cf5429a-640_9999.jpg", "type": "IMAGE"}, {"action": "-", "source": "http://api.photochina.china.cn/oss/media/images/20201109/15/img_de786c35004f6dfbb2d2c8ed7f3a94b8-640_9999.jpg", "type": "IMAGE"}, {"action": "-", "source": "http://api.photochina.china.cn/oss/media/images/20201109/15/img_bb91efb292ce8c6902afb7cdfb5ee6a9-640_9999.jpg", "type": "IMAGE"}, {"action": "-", "source": "http://api.photochina.china.cn/oss/media/images/20201109/15/img_a9eb51a36f23c16ae766236c1bcaf951-640_9999.jpg", "type": "IMAGE"}], "text": "都说美女的朋友都是美女，杨颖与她的这5名闺蜜，都长得非常漂亮。只是，她们的妆容太接近，加上长相也相似，反正就是相似度太高了。让网友忍不住留言，差点找不到baby在哪里。"}], "summary": "某微电影导演在个人社交账号上晒出一组聚会照，并配文称，谢谢大家对天蝎的爱。照片的背景上放了很多气球的装饰物，桌子上还放着一个精致的蛋糕。很显...", "title": "曝！杨颖与闺蜜聚会_妆容接近长相相似", "voice": "none"}'
    # )
    a.message_process(
        message='{"articleId":0,"title":"测试测试测_这是一个测试,让我们快乐的测试","cover":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1819216937,2118754409&fm=26&gp=0.jpg","source":[{"pic":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3363295869,2467511306&fm=26&gp=0.jpg","text":"test1_test","title":"title1_test"},{"pic":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1963304009,2816364381&fm=26&gp=0.jpg","text":"test2_test","title":"title2_test"}],"text":"test0_test"}', )
    a.gen_video()
