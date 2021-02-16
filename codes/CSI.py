import nanocamera as nano
import cv2

def videoFrame():
	camera = nano.Camera(flip=2,width=1280,height=720,fps=30)
	
	answer = camera.isReady()
	print("Camera: ",answer)
	
	while answer:
		try:
			frame = camera.read()
			cv2.imshow("Live",frame)
			
			if cv2.waitKey(25) & 0xFF == ord("q"):
				break
		except KeyboardInterrupt:
			break
	
	camera.release()

	del camera

if __name__ == "__main__":
	videoFrame()
