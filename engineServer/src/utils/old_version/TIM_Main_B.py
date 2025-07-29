# Face Recognition / Video Processing
import cv2
import face_recognition
# Tensor FLow Lite-MediaPipe
import pyautogui
# DataFrames / dataBase Connection Modules
from sqlalchemy import create_engine
# System Module
import sys
# Kivy / KivyMD Modules
import kivy
from kivymd.app import MDApp
# Kivy Modules
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image
from kivy.core.text import LabelBase
from kivy.utils import get_color_from_hex
from kivy.uix.floatlayout import FloatLayout
from kivy_garden.mapview import MapView, MapMarkerPopup
from kivy.graphics.texture import Texture
# kivyMD Modules
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.datatables import MDDataTable, TableHeader, TableData, TablePagination
from kivymd.uix.dialog import BaseDialog
from kivymd.uix.taptargetview import MDTapTargetView
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivy.uix.screenmanager import ScreenManager, Screen, \
    SwapTransition, SlideTransition, CardTransition, \
    FadeTransition, WipeTransition, FallOutTransition
from kivymd.theming import ThemableBehavior
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.list import OneLineAvatarIconListItem
from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image as kiImage
# Email / TextMessage sending Modules
# Image processing
# GeoLocation Module
import geocoder

###LOADING UI###LOADING UI###LOADING UI###LOADING UI###LOADING UI###LOADING UI###LOADING UI###LOADING UI###
###LOADING UI###LOADING UI###LOADING UI###LOADING UI###LOADING UI###LOADING UI###LOADING UI###LOADING UI###
# from TIM_UI_A_ import _KV_
# KV = _KV_

###LOADING FACE RECOGNITION MODULE###LOADING FACE RECOGNITION MODULE###LOADING FACE RECOGNITION MODULE###
###LOADING FACE RECOGNITION MODULE###LOADING FACE RECOGNITION MODULE###LOADING FACE RECOGNITION MODULE###
from src.utils.old_version.modules._Face_Recognition_Module import FaceRecognition
###LOADING AUTO MOUSE###LOADING AUTO MOUSE###LOADING AUTO MOUSE###LOADING AUTO MOUSE###LOADING AUTO MOUSE###
###LOADING AUTO MOUSE###LOADING AUTO MOUSE###LOADING AUTO MOUSE###LOADING AUTO MOUSE###LOADING AUTO MOUSE###
from src.utils.old_version.modules._AUTO_Mouse_Module_ import  AutoMouse
###LOADING HAND DECODER[SIGNED VER]###LOADING HAND DECODER[SIGNED VER]###LOADING HAND DECODER[SIGNED VER]###
###LOADING HAND DECODER[SIGNED VER]###LOADING HAND DECODER[SIGNED VER]###LOADING HAND DECODER[SIGNED VER]###
from src.utils.old_version.modules._Hand_Counter_Module import HandRecongnition

###IMPORTING SWTICHER###IMPORTING SWTICHER###IMPORTING SWTICHER###IMPORTING SWTICHER
###IMPORTING SWTICHER###IMPORTING SWTICHER###IMPORTING SWTICHER###IMPORTING SWTICHER
from src.utils.old_version.modules.functional_modules._TIM_SWITCHER_ import _SWITCHER_
###IMPORTING SWTICHER###IMPORTING SWTICHER###IMPORTING SWTICHER###IMPORTING SWTICHER
###IMPORTING SWTICHER###IMPORTING SWTICHER###IMPORTING SWTICHER###IMPORTING SWTICHER

###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE
###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE
screenSize_A = (640, 900)
###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE
Window.size = screenSize_A
###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE ###WINDOW SIZE


# class ItemConfirm(OneLineAvatarIconListItem):
#     divider = None
#
#     def set_icon(self, instance_check):
#         instance_check.active = True
#         check_list = instance_check.get_widgets(instance_check.group)
#         for check in check_list:
#             if check != instance_check:
#                 check.active = False
#
#
# class EMP_Cycle_DataTable(MDDataTable):
#     pass
#
#
# class Item_Cycle_DataTable(MDDataTable):
#     pass
#
#
# # Add on elements for the code
# class Card(MDCard):
#     pass
#
#
# class Tab(FloatLayout, MDTabsBase):
#     pass
#
#
# class IconListItem(OneLineIconListItem):
#     icon = StringProperty()
#
#
# class Item(OneLineAvatarListItem):
#     divider = None
#     source = StringProperty()
#
#
# class Intro(Screen):
#     pass
#
#
# class LogIn(Screen):
#     pass
#
#
# class MenuScreen(Screen):
#     pass
#
#
# class AfterStepsScreen(Screen):
#     pass
#

