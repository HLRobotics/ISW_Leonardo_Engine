import Engine
VIDEO_PATH="Coke inspection2021_08_19_12_52_5.mp4"
FRAME="FRAMES"
RUST="RUST"
MARKED="MARKED"
EDGE="EDGE"
CRACK="CRACK"
#Engine.logger(VIDEO_PATH,True)
#Engine.VIdeo_to_Image(VIDEO_PATH)
#Engine.Removing_Unwanted(FRAME)
#Engine.Image_to_Rust(FRAME)
Engine.Crack_Detection(FRAME)
#Engine.Edge_Generator(RUST)#Run Either one
#Engine.Edge_Generator(CRACK)#Run Either one
#Engine.Mark()
#Engine.Image_to_Video(MARKED)
#Engine.logger(VIDEO_PATH,False)
print("[********COMPLETED********]")
