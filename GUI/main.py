from gui import main_gui

from backend_esp import backend

if __name__ == "__main__":
    main_gui()


def example():
    # from c_inversa import c_inversa
    payload = {"Micros": 32, "M1": 50, "M2": 50, "M3": 50, "speed": 3000, "accel": 20}
    ip = "192.168.195.61"
    # ip = "192.168.251.233"
    # c_inversa(L_1= 200,L_2= 400,
    #           D= 216, d= 100,h = 110,
    #           P =np.array([380,40,300]))
    r = backend(ip=ip, payload=payload)
    pass
