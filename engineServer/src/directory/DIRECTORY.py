class Directory:
    def __init__(self):
        self.NEW_USER_DIR = None
        self.FOLDER_STRUCTURE = {
            'src': [
                # //> BROADCASTER FOLDER
                {'broadcaster': [
                    'BROADCASTER', 'COMM_IO'
                ]},
                # //> CAMERA FOLDER
                {'camera': [
                    'ARGS_init_', 'CAMERA_', 'FPS'
                ]},
                # //> CONVERTER FOLDER
                {'': [
                    ''
                ]},
                # //> DATABASE FOLDER
                {'': [
                    ''
                ]},
                # //> DIRECTORY FOLDER
                {'': [
                    ''
                ]},
                # //> DRAWERS FOLDER
                {'': [
                    ''
                ]},
                # //> MODELS FOLDER
                {'': [
                    ''
                ]},
                # //> MODULES FOLDER
                {'': [
                    ''
                ]},
                # //> NAVIGATOR FOLDER
                {'': [
                    ''
                ]},
                # //> PHASER FOLDER
                {'': [
                    ''
                ]},
                # //> SWITCHER FOLDER
                {'': [
                    ''
                ]},
                # //> UTILS FOLDER
                {'': [
                    ''
                ]},

            ]
        }

    def find_folder(self):
        pass

    def get_folder_at(self):
        pass

    def get_file_at(self):
        pass
