# import the opencv library
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Define a video capture object
vid = cv2.VideoCapture(0)



while(True):
   
    # Capture the video frame by frame
    ret, frame = vid.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # function will return a rectangle with it (x,y,w,h) co-ordinates around the detected face.
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x,y,w,h) in faces:
       # rectangle(image, strat_pt of x and y pixels, end_pt of x and y pixels,color, thickness) 
       cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # Display the resulting frame
    cv2.imshow("Web cam", frame)
      
    # Quit Window by Spacebar Key
    if cv2.waitKey(25) == 32:
        break
  
# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()