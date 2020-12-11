import face_recognition
import cv2
import os
import time
from picamera import PiCamera

path_base = './pic/faces'

KnowImage1_FileLocation = path_base+"/admin/Jay.jpg"
KnowImage2_FileLocation = path_base+"/admin/Prime.jpg"

KnowImage1 = face_recognition.load_image_file(KnowImage1_FileLocation)
KnowImage1_encoding = face_recognition.face_encodings(KnowImage1)[0]

KnowImage2 = face_recognition.load_image_file(KnowImage2_FileLocation)
KnowImage2_encoding = face_recognition.face_encodings(KnowImage2)[0]


def detect_face():
    print('start detect!')

    name = ''

    #Create Array of Encoding and Name
    knownFaces_encodings = [KnowImage1_encoding,KnowImage2_encoding]
    KnownFaces_Name = ["Jay", "Prime"]    

    #Add other faces
    loop = 1

    while True:
        img_path = path_base+'/others/capture{}.jpg'.format(str(loop))

        if(not os.path.exists(img_path)):
            break

        guest = face_recognition.load_image_file(img_path)
        guest_encode = face_recognition.face_encodings(guest)[0]
        knownFaces_encodings.append(guest_encode)
        KnownFaces_Name.append('guest')
        loop += 1

    #Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        scale_percent = 70 # percent of original size
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

        face_location = face_recognition.face_locations(frame)
        face_encoding = face_recognition.face_encodings(frame,face_location)
        print("There are " + str(len(face_location)) + " people in this camera.")

        if(len(face_location) > 0) :
            for (y0,x1,y1,x0), var_face_encoding in zip(face_location,face_encoding):
                matchs = face_recognition.compare_faces(knownFaces_encodings, var_face_encoding)

                if True in matchs:
                    match_index = matchs.index(True) # find index number of true
                    name = KnownFaces_Name[match_index]
                else: 
                    name = 'unknown'

                # cv2.rectangle(frame,(x0,y0),(x1,y1),(255,0,0),2)
                # cv2.putText(frame,name,(x0,y1+25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)  
            
            if(name != ''):
                break           

        cv2.imshow("Detect Face",frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    ret, frame = video_capture.read()
    cv2.imwrite(path_base+'/others/capture{}.jpg'.format(str(loop)),frame)
    cv2.putText(frame,'CHEESE!',(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("Capture",frame)
    cv2.waitKey(3000)
    
    video_capture.release()
    
    cv2.destroyAllWindows()

    return name

def detect_admin():
    print('start detect admin!')

    name = ''

    knownFaces_encodings = [KnowImage1_encoding,KnowImage2_encoding]
    KnownFaces_Name = ["Jay", "Prime"] 

    video_capture = cv2.VideoCapture(0)

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        scale_percent = 70 # percent of original size
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

        face_location = face_recognition.face_locations(frame)
        face_encoding = face_recognition.face_encodings(frame,face_location)
        print("There are " + str(len(face_location)) + " people in this camera.")

        if(len(face_location) > 0) :
            for (y0,x1,y1,x0), var_face_encoding in zip(face_location,face_encoding):
                matchs = face_recognition.compare_faces(knownFaces_encodings, var_face_encoding)

                if True in matchs:
                    match_index = matchs.index(True) # find index number of true
                    name = KnownFaces_Name[match_index]
                else: 
                    name = 'unknown'
            
            if(name != ''):
                break           

        cv2.imshow("Detect Face",frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

    return name
    
# detect_face()