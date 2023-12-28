import cv2 as cv

class Camera:
    
    def __init__(self):
        self.camera = cv.VideoCapture(0)
        if not self.camera.isOpened():
            raise ValueError("Unable to open camera")
        
        self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)
        
        # Set camera resolution based on desired aspect ratio (e.g., 16:9)
        desired_width = 640
        desired_height = int((desired_width / self.width) * self.height)
        self.camera.set(cv.CAP_PROP_FRAME_WIDTH, desired_width)
        self.camera.set(cv.CAP_PROP_FRAME_HEIGHT, desired_height)

        # Update width and height after setting the resolution
        self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)
    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()
    
    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()
            
            if ret:
                return (ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return None