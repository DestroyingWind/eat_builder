import os

inner_url='http://manager.media.yidianzx.com/api/article/info.do?id={}'
callback_url="http://manager.media.yidianzx.com/api/article/videoUrl.do?id={}&videoUrl={}"
statue_url="http://manager.media.yidianzx.com/api/article/getMessage.do?id={}&message={}"
statue= {'error':'err', 'doing':'creating'}

cover_title_dict = {
    'fadein':False,
    "alignment": 'center',
    "font": os.path.join('source', 'benmojinsong.ttf'),
    "size": 60,
    "position": (304, 320),
    "color": (255, 255, 255),
    "border_flag": True,
    "row_spacing": 15,
    "type": "alllines",
}
cover_subtitle_dict = {
    'fadein':True,
    "alignment": 'left',
    "font": os.path.join('source', 'benmojinsong.ttf'),
    "size": 40,
    "position": (304, 730),
    "color": (255, 255, 255),
    "border_flag": True,
    "row_spacing": 10,
    "type": "alllines",
}


title_dict = {
    'fadein':False,
    "alignment": 'center',
    "font": os.path.join('source', 'benmojinsong.ttf'),
    "size": 60,
    "position": (304, 130),
    "color": (255, 255, 255),
    "border_flag": True,
    "row_spacing": 15,
    "type": "alllines",
}
subtitle_dict = {
    'fadein':True,
    "alignment": 'left',
    "font": os.path.join('source', 'benmojinsong.ttf'),
    "size": 30,
    "position": (304, 730),
    "color": (255, 255, 255),
    "border_flag": True,
    "row_spacing": 10,
    "type": "alllines",
}