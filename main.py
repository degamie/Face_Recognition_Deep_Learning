import cv2,os,cv

video = cv2.VideoCapture(0)
#os.chdir("C:/Users/dishi/PycharmProjects/face_recognition_dl/images")

#face_detect(fd)
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
count = 0

name = str(input("Enter Your Name:")).lower()

path = 'images/'+name
#path= r'C:Users\dishi\PycharmProjects\face_recognition_dl'

isExist = os.path.exists(path)
test_image = "./images.jpg"

#image = cv2.imread(test_image)
image=cv2.imread(path)
#path = "./images/"

#file_1="/sarthak_12.jpg"

#images = os.listdir(path)
if isExist:
    print('Name already Taken')
    in_1 = input("Enter Your Name Again")


else:
    os.makedirs(path)
    while True:

        ret, frame = video.read()

        #fd
        faces = facedetect.detectMultiScale(frame, 1.3, 5)
        for x, y, w, h in faces:

            count = count + 1
            name_1 = './images/'+ name + '/' + str(count) + '.jpg'
            print("creating Images ...."+name)
            #cv2.imwrite(name, frame[y:y+h,x:x+w])
            #cv2.imwrite("/.jpg", image)
            cv2.imwrite(name_1,frame[y:y + h, x:x + w])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 20), 3)
        cv2.imshow("WindowFrame",frame)
        k = cv2.waitKey(1)
        #if (k == ord('q')):
        if count>500:
                break
video.release()
cv2.destroyAllWindows()