######MAIN APP######MAIN APP#####MAIN APP#####MAIN APP#####MAIN APP#####MAIN APP#####MAIN APP#####MAIN APP######MAIN APP######
######MAIN APP######MAIN APP#####MAIN APP#####MAIN APP#####MAIN APP#####MAIN APP#####MAIN APP#####MAIN APP######MAIN APP######
######MAIN APP######MAIN APP#####MAIN APP#####MAIN APP#####MAIN APP#####MAIN APP#####MAIN APP#####MAIN APP######MAIN APP######
######MAIN APP######MAIN APP#####MAIN APP#####MAIN APP#####MAIN APP#####MAIN APP#####MAIN APP#####MAIN APP######MAIN APP######
#class MainApp(MDApp):
class MainApp():

    # txtReadData = StringProperty()
    # dialog = None
    # dialog_2 = None

    def __init__(self, **kwargs):
        # super().__init__(**kwargs)
        ###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###
        ###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###
        self._capture_ = cv2.VideoCapture(0)
        Clock.schedule_interval(self._updateManager_, 1.0 / 30.0)
        ###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###
        ###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###CV2 SOURCE###


    ###BUILDER###BUILDER###BUILDER###BUILDER###BUILDER###BUILDER###BUILDER###BUILDER###BUILDER###BUILDER###BUILDER###
    ###BUILDER###BUILDER###BUILDER###BUILDER###BUILDER###BUILDER###BUILDER###BUILDER###BUILDER###BUILDER###BUILDER###
    #def build(self):
        # self.theme_cls.theme_style = "Dark"  # "Light"
        # self.theme_cls.material_style = "M3"
        # LabelBase.register(
        #     name="Roboto-Condensed",
        #     fn_regular="fonts/RobotoCondensed-LightItalic.ttf")
        #
        # theme_font_styles.append('Roboto-Condensed')
        # self.theme_cls.primary_palette = "Gray"
        # self.theme_cls.primary_hue = "800"
        # self.theme_cls.font_styles["Roboto-Condensed"] = [
        #     "Roboto-Condensed",
        #     16,
        #     False,
        #     0.15,
        # ]

        ####SCREEN_MANAGER####SCREEN_MANAGER####SCREEN_MANAGER####
        ####SCREEN_MANAGER####SCREEN_MANAGER####SCREEN_MANAGER####
        # self._sm = ScreenManager(transition=FadeTransition())
        # self._main = MenuScreen(name='Main')
        # self._sm.add_widget(self._main)
        ####SCREEN_MANAGER####SCREEN_MANAGER####SCREEN_MANAGER####
        ####SCREEN_MANAGER####SCREEN_MANAGER####SCREEN_MANAGER####


        ####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####
        ####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####
        #return self._sm
        ####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####
        ####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####BUILDER####

    def _routerVideo(self, lineIn):
        ####MAIN_VIDEO_ROUTE####MAIN_VIDEO_ROUTE####MAIN_VIDEO_ROUTE####MAIN_VIDEO_ROUTE####MAIN_VIDEO_ROUTE###
        ####MAIN_VIDEO_ROUTE####MAIN_VIDEO_ROUTE####MAIN_VIDEO_ROUTE####MAIN_VIDEO_ROUTE####MAIN_VIDEO_ROUTE###
        buf_ = cv2.flip(lineIn, 0)
        _buf = buf_.tostring()
        image_texture = Texture.create(size=(lineIn.shape[1], lineIn.shape[0]), colorfmt='bgr')
        image_texture.blit_buffer(_buf, colorfmt='bgr', bufferfmt='ubyte')
        return image_texture
        ####MAIN_VIDEO_ROUTE####MAIN_VIDEO_ROUTE####MAIN_VIDEO_ROUTE####MAIN_VIDEO_ROUTE####MAIN_VIDEO_ROUTE###
        ####MAIN_VIDEO_ROUTE####MAIN_VIDEO_ROUTE####MAIN_VIDEO_ROUTE####MAIN_VIDEO_ROUTE####MAIN_VIDEO_ROUTE###

