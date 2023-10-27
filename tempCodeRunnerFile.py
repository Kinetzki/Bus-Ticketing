import customtkinter as ctk
import retrieve
import argparse
import os

window = ctk.CTk()
SCREEN_WIDTH = window.winfo_screenwidth()
WIDTH = 650
HEIGHT = 650
bgcolor = '#181460'
window.geometry(f'{WIDTH}x{HEIGHT}+{int(SCREEN_WIDTH/2)-int(WIDTH/2)}+{10}')
window.title('Bus Ticketing')
window.configure(fg_color=bgcolor)

neon_blue = '#58c1f6'

info_frame = ctk.CTkFrame(master=window,
                          fg_color='#242172',
                          width=600,
                          height=300)
right_frame = ctk.CTkFrame(master=info_frame,
                           height=250, width=280,
                           fg_color='#181460')
right_frame.pack(side='left', padx=10)
right_frame.pack_propagate(False)
left_frame = ctk.CTkFrame(master=info_frame,
                          height=250, width=280,
                          fg_color='#181460')
left_frame.pack(side='left')
left_frame.pack_propagate(False)

bus_name_var = ctk.StringVar(value = 'Bus name: ')
bus_name = ctk.CTkLabel(master=right_frame,
                        textvariable = bus_name_var,
                        font=('Arial', 18),
                        fg_color=neon_blue, text_color=bgcolor,
                        corner_radius=20, width=200
                        )
bus_name.pack(pady=10)
bus_name.pack_propagate(False)

bus_number_var = ctk.StringVar(value = 'Bus number: ')
bus_number = ctk.CTkLabel(master=right_frame,
                        textvariable=bus_number_var,
                        font=('Arial', 18),
                        fg_color=neon_blue, text_color=bgcolor,
                        corner_radius=20, width=200)
bus_number.pack(pady=10)
bus_number.pack_propagate(False)
name_var = ctk.StringVar(value = 'Name: ')
name_number = ctk.CTkLabel(master=right_frame,
                        textvariable=name_var,
                        font=('Arial', 18),
                        fg_color=neon_blue, text_color=bgcolor,
                        corner_radius=20, width=200)
name_number.pack(pady=10)

date_var = ctk.StringVar(value = 'Date: ')
date_label = ctk.CTkLabel(master=right_frame,
                        font=('Arial', 18),
                        fg_color=neon_blue, text_color=bgcolor,
                        corner_radius=20, width=200,
                        textvariable = date_var)
date_label.pack(pady=10)

seat_label = ctk.CTkLabel(master=right_frame,
                        font=('Arial', 18),
                        text= 'Please choose seat number')
seat_label.pack()

#RIGHT
bus_name_var = ctk.StringVar(value = 'Bus name: ')
bus_name = ctk.CTkLabel(master=left_frame,
                        textvariable = bus_name_var,
                        font=('Arial', 18),
                        fg_color=neon_blue, text_color=bgcolor,
                        corner_radius=20, width=200
                        )
bus_name.pack(pady=10)
bus_name.pack_propagate(False)

bus_number_var = ctk.StringVar(value = 'Bus number: ')
bus_number = ctk.CTkLabel(master=left_frame,
                        textvariable=bus_number_var,
                        font=('Arial', 18),
                        fg_color=neon_blue, text_color=bgcolor,
                        corner_radius=20, width=200)
bus_number.pack(pady=10)
bus_number.pack_propagate(False)
name_var = ctk.StringVar(value = 'Name: ')
name_number = ctk.CTkLabel(master=left_frame,
                        textvariable=name_var,
                        font=('Arial', 18),
                        fg_color=neon_blue, text_color=bgcolor,
                        corner_radius=20, width=200)
name_number.pack(pady=10)

date_var = ctk.StringVar(value = 'Date: ')
date_label = ctk.CTkLabel(master=left_frame,
                        font=('Arial', 18),
                        fg_color=neon_blue, text_color=bgcolor,
                        corner_radius=20, width=200,
                        textvariable = date_var)
date_label.pack(pady=10)


seats = ['1', '2']
seats_box = ctk.CTkComboBox(master = left_frame,
                                values=seats,
                                fg_color='#242172',
                                border_color=neon_blue,
                                button_color=neon_blue,
                                width=180,
                                height=35)
seats_box.pack(padx=10)


info_frame.pack(pady=60)
info_frame.pack_propagate(False)

confirm_button = ctk.CTkButton(master=window,
                               fg_color=neon_blue,
                               text='Confirm Booking',
                               font=('Arial', 18),
                               corner_radius=20,
                               width=200,
                               height=45)
confirm_button.pack(pady=40)

window.mainloop()
