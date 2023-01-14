"""
# changes hierachy level to import other modules
from sys import path
path.insert(1, '.')
# imports
from widgets.CustomTk import CustomTk
"""
from definitions import ROOT_DIR
from ROOT_DIR/widgets/CustomTk import *

class Updater(CustomTk):
    def __init__(self, *args, **kwargs):
        # initalizes super
        CustomTk.__init__(
            self,
            initial_state = 'visible',
            fade_speed = 1,
            fade_speed_unit = 'ms',
            fade_updates = 1000,
            *args, 
            **kwargs)
test = Updater()
test.mainloop()