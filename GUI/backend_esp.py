from tkinter import messagebox
import requests


def backend(ip: str, payload: dict = {"M1": 0, "M2": 0, "M3": 0}):
    try:
        r = requests.post(f"http://{ip}:80", json=payload)
    except Exception as e:
        messagebox.showerror("Error", "Error estableciendo conexión " + str(e))
        # print("Error de backend: " + str(e))
        r = None
    return r


def example():
    payload = {"Micros": -2, "M1": 0, "M2": 0, "M3": 0,
               "speed": 2000, "accel": 400}
    ip = "192.168.195.61"
    # ip = "192.168.251.233"
    # c_inversa(L_1= 200,L_2= 400,
    #           D= 216, d= 100,h = 110,
    #           P =np.array([380,40,300]))
    r = backend(ip=ip, payload=payload)
    print(r)


if __name__ == "__main__":
    example()
