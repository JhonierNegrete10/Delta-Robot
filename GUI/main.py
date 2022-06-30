import requests 
import numpy as np 
from math import *
import json

import gui

from c_inversa import c_inversa
from backend_esp import backend

from tkinter import *
import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox

    


def run(): 
    gui.main()
    


if __name__ =="__main__": 
    run()

def example(): 
    payload = {"Micros":32, "M1":50,"M2":50,"M3":50, "speed":3000, "accel":20}
    ip = "192.168.195.61"
    # ip = "192.168.251.233"
    # c_inversa(L_1= 200,L_2= 400, 
    #           D= 216, d= 100,h = 110,
    #           P =np.array([380,40,300]))
    r = backend(ip= ip, payload= payload)
    pass 