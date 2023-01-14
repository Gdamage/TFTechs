from tkinter import Tk

class CustomTk(Tk):
    """Customized implementation of Tk window with support to fading"""

    def __init__(
        self, 
        initial_state: ['invisible', 'visible'] = 'visible',
        fade_speed: [int, float] = 1,
        fade_speed_unit: ['ms', 's'] = 'ms',
        fade_updates: [int] = 1000,
        *args, 
        **kwargs):

        # initializes super
        Tk.__init__(self)
        
        # control variables
        self.fade_speed = fade_speed
        if(fade_speed_unit == 's'):
            self.fade_speed *= 1000
        self.fade_updates = fade_updates
        if(self.fade_updates <= 0):
            self.fade_updates = 1
        self.fade_delta = int(self.fade_speed/self.fade_updates)
        self.next_event = None
        self.closing = False

        if(initial_state == 'visible'):
            self.alpha = 1.0  # starts at 100% opacity
            self.attributes("-alpha", self.alpha)
        elif(initial_state == 'invisible'):
            self.alpha = 0.0  # starts at 0% opacity
            self.attributes("-alpha", self.alpha)
        else:
            wrong_type = type(initial_state).__name__
            raise ValueError(f"Expeted ['invisible', 'visible'] for initial_state but instead got {wrong_type}")

    def fade_out(
        self, 
        on_fade: [None, 'close', callable] = None):
        
        if(self.alpha == 0.0):
            raise Exception('Already invisible, did you mean to fade in instead?')

        if(on_fade == 'close'):
            self.closing = True
       
        if(self.alpha > 0):
            self.alpha -= 1/self.fade_updates
            self.attributes("-alpha", self.alpha)

            self.next_event = self.after(self.fade_delta, self.fade_out)
        else:
            if(self.closing):
                self.quit()
                self.destroy()
    def fade_in(self, on_fade: [None, callable] = None):
        if(self.alpha == 1.0):
            raise Exception('Already visible, did you mean to fade out instead?')

        if(callable(on_fade)):
            self.callback = on_fade
       
        if(self.alpha < 1):
            self.alpha += 1/self.fade_updates
            self.attributes("-alpha", self.alpha)

            self.next_event = self.after(self.fade_delta, self.fade_in)
        else:
            if(self.callback):
                self.callback()
    def cancel_remaining_events(self):
        try:
            self.after_cancel(self.next_event)
        except:
            raise(f'Scheduled root event {self.next_event} is invalid')