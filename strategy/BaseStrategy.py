# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def bundle_id(self):
        return 'com.zlongame.mhmnz'

    @abstractmethod
    def name(self):
        return "aaa"

    @abstractmethod
    def execute_daily(self, client):
        s = client.session(self.bundle_id)

