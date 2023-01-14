from tkinter import Tk
from model import Model

class App(Tk):
    def __init__(self, *args, **kwargs):
        # initializes super
        Tk.__init__(self, *args, **kwargs)

        self.model = Model