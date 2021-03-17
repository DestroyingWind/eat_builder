import numpy as np
import random
from utils import utils


def trans_builder(pic1,pic2,frames_num=25,trans_type="random"):
    methods = ["anamorphism", "windmill"]
    if trans_type=="random":
        action = random.choice(methods)
    elif trans_type in methods:
        action=trans_type
    else:
        action=random.choice(methods)
    shape = pic1.shape
    trans=[]
    if action == "anamorphism":
        for i in range(1, frames_num - 1):
            t1 = (pic1 // frames_num) * (frames_num - i)
            t2 = (pic2 // frames_num) * i
            image = t1 + t2
            trans.append(image)
    elif action == "windmill":
        counter_clock = random.choice([True, False])
        fans = random.randint(1, 20)
        mid = [(shape[0] - 1) / 2, (shape[1] - 1) / 2]
        base_angle =2* np.pi / fans
        for i in range(1, frames_num - 1):
            image = pic1.copy()
            for j in range(shape[0]):
                for k in range(shape[1]):
                    angle = utils.cal_angle(j - mid[0], k - mid[1])
                    if counter_clock:
                        if (angle % base_angle) / base_angle < (i + 1) / frames_num:
                            image[j, k] = pic2[j, k]
                    else:
                        if (angle % base_angle) / base_angle > 1 - (i + 1) / frames_num:
                            image[j, k] = pic2[j, k]
            trans.append(image)
    return trans