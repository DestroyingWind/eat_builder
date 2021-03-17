from short_video import template
from os.path import join

# kuaishou = template.video_template(
#     resolution=(608, 1080), title_position=(None, 200), title_size=40,
#     title_color=(245, 151, 0), subtitle_alignment="left", subtitle_font="YH.ttf",
#     subtitle_size=32, subtitle_position=(20, 668), subtitle_border=False,
#     pic_window=(0, 310, 608, 652), subtitle_row_spacing=16, title_row_spacing=20, name="kuaishou", opening=None
# )

kuaishou = template.video_template(output_resolution=(720, 1280),
                                   resolution=(608, 1080), title_position=(None, 900), title_size=40, title_font=join("source","simhei.ttf"),
                                   title_color=(245, 151, 0), subtitle_alignment="left", subtitle_font=join("source","simhei.ttf"),
                                   subtitle_size=32, subtitle_position=(20, 668), subtitle_border=False,
                                   pic_window=(0, 0, 608, 850), subtitle_row_spacing=16, title_row_spacing=20, background=join("source","bg_kuaishou.png"),
                                   subtitle_type="none", name="kuaishou", opening=False,
                                   cover=False, cover_title_alignment="center",
                                   cover_title_font=join("source","simhei.ttf"), cover_title_size=50,
                                   cover_title_position=(40, 400), cover_title_color=(0, 39, 255), cover_title_border=False,
                                   cover_title_row_spacing=25, cover_background=join("source","cover_douyin.jpg"))

xigua = template.video_template(output_resolution=(1280, 720),
                                resolution=(640, 360), title_position=(None, 200), title_size=40,
                                title_color=(245, 151, 0), subtitle_alignment="center", subtitle_font=join("source","YH.ttf"),
                                subtitle_size=20, subtitle_position=(20, 300), subtitle_border=True,
                                pic_window=(0, 0, 640, 360), subtitle_row_spacing=16, title_row_spacing=20, name="xigua", subtitle_type="eachline",
                                title_animation=False, title_start_time=2, background=None, bgm=join("source","bgm_xigua.wav")
                                )

douyin = template.video_template(output_resolution=(720, 1280),
                                 resolution=(608, 1080), title_position=(None, 900), title_size=40, title_font=join("soure","simhei.ttf"),
                                 title_color=(0, 39, 255), subtitle_alignment="left", subtitle_font=join("soure","simhei.ttf"),
                                 subtitle_size=32, subtitle_position=(20, 668), subtitle_border=False,
                                 pic_window=(0, 0, 608, 850), subtitle_row_spacing=16, title_row_spacing=20, background=join("source","bg_douyin.png"),
                                 subtitle_type="none", name="douyin", opening=False,
                                 cover=True, cover_title_alignment="center",
                                 cover_title_font=join("source","benmojinsong.ttf"), cover_title_size=50,
                                 cover_title_position=(40, 400), cover_title_color=(0, 39, 255), cover_title_border=False,
                                 cover_title_row_spacing=25, cover_background=join("source","cover_douyin.jpg"))

t1= template.video_template(output_resolution=(720, 1280),
                            resolution=(608, 1080), title_position=(None, 900), title_size=40, title_font=join("source", "simhei.ttf"),
                            title_color=(0, 39, 255), subtitle_alignment="left", subtitle_font=join("source", "simhei.ttf"),
                            subtitle_size=32, subtitle_position=(20, 668), subtitle_border=False,
                            pic_window=(0, 0, 608, 850), subtitle_row_spacing=16, title_row_spacing=20,
                            background=join("source", "vertical1.png"),
                            subtitle_type="none", name="ver1", opening=False,
                            cover=True, cover_title_alignment="center",
                            cover_title_font=join("source", "benmojinsong.ttf"), cover_title_size=50,
                            cover_title_position=(40, 400), cover_title_color=(0, 39, 255), cover_title_border=False,
                            cover_title_row_spacing=25, cover_background=join("source", "cover1.jpg"), bgm=join("source", "bgm1.wav"),
                            bgm_type="repeat"
                            )

t2= template.video_template(output_resolution=(720, 1280),
                            resolution=(608, 1080), title_position=(None, 900), title_size=40, title_font=join("source", "simhei.ttf"),
                            title_color=(96, 25, 134), subtitle_alignment="left", subtitle_font=join("source", "simhei.ttf"),
                            subtitle_size=32, subtitle_position=(20, 668), subtitle_border=False,
                            pic_window=(0, 0, 608, 850), subtitle_row_spacing=16, title_row_spacing=20,
                            background=join("source", "vertical2.png"),
                            subtitle_type="none", name="ver2", opening=False,
                            cover=True, cover_title_alignment="center",
                            cover_title_font=join("source", "benmojinsong.ttf"), cover_title_size=50,
                            cover_title_position=(40, 400), cover_title_color=(96, 25, 134), cover_title_border=False,
                            cover_title_row_spacing=25, cover_background=join("source", "cover2.png"), bgm=join("source", "bgm2.wav"),
                            bgm_type="repeat"
                            )

t3= template.video_template(output_resolution=(720, 1280),
                            resolution=(608, 1080), title_position=(None, 900), title_size=40, title_font=join("source", "simhei.ttf"),
                            title_color=(0, 71, 157), subtitle_alignment="left", subtitle_font=join("source", "simhei.ttf"),
                            subtitle_size=32, subtitle_position=(20, 668), subtitle_border=False,
                            pic_window=(0, 0, 608, 850), subtitle_row_spacing=16, title_row_spacing=20,
                            background=join("source", "vertical3.png"),
                            subtitle_type="none", name="ver3", opening=False,
                            cover=True, cover_title_alignment="center",
                            cover_title_font=join("source", "benmojinsong.ttf"), cover_title_size=50,
                            cover_title_position=(40, 400), cover_title_color=(0, 71, 157), cover_title_border=False,
                            cover_title_row_spacing=25, cover_background=join("source", "cover3.png"), bgm=join("source", "bgm3.wav"),
                            bgm_type="repeat"
                            )

test = template.video_template(output_resolution=(720, 1280),
                               resolution=(608, 1080), title_position=(None, 900), title_size=40, title_font=join("source","simhei.ttf"),
                               title_color=(0, 39, 255), subtitle_alignment="left", subtitle_font=join("source","simhei.ttf"),
                               subtitle_size=32, subtitle_position=(20, 668), subtitle_border=False,
                               pic_window=(0, 0, 608, 850), subtitle_row_spacing=16, title_row_spacing=20, background=join("source","bg_douyin.png"),
                               subtitle_type="none", name="test", opening=False,
                               cover=False, cover_title_alignment="center",
                               cover_title_font=join("source","benmojinsong.ttf"), cover_title_size=50,
                               cover_title_position=(40, 400), cover_title_color=(0, 39, 255), cover_title_border=False,
                               cover_title_row_spacing=25, cover_background=join("source","cover_douyin.jpg"), bgm=join("source","bgm_xigua.wav"), bgm_type="repeat",
                               trans_time=1
                               )


laoguodabaihua = [t1,t2,t3, xigua,kuaishou]
test_laoguodabaihua=[t1]
