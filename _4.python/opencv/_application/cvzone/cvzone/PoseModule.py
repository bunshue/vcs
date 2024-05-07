"""
Pose Module
By: Computer Vision Zone
Website: https://www.computervision.zone/
"""
import cv2
import mediapipe as mp
import math


class PoseDetector:
    """
    Estimates Pose points of a human body using the mediapipe library.
    """

    def __init__(self, mode=False, smooth=True,
                 detectionCon=0.5, trackCon=0.5):
        """
        :param mode: In static mode, detection is done on each image: slower
        :param smooth: Smoothness Flag
        :param detectionCon: Minimum Detection Confidence Threshold
        :param trackCon: Minimum Tracking Confidence Threshold
        """

        self.mode = mode
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(static_image_mode=self.mode,
                                     smooth_landmarks=self.smooth,
                                     min_detection_confidence=self.detectionCon,
                                     min_tracking_confidence=self.trackCon)
        self.lmList = [] 

    def findPose(self, img, draw=True, bboxWithHands=False):
        """
        Find the pose landmarks in an Image of BGR color space.
        :param img: Image to find the pose in.
        :param draw: Flag to draw the output on the image.
        :return: Image with or without drawings
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        mylmList = []
        poseInfo = {}
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                mylmList.append([cx, cy])

            # Bounding Box
            ad = abs(mylmList[12][0] - mylmList[11][0]) // 2
            if bboxWithHands:
                if mylmList[15][0] > mylmList[16][0]:
                    x1 = mylmList[16][0] - ad
                    x2 = mylmList[15][0] + ad
                else:
                    x1 = mylmList[15][0] - ad
                    x2 = mylmList[16][0] + ad
            else:
                if mylmList[11][0] > mylmList[12][0]:
                    x1 = mylmList[12][0] - ad
                    x2 = mylmList[11][0] + ad
                else:
                    x1 = mylmList[11][0] - ad
                    x2 = mylmList[12][0] + ad

            y1 = mylmList[1][1] - ad
            if mylmList[30][1] > mylmList[29][1]:
                y2 = mylmList[30][1] + ad
            else:
                y2 = mylmList[29][1] + ad

            if x1 < 0: x1 = 0
            if y1 < 0: y1 = 0
            bbox = (x1, y1, x2 - x1, y2 - y1)
            cx, cy = bbox[0] + (bbox[2] // 2), \
                     bbox[1] + bbox[3] // 2

            poseInfo = {"lmList": mylmList, "bbox": bbox, "center": (cx, cy)}

            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        if draw:
            return poseInfo, img
        else:
            return poseInfo

    def findAngle(self, p1, p2, p3, img=None):
        """
        Finds angle between three landmark points.
        :param img: Image to draw output on.
        :param p1: Point1
        :param p2: Point2
        :param p3: Point3
        :param img: Image to draw output on.
        :return: Angle
                 Image with or without drawings
        """

        # Get the landmarks
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        # Calculate the Angle
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                             math.atan2(y1 - y2, x1 - x2))
        if angle < 0:
            angle += 360
            
        if angle > 180:
            angle = 360 - angle

        if img is not None:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 10, (0, 255, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 255, 255), 2)
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
            cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            return angle, img
        else:
            return angle

    def findDistance(self, p1, p2, img=None):
        """
        Find the distance between two landmark points.
        :param p1: Point1
        :param p2: Point2
        :param img: Image to draw on.
        :return: Distance between the points
                 Line information
                 Image with output drawn                 
        """ 
        x1, y1 = p1
        x2, y2 = p2
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        length = math.hypot(x2 - x1, y2 - y1)
        info = [(x1, y1), (x2, y2), (cx, cy)]
        if img is not None:
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (cx, cy), 15, (0, 0, 255), cv2.FILLED)
            cv2.putText(img, str(int(length)), (cx - 50, cy + 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2) 
            return length, info, img
        else:
            return length, info

    def angleCheck(self, myAngle, targetAngle, addOn=20):
        return targetAngle - addOn < myAngle < targetAngle + addOn


def main():
    cap = cv2.VideoCapture(0)
    detector = PoseDetector()
    while True:
        success, img = cap.read()
        pose, img = detector.findPose(img, bboxWithHands=False)
        if pose:
            center = pose["center"]
            cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
