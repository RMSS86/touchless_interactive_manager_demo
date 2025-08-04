
class DRAWER:
    def __init__(self,__cv):
        self.lmList = []
        self.__cv = __cv
        self.dot_radio = 2 # //> DEFINES DE UI DOT RADIO
        self.selected_color = None
        self.LH_hand_counter_point_color = (230, 226, 109) # //> DEFINES DOT COLOR
        self.RH_hand_counter_point_color = (0, 226, 109) # //> DEFINES DOT COLOR
        self.BH_hands_counter_point_color = (0, 226, 0) # //> DEFINES DOT COLOR
        self.INC_hand_point_color = (39,73,245) # //> DEFINES DOT COLOR



    # //> THIS PAINT THE POINT FOR THE LEFT HAND DIGIT COMMAND RECEIVER
    def DGT_point_drawer(self, __img, __points, _color='COR'):
        if _color == 'COR':
            self.selected_color = self.LH_hand_counter_point_color
        if _color == 'INC':
            self.selected_color = self.INC_hand_point_color

        for point in __points:
            self.__cv.driver_().circle(__img, point, self.dot_radio, self.selected_color , self.__cv.driver_().FILLED)

    # //> THIS PAINT THE POINT FOR THE LEFT HAND DIGIT COMMAND RECEIVER
    def BH_point_drawer(self, __img, __points, _color=0):
        if _color == 0:
            self.selected_color = self.LH_hand_counter_point_color # //> COLOR ?
        if _color == 1:
            self.selected_color = self.RH_hand_counter_point_color # //> COLOR ?

        for point in __points: # //> DRIVER UI PAINTER
            self.__cv.driver_().circle(__img, point, self.dot_radio, self.selected_color , self.__cv.driver_().FILLED)


    # //> SINGLE HAND POINTER DRAWER PROTOTYPE
    def CMD_point_drawer(self, __img, __points):
        for point in __points:
            self.__cv.driver_().circle(__img, point, self.dot_radio, self.RH_hand_counter_point_color,
                                       self.__cv.driver_().FILLED)


    def CMD_BH_points_drawer(self, __img, __results, __hander=0):
        if __results.multi_hand_landmarks:  # //> GETS LANDMARK ON LH IF EXIST
            for id, lm in enumerate(__results.multi_hand_landmarks[0].landmark):

                h, w, c = __img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append((cx, cy))

            self.BH_point_drawer(__img, self.lmList, __hander)

            # for point in self.lmList:
            #     self.__cv.driver_().circle(__img, point, self.dot_radio, self.BH_hands_counter_point_color,
            #                                self.__cv.driver_().FILLED)

            # for _hand in __handiness:
            #     # //>  MAKE A FOR HLOOP USING HANDINESS __handiness
            #
            #     print('__results _hand FROM CMD DRAWER {}'.format(_hand)) #[__handiness.classification[0].index]
                #__results.multi_hand_landmarks[0]
                # print('__results FROM CMD DRAWER {}'.format(__results.multi_hand_landmarks[__handiness.classification[_hand].index])) #[__handiness.classification[0].index]
                # print('__handiness FROM CMD DRAWER {}'.format(__handiness.classification[_hand].label))

        # for _hand in __handiness:
        #     if __results.multi_hand_landmarks:  # //> GETS LANDMARK ON LH IF EXIST
        #             for id, lm in enumerate(self.results.multi_hand_landmarks[self.handNo].landmark):
        #             h, w, c = __img.shape
        #             cx, cy = int(lm.x * w), int(lm.y * h)
        #
        #             self.lmList.append((cx, cy))
        #
        #     for point in self.lmList:
        #         self.__cv.driver_().circle(__img, point, self.dot_radio, self.BH_hands_counter_point_color,
        #                                    self.__cv.driver_().FILLED)


            # if self.results.multi_hand_landmarks:  # //> GETS LANDMARK ON LH IF EXIST
            #     for id, lm in enumerate(self.results.multi_hand_landmarks[self.handNo].landmark):
            #         h, w, c = self._img.shape
            #         cx, cy = int(lm.x * w), int(lm.y * h)
            #
            #         self.lmList.append((cx, cy))


# classification {
#   index: 0
#   score: 0.987991452217102
#   label: "Left"
# }