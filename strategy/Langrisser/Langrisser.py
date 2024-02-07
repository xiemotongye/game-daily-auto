# -*- coding: utf-8 -*-
from strategy import BaseStrategy

class Langrisser:
    def __init__(self):
        pass

    def bundle_id(self):
        return 'com.zlongame.mhmnz'

    def name(self):
        return 'aaa'

    def execute_daily(self, client):
        s = client.session(self.bundle_id())