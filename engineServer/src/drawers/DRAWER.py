
class DRAWER:
    def __init__(self,__cv):
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


    def CMD_BH_points_drawer(self, __img, __points, ):
        for point in __points:
            self.__cv.driver_().circle(__img, point, self.dot_radio, self.BH_hands_counter_point_color,
                                       self.__cv.driver_().FILLED)
