import customtkinter as ctk
import datetime
import retrieve
import os
from PIL import Image
import time 
import subprocess

date_1 = datetime.datetime.strptime(datetime.datetime.now().strftime('%m/%d/%y'), "%m/%d/%y")
dates = [(date_1 + datetime.timedelta(days=x)).strftime('%m/%d/%y - %A') for x in range(11)]
def register_this():
  dat = date_box.get()
  dat = dat.split(' - ')[0].replace('/', '_')
  display_bookings(dat)
  display_buses()
  bus = bus_entry.get()
  bus_entry.delete(0, 'end')
  num = bus_num_entry.get()
  bus_num_entry.delete(0, 'end')
  comp = bus_company_entry.get()
  bus_company_entry.delete(0, 'end')
  dest = destination_box.get()
  destination_box.delete(0, 'end')
  source = source_box.get()
  fare = fare_entry.get()
  fare_entry.delete(0, 'end')
  seat_num = seats_entry.get()
  seats_entry.delete(0, 'end')
  air = air_box.get()
  depart = departure_box.get()
  clock = clock_box.get()
  entries = [bus, num, comp, fare, seat_num]
  for i in entries:
    if i == '':
      return
  retrieve.add_bus(bus, num, comp, dest, source, fare, seat_num, air, depart, clock)
  update()

def display_bookings(choice):
  date = date_box.get()
  date = date.split(' - ')[0].replace('/', '_')
  count.set(str(retrieve.get_ticket_count(date)))
  for i in booking_scroll.slaves():
    i.destroy()
  
  date = choice.split(' - ')[0].replace('/', '_')
  print(date)
  buses = retrieve.get_buses()
  bookings = []
  for bus in buses:
    booking = retrieve.get_booking(bus, date)
    bookings.append(len(booking))
  for bus, book in zip(buses, bookings):
    frame = ctk.CTkFrame(master=booking_scroll,
                         height=50,
                        fg_color='#111E6C',
                        width=500)
    bus_label = ctk.CTkLabel(master=frame,
                         text=bus,
                        font=('Arial bold', 15))
    bus_label.pack(side='left', pady=10, padx=20)
    desti = retrieve.get_destination(bus)
    bus_books = ctk.CTkLabel(master=frame,
                          text=book,
                          font=('Arial', 20),
                          fg_color='#0E4D92',
                          width=40,
                          corner_radius=20)
    bus_books.pack(side='right',anchor='e', padx=20)
    rout_label = ctk.CTkLabel(master=frame,
                        text='Bound ' + desti,
                        font=('Arial bold', 10))
    rout_label.pack(side='right', pady=10, padx=20)
    bus_books.pack_propagate(False)
    frame.pack(pady=10, anchor='nw')
    frame.pack_propagate(False)

def remove_func(vals):
  frame, bus_name = vals 
  frame.destroy()
  retrieve.remove_bus(bus_name)
  update()

def logout():
  # os.system('python admin_login.py')
  subprocess.Popen(['python', 'admin_login.py'])
  time.sleep(3)
  window.destroy()

def update():
  dat = date_box.get()
  dat = dat.split(' - ')[0].replace('/', '_')
  display_bookings(dat)
  display_buses()
  buses_count = str(len(retrieve.get_buses()))
  buses_var.set(value=buses_count)

def update_bus_price(vals):
  new_price, bus = vals
  print(f"{new_price.get()}")
  new_pr = new_price.get()
  if new_pr == '':
    return
  retrieve.set_new_price(bus, new_pr)
  new_price.delete(0, 'end')
  update()

