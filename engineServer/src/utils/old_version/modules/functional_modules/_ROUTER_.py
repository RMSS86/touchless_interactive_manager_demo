from _TIM_MAIN_ import _App_
from _TIM_SWITCHER_ import _SWITCHER_
import cv2
import sys
import time

class _Router_IN_():
    def __init__(self, *args, **kwargs):
        self.signal_IN = None
        self.signal_OUT = None
        self.testSig = None
        self.switcher = False

    #BLOCK 1:
    def _Video_IO_I_(self, val, routeIn):
        print('receiving from _Video_IO_I_')
        return routeIn

    def _Video_IO_II_(self, val, routeIn):
        print('receiving from _Video_IO_I_')
        return routeIn

class _Router_OUT_():
    def __init__(self, *args, **kwargs):
        self.switcher = False

    def _Video_IO_OUT_(self, val, routeIn):
        print('receiving from _Video_IO_I_')
        return routeIn




_MA_ = _App_()