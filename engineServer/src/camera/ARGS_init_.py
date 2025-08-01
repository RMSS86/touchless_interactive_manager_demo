import argparse

class ArgsInit:
    def __init__(self):
        # //> ARG DICTIONARY
        self.args_mp = None
        self.args = None
        self.parser = argparse.ArgumentParser()

    def get_args(self):
        self.parser.add_argument("--device", type=int, default=0)
        self.parser.add_argument("--width", help='cap width', type=int, default=960)
        self.parser.add_argument("--height", help='cap height', type=int, default=540)

        # self.parser.add_argument('--use_static_image_mode', action='store_true')
        # self.parser.add_argument("--min_detection_confidence",
        #                     help='min_detection_confidence',
        #                     type=float,
        #                     default=0.7)
        # self.parser.add_argument("--min_tracking_confidence",
        #                     help='min_tracking_confidence',
        #                     type=int,
        #                     default=0.5)

        self.args = self.parser.parse_args()

        return self.args

    def get_args_mp(self):

        self.parser.add_argument('--use_static_image_mode', action='store_true')
        self.parser.add_argument("--min_detection_confidence",
                            help='min_detection_confidence',
                            type=float,
                            default=0.7)
        self.parser.add_argument("--min_tracking_confidence",
                            help='min_tracking_confidence',
                            type=int,
                            default=0.5)

        self.args_mp = self.parser.parse_args()

        return self.args_mp