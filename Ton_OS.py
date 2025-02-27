import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time
import threading

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
root.title("Ton")
root.attributes('-fullscreen', True)
root.config(cursor="none")
root.config(bg="black")

boot_text = tk.Label(root, text="Finding boot device.", font=("Fixedsys", 27))
boot_text.config(bg="black", fg="#8f8f8f")
boot_text.place(x=20, y=20)

def update_boot_text():
    boot_text.config(text="Booting.")

def dot1_update():
    boot_text.config(text="Finding boot device..")

def dot2_update():
    boot_text.config(text="Finding boot device...")

def dot3_update():
    boot_text.config(text="Booting..")

def dot4_update():
    boot_text.config(text="Booting...")

def delete_boot_text():
    boot_text.destroy()

TonImage = tk.PhotoImage(file="Ton_Logo.png")
DesktopBGimage = tk.PhotoImage(file="Black hole_BG.png")
EnterBGImage = tk.PhotoImage(file="Black_hole_blur.png")

def showbootlogo():
    global TonLogo
    TonLogo = tk.Label(root, image=TonImage, bg="black")
    TonLogo.place(x=750, y=270)

def desbootlogo():
    global TonLogo  
    TonLogo.destroy()


def run_scan():
    scan_window = tk.Toplevel(root)
    scan_window.title("Running Scan...")
    scan_window.geometry("300x150")
    scan_window.config(bg="#696969")
    center_window(scan_window, 300, 150)
    
    
    progress = ttk.Progressbar(scan_window, length=250, mode='determinate', maximum=100)
    progress.pack(pady=30)
    

    def update_progress():
        for i in range(101):
            progress['value'] = i
            scan_window.update()
            time.sleep(0.15) 
        messagebox.showinfo("Scan Complete", "The scan has completed successfully!")
        scan_window.destroy()  

    
    threading.Thread(target=update_progress).start()

def OpenStartMenu():
    global StartMenu
    StartMenu = tk.Toplevel()
    StartMenu.config(bg="#212121")
    StartMenu.resizable(False, False)
    StartMenu.overrideredirect(True)
    StartMenu.geometry("500x600+20+400")

    label = tk.Label(StartMenu, width=66, height=37, bg='#3b3a3a')
    label.place(x=15, y=16)

    CloseStartMenuButton = tk.Button(StartMenu, text="❌", font=("Arial", 24), bg="#292929", fg="white", activebackground="#1c1b1b", activeforeground="white", command=CloseStartMenu)
    CloseStartMenuButton.place(x=390, y=35)

    ShutDownButton = tk.Button(StartMenu, text="⏹️", font=("Arial", 24), bg="#292929", fg="white", activebackground="#1c1b1b", activeforeground="white", command=ShutDown)
    ShutDownButton.place(x=30, y=500)

    RestartButton = tk.Button(StartMenu, text="🔁", font=("Arial", 28), bg="#292929", fg="white", activebackground="#1c1b1b", activeforeground="white", height=1, command=Restart)
    RestartButton.place(x=30, y=390)

def ShutDown():
    root.quit()
    
def CloseStartMenu():
    StartMenu.destroy()

def GUIboot():
    global TonLogo, EnterButton, DesktopBG, StartMenuButton, MyPCButton
    root.config(bg="black")
    TonLogo.destroy()  
    EnterBG.destroy()
    EnterButton.destroy() 
    DesktopBG = tk.Label(root, image=DesktopBGimage, bg="black")
    DesktopBG.place(x=0, y=0)
    DesktopBG.lower()

    StartMenuButton = tk.Button(root, text="🚀", font=("Arial", 19), bg="#292929", fg="white", activebackground="#1c1b1b", activeforeground="#cfcccc", command=OpenStartMenu)
    StartMenuButton.place(x=10, y=1020)

    MyPCButton = tk.Button(root, text="🖥", font=("Arial", 30), bg="#292929", fg="white", activebackground="#1c1b1b", activeforeground="#cfcccc", command=OpenMyPC)
    MyPCButton.place(x=30, y=30)

