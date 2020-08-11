import nanocamera as nano

camera = nano.Camera(device_id=0,flip=0,width=1280,height=800,fps=30)

# flip=0 means no rotation also we can use flip=2
# for multiple device_id=0 or device_id=1

# for USB cameras camera_type=1 then set the device_id as well

# Frame Rate Enforcement ----> enforce_fps = True
