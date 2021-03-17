import cv2

def action_builder(pic,action,duration,dsize):
    shape = pic.shape
    length = duration
    this_segment=[]
    if action == "global_to_local":
        for i in range(length):
            this_segment.append(cv2.resize(
                pic[int(shape[0] * (i * 0.1 / (length - 1))):int(shape[0] * (1 - i * 0.1 / (length - 1))),
                int(shape[1] * (i * 0.1 / (length - 1))):int(shape[1] * (1 - i * 0.1 / (length - 1))),
                :],
                dsize
            ))
    elif action == "local_to_global":
        for i in range(length):
            this_segment.append(cv2.resize(
                pic[int(shape[0] * (0.1 - i * 0.1 / (length - 1))):int(shape[0] * (0.9 + i * 0.1 / (length - 1))),
                int(shape[1] * (0.1 - i * 0.1 / (length - 1))):int(shape[1] * (0.9 + i * 0.1 / (length - 1))),
                :],
                dsize
            ))
    elif action == "top_to_bottom":
        height = shape[1] * dsize[1] / dsize[0]
        speed = (shape[0] - height) / length
        for i in range(length):
            this_segment.append(cv2.resize(
                pic[int(speed * i):int(height) + int(speed * i),
                :,
                :],
                dsize
            ))
    elif action == "left_to_right":
        width = shape[0] * dsize[0] / dsize[1]
        speed = (shape[1] - width) / length
        for i in range(length):
            this_segment.append( cv2.resize(
                pic[:, int(speed * i):int(width) + int(speed * i),
                :],
                dsize
            ))
    else:
        for i in range(length):
            this_segment.append(cv2.resize(pic, dsize))
    return this_segment