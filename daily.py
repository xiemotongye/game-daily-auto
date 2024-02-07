# -*- coding: utf-8 -*-
import wda
from strategy.Langrisser import Langrisser

def main():
    c = wda.Client('http://localhost:8100')
    
    langrisser = Langrisser.Langrisser()
    langrisser.execute_daily(c)

main()