import cv2

def draw_boundary(img, faceCascade, scaleFactor, minNeighbors, color, label):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors)
    coords = []
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
        cv2.putText(img, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        coords = [x, y, w, h]
    return coords


def detect(img, faceCascade, eyeCascade, noseCascade, mouthCascade):
    color = {"blue":(255,0,0), "red":(0,0,255), "green":(0,255,0), "white":(255,255,255)}
    coords = draw_boundary(img, faceCascade, 1.1, 10, color['blue'], "Face")   

    if len(coords) == 4:
        roi_img = img[coords[1]:coords[1]+coords[3], coords[0]:coords[0]+coords[2]]
        coords = draw_boundary(roi_img, eyesCascade, 1.1, 14, color['red'], "Eyes")   
        coords = draw_boundary(roi_img, noseCascade, 1.1, 10, color['green'], "Nose") 
        coords = draw_boundary(roi_img, mouthCascade, 1.1, 20, color['white'], "Mouth") 
    return img

faceCascade = cv2.CascadeClassifier("C:/Users/Shreyansh Katiyar/Downloads/haarcascade_frontalface_default.xml")
eyesCascade = cv2.CascadeClassifier("C:/Users/Shreyansh Katiyar/Downloads/haarcascade_eye.xml")
noseCascade = cv2.CascadeClassifier("C:/Users/Shreyansh Katiyar/Downloads/haarcascade_nose2.xml")
mouthCascade = cv2.CascadeClassifier("C:/Users/Shreyansh Katiyar/Downloads/haarcascade_mouth.xml")
video_capture = cv2.VideoCapture(0)


while True:
    _, img = video_capture.read()
    img = detect(img, faceCascade, eyesCascade, noseCascade, mouthCascade)
    cv2.imshow("Face Detection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
video_capture.release()
cv2.destroyAllWindows()
    
