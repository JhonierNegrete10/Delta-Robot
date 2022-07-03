from tkinter import * 
import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox 
# import tkinter.font as font 
# from tkinter import filedialog

from c_inversa import c_inversa
from backend_esp import backend

import numpy as np 

# import os 


class Application(ttk.Frame):
    def __init__(self, master= None):
        # self.log = loggingReport.Logging()
        try: 
            super().__init__(master)
            self.master = master 
            self.master.geometry("800x400")
            self.master.resizable(False,False)
            
            self.puntos = {"x":[], "y":[],"z":[]}
            
            self.delta_config = {"L_1": 200,
                                "L_2": 400, 
                                "D": 415,
                                "d": 100,
                                "h" : 100,
                                "speed":2000,
                                "accel":600
                                }
            
            self.frame_title = tk.Frame(master=self.master,
                                        width=800, height=50, 
                                        relief=tk.SOLID,
                                        borderwidth=2)
            self.frame_title_in()
            self.frame_title.pack(fill=tk.X)
            
            self.frame_Body = tk.Frame(master=self.master, 
                                       width=800, height=350)
            self.frame_body_in()
            self.frame_Body.pack(fill=tk.BOTH, expand="yes")
            
            self.create_widgets()
            self.master.mainloop()
            
        except Exception as e:
            print(str(e))
            
    
    
    def create_widgets(self): 
        
        self.frame_ip_widget()
        self.frame_micro_widget()
        self.frame_puntos_widget()
        self.frame_btton_agregar_widget()
        self.frame_btton_enviar_widget()
        self.frame_btton_home_widget()
        self.frame_btton_config_widget()
        self.frame_btton_test_widget()
        
    
    def  frame_btton_test_widget(self): 
        self.frame_test =tk.Frame(master=self.frame_right, 
                                    width=400, height=100)
        self.frame_test.pack(fill=tk.BOTH, expand="yes" )
        
        text_test = Label(self.frame_test, 
                        text= "Test cuarto de milla", 
                        bd=4, font=("curier 10 bold") )
        
        text_test.pack(side=TOP ,fill=tk.X)
        self.frame_btton_test = tk.Frame(master=self.frame_test, 
                                           width=400, height=50)
        
        ttk.Button(self.frame_btton_test, 
                   text="test", 
                   command= self.bttn_test).pack(side=TOP)
        
        self.frame_btton_test.pack()
        
    def bttn_test(self): 
        list_t1 =[53.78,49.57,1.31,8.29]
        list_t2 =[8.29, 1.31, 49.57, 53.7]
        list_t3 =[33.25, 27.63, 27.63,33.25]

        
        payload = {"Micros":2**int(self.micro.get()), 
                   "M1":list_t1,
                   "M2":list_t2,
                   "M3":list_t3, 
                   "speed":self.delta_config["speed"], 
                   "accel":self.delta_config["accel"]}
        
        r = backend(ip= str(self.ip.get()), payload= payload) 
       
       
    def frame_btton_config_widget(self): 
        self.frame_config =tk.Frame(master=self.frame_right, 
                                    width=400, height=100)
        self.frame_config.pack(fill=tk.BOTH, expand="yes" )
        
        text_config = Label(self.frame_config, 
                        text= "Configurar dimensiones del robot delta", 
                        bd=4, font=("curier 10 bold") )
        
        text_config.pack(side=TOP ,fill=tk.X)
        self.frame_btton_config = tk.Frame(master=self.frame_config, 
                                           width=400, height=50)
        
        ttk.Button(self.frame_btton_config, 
                   text="Config", 
                   command= self.bttn_config).pack(side=TOP)
        
        self.frame_btton_config.pack()
        pass 
    
    def bttn_config(self): 
        self.newWindow = Toplevel(self.master)
        self.newWindow.title("config Window")
 
        # sets the geometry of toplevel
        self.newWindow.geometry("300x300")
    
        # A Label widget to show in toplevel
        Text_title = Label(self.newWindow,
                            text ="configuración de valores del robot Delta",
                            font=("curier 10 bold"))
        Text_title.pack()
        
        self.entrys(self.newWindow)
        self.frame_btton_save = tk.Frame(master=self.newWindow,
                                     width=300, 
                                     height=50)
        ttk.Button(self.frame_btton_save, 
                   text="Save", 
                   command= self.bttn_save).pack(side=TOP)
        
        self.frame_btton_save.pack()
        
    
    def bttn_save(self): 
        for keys, value in self.config_StringVar.items(): 
            self.delta_config[keys] = int(value.get())
              
        self.newWindow.destroy()
               

        
    def entrys(self, Window):
        self.config_StringVar ={} #  variables stringVar
        self.entrys_config ={} # los entrys 
        self.labels_config = {}
        
        self.list_frames_nw = [tk.Frame(master=Window,
                                     width=300, 
                                     height=50)for i in self.delta_config.keys()]
        id = 0 
        for key, value in self.delta_config.items():
            self.labels_config[key] = Label(self.list_frames_nw[id], 
                                          text= key, 
                                          bd=0, 
                                          font=("curier 11 bold"))
            
            self.labels_config[key].pack(side= LEFT)
            
            self.config_StringVar[key] =IntVar(value= value)
            # self.config_StringVar[value].set("0")
            
            self.entrys_config[key] = Entry(self.list_frames_nw[id],
                                          textvariable= self.config_StringVar[key])
            self.entrys_config[key].pack(side= RIGHT)
            id += 1 
        
        for frames in self.list_frames_nw: 
            frames.pack(fill=tk.X, expand="yes" )
            
    
    
    def frame_btton_home_widget(self): 
        self.frame_home =tk.Frame(master=self.frame_right, 
                                    width=400, height=100)
        self.frame_home.pack(fill=tk.X, expand="yes" )
        
        text_home = Label(self.frame_home, 
                        text= "Configurar posición actual como posición home", 
                        bd=4, font=("curier 10 bold") )
        
        text_home.pack(side=TOP ,fill=tk.X)
        self.frame_btton_home = tk.Frame(master=self.frame_home, 
                                           width=400, height=50)
        
        ttk.Button(self.frame_btton_home, 
                   text="Home", 
                   command= self.bttn_home).pack(side=TOP)
        
        self.frame_btton_home.pack()
        pass 
    
    def bttn_home(self): 
        payload = {"Micros":-1, 
                   "M1":[0],"M2":[0],"M3":[0], 
                   "speed":self.delta_config["speed"], 
                   "accel":self.delta_config["accel"]}
        
        r = backend(ip= str(self.ip.get()), payload= payload)
        
    
    
    def frame_btton_enviar_widget(self):
        self.frame_enviar =tk.Frame(master=self.frame_right, 
                                    width=400, height=50)
        self.frame_enviar.pack(side =TOP ,fill=tk.X, expand="yes" )
    
        text_enviar = Label(self.frame_enviar, 
                        text= "Enviar datos a Servidor WEB", 
                        bd=4, font=("curier 10 bold") )
        
        text_enviar.pack(side=TOP ,fill=tk.X)
        self.frame_btton_enviar = tk.Frame(master=self.frame_enviar, 
                                           width=400, height=50)
        
        ttk.Button(self.frame_btton_enviar, 
                   text="Enviar", 
                   command= self.bttn_enviar).pack(side=TOP)
        self.frame_btton_enviar.pack()
        
        
    def transform(self): 
        # ip = 
        # ip = "192.168.251.233"
        if not self.puntos["x"]: 
            messagebox.showwarning("Warning","No existen puntos agregados")
            return 

        list_t1 = []
        list_t2 = []
        list_t3 = []
        for i, value in enumerate(self.puntos["x"]): 
            Punto = np.array([int(value),
                    int(self.puntos["y"][i]),
                    int(self.puntos["z"][i])])
            k, movimientos = c_inversa(L_1= self.delta_config["L_1"],
                                       L_2= self.delta_config["L_2"], 
                                        D= self.delta_config["D"],
                                        d= self.delta_config["d"],
                                        h = self.delta_config["h"],
                                        P =Punto)
            if k: 
                list_t1.append(int(movimientos[0]*100)/100.0)
                list_t2.append(int(movimientos[1]*100)/100.0)
                list_t3.append(int(movimientos[2]*100)/100.0)
                
            else: 
                messagebox.showerror("Error",f"El punto {Punto} no existe dentro del espacio de trabajo")
        if list_t1: 
            payload = {"Micros":2**int(self.micro.get()),
                        "M1":list_t1,
                        "M2":list_t2,
                        "M3":list_t3,
                        "speed":self.delta_config["speed"],
                        "accel":self.delta_config["accel"]}
            # print(payload)
            r = backend(ip= str(self.ip.get()), payload= payload)
                
                

    def clear(self): 
        self.puntos = {"x":[], "y":[],"z":[]}
        for id, value in enumerate(self.list_ejes):
            text = value +":" +str(self.puntos[value]) 
            self.dict_texts[value].config(text= text)


    def bttn_enviar(self):
        # payload = {
        #     "Micro": str(self.micro.get()),
        #     "X": self.puntos["x"],
        #     "Y": self.puntos["y"],
        #     "Z": self.puntos["z"],
        # }
        self.transform()
        self.clear()
        
            
    def frame_title_in(self):
        text = Label(self.frame_title, 
                     text= "Interfaz grafica robot delta de 3 grados de libertad", 
                     bd=4, fg= "#666a88", 
                     bg="#fcfcfc", 
                     font=("Times 18 bold"))
        text.pack(fill=tk.X, side=TOP)
        
    
    def frame_body_in(self): 
        self.frame_left = LabelFrame(master=self.frame_Body, 
                                     width=300, height=350,
                                     relief=tk.RAISED,
                                     borderwidth=1)
        self.frame_right = LabelFrame(master=self.frame_Body, 
                                      width=300, height=350,
                                      relief=tk.RAISED,
                                      borderwidth=1)
        
        self.frame_right.pack(side=RIGHT, fill=tk.BOTH, expand="yes")
        self.frame_left.pack(side=LEFT, fill=tk.BOTH, expand="yes")
            
    
    def frame_ip_widget(self): 
        self.frame_ip =tk.Frame(master=self.frame_left, 
                                width=400, height=50)
        
        text_ip = Label(self.frame_ip, 
                        text= "Escribe aquí la ip del servidor", 
                        bd=4, font=("curier 10"))
        text_ip.pack(side= LEFT)
        
        self.ip = StringVar()
        self.ip.set("192.168.195.61")
        self.set_ip = Entry(self.frame_ip , textvariable= self.ip)
        self.set_ip.pack(side=LEFT)
        
        self.frame_ip.pack(fill=tk.BOTH, expand="yes")
        
        
    def frame_micro_widget(self): 
        self.frame_micro = tk.Frame(master=self.frame_left, 
                                    width=400, height=150)
        
        text_micro = Label(self.frame_micro,
                           text= "Microstepping",
                           bd=4, font=("curier 14 bold"))
        text_micro.pack()
        
        self.text_sel_micro =  Label(self.frame_micro, 
                                     text= "Seleciona un Microstepping", 
                                     bd=4, font=("curier 9"))
        self.text_sel_micro.pack()
        
        self.frame_micro.pack(fill=tk.BOTH, expand="yes")
        
        self.list_micros = ["Full","1/2","1/4","1/8","1/16","1/32"]
        self.dict_micros= {}
        self.micro = IntVar()
        
        for id, value in enumerate(self.list_micros): 
            self.dict_micros[value]=Radiobutton(self.frame_micro, 
                                           text=value, 
                                           value=id, 
                                           variable=self.micro,
                                           command=self.sel) 
            self.dict_micros[value].pack(side =LEFT ,anchor= W)


    def sel(self):
        selection = "Has seleccionado " \
            + str(self.list_micros[self.micro.get()])
        self.text_sel_micro.config(text = selection)

            
    def frame_puntos_widget(self):
        self.frame_puntos = tk.Frame(master=self.frame_left, width=400, height=300)
        
        text_puntos = Label(self.frame_puntos, 
                            text= "Lista de puntos en el espacio de trabajo", 
                            bd=4, #bg="#3a7ff6",
                            font=("curier 14 bold"))
        text_puntos.pack()
        
        self.list_ejes = ["x", "y", "z"] #valores 
        self.ejes_StringVar ={} #  variables stringVar
        self.dict_ejes ={} # los entrys 
        
        
        self.list_frames = [tk.Frame(master=self.frame_puntos,
                                     width=400, 
                                     height=100)for i in self.list_ejes]
            
        for id, value in enumerate(self.list_ejes):
            self.dict_ejes[value] = Label(self.list_frames[id], 
                                          text= value, 
                                          bd=0, 
                                          font=("curier 11"))
            self.dict_ejes[value].pack(side= LEFT)
            
            self.ejes_StringVar[value] =StringVar()
            self.ejes_StringVar[value].set("0")
            
            self.dict_ejes[value] = Entry(self.list_frames[id],
                                          textvariable= self.ejes_StringVar[value])
            self.dict_ejes[value].pack(side= RIGHT)
        
        for value in self.list_frames: 
            value.pack()
       
        self.frame_puntos.pack(fill=tk.BOTH, expand="yes")
        
            
    def frame_btton_agregar_widget(self):
        self.list_text = [tk.Frame(master=self.frame_left, 
                                   width=400, 
                                   height=100)for i in self.list_ejes]
        self.dict_texts = {}
        for id, value in enumerate(self.list_ejes):
            
            self.dict_texts[value] = Label(self.list_text[id], 
                                          text= value, 
                                          bd=0, 
                                          font=("curier 11"))
            
            self.dict_texts[value].pack(side=LEFT)
        
        ttk.Button(self.frame_left, 
                   text="Agregar", 
                   command= self.bttn_agregar).pack()
        
        for value in self.list_text: 
            value.pack()
    
        
    def bttn_agregar(self): 
        for id, value in enumerate(self.list_ejes):
            self.puntos[value].append(self.ejes_StringVar[value].get())
            
            text = value +":" +str(self.puntos[value]) 
            self.dict_texts[value].config(text= text)
       
        

def main(): 
    root = tk.Tk()
    # default_font = font.Font(family="Helvetica", size=25, weight="bold")
    root.title("Robot delta")
    app = Application(master = root )