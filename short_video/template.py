from os.path import join


class video_template(object):
    def __init__(self,output_resolution=(720,1080), resolution=(1280, 800), fps=30, trans_action="random", trans_time=0.5, bgm=None,
                 name="laoguodabaihua", title_alignment="center", title_font=join("source", "FZXBSJT.TTF"),
                 title_size=60, title_position=(0, 40), title_color=(0, 0, 0), title_border=False, title_row_spacing=30,
                 subtitle_alignment="center", subtitle_font=join("source", "FZXBSJT.TTF"), subtitle_size=20,
                 subtitle_position=(0, 740), subtitle_color=(255, 255, 255), subtitle_border=True,
                 subtitle_row_spacing=10, subtitle_type="alllines", pic_window=(0, 0, 1280, 800), pic_action=True,
                 background=join("source", "bg_kuaishou.png"), opening=join("source", "opening.mp4"),
                 title_animation=False, title_start_time=9, cover=False, cover_title_alignment="center",
                 cover_title_font=join("source", "benmojinsong.ttf"), cover_title_size=45,
                 cover_title_position=(500, 40), cover_title_color=(255, 241, 0), cover_title_border=False,
                 cover_title_row_spacing=30, cover_background=join("source", "bg_kuaishou.png"), bgm_type="once"):
        self.output_resolution=output_resolution
        self.resolution = resolution
        self.fps = fps
        self.trans_action = trans_action
        assert self.trans_action in ["anamorphism", "random", "None"]
        self.trans_time = trans_time
        self.bgm = bgm
        if self.bgm:
            self.bgm_flag = True
        else:
            self.bgm_flag = False
        self.name = name
        self.title = {
            "alignment": title_alignment,
            "font": title_font,
            "size": title_size,
            "position": title_position,
            "color": title_color,
            "border_flag": title_border,
            "row_spacing": title_row_spacing,
            "type": "alllines"
        }
        assert subtitle_type in ["alllines", "eachline","none"]
        self.subtitle = {
            "alignment": subtitle_alignment,
            "font": subtitle_font,
            "size": subtitle_size,
            "position": subtitle_position,
            "color": subtitle_color,
            "border_flag": subtitle_border,
            "row_spacing": subtitle_row_spacing,
            "type": subtitle_type
        }
        self.pic_window = pic_window
        self.pic_action_flag = pic_action
        self.background = background
        if self.background:
            self.background_flag = True
        else:
            self.background_flag = False
        self.opening = opening
        self.title_animation_flag = title_animation
        self.title_start_time = title_start_time

        self.cover_flag = cover
        self.cover_title = {
            "alignment": cover_title_alignment,
            "font": cover_title_font,
            "size": cover_title_size,
            "position": cover_title_position,
            "color": cover_title_color,
            "border_flag": cover_title_border,
            "row_spacing": cover_title_row_spacing,
            "type": "alllines"
        }
        self.cover_background = cover_background
        self.bgm_type = bgm_type
        assert self.bgm_type in ["once", "repeat"]
