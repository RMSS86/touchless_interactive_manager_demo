import TIM_OPTIONS_
from  TIM_NAVIGATOR import _NAVIGATOR_
#TODO: this is the module in charge of modfying and directing functions and values in order for the Navigator to work
###MENU_NAVIGATOR###MENU_NAVIGATOR###MENU_NAVIGATOR###MENU_NAVIGATOR###
###MENU_NAVIGATOR###MENU_NAVIGATOR###MENU_NAVIGATOR###MENU_NAVIGATOR###
class _SWITCHER_():
    def __int__(self, *args, **kwargs):
        self._bridge_ = None
        self.COMM_translate = None

    #TODO:#SWITCHER FOR DEFINING STREAMING MODE IN MAIN APP UNDER DEMAND for complement recognition count, symbol marthcer or automouse
    #INstead of having the count 4 on the faciare recognition do the swithch en here:)
    def COMM_brindge(self, comm_):
        self._bridge_ =comm_
        print('from switcher ', self._bridge_)
        return self._bridge_

    ####SWITCH FOR CHANGING FACIAL DETECTOR FEEDING MODE API VS LOCAL STORAGE MODE
    def face_rotorMode_SWITCH_(self, mode, opt):
        pass

    #TODO: Clasify the COMMANDS SENT BETWEEN MODES AND ASSIGN MODES FROM THE CMD OPT
    #####UNIVERSAL RECEIVER FOR ONE OF THE 7 COMMANDS PLUS THE 2 INTERACTIONS.
    def _universal_COMM_Receiver_(self,_comm):
        self.dictionary_CMMDS={
            '0':'ZERO_',
            '1': 'ONE_',
            '2': 'TWO_',
            '3': 'THREE_',
            '4': 'FOUR_',
            '5': 'FIVE_',
            '6': 'ACCEPT_',
        }

        self._DICT_Builder_(_mainbody=self.dictionary_CMMDS,_selectioned=_comm)
        _NV_._to_Client_COMMD(self._format_build_)

    def _DICT_Builder_(self, _mainbody, _selectioned):
        self._comm = str(_selectioned)
        self.COMM_translated = self.dictionary_CMMDS[self._comm]

        self._format_build_ = {
            "TYPE": "CMD",
            "_CMD": self.COMM_translated
        }

        #TODO: classify the types of entries from a dictuionary make a transaltion>>>
        #TODO: either for navigator or from here send order to node server to project comm on screen :)

        #TODO: EVALUATE IF RECOGNIZED PERSON IS STILL ON CAMERA AND TAKING DESITION FOR SELF
    def _PERSON_SILL_ON_CAM(self):
        pass



_NV_ = _NAVIGATOR_()
_SWITCHER_()