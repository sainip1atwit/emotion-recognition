import cv2 as cv

# FILEPATH FOR IMAGE TESTING
FILEPATH = "test_material/Lebron_James.jpg"

def detect_faces(file):

    # Preloaded face and eye cascades
    fc = cv.CascadeClassifier("xml_files\\haarcascade_frontalface_default.xml")
    ec = cv.CascadeClassifier("xml_files\\haarcascade_eye.xml")

    # read image (and in grayscale)
    img = cv.imread(file)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # detect the faces using face cascade
    faces = fc.detectMultiScale(img_gray, 1.3, 5)

    # Outline all faces detected
    for(x, y, w, h) in faces:

        # create a rectangle outline for face
        cv.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 2)
        
        # grayscale and color matrices
        roi_gray = img_gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # Use grayscale to detect eyes
        eyes = ec.detectMultiScale(roi_gray)

        #draW rectangles for the eyes
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,127,255), 2)

        # display image and wait for user to escape
        cv.imshow("Face Detection", img)
        cv.waitKey(0)
        cv.destroyAllWindows()

detect_faces(FILEPATH)