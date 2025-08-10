
class DRAWER:
    def __init__(self,__cv):
        self.lmList = []
        self.__cv = __cv
        self.dot_radio = 1 # //> DEFINES DE UI DOT RADIO
        self.selected_color = None

        self.CRR_hands_counter_point_color = None
        self.LH_hand_counter_point_color = (230, 226, 109) # //> DEFINES DOT COLOR
        self.RH_hand_counter_point_color = (0, 226, 109) # //> DEFINES DOT COLOR
        self.BH_hands_counter_point_color = (0, 226, 0) # //> DEFINES DOT COLOR
        self.INC_hand_point_color = (39,73,245) # //> DEFINES DOT COLOR

    # //> SINGLE HAND POINTER DRAWER PROTOTYPE
    def CMD_point_drawer(self, __img, __points):
        for point in __points:
            self.__cv.driver_().circle(__img, point, self.dot_radio, self.RH_hand_counter_point_color,
                                       self.__cv.driver_().FILLED)

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


    # //> DEFINES IN COMMAND OUT HANDS COLORS
    def CMD_BH_points_drawer(self, __img, __results, __hander=0):

        if __hander == 0:
            self.CRR_hands_counter_point_color = self.LH_hand_counter_point_color

        if __hander == 1:
            self.CRR_hands_counter_point_color = self.RH_hand_counter_point_color

        if __results:  # //> GETS LANDMARK ON LH IF EXIST
            for id, lm in enumerate(__results.landmark):

                h, w, c = __img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append((cx, cy))

            self.BH_point_drawer(__img, self.lmList, __hander)

            for point in self.lmList:
                self.__cv.driver_().circle(__img, point, self.dot_radio, self.CRR_hands_counter_point_color,
                                           self.__cv.driver_().FILLED)

    def FR_Drawer(self, __img, __points):
        pass
        # //> TODO: MAKE A SQUARE DRAWER FOR FACE_RECOG SIMPLE USAGE
        # //> TODO: MAKE FE PSEUDO MODAL FOR SQUARE TO ALIGN WITH FACE SQUARE

# //> REFERENCE FROM RESULTS
# classification {
#   index: 0
#   score: 0.987991452217102
#   label: "Left"
# }