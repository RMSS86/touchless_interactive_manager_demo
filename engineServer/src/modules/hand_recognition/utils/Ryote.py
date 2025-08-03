from src.modules.hand_recognition.keypoint_classifier.keypoint_classifier import KeyPointClassifier
from collections import deque
import itertools
import copy
import csv

class RYOTE():

    def __init__(self):
        self.active = True
        self.landmark_list = []
        self.pre_processed_landmark_list = []
        self.keypoint_classifier = KeyPointClassifier()
        self.keypoint_classifier_labels = None
        self.hand_sign_id = None

        with open('modules/hand_recognition/keypoint_classifier/keypoint_classifier_label.csv',
                  encoding='utf-8-sig') as f:
            self.keypoint_classifier_labels = csv.reader(f)
            self.keypoint_classifier_labels = [
                row[0] for row in self.keypoint_classifier_labels
            ]

        self.history_length = 16
        self.point_history = deque(maxlen=self.history_length) # //> DUQUE FOR POINT HISTORY
        self.finger_gesture_history = deque(maxlen=self.history_length) # //> DUQUE FOR POINT GESTURE HISTORY

    def calc_landmark_list(self, image, landmarks):

        # //> GETS THE IMAGE PROPORTIONS
        image_width, image_height = image.shape[1], image.shape[0]

        # //> CREATES AN EMPTY LIST OBJECT
        landmark_point = []

        # Keypoint
        for _, landmark in enumerate(landmarks.landmark):
            landmark_x = min(int(landmark.x * image_width), image_width - 1)
            landmark_y = min(int(landmark.y * image_height), image_height - 1)
            # landmark_z = landmark.z

            landmark_point.append([landmark_x, landmark_y])
        return landmark_point

    def pre_process_landmark(self, landmark_list):
        temp_landmark_list = copy.deepcopy(landmark_list)

        # Convert to relative coordinates
        base_x, base_y = 0, 0
        for index, landmark_point in enumerate(temp_landmark_list):
            if index == 0:
                base_x, base_y = landmark_point[0], landmark_point[1]

            temp_landmark_list[index][0] = temp_landmark_list[index][0] - base_x
            temp_landmark_list[index][1] = temp_landmark_list[index][1] - base_y

        # Convert to a one-dimensional list
        temp_landmark_list = list(
            itertools.chain.from_iterable(temp_landmark_list))

        # Normalization
        max_value = max(list(map(abs, temp_landmark_list)))

        def normalize_(n):
            return n / max_value

        temp_landmark_list = list(map(normalize_, temp_landmark_list))
        return temp_landmark_list

    def processor_(self, __image, __LandMarks):
        # //> LANDMARK CALCULATION FOR FURTHER USES
        self.landmark_list = self.calc_landmark_list(__image, __LandMarks)
        # //> CONVERSION FORM RELATIVE COORDINATES => NORMALIZED COORDINATES
        self.pre_processed_landmark_list = self.pre_process_landmark(self.landmark_list)
        # //> SIGN CLASSIFICATION
        self.hand_sign_id = _KP_CLASSIFIER_(self.pre_processed_landmark_list)
        return self.keypoint_classifier_labels[self.hand_sign_id]


_KP_CLASSIFIER_ = KeyPointClassifier()
