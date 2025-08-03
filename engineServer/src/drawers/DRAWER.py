
class DRAWER:
    def __init__(self,__cv):
        self.lmList = []
        self.__cv = __cv
        self.dot_radio = 2 # //> DEFINES DE UI DOT RADIO
        self.LH_hand_counter_point_color = (230, 226, 109) # //> DEFINES DOT COLOR
        self.RH_hand_counter_point_color = (0, 226, 109) # //> DEFINES DOT COLOR
        self.BH_hands_counter_point_color = (0, 226, 0) # //> DEFINES DOT COLOR


    # //> THIS PAINT THE POINT FOR THE LEFT HAND DIGIT COMMAND RECEIVER
    def DGT_point_drawer(self, __img, __points):
        # TODO: MAKE IT A GENERIC CLASS
        for point in __points:
            self.__cv.driver_().circle(__img, point, self.dot_radio, self.LH_hand_counter_point_color , self.__cv.driver_().FILLED)

    # //>
    def CMD_point_drawer(self, __img, __points, ):
        for point in __points:
            self.__cv.driver_().circle(__img, point, self.dot_radio, self.RH_hand_counter_point_color,
                                       self.__cv.driver_().FILLED)


    def CMD_BH_points_drawer(self, __img, __results ):
        if __results.multi_hand_landmarks:  # //> GETS LANDMARK ON LH IF EXIST
            # print('__results _hand FROM CMD DRAWER {}'.format(__results.multi_hand_landmarks[0].landmark))
            # print('__handiness _hand FROM CMD DRAWER {}'.format(__handiness.classification[0].label))  #
            for id, lm in enumerate(__results.multi_hand_landmarks[0].landmark):
                # print('__results.multi_hand_landmarks[0].landmark _hand FROM CMD DRAWER {} {}'.format(id, lm ))
                # print('__img.shape _hand FROM CMD DRAWER {}'.format(__img.shape ))

                h, w, c = __img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append((cx, cy))

            for point in self.lmList:
                self.__cv.driver_().circle(__img, point, self.dot_radio, self.BH_hands_counter_point_color,
                                           self.__cv.driver_().FILLED)
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