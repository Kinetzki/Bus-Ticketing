import customtkinter as ctk
import retrieve
import argparse
import subprocess
import time 
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("bus", type=str)
parser.add_argument("num", type=str)
parser.add_argument("date", type=str)
parser.add_argument("user", type=str)
args = parser.parse_args()

def summarize():
    seat_num = seats_box.get()
    #os.system(f'python summary.py "{args.bus}" "{args.num}" "{args.date}" "{args.user}" "{seat_num}"')
    subprocess.Popen(['python', 'summary.py', args.bus, args.num, args.date, args.user, seat_num])
    time.sleep(2.5)
    window.destroy()

window = ctk.CTk()
SCREEN_WIDTH = window.winfo_screenwidth()
WIDTH = 650
HEIGHT = 650
bgcolor = '#181460'
window.geometry(f'{WIDTH}x{HEIGHT}+{int(SCREEN_WIDTH/2)-int(WIDTH/2)}+{10}')
window.title('Bus Reservation Convenience Kiosk Seat Confirmation')
window.configure(fg_color=bgcolor)

neon_blue = '#58c1f6'
header_frame = ctk.CTkFrame(master=window,
                          fg_color='#242172',
                          width=600,
                          height=50)
header_label = ctk.CTkLabel(master=header_frame,
                            font=('Arial bold', 20),
                            text='Validate your booking')
header_label.pack(pady=15)
header_frame.pack(pady=10)
header_frame.pack_propagate(False)

info_frame = ctk.CTkFrame(master=window,
                          fg_color='#242172',
                          width=600,
                          height=300)
right_frame = ctk.CTkFrame(master=info_frame,
                           height=250, width=220,
                           fg_color='#181460')
right_frame.pack(side='left', padx=10)
right_frame.pack_propagate(False)
left_frame = ctk.CTkFrame(master=info_frame,
                          height=250, width=350,
                          fg_color='#181460')
left_frame.pack(side='left')
left_frame.pack_propagate(False)

bus_name_var = ctk.StringVar(value = 'Bus name: ')
bus_name = ctk.CTkLabel(master=right_frame,
                        textvariable = bus_name_var,
                        font=('Arial', 18),
                        fg_color=neon_blue, text_color=bgcolor,
                        corner_radius=20, width=150
                        )
bus_name.pack(pady=10)
bus_name.pack_propagate(False)

bus_number_var = ctk.StringVar(value = 'Bus number: ')
bus_number = ctk.CTkLabel(master=right_frame,
                        textvariable=bus_number_var,
                        font=('Arial', 18),
                        fg_color=neon_blue, text_color=bgcolor,
                        corner_radius=20, width=150)
bus_number.pack(pady=10)
bus_number.pack_propagate(False)
name_var = ctk.StringVar(value = 'Name: ')
name_number = ctk.CTkLabel(master=right_frame,
                        textvariable=name_var,
                        font=('Arial', 18),
                        fg_color=neon_blue, text_color=bgcolor,
                        corner_radius=20, width=150)
name_number.pack(pady=10)

date_var = ctk.StringVar(value = 'Date: ')
date_label = ctk.CTkLabel(master=right_frame,
                        font=('Arial', 18),
                        fg_color=neon_blue, text_color=bgcolor,
                        corner_radius=20, width=150,
                        textvariable = date_var)
date_label.pack(pady=10)

seat_label = ctk.CTkLabel(master=right_frame,
                        font=('Arial', 15),
                        text= 'Please choose seat number')
seat_label.pack()

#RIGHT
bus_name_var = ctk.StringVar(value = args.bus)
bus_name = ctk.CTkLabel(master=left_frame,
                        textvariable = bus_name_var,
                        font=('Arial', 18),
                        fg_color=neon_blue, text_color=bgcolor,
                        corner_radius=20, width=260
                        )
bus_name.pack(pady=10)
bus_name.pack_propagate(False)

bus_number_var = ctk.StringVar(value = args.num)
bus_number = ctk.CTkLabel(master=left_frame,
                        textvariable=bus_number_var,
                        font=('Arial', 18),
                        fg_color=neon_blue, text_color=bgcolor,
                        corner_radius=20, width=200)
bus_number.pack(pady=10)
bus_number.pack_propagate(False)
name_var = ctk.StringVar(value = args.user)
name_number = ctk.CTkLabel(master=left_frame,
                        textvariable=name_var,
                        font=('Arial', 18),
                        fg_color=neon_blue, text_color=bgcolor,
                        corner_radius=20, width=280)
name_number.pack(pady=10)

date_var = ctk.StringVar(value = args.date)
date_label = ctk.CTkLabel(master=left_frame,
                        font=('Arial', 18),
                        fg_color=neon_blue, text_color=bgcolor,
                        corner_radius=20, width=200,
                        textvariable = date_var)
date_label.pack(pady=10)

seats = retrieve.get_available_seat_numbers(args.bus, args.date)
seats_box = ctk.CTkComboBox(master = left_frame,
                                values=seats,
                                fg_color='#242172',
                                border_color='#242172',
                                button_color=neon_blue,
                                width=180,
                                height=35,
                                dropdown_fg_color='#242172',
                                dropdown_text_color='white')
seats_box.pack(padx=10)
info_frame.pack(pady=10)
info_frame.pack_propagate(False)

write_img = ctk.CTkImage(light_image=Image.open("icons/confirm.png"), size=(30, 30))
confirm_button = ctk.CTkButton(master=window,
                               fg_color='#008ECC',
                               text='Confirm Booking',
                               font=('Arial', 18),
                               corner_radius=20,
                               width=200,
                               height=45,
                               command=summarize,
                               text_color='white',
                               image=write_img)
confirm_button.pack(pady=20)

window.mainloop()
