
###GLOBAL OPTIONS FOR GENERAL RULES AND MODES######GLOBAL OPTIONS FOR GENERAL RULES AND MODES###
###GLOBAL OPTIONS FOR GENERAL RULES AND MODES######GLOBAL OPTIONS FOR GENERAL RULES AND MODES###
class _OPTIONS_():
    def __init__(self,*args, **kwargs):
        ###FOR MODE MANAGING###FOR MODE MANAGING###FOR MODE MANAGING###FOR MODE MANAGING###
        self._INDEX_ = {
            'MAIN_MENU': {
                0: ['OPTIONS', 'Options'],
                1: ['LOG_IN', 'Log Agent In'],
                2: ['LOG_OUT', 'Log Agent Out'],
                3: ['_IDLE_MODE', 'Free Play Mode'],
                4: ['_BREAK', 'Break Time/Exceptions'],
                5: ['HELP', 'Help Menu']},

            'MODES': {
                0: ['OPTIONS', 'List of Options'],
                1: ['_FD_API_MODE', 'Real-Time Cloud Connection Mode'],
                2: ['_FD_SELF_STORAGE_MODE', 'Local Database Inquiry Mode'],
                3: ['SENTINEL_MODE', 'Sentinel Mode'],
                4: ['_IDLE_MODE_', 'Idle Mode']},
            # _IDLE_MODE Displays progpaganda or messages on screen, when face detected gets back to A or B(previously selected)

            'ON_MATCH_MENU': {
                0: ['OPTIONS', 'For Agent Options'],
                1: ['LOG_IN', 'Log Agent-In'],
                2: ['LOG_OUT', 'Log Agent-Out'],
                3: ['CLOCK_IN', 'Agent Clock-In Attendance'],
                4: ['CLOCK_OUT','Agent CLock-Out Attendance'],
                5: ['HELP','Help Menu']},

            'COMMANDS': {
                0: ['COMMANDS_LIST', 'List of Available Commands'],
                1: ['MOVE_UP', 'Move Up'],
                2: ['MOVE_DOWN', 'Move Down'],
                3: ['ACCEPT', 'Accept'],
                4: ['CANCEL', 'Cancel'],
                5: ['MENU', 'General Menu']},

            'COMPLEMENTS': {
                0: ['OPTIONS', 'List of Options'],
                1: ['_AUTO_MOUSE_MODE_', 'Real-Time Cloud Connection Mode'],
                2: ['_SOUND_MODE_', 'Local Database Inquiry Mode'],
                3: ['_SELF_REPORT_MODE_', 'Idle Mode'],
                4: ['__', 'Sentinel Mode']},

            'INDEX': {
                0: 'MAIN_MENU',
                1: 'MODES',
                2: 'ON_MATCH_MENU',
                3: 'COMMANDS',
                4: 'COMPLEMENTS'
            }

        }
        self._Get_Index_Labels_()
        self._RULES_ = {
            'MODE':'',
        }


    def _Get_Index_Labels_(self):
        self.MENUS_ = [self._INDEX_['INDEX'][i] for i in range(len(self._INDEX_['INDEX']))]
        print(self.MENUS_)
        self._get_menu_cycle_(self.MENUS_)

    def _get_menu_cycle_(self,  menu):
        self.MAIN_MENU_List_ = [self._INDEX_[menu[0]][i][1] for i in range(int(len(self._INDEX_['MAIN_MENU'])))]
        self.MODES_List_ = [self._INDEX_[menu[1]][i][1] for i in range(int(len(self._INDEX_['MODES'])))]
        self.ON_MATCH_MENU_List_ = [self._INDEX_[menu[2]][i][1] for i in range(int(len(self._INDEX_['ON_MATCH_MENU'])))]
        self.COMMANDS_List_ = [self._INDEX_[menu[3]][i][1] for i in range(int(len(self._INDEX_['COMMANDS'])))]
        self.COMPLEMENTS_List_ = [self._INDEX_[menu[4]][i][1] for i in range(int(len(self._INDEX_['COMPLEMENTS'])))]

        print(self.MODES_List_)
        print(self.MAIN_MENU_List_)
        print(self.ON_MATCH_MENU_List_)
        print(self.COMMANDS_List_)
        print(self.COMPLEMENTS_List_)

_OPTIONS_()

