"""
Face Mesh Module
By: Computer Vision Zone
Website: https://www.computervision.zone/
"""

import cv2
import itertools
import mediapipe as mp 
import numpy as np

class FaceMeshDetector:
    """
    Face Mesh Detector to find 468 Landmarks using the mediapipe library.
    Helps acquire the landmark points in pixel format
    """

    def __init__(self, staticMode=False, maxFaces=2, minDetectionCon=0.5, minTrackCon=0.5):
        """
        :param staticMode: In static mode, detection is done on each image: slower
        :param maxFaces: Maximum number of faces to detect
        :param minDetectionCon: Minimum Detection Confidence Threshold
        :param minTrackCon: Minimum Tracking Confidence Threshold
        """
        self.staticMode = staticMode
        self.maxFaces = maxFaces
        self.minDetectionCon = minDetectionCon
        self.minTrackCon = minTrackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        #self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces,
        #                                         self.minDetectionCon, self.minTrackCon)
        self.faceMesh = self.mpFaceMesh.FaceMesh(                                         
                           static_image_mode=self.staticMode,
                           max_num_faces=self.maxFaces,
                           min_tracking_confidence=self.minTrackCon,
                           min_detection_confidence=self.minDetectionCon)                                                    
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=0)

    def findFaceMesh(self, img, draw=True):
        """
        Finds face landmarks in BGR Image.
        :param img: Image to find the face landmarks in.
        :param draw: Flag to draw the output on the image.
        :return: Image with or without drawings
        """
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)
        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    # 2021/09/09
                    self.mpDraw.draw_landmarks(image=img,
                         landmark_list=faceLms,
                         connections=self.mpFaceMesh.FACEMESH_TESSELATION,
                         landmark_drawing_spec=None,
                         connection_drawing_spec=mp.solutions.drawing_styles.get_default_face_mesh_tesselation_style())
                    self.mpDraw.draw_landmarks(image=img,
                         landmark_list=faceLms,
                         connections=self.mpFaceMesh.FACEMESH_CONTOURS,
                         landmark_drawing_spec=self.drawSpec,
                         connection_drawing_spec=mp.solutions.drawing_styles.get_default_face_mesh_contours_style())
                  #  self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACE_CONNECTIONS,
                  #                             self.drawSpec, self.drawSpec)
                face = []
                for id, lm in enumerate(faceLms.landmark):
                    ih, iw, ic = img.shape
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    face.append([x, y])
                faces.append(face)
        return img, faces
        
    def getFacePart(self, img, face_idx=0, facePart="FACE_OVAL"):
        faceLms = self.results.multi_face_landmarks[face_idx]
        face_part = self.mpFaceMesh.FACEMESH_FACE_OVAL
        if facePart == "FACE_OVAL": 
            face_part = self.mpFaceMesh.FACEMESH_FACE_OVAL
        if facePart == "LIPS":   
            face_part = self.mpFaceMesh.FACEMESH_LIPS
        if facePart == "LEFT_EYE":
            face_part = self.mpFaceMesh.FACEMESH_LEFT_EYE
        if facePart == "RIGHT_EYE":
            face_part = self.mpFaceMesh.FACEMESH_RIGHT_EYE
        if facePart == "LEFT_EYEBROW":
            face_part = self.mpFaceMesh.FACEMESH_LEFT_EYEBROW
        if facePart == "RIGHT_EYEBROW":
            face_part = self.mpFaceMesh.FACEMESH_RIGHT_EYEBROW
        face = []
        ih, iw, ic = img.shape
        # Iterate over the indexes of the landmarks of the face part. 
        for idx in list(itertools.chain(*face_part)):
            # Append the landmark into the list.
            face.append([int(faceLms.landmark[idx].x * iw),
                           int(faceLms.landmark[idx].y * ih)])
        return face   
         
    def getFacePartSize(self, face):        
        _, _, width, height = cv2.boundingRect(np.array(face))
        return height, width   
                 

def main():
    cap = cv2.VideoCapture(0)
    detector = FaceMeshDetector(maxFaces=2)
    while True:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img)
        if faces:
            print(faces[0])
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
