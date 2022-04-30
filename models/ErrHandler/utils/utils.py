import os


class Utils:
    def __init__(self, info):
        self.dirs = info.base['dirs']

    def check_dir(self):
        for directory in self.dirs:
            if not os.path.exists(directory):
                os.mkdir(directory)
