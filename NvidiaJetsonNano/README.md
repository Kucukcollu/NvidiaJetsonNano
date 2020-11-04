## Nvidia Jetson Nano Developer Kit Projects

### Aim
###### This repository includes AI and Robotics projects.

### Languages
###### Python 3.6.9

### Libraries
###### [OpenCv 4.1.1](https://opencv.org/)
###### [Nanocamera](https://pypi.org/project/nanocamera/)

### Materials
###### [Nvidia Jetson Nano Developer Kit](https://developer.nvidia.com/embedded/jetson-nano-developer-kit)
###### [Raspberry Pi CameraModule V2](https://www.raspberrypi.org/products/camera-module-v2/)
###### Some items to use Jetson Nano

### Setup

##### Actually OpenCV comes as a default with ISO file that you can reach from [here](https://developer.nvidia.com/jetson-nano-sd-card-image) but if you face up with any problem you can use this command to install OpenCv

###### `pip3 install opencv-python`

##### check for installation

###### `import cv2`

##### you can learn the version of OpenCv

###### `print(cv2.__version__)`

##### Install this library to work with CSI camera and also you can reach more information from the link given above

###### `pip3 install nanocamera`

##### check for installation

###### `import nanocamera as nano`