def OpenMyPC():
    global MyPC
    MyPC = tk.Toplevel()
    MyPC.title("My PC")
    MyPC.resizable(False, False)
    MyPC.geometry("900x600")
    MyPC.config(bg="#696969")
    center_window(MyPC, 900, 600)

    def openSystem():
        System = tk.Toplevel()
        System.title("System")
        System.geometry("900x600")
        System.config(bg="#696969")
        System.resizable(False, False)
        center_window(System, 900, 600)

        UI_SYS_label = tk.Label(System, text="", font=("Arial", 24), width=46, height=16, bg="#3d3d3d")
        UI_SYS_label.lower()
        UI_SYS_label.place(x=10, y=10)

        SYS_Error_label = tk.Label(System, text="No errors detected :)", bg="#3d3d3d", fg="#ebebeb", font=("Arial", 28))
        SYS_Error_label.place(x=300, y=50)

        SYS_Run_scan_button = tk.Button(System, text="Run scan", font=("Arial", 28), bg="#6b6b6b", activebackground="#949494", command=run_scan)
        SYS_Run_scan_button.place(x=350, y=250)

    def openDrivers():
        Drivers = tk.Toplevel()
        Drivers.title("Drivers")
        Drivers.geometry("900x600")
        Drivers.config(bg="#696969")
        Drivers.resizable(False, False)
        center_window(Drivers, 900, 600)

        UI_DRV_label = tk.Label(Drivers, text="", font=("Arial", 24), width=46, height=16, bg="#3d3d3d")
        UI_DRV_label.lower()
        UI_DRV_label.place(x=10, y=10)

        GPU_Driver_button = tk.Button(Drivers, text="GPU Drivers", font=("Arial", 26), command=openGPU_Drivers_menu, bg="#6b6b6b", activebackground="#949494")
        GPU_Driver_button.place(x=340, y=50)

    def openGPU_Drivers_menu():
        GPU_Drivers_menu = tk.Toplevel()
        GPU_Drivers_menu.title("GPU Drivers")
        GPU_Drivers_menu.geometry("900x600")
        GPU_Drivers_menu.config(bg="#696969")
        GPU_Drivers_menu.resizable(False, False)
        center_window(GPU_Drivers_menu, 900, 600)
        
        UI_GPD_label = tk.Label(GPU_Drivers_menu, text="", font=("Arial", 24), width=46, height=16, bg="#3d3d3d")
        UI_GPD_label.lower()
        UI_GPD_label.place(x=10, y=10)

        DRV_GPU_missing_label = tk.Label(GPU_Drivers_menu, text="No drivers missing", font=("Arial", 28), bg="#3d3d3d", fg="white")
        DRV_GPU_missing_label.place(x=300, y=60)

        UI_GDM_label = tk.Label(GPU_Drivers_menu, text="", font=("Arial", 24), width=23, height=4, bg="#1c1c1c")
        UI_GDM_label.place(x=245, y=130)

        DRV_GPU_updates_label = tk.Label(GPU_Drivers_menu, text="No new GPU drivers updates", font=("Arial", 28), bg="#3d3d3d", fg="white")
        DRV_GPU_updates_label.place(x=230, y=300)

    def openComponents():
        ComponentError = tk.Toplevel()
        ComponentError.title("Components")
        ComponentError.geometry("900x600")
        ComponentError.resizable(False, False)
        ComponentError.config(bg="#696969")
        center_window(ComponentError, 900, 600)

        UI_CME_label = tk.Label(ComponentError, text="", font=("Arial", 24), width=46, height=16, bg="#3d3d3d")
        UI_CME_label.lower()
        UI_CME_label.place(x=10, y=10)  

    def openDelete():
        DeleteProg = tk.Toplevel()
        DeleteProg.title("Delete Programs")
        DeleteProg.geometry("900x600")
        DeleteProg.resizable(False, False)
        DeleteProg.config(bg="#696969")
        center_window(DeleteProg, 900, 600)

        UI_DEP_label = tk.Label(DeleteProg, text="", font=("Arial", 24), width=46, height=16, bg="#3d3d3d")
        UI_DEP_label.lower()
        UI_DEP_label.place(x=10, y=10)

    def openOS_data():
        OSdata = tk.Toplevel()
        OSdata.title("OS Data")
        OSdata.geometry("900x600")
        OSdata.resizable(False, False)
        OSdata.config(bg="#696969")
        center_window(OSdata, 900, 600)

        UI_OSD_label = tk.Label(OSdata, text="", font=("Arial", 24), width=46, height=16, bg="#3d3d3d")
        UI_OSD_label.lower()
        UI_OSD_label.place(x=10, y=10)

    DividerLabel = tk.Label(MyPC, text="", height=300)
    DividerLabel.config(bg="#b3b3b3")
    DividerLabel.place(x=310)

    UI_MP_label = tk.Label(MyPC, text="", font=("Arial", 24), width=46, height=16, bg="#3d3d3d")
    UI_MP_label.lower()
    UI_MP_label.place(x=10, y=10)

    SystemButton = tk.Button(MyPC, text="System", font=("Arial", 24), command=openSystem, bg="#6b6b6b", activebackground="#949494")
    SystemButton.place(x=55, y=30)

    DriversButton = tk.Button(MyPC, text="Drivers", font=("Arial", 24), command=openDrivers, bg="#6b6b6b", activebackground="#949494")
    DriversButton.place(x=55, y=150)

    ComponentsButton = tk.Button(MyPC, text="Components", font=("Arial", 24), command=openComponents, bg="#6b6b6b", activebackground="#949494")
    ComponentsButton.place(x=55, y=270)

    DeleteButton = tk.Button(MyPC, text="Delete", font=("Arial", 24), command=openDelete, bg="#6b6b6b", activebackground="#949494")
    DeleteButton.place(x=55, y=390)

    OSButton = tk.Button(MyPC, text="OS", font=("Arial", 24), command=openOS_data, bg="#6b6b6b", activebackground="#949494")
    OSButton.place(x=55, y=510)

    MemoryC = tk.Label(MyPC, text="[|||     ] 213 GB used of 512 GB", font=("Arial", 24), bg="#3d3d3d", fg="#ebebeb")
    MemoryC.place(x=380, y=150)

    Cmem_Label = tk.Label(MyPC, text="C: Disk | 512 GB", font=("Arial", 24), bg="#3d3d3d", fg="#ebebeb")
    Cmem_Label.place(x=470, y=80)

    Dmem_Label = tk.Label(MyPC, text="D: Disk | 512 GB", font=("Arial", 24), bg="#3d3d3d", fg="#ebebeb")
    Dmem_Label.place(x=470, y=250)

    MemoryD = tk.Label(MyPC, text="[||      ] 167 GB used of 512 GB", font=("Arial", 24), bg="#3d3d3d", fg="#ebebeb")
    MemoryD.place(x=380, y=320)

    MemoryF = tk.Label(MyPC, text="[||      ] 182 GB used of 512 GB", font=("Arial", 24), bg="#3d3d3d", fg="#ebebeb")
    MemoryF.place(x=380, y=490)

    Fmem_label = tk.Label(MyPC , text="F: Disk | 512 GB", font=("Arial", 24), bg="#3d3d3d", fg="#ebebeb")
    Fmem_label.place(x=470, y=420)


def boot():
    global TonLogo, EnterButton, EnterBG
    EnterBG = tk.Label(root, image=EnterBGImage)
    EnterBG.pack()
    TonLogo = tk.Label(root, image=TonImage, bg="#6d0fd1")
    TonLogo.place(x=75000, y=12000 )
    root.config(cursor="arrow")
    EnterButton = tk.Button(root, text="Enter", font=("Arial", 30), width=10, bg="#9c45ff", fg="white", activebackground="#8419fc", activeforeground="white", command=GUIboot, relief="ridge")
    EnterButton.place(x=850, y=500)

def Restart():
    DesktopBG.destroy()
    StartMenuButton.destroy()
    StartMenu.destroy()
    MyPCButton.destroy()
    root.config(cursor="none")
    root.after(13000, showbootlogo)
    root.after(17000, desbootlogo)
    root.after(17500, boot)

boot_text.after(5000, update_boot_text)
boot_text.after(2000, dot1_update)
boot_text.after(3500, dot2_update)
boot_text.after(6000, dot3_update)
boot_text.after(8000, dot4_update)
boot_text.after(10000, delete_boot_text)
root.after(13000, showbootlogo)
root.after(17000, desbootlogo)
root.after(1700, boot)

root.mainloop()
