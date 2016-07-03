import cv2
import threading
import urllib2


# import numpy as np


def threaded(function):
    def wrapper(*args, **kwargs):
        threading.Thread(target=function, args=args, kwargs=kwargs).start()

    return wrapper


@threaded
def internet_on():
    try:
        urllib2.urlopen('http://216.58.194.78', timeout=1)
        print('Online')
    except urllib2.URLError:
        print('Offline')


class VidShow:
    """
    VidShow loops through the video frame-by-frame
    a. detects faces from the video feed and retrieves locations
    b. finds and draws contours depending on shadowing on faces
    c. updates faces brightness to distribute illumination evenly
    """

    def __init__(self, title, cap):
        self.capture = cap
        self.frame = cap.read()
        self.title = title
        self.run()

    def run(self):
        while self.capture.isOpened():
            # read frame-by-frame
            ret, self.frame = cap.read()
            # mirror frame
            self.frame = cv2.flip(self.frame, 1)
            gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            # a
            self.face_detection(self.frame, gray)
            # b
            self.roi_contours()
            # c
            self.flat_illumination()

            ret, thresh = cv2.threshold(gray, 127, 255, 0)
            roi_face = self.face_detection(gray, thresh)
            # contours = roi_contours(thresh)
            # cv2.drawContours(roi_gray, contours, -1, (0, 255, 155), 3)
            ''' mirror image '''
            out.write(self.frame)
            cv2.imshow(self.title, self.frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def flat_illumination(self):
        pass

    @staticmethod
    def roi_contours(thresh):
        ret, thresh = cv2.threshold(thresh, 127, 255, 0)
        _, contours, hierarchy = cv2.findContours(thresh,
                                                  cv2.RETR_LIST,
                                                  cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def face_detection(self, frame, gray):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        roi_gray = ''
        for (x, y, w, h) in faces:
            cv2.rectangle()
            roi = self.frame[y:y + h, x:x + w]
            roi2 = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            ret, roi_thresh = cv2.threshold(roi2, 127, 255, 0)
            cv2.drawContours(roi, self.roi_contours(roi_thresh), -1, (0, 255, 155), 3)
            # cv2.circle(frame, (x + w / 2, y + h / 2), w / 2, (125, 125, 125), 2)
        return roi_gray


if __name__ == '__main__':
    internet_on()

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1920, 1080))

    cap = cv2.VideoCapture(0)

    vid = VidShow('lenna', cap)

    # Deinitialize
    cap.release()
    out.release()
    cv2.destroyAllWindows()
