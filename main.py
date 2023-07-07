from functools import partial
import gui
from kivy.app import App
import logging
import time
from trade.initTrading import AccountData
from threading import Thread, Timer

class autoRefresh(object):

    """
    Refreshes account data every t seconds. 
    
    Args:
        PAPER (bool): Chooses if the paper account should be used or not. True is paper trading. Enabled by default.
        multiplier (float): Multiplies t seconds to determine the refresh time. t by default is 1 hour (3600 seconds).
    """
    
    def __init__(self, multiplier, function, *args, **kwargs):        
        self.interval = round(3600.0 * multiplier, 2)
        self.function = partial(function, *args, **kwargs)
        self.running = False
        self._timer = None
    
    def __call__(self):
        """
        Handler function for calling the partial and continuting. 
        """
        self.running = False  # mark not running
        self.start()          # reset the timer for the next go 
        self.function()       # call the partial function 

    def start(self):
         if self.running:
              logging.info('TRADE: Timer already running.')
              return
         
         logging.info('TRADE: Starting timer for %d seconds...' % int(self.interval))
         self._timer = Timer(self.interval, self)
         self._timer.start()
         self.running = True
    
    def stop(self):
        """
        Cancel the interval (no more function calls).
        """
        logging.info('TRADE: Stopping timer...')
        if self._timer:
            self._timer.cancel() 
        self.running = False 
        self._timer  = None

def manRefresh(PAPER):
    """
    Manually refresh the account data.
    Args:
        PAPER (bool): Chooses if the paper account should be used or not. True is paper trading. Enabled by default.
    """

    AccountData.updateAccount(PAPER)

class InitApp(App):
    
    #def on_start(self):
        #self.auto_acct_refresh = autoRefresh(.001, AccountData.updateAccount, PAPER=True)
        #self.auto_acct_refresh.start()

    def build(self):
        app = gui.MainScreen()
        return app
        
    #def on_stop(self):
    #    self.auto_acct_refresh.stop()

if __name__ == "__main__":
    InitApp().run()