def display_buses():
  for i in buses_scroll.slaves():
    i.destroy()
  buses1 = retrieve.get_buses()
  for i in buses1:
    frame = ctk.CTkFrame(master=buses_scroll,
                          height=95,
                          fg_color='#111E6C',
                          width=500)
    inner_frame = ctk.CTkFrame(master=frame, fg_color='transparent')
    bus_label = ctk.CTkLabel(master=inner_frame,
                          text=i,
                          font=('Arial bold', 15))
    bus_label.pack(padx=20, anchor='nw')
    num = retrieve.get_bus_number(i)
    num_label = ctk.CTkLabel(master=inner_frame,
                          text='# ' + num,
                          font=('Arial bold', 10))
    num_label.pack(anchor = 'nw',padx=20)
    pers = retrieve.get_price(i)
    price_label = ctk.CTkLabel(master=inner_frame,
                          text='PHP ' + pers,
                          font=('Arial bold', 13))
    price_label.pack(anchor = 'nw',padx=20)
    inner_frame.pack(side='left')
    remove_img = ctk.CTkImage(light_image=Image.open("icons/delete.png"), size=(20, 20))
    remove_bus = ctk.CTkButton(master=frame,
                               text='delete',
                               fg_color='red',
                               width=100,
                               command= lambda vals=(frame, i): remove_func(vals),
                               image=remove_img)
    remove_bus.pack(side='right', padx=5)
    inner_frame2 = ctk.CTkFrame(master=frame, fg_color='transparent')
    new_price_entry = ctk.CTkEntry(master=inner_frame2,
                         font=('Arial', 10),
                            fg_color='#0E4D92',
                            border_color="#58c1f6",
                            corner_radius=10,
                            placeholder_text='PHP',
                            width=50)
    new_price_entry.pack(side='left')
    update_price = ctk.CTkButton(master=inner_frame2,
                                 text='Update Price',
                                 font=('Arial', 12),
                                 width=100,
                                 command=lambda vals=(new_price_entry, i): update_bus_price(vals),
                                 fg_color=neon_blue,
                                 text_color='#181460')
    update_price.pack(side='left', padx=5)
    inner_frame2.pack(side='right')
    
    
    frame.pack(pady=10, anchor='nw')
    frame.pack_propagate(False)

window = ctk.CTk()
SCREEN_WIDTH = window.winfo_screenwidth()
SCREEN_HEIGHT = window.winfo_screenheight()
window.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
window.after(0, lambda:window.state('zoomed'))
window.title('Bus Reservation Convenience Kiosk Admin Panel')
window.configure(fg_color='#181460')
neon_blue = '#58c1f6'

top_frame = ctk.CTkFrame(master=window,
                         width=SCREEN_WIDTH,
                         height=60,
                         fg_color='#242172')
top_frame.pack(anchor='nw',padx=4,pady=3)
top_frame.pack_propagate(False)

booking_img = ctk.CTkImage(light_image=Image.open("icons/booking.png"), size=(40, 40))
img_label = ctk.CTkLabel(master=top_frame,
                           text='',
                           image=booking_img)
img_label.pack(side='left', pady=5, padx=8)
title_label = ctk.CTkLabel(master=top_frame,
                           text='Bus Reservation Information Panel',
                           font=('Arial bold', 20))
title_label.pack(side='left', pady=5, padx=3)

spacer_label = ctk.CTkLabel(master=top_frame,
                           text='',
                           font=('Arial bold', 20),
                           width=100)
spacer_label.pack(side='left', pady=5, padx=10)

total_buses_label = ctk.CTkLabel(master=top_frame,
                           text='Total Buses: ',
                           font=('Arial bold', 15))
total_buses_label.pack(side='left', pady=5, padx=10)
buses_count = str(len(retrieve.get_buses()))
buses_var = ctk.StringVar(value=buses_count)
total_bus_count_label = ctk.CTkLabel(master=top_frame,
                           textvariable=buses_var,
                           font=('Arial bold', 17),
                           fg_color='#0E4D92',
                           width=40,
                           text_color='white',
                           corner_radius=20)
total_bus_count_label.pack(side='left', padx=20)

total_tickets_label = ctk.CTkLabel(master=top_frame,
                           text='Total Ticket Reservations: ',
                           font=('Arial bold', 15))
total_tickets_label.pack(side='left', pady=5, padx=10)

ticks = str(retrieve.get_all_tickets())
tickets_var = ctk.StringVar(value=ticks)
total_tickets_count_label = ctk.CTkLabel(master=top_frame,
                           textvariable=tickets_var,
                           font=('Arial bold', 17),
                           fg_color='#0E4D92',
                           width=40,
                           text_color='white',
                           corner_radius=20)
total_tickets_count_label.pack(side='left', padx=20)

logout_img = ctk.CTkImage(light_image=Image.open("icons/logout.png"), size=(30, 30))
logout_button = ctk.CTkButton(master=top_frame,
                             text='Logout',
                             font=('Arial bold', 17),
                            fg_color=neon_blue,
                            width=150,
                            height=35,
                            corner_radius=18,
                            command=logout,
                            text_color='#181460',
                            image=logout_img)
logout_button.pack(side='right',padx=20)

left_Frame = ctk.CTkFrame(master=window,
                          fg_color='#242172',
                          width=300,
                          height=(SCREEN_HEIGHT-132))

add_label = ctk.CTkLabel(master=left_Frame,
                         text='Bus Add Panel',
                         font=('Arial', 20))
add_label.pack(pady=2)
bus_label = ctk.CTkLabel(master=left_Frame,
                         text='Bus Name',
                         font=('Arial', 15))
bus_label.pack()

bus_entry = ctk.CTkEntry(master=left_Frame,
                         font=('Arial', 10),
                            fg_color='#0E4D92',
                            border_color="#58c1f6",
                            corner_radius=10,
                            placeholder_text='Enter bus name')
bus_entry.pack()
bus_number_label = ctk.CTkLabel(master=left_Frame,
                         text='Bus Number',
                         font=('Arial', 15))
bus_number_label.pack()

bus_num_entry = ctk.CTkEntry(master=left_Frame,
                             font=('Arial', 10),
                            fg_color='#0E4D92',
                            border_color="#58c1f6",
                            corner_radius=10,
                            placeholder_text='Enter bus number')
bus_num_entry.pack()
bus_company_label = ctk.CTkLabel(master=left_Frame,
                         text='Bus Company',
                         font=('Arial', 15))
bus_company_label.pack()

bus_company_entry = ctk.CTkEntry(master=left_Frame,
                             font=('Arial', 10),
                            fg_color='#0E4D92',
                            border_color="#58c1f6",
                            corner_radius=10,
                            placeholder_text='Enter bus number')
bus_company_entry.pack()

fare_label = ctk.CTkLabel(master=left_Frame,
                         text='Bus Fare Price',
                         font=('Arial', 15))
fare_label.pack()

fare_entry = ctk.CTkEntry(master=left_Frame,
                             font=('Arial', 10),
                            fg_color='#0E4D92',
                            border_color="#58c1f6",
                            corner_radius=10,
                            placeholder_text='Enter fare Price')
fare_entry.pack()

source_label = ctk.CTkLabel(master=left_Frame,
                          text='Choose Source terminal: ',
                          font=('Arial', 15))
source_label.pack()
sources = retrieve.get_sources()
source_box = ctk.CTkComboBox(master=left_Frame,
                          values= sources,
                          fg_color='#242172',
                        border_color=neon_blue,
                        button_color=neon_blue,
                        width=200,
                                dropdown_fg_color='#242172',
                                dropdown_text_color='white')
source_box.pack(pady=5)
destination_label = ctk.CTkLabel(master=left_Frame,
                          text='Enter Destination terminal: ',
                          font=('Arial', 15))
destination_label.pack()
destinations = retrieve.get_destinations()
destination_box = ctk.CTkEntry(master=left_Frame,
                             font=('Arial', 10),
                            fg_color='#0E4D92',
                            border_color="#58c1f6",
                            corner_radius=10,
                            placeholder_text='Enter destination terminal',
                            width=200)
destination_box.pack(pady=5)

departure_label = ctk.CTkLabel(master=left_Frame,
                               text='Time of Departure',
                               font=('Arial', 15))
departure_label.pack()
departure_frame = ctk.CTkFrame(master=left_Frame,
                               fg_color='transparent')
departure_box = ctk.CTkComboBox(master=departure_frame,
                                values=['1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00','12:00' ],
                                fg_color='#242172',
                                border_color=neon_blue,
                                button_color=neon_blue,
                                dropdown_fg_color='#242172',
                                dropdown_text_color='white')
departure_box.pack(side='left', anchor='nw',padx=10)
clock_box = ctk.CTkComboBox(master=departure_frame,
                            values=['AM', 'PM'],
                            width=70,
                            fg_color='#242172',
                            border_color=neon_blue,
                            button_color=neon_blue,
                                dropdown_fg_color='#242172',
                                dropdown_text_color='white')
clock_box.pack(anchor='nw')

departure_frame.pack(pady=5)
seats_label = ctk.CTkLabel(master=left_Frame,
                         text='No. of seats',
                         font=('Arial', 15))
seats_label.pack()

seats_entry = ctk.CTkEntry(master=left_Frame,
                             font=('Arial', 10),
                            fg_color='#0E4D92',
                            border_color="#58c1f6",
                            corner_radius=10,
                            placeholder_text='Enter no. of seats')
seats_entry.pack()
air_label = ctk.CTkLabel(master=left_Frame,
                         text='Air-conditioned',
                         font=('Arial', 15))
air_label.pack()
air_box = ctk.CTkComboBox(master=left_Frame,
                            values=['YES', 'NO'],
                            width=70,
                            fg_color='#242172',
                            border_color=neon_blue,
                            button_color=neon_blue,
                                dropdown_fg_color='#242172',
                                dropdown_text_color='white')
air_box.pack(pady=5)
register_img = ctk.CTkImage(light_image=Image.open("icons/add.png"), size=(30, 30))
register_bus = ctk.CTkButton(master=left_Frame,
                             text='Register new Bus',
                             font=('Arial bold', 17),
                            fg_color='#008ECC',
                            width=200,
                            height=35,
                            corner_radius=18,
                            command=register_this,
                            image=register_img)
register_bus.pack(pady=15)

left_Frame.pack(side='left',anchor='nw',padx=4)
left_Frame.pack_propagate(False)

right_frame = ctk.CTkFrame(master=window,
                           fg_color='#242172')
frame3 = ctk.CTkFrame(master=right_frame, fg_color='transparent')
frame3.pack(anchor='nw')
sched_label = ctk.CTkLabel(master=frame3,
                           text='Bus Reservations',
                           font=('Arial', 20))
sched_label.pack(anchor='nw', padx= 20, pady= 5, side='left')

refresh_img = ctk.CTkImage(light_image=Image.open("icons/refresh.png"), size=(20, 20))
refresh_button = ctk.CTkButton(master=frame3,
                             text='Refresh',
                             font=('Arial bold', 15),
                            fg_color=neon_blue,
                            width=160,
                            height=30,
                            corner_radius=18,
                            command=update,
                            text_color='#181460',
                            image=refresh_img)
refresh_button.pack(side='left',padx=20, pady=5)

bookings_frame = ctk.CTkFrame(master=right_frame,
                           fg_color='#181460',
                           height=600,
                           width=505)
head_frame = ctk.CTkFrame(master=bookings_frame,
                          fg_color='transparent')
head_frame.pack()
date_box = ctk.CTkComboBox(master=head_frame,
                           values=dates,
                           fg_color='#242172',
                        border_color='#242172',
                        button_color=neon_blue,
                        width=200,
                        command=display_bookings,
                                dropdown_fg_color='#242172',
                                dropdown_text_color='white')
date_box.pack(side='left',
              pady=10)

date = date_box.get()
date = date.split(' - ')[0].replace('/', '_')
count = ctk.StringVar(value = retrieve.get_ticket_count(date))
bok_label = ctk.CTkLabel(master=head_frame,
                           text= 'Total Reservations - ',
                           font=('Arial bold', 12))
bok_label.pack(side='left', padx=10)
count_label = ctk.CTkLabel(master=head_frame,
                           textvariable=count,
                           font=('Arial bold', 17),
                           fg_color='#0E4D92',
                           width=40,
                           text_color='white',
                           corner_radius=20)
count_label.pack(side='left', padx=20)

bookings_frame.pack(pady=5,padx=10,side='left')
bookings_frame.pack_propagate(False)

buses_frame = ctk.CTkFrame(master=right_frame,
                           fg_color='#181460',
                           height=600,
                           width=505)
buses_frame.pack(pady=5,padx=10,side='left')
buses_frame.pack_propagate(False)

booking_scroll = ctk.CTkScrollableFrame(master=bookings_frame,
                                        width=800, height=600,
                                        fg_color='#181460',
                                        scrollbar_button_color='#58c1f6')
booking_scroll.pack()
date1 = date_box.get()
date1 = date1.split(' - ')[0].replace('/', '_')
buses1 = retrieve.get_buses()
bookings = []
for bus in buses1:
  booking0 = retrieve.get_booking(bus, date1)
  bookings.append(len(booking0))
for bus, book in zip(buses1, bookings):
  frame = ctk.CTkFrame(master=booking_scroll,
                        height=50,
                        fg_color='#111E6C',
                        width=500)
  bus_label = ctk.CTkLabel(master=frame,
                        text=bus,
                        font=('Arial bold', 15))
  bus_label.pack(side='left', pady=10, padx=20)
  dest = retrieve.get_destination(bus)
  bus_books = ctk.CTkLabel(master=frame,
                        text=book,
                        font=('Arial', 20),
                        fg_color='#0E4D92',
                        width=40,
                        corner_radius=20)
  bus_books.pack(side='right',anchor='e', padx=20)
  rot_label = ctk.CTkLabel(master=frame,
                        text='Bound ' + dest,
                        font=('Arial bold', 10))
  rot_label.pack(side='right', pady=10, padx=20)
  
  bus_books.pack_propagate(False)
  frame.pack(pady=10, anchor='nw')
  frame.pack_propagate(False)

buses_scroll = ctk.CTkScrollableFrame(master=buses_frame,
                                        width=900, height=600,
                                        fg_color='#181460',
                                        scrollbar_button_color='#58c1f6')
label1 = ctk.CTkLabel(master=buses_frame,
                        text='Bus Configuration Panel',
                        font=('Arial bold', 15))
label1.pack(pady=10, padx=20)
display_buses()
buses_scroll.pack()


right_frame.pack(side='left',anchor='nw')
right_frame.pack_propagate(False)

window.mainloop()
