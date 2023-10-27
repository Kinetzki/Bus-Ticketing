import customtkinter as ctk
import time
from PIL import Image
import subprocess

window = ctk.CTk()
SCREEN_WIDTH = window.winfo_screenwidth()
SCREEN_HEIGHT = window.winfo_screenheight()
window.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
window.after(0, lambda:window.state('zoomed'))
window.title('Bus Reservation Convenience Kiosk Admin LOGIN')
window.configure(fg_color='#181460')

def verify_login():
    password = 'admin'
    username = 'admin'
    if username_entry.get() != username or password_entry.get() != password:
        print('Incorrect')
        incorrect_label = ctk.CTkLabel(master=frame1,
                                text='Incorrect username/password...Please try again.',
                                font=('Arial', 15),
                                text_color='#58c1f6')
        incorrect_label.pack(pady=20)
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
    elif username_entry.get() == username and password_entry.get() == password:
        subprocess.Popen(['python', 'admin_panel.py'])
        time.sleep(2.5)
        window.destroy()


admin_img = ctk.CTkImage(light_image=Image.open("icons/setting.png"), size=(60, 60))
head_frame = ctk.CTkFrame(master=window, fg_color='transparent')
head_frame.pack()
admin_label = ctk.CTkLabel(master=head_frame, fg_color='transparent', image=admin_img,
                           text='')
admin_label.pack(side='left')
verify_label = ctk.CTkLabel(master=head_frame,
                            font=('Berlin bold', 20),
                            text='Log in as admin')
verify_label.pack(pady=30, side='left')

login_frame = ctk.CTkFrame(master=window,
                           fg_color="#242172",
                           width=450,
                           height=500,corner_radius=50)
spacer = ctk.CTkFrame(master=login_frame,
                      fg_color='transparent',
                      height=50)
spacer.pack(pady=3)
username_label = ctk.CTkLabel(master=login_frame,
                              text="Username",
                              font=('Arial bold', 15))
username_label.pack(pady=20,anchor='nw',padx=55)
username_entry = ctk.CTkEntry(master=login_frame, 
                            font=('Arial', 18),
                            fg_color='#0E4D92',
                            border_color="#58c1f6",
                            height=50,
                            width=350,
                            corner_radius=10,
                            placeholder_text='Enter username')
username_entry.pack()
password_label = ctk.CTkLabel(master=login_frame,
                              text="Password",
                              font=('Arial bold', 15))
password_label.pack(pady=20,anchor='nw',padx=55)
password_entry = ctk.CTkEntry(master=login_frame, 
                            font=('Arial', 18),
                            fg_color='#0E4D92',
                            border_color="#58c1f6",
                            height=50,
                            width=350,
                            corner_radius=10,
                            placeholder_text='Enter password',
                            show='*')
password_entry.pack()

verify_img = ctk.CTkImage(light_image=Image.open("icons/enter.png"), size=(30, 30))
verify_button = ctk.CTkButton(master=login_frame,
                              text='Verify',
                              fg_color='#181460',
                              font=('Arial bold', 17),
                              width=200,
                              height=40,
                              corner_radius=20,
                              command=verify_login,
                              image=verify_img)
verify_button.pack(pady=40)
frame1 = ctk.CTkFrame(master=login_frame,
                              fg_color='#242172', #181460
                              width=300,height=60)
frame1.pack()
frame1.pack_propagate(False)
login_frame.pack()
login_frame.pack_propagate(False)

window.mainloop()