###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###
###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###
###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###

    ####WEB CAM FEEDER####WEB CAM FEEDER####WEB CAM FEEDER####WEB CAM FEEDER####WEB CAM FEEDER####WEB CAM FEEDER####
    ####WEB CAM FEEDER####WEB CAM FEEDER####WEB CAM FEEDER####WEB CAM FEEDER####WEB CAM FEEDER####WEB CAM FEEDER####
    def _updateManager_(self, *args):

        #####FUNCT_LOGACAL_ASSESMENT####FUNCT_LOGACAL_ASSESMENT####
        ###CAPTURE###CAPTURE###CAPTURE###CAPTURE###
        ret, self.frame, = self._capture_.read()
        self._FM = _FR_.FacialRotor(self.frame)
        ###CAPTURE###CAPTURE###CAPTURE###CAPTURE###
        #####FUNCT_LOGACAL_ASSESMENT####FUNCT_LOGACAL_ASSESMENT####

#TODO:  change all self.frame to

        ###CV-2-TEXTURE###CV-2-TEXTURE###CV-2-TEXTURE###CV-2-TEXTURE###CV-2-TEXTURE###CV-2-TEXTURE###
        ###CV-2-TEXTURE###CV-2-TEXTURE###CV-2-TEXTURE###CV-2-TEXTURE###CV-2-TEXTURE###CV-2-TEXTURE###
        if ret:
            ###SWITCH DYNAMIC IMPLEMENTATION###SWITCH DYNAMIC IMPLEMENTATION###SWITCH DYNAMIC IMPLEMENTATION
            ###SWITCH DYNAMIC IMPLEMENTATION###SWITCH DYNAMIC IMPLEMENTATION###SWITCH DYNAMIC IMPLEMENTATION
            self.inst_ = _SWITCHER_().COMM_brindge(comm_=_FR_.bridge)###FR_.bridge  DIRECT INPUT
            ###SWITCH DYNAMIC IMPLEMENTATION###SWITCH DYNAMIC IMPLEMENTATION###SWITCH DYNAMIC IMPLEMENTATION
            ###SWITCH DYNAMIC IMPLEMENTATION###SWITCH DYNAMIC IMPLEMENTATION###SWITCH DYNAMIC IMPLEMENTATION

            ###STREAMER ON AUTO MODE FROM FACE ENCODING ASSESMENT###STREAMER ON AUTO MODE FROM FACE ENCODING ASSESMENT
            ###STREAMER ON AUTO MODE FROM FACE ENCODING ASSESMENT###STREAMER ON AUTO MODE FROM FACE ENCODING ASSESMENT
            self.dist = cv2.addWeighted(self._FM, .8, self.onRoute(self.inst_),.5, 0)
            self._Dist_ = self._routerVideo(lineIn=self.dist)
            #self._main.ids.autoMauseDetector_.texture = self._Dist_ #####MAIN VIDEO OUTPUT#####MAIN VIDEO OUTPUT######
            ###STREAMER ON AUTO MODE FROM FACE ENCODING ASSESMENT###STREAMER ON AUTO MODE FROM FACE ENCODING ASSESMENT
            ###STREAMER ON AUTO MODE FROM FACE ENCODING ASSESMENT###STREAMER ON AUTO MODE FROM FACE ENCODING ASSESMENT
            return self.dist#####MAIN VIDEO OUTPUT#####MAIN VIDEO OUTPUT######



    ###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###
    ###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###TO_UI_IMAGE###
    def onRoute(self, comm):
        self.router = comm
        ####MAIN_CLASSES_ROUTE####MAIN_CLASSES_ROUTE####MAIN_CLASSES_ROUTE####MAIN_CLASSES_ROUTE####
        ####MAIN_CLASSES_ROUTE####MAIN_CLASSES_ROUTE####MAIN_CLASSES_ROUTE####MAIN_CLASSES_ROUTE####

        if self.router  == 'MOUSE':
            self._FM_ = _AUMO_._auto_mouse_(self.frame)  # AutoMouse Router
            print('AUTO-MOUSE SELECTED')
            return self._FM_
        elif self.router == 'COUNT':
            self._FM_ = _HR_.HandCounter(self.frame)  # HandCounter Router
            print('HAND-COUNTER SELECTED')
            return self._FM_
        elif self.router == 'HAND-GESTURE':
            self._FM_ = _HR_.HandCounter(self.frame)  # HandCounter Router
            print('HAND-GESTURE INTERPRETER SELECTED')
            return self._FM_
    ####MOVEMENTS###MOVEMENTS###MOVEMENTS###MOVEMENTS###MOVEMENTS###MOVEMENTS###MOVEMENTS###
    ####MOVEMENTS###MOVEMENTS###MOVEMENTS###MOVEMENTS###MOVEMENTS###MOVEMENTS###MOVEMENTS###

    ###GOTO _AM_###GOTO _AM_###GOTO _AM_###GOTO _AM_###
    ###GOTO _AM_###GOTO _AM_###GOTO _AM_###GOTO _AM_###
    def Go_to_AM_(self, *args):
        self._index_ = 0
        print('called fucntion _index_ current: ',self._index_)
        # self._FM__ = _AUMO_._auto_mouse_(self.frame)  # AutoMouse Router

    def Go_to_AM_from_FR_TRUE(self, *args):
        # self.Go_to_AM_()
        self.show_alert_dialog_FR_command_DO_TRUE()

    def Go_to_AM_from_FR_FALSE(self, *args):
        # self.Go_to_AM_()
        self.show_alert_dialog_FR_command_DO_FALSE()

    def Go_to_FR_(self, *args):
        self._index_ = 1

    def Go_to_HR_(self, *args):
        self._index_ = 2

    def Go_to_VK_(self, *args):
        self._index_ = 3



    ####ALERTS!####ALERTS!####ALERTS!####ALERTS!####ALERTS!####ALERTS!####ALERTS!####ALERTS!####ALERTS!####ALERTS!####
    ####ALERTS!####ALERTS!####ALERTS!####ALERTS!####ALERTS!####ALERTS!####ALERTS!####ALERTS!####ALERTS!####ALERTS!####
    ####ALERTS!####ALERTS!####ALERTS!####ALERTS!####ALERTS!####ALERTS!####ALERTS!####ALERTS!####ALERTS!####ALERTS!####
    def show_alert_dialog_accpet_command(self, *args):
        if not self.dialog:
            self.dialog = MDDialog(
                title='',#f"{a}",#COMMAND
                text=f"Accept Command?",
                buttons=[
                    MDFlatButton(
                        text="YES", text_color=self.theme_cls.primary_color, on_press=self.close_dialog,
                        on_release=self.back_to_HR_,
                    ),
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    ),

                ],
            )
        self.dialog.open()

    def show_alert_dialog_FR_command(self, *args):
        if not self.dialog:
            self.dialog = MDDialog(
                title=f"Want To Move To FaceRecognition Module",#COMMAND
                text=f"Accept Command?",
                buttons=[
                    MDFlatButton(
                        text="YES", text_color=self.theme_cls.primary_color, on_press=self.close_dialog,
                        on_release=self.Go_to_FR_,
                    ),
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    ),

                ],
            )
        self.dialog.open()

    def show_alert_dialog_AM_command(self, *args):
        if not self.dialog:
            self.dialog = MDDialog(
                title=f"Want To Move Back AUTOMOUSE Mode?",#COMMAND
                text=f"Accept Command?",
                buttons=[
                    MDFlatButton(
                        text="YES", text_color=self.theme_cls.primary_color, on_press=self.close_dialog,
                        on_release=self.back_to_HR_,
                    ),
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    ),

                ],
            )
        self.dialog.open()

    def show_alert_dialog_command_error(self, *args):
        if not self.dialog:
            self.dialog = MDDialog(
                title='Opps Something Hapened',
                text=f"Please try a Command again.",
                buttons=[
                    MDFlatButton(
                        text="OK(1)", text_color=self.theme_cls.primary_color, on_press=self.close_dialog,
                        on_release=self.back_to_HR_,
                    ),

                ],
            )
        self.dialog.open()


    ###MOVE FROM FR###
    ###MOVE FROM FR###
    def show_alert_dialog_FR_command_DO_TRUE(self, *args):
        if not self.dialog:
            self.dialog = MDDialog(
                title=f"HI {_FR_._nameTag}!",#COMMAND
                text=f"Let's Clock In Today?",
                buttons=[
                    MDFlatButton(
                        text="YES", text_color=self.theme_cls.primary_color, on_press=self.close_dialog,
                        on_release=self.close_dialog,
                    ),
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    ),

                ],
            )
        self.dialog.open()

    def show_alert_dialog_FR_command_DO_FALSE(self, *args):
        if not self.dialog:
            self.dialog = MDDialog(
                title=f"UNREGISTERED USER",#COMMAND
                text=f"Sorry we're unable to Log You In.",
                buttons=[
                    MDFlatButton(
                        text="YES", text_color=self.theme_cls.primary_color, on_press=self.close_dialog,
                        on_release=self.close_dialog,
                    ),
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    ),

                ],
            )
        self.dialog.open()





    ###EXIT###
    ###EXIT###
    def show_alert_dialog_logout_or_exit(self, *args):
        if not self.dialog:
            self.dialog = MDDialog(
                title=f"Done for now?",
                text=f"Log out or Exit App?",
                buttons=[
                    MDFlatButton(
                        text="LOGOUT", text_color=self.theme_cls.primary_color, on_press=self.close_dialog
                    ),
                    MDFlatButton(
                        text="EXIT", text_color=self.theme_cls.primary_color, on_press=self.close_dialog,
                        on_release=self.btnClose
                    ),
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_press=self.close_dialog
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
        # self.dialog = None

    ####EXIT_COMM###EXIT_COMM###EXIT_COMM###EXIT_COMM###EXIT_COMM###EXIT_COMM###EXIT_COMM###EXIT_COMM###EXIT_COMM###
    ####EXIT_COMM###EXIT_COMM###EXIT_COMM###EXIT_COMM###EXIT_COMM###EXIT_COMM###EXIT_COMM###EXIT_COMM###EXIT_COMM###
    def btnClose(self, *args):
        sys.exit()




####CLASSES####CLASSES####CLASSES####CLASSES####CLASSES####CLASSES####CLASSES####CLASSES####CLASSES####CLASSES####
####CLASSES####CLASSES####CLASSES####CLASSES####CLASSES####CLASSES####CLASSES####CLASSES####CLASSES####CLASSES####
####CLASSES####CLASSES####CLASSES####CLASSES####CLASSES####CLASSES####CLASSES####CLASSES####CLASSES####CLASSES####
_FR_ = FaceRecognition()
_AUMO_ = AutoMouse()
_HR_ = HandRecongnition()
_MA_ = MainApp()

###BULDER###BULDER###BULDER###BULDER###BULDER###BULDER###
###BULDER###BULDER###BULDER###BULDER###BULDER###BULDER###
#Builder.load_string(KV)

if __name__ == "__main__":
    MainApp().run()
    input()

######################################################################################################################
#########BACK UP#################BACK UP##################BACK UP#######################BACK UP####################
######################################################################################################################
#########BACK UP#################BACK UP##################BACK UP#######################BACK UP####################
######################################################################################################################
#########BACK UP#################BACK UP##################BACK UP#######################BACK UP####################
######################################################################################################################
#########BACK UP#################BACK UP##################BACK UP#######################BACK UP####################
######################################################################################################################
#########BACK UP#################BACK UP##################BACK UP#######################BACK UP####################




#
#
# #
# # # arr = arr.astype('float64')
# #
# #
# # ClassNames = ['Milton Mejia']
# #
# # encodeListKnown = [array([-1.01208881e-01,  5.26553430e-02, -2.48503797e-02, -4.29867283e-02,
# #         7.42597831e-03, -7.00685307e-02, -2.18614303e-02, -1.22584589e-01,
# #         1.48738280e-01, -2.92660221e-02,  1.17231436e-01, -1.05867768e-02,
# #        -1.84168085e-01, -6.66904077e-02,  3.90766189e-04,  5.27955219e-02,
# #        -1.52275831e-01, -1.49048835e-01, -1.21727318e-01, -5.98603077e-02,
# #         2.95286607e-02, -5.20711280e-02,  2.09281892e-02,  9.40438882e-02,
# #        -1.57574221e-01, -3.06855291e-01, -8.44995603e-02, -1.64965004e-01,
# #         1.29245371e-01, -8.10889751e-02, -2.36756913e-03, -2.01506689e-02,
# #        -2.13750288e-01, -4.79536951e-02,  4.92529012e-02,  8.23812336e-02,
# #         2.87476014e-02, -4.17109691e-02,  2.14665160e-01,  9.16964635e-02,
# #        -1.43224537e-01,  4.85362299e-02, -4.73747477e-02,  3.01594257e-01,
# #         1.36590362e-01,  1.04336217e-01,  5.51058464e-02, -1.04246400e-01,
# #         1.20416209e-01, -2.17327014e-01,  8.38369429e-02,  1.72934800e-01,
# #         1.19885720e-01, -2.72365194e-03,  1.36808589e-01, -1.83543533e-01,
# #         9.27472115e-02,  4.59132381e-02, -3.18952948e-01,  1.44246757e-01,
# #         4.80802879e-02,  3.87425572e-02,  1.20290583e-02, -2.04075221e-02,
# #         1.97051451e-01,  9.37782452e-02, -1.19946331e-01, -7.46130645e-02,
# #         1.74419358e-01, -2.19352603e-01,  6.06868044e-02,  4.26389650e-02,
# #        -5.51040396e-02, -2.05455422e-01, -2.79723704e-01,  2.64573507e-02,
# #         4.25955594e-01,  2.24557057e-01, -1.84303790e-01,  2.07768735e-02,
# #        -1.34350613e-01, -7.53984079e-02,  9.32889730e-02,  4.50722612e-02,
# #        -1.54945165e-01,  1.70608349e-02, -5.05125597e-02,  1.57147497e-02,
# #         1.71191648e-01,  6.61460310e-02,  9.90901981e-03,  2.22860873e-01,
# #        -4.90081497e-03, -3.97936553e-02, -1.56095531e-02, -1.70985945e-02,
# #        -1.72524437e-01, -2.53976211e-02, -3.53228822e-02, -1.22429263e-02,
# #        -1.55609818e-02, -9.91887376e-02,  7.87643790e-02,  1.25781149e-01,
# #        -2.37371191e-01,  6.16111495e-02, -2.18836088e-02, -1.11441649e-01,
# #        -3.53960209e-02,  1.07607335e-01, -1.52315542e-01, -1.22102313e-01,
# #         1.26247242e-01, -3.28053564e-01,  1.78248659e-01,  2.71885425e-01,
# #         4.71141264e-02,  7.24657029e-02,  1.80469565e-02,  3.27628143e-02,
# #         3.59705314e-02,  4.33952585e-02, -1.09920926e-01, -6.31711558e-02,
# #        -2.59250570e-02, -4.71082106e-02, -3.66834458e-03,  1.50470659e-02])]

# # # # # TODO: On Start Up: reconize the IP of the machine and looks for the Users Profile, loards the profile and Starts from there(No log in needed(for installed machines))
# # # # # TODO: https://realpython.com/face-recognition-with-python/ multiple faces recognition project.
# # # # https://www.analyticsvidhya.com/blog/2022/04/building-vehicle-counter-system-using-opencv/


# def Ori_FR(self):
#     # TODO: modify functionality for LOCAL STORAGE MODE(single API_call) or API DRIVEN MODE
#     # TODO: modify flow for SINGLE PERSON ALLOWAED MODE or for SENTINEL MODE(n amount of faces(local or api))
#     for self.encondedFace, self.FaceLoc in zip(self.encodedCurrentFrame, self.faceCurrentFrame):
#
#         self.matches = face_recognition.compare_faces(self._encodeListKnown_, self.encondedFace)
#         self.faceDis = face_recognition.face_distance(self._encodeListKnown_, self.encondedFace)
#
#         ####REPALCE WITH API####REPALCE WITH API####REPALCE WITH API####REPALCE WITH API!!!
#         # TODO: ####REPALCE WITH API####REPALCE WITH API####REPALCE WITH API####REPALCE WITH API!!!
#         ####REPALCE WITH API####REPALCE WITH API####REPALCE WITH API####REPALCE WITH API!!!
#
#         print(f'Face Disrance from Enconder Loop: {self.faceDis}')  # RawReference Between distances.
#         self.matchIndex = np.argmin(self.faceDis)
#         print(f'Match index from np calc: {self.matchIndex}')
#
#         if self.matches[self.matchIndex]:  # Loop to assest the proximity Between Enconders
#             print(f'Emcoded-coor distance matches as : {self.matches[self.matchIndex]}')
#             # Set the assestment's result as UPPER_CASE
#             self._nameTag = self.ClassNames[self.matchIndex].upper()
#             # Reference of matching name from the Image taken prevously(Include EMP_ID! and decompose string)
#             y1, x2, y2, x1 = self.FaceLoc  # Coordinates of the Face Location.
#             ###Arragenment of the Face Location Diagram
#             y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
#             # Directly from: cap.read() places the rectangle in place.
#             # Set the Rectangle Color real time.
#             cv2.rectangle(self.img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.rectangle(self.img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
#             cv2.putText(self.img, self._nameTag, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
#
#             ###COUNTS TIMES OF REC TO CONFIRM AND CHANGES TO _AM_ MODULE###COUNTS TIMES OF REC TO CONFIRM AND CHANGES TO _AM_ MODULE###
#             ###COUNTS TIMES OF REC TO CONFIRM AND CHANGES TO _AM_ MODULE###COUNTS TIMES OF REC TO CONFIRM AND CHANGES TO _AM_ MODULE###
#             self._tag_counter_true.append(self._nameTag)
#             print('Record generated _tag_counter_true', self._tag_counter_true)
#             print('Record length', len(self._tag_counter_true))
#
#             ###Add regulator of appends as BOOLean
#             if len(self._tag_counter_true) == 4:
#                 # self.AutoMouse_invoker_TRUE()
#                 print('Nailed it! API invoked for access MF!', self._nameTag)
#                 self.bridge = self.COMMS[1]
#                 print('Mode get switched to:', self.bridge)
#
#                 self.TAG_RESETER_()
#         ###COUNTS TIMES OF REC TO CONFIRM AND CHANGES TO _AM_ MODULE###COUNTS TIMES OF REC TO CONFIRM AND CHANGES TO _AM_ MODULE###
#         ###COUNTS TIMES OF REC TO CONFIRM AND CHANGES TO _AM_ MODULE###COUNTS TIMES OF REC TO CONFIRM AND CHANGES TO _AM_ MODULE###
#
#         else:
#             self._nameTag = '_UNKNOWN_'
#
#             y1, x2, y2, x1 = self.FaceLoc  # Coordinates of the Face Location.
#             y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4  # Arragenment of the Face Location Diagram
#             cv2.rectangle(self.img, (x1, y1), (x2, y2), (112, 112, 246), 2)  # places the rectangle in place.
#             cv2.rectangle(self.img, (x1, y2 - 35), (x2, y2), (112, 112, 246),
#                           cv2.FILLED)  # Set the Rectangle Color real time.
#             cv2.putText(self.img, self._nameTag, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255),
#                         2)  # Font Type and color .
#
#             ###COUNTS TIMES OF REC TO CONFIRM AND CHANGES TO _AM_ MODULE###
#
#             self._tag_counter_false.append(self._nameTag)
#             print('Record generated from _tag_counter_false', self._tag_counter_false)
#             print('Record length', len(self._tag_counter_false))
#
#             if len(self._tag_counter_false) == 3:
#                 # self.AutoMouse_invoker_FALSE()
#                 print('User not found, please contact administrator at 1800-547-8548', self._tag_counter_true)
#                 self.bridge = self.COMMS[0]
#                 print('Count get swithed to:', self.bridge)
#                 self.TAG_RESETER_()
#     ####REPALCE WITH API####REPALCE WITH API####REPALCE WITH API####REPALCE WITH API!!!
#     ####REPALCE WITH API####REPALCE WITH API####REPALCE WITH API####REPALCE WITH API!!!

