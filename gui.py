# -----DEBUGGING SETTIGNS----
# Modify for production
import os
os.environ['KIVY_HOME'] = ".kivy"

# -----KIVY APP MODULES -----
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, StringProperty, ReferenceListProperty
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.clock import Clock

import json
from trade.initTrading import AccountData

class MainScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.add_widget(Nav(), 0)
        self.add_widget(Account(), 1)
        #self.add_Widget(PaperAccount(), 2)

class Nav(Widget):
    pass

class Account(TabbedPanel):
    account_live = ObjectProperty(None)
    account_paper = ObjectProperty(None)
    
    def on_parent(self, *args, **kwargs):
        PAPER = False
        self.account_live.initAccount(PAPER)
        PAPER = True
        self.account_paper.initAccount(PAPER)

    def update(self, PAPER):
        if PAPER is True:
            self.account_paper.accountRefresh(PAPER)
        
        else:
            self.account_live.accountRefresh(PAPER)

class AccountWidget(Widget):
    def initAccount(self, PAPER):
        account_info = AccountData.getAccount(PAPER)
        self.ids.number.text = str(account_info[0])
        self.ids.api.text = str(account_info[1])
        self.ids.secret.text = str(account_info[2])

    def accountRefresh(self, PAPER):
        AccountData.updateAccount(PAPER)
        account_info = AccountData.getAccount(PAPER)
        self.ids.number.text = str(account_info[0])
        self.ids.api.text = str(account_info[1])
        self.ids.secret.text = str(account_info[2])