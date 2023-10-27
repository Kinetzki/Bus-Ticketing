import qrcode
import random
import customtkinter as ctk
import argparse
from PIL import Image
import retrieve
import subprocess 
import time

parser = argparse.ArgumentParser()
parser.add_argument("bus", type=str)
parser.add_argument("num", type=str)
parser.add_argument("date", type=str)
parser.add_argument("user", type=str)
parser.add_argument("seat", type=str)
args = parser.parse_args()

source = retrieve.get_source(args.bus)
destination = retrieve.get_destination(args.bus)
unique = ''.join(random.choices([str(x) for x in range(10)], k=6))


def go_main():
    retrieve.book_ticket(args.date, args.bus, unique, 'n/a', args.seat)
    retrieve.record_ticket(args.num, args.bus, unique, args.date, price, args.user, 'n/a')
    #os.system('python main.py')
    subprocess.Popen(['python', 'main.py'])
    time.sleep(2.5)
    window.destroy()

def gen_qr():
    # Data to encode
    data = {'Ticket number':unique,
            'Bus number': args.num,
            'Bus Name': args.bus,
            'Date': args.date,
            'User': args.user,
            'Seat Number': args.seat,
            'From': source,
            'To': destination}
    
    # Creating an instance of QRCode class
    qr = qrcode.QRCode(version = 1,
                    box_size = 20,
                    border = 2)
    
    # Adding data to the instance 'qr'
    qr.add_data(data)
    
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'black',
                        back_color = 'white')
    file = 'ticket_qr.png'
    
    img.save(file)
    return file

window = ctk.CTk()
SCREEN_WIDTH = window.winfo_screenwidth()
WIDTH = 650
HEIGHT = 700
bgcolor = '#181460'
window.geometry(f'{WIDTH}x{HEIGHT}+{int(SCREEN_WIDTH/2)-int(WIDTH/2)}+{0}')
window.title('Bus Reservation Convenience Kiosk Ticket Generation')
window.configure(fg_color=bgcolor)

frame1 = ctk.CTkFrame(master=window,
                      width=400, height=600,
                      fg_color='white')

thank_you_label = ctk.CTkLabel(master=frame1,
                               text='Thank you for booking!!',
                               font=('Arial bold', 26),
                               text_color='black')
thank_you_label.pack(pady=5)
capture_label = ctk.CTkLabel(master=frame1,
                               text='Please take a photo of your qr code',
                               font=('Arial bold', 13),
                               text_color='black')
capture_label.pack()

qr = gen_qr()
qr_image = ctk.CTkImage(light_image=Image.open(qr),
                        size=(300, 300))
qr_label = ctk.CTkLabel(master=frame1,
                        image=qr_image,
                        text='')
qr_label.pack()

info_holder = ctk.CTkFrame(master=frame1,
                           fg_color='white'
                           )

bus_name = ctk.CTkLabel(master=info_holder,
                        text=args.bus,
                        font=('Arial bold', 15),
                        text_color='black')
bus_name.pack()
bus_number = ctk.CTkLabel(master=info_holder,
                        text='Bus number: ' + args.num,
                        font=('Arial bold', 15),
                        text_color='black')
bus_number.pack()

route_label = ctk.CTkLabel(master=info_holder,
                        text='Route: ' + source + ' to \n' + destination,
                        font=('Arial bold', 15),
                        text_color='black')
route_label.pack()
date_ = ctk.CTkLabel(master=info_holder,
                        text='Date: ' + args.date,
                        font=('Arial bold', 15),
                        text_color='black')
date_.pack()
user_name = ctk.CTkLabel(master=info_holder,
                        text='Name: ' + args.user,
                        font=('Arial bold', 15),
                        text_color='black')
user_name.pack()
seat_num = ctk.CTkLabel(master=info_holder,
                        text='Seat No. ' + args.seat,
                        font=('Arial bold', 15),
                        text_color='black')
seat_num.pack()

price = retrieve.get_price(args.bus)
fare_price = ctk.CTkLabel(master=info_holder,
                        text='Fare: PHP ' + price,
                        font=('Arial bold', 25),
                        text_color='black')
fare_price.pack()
ticket_num = ctk.CTkLabel(master=info_holder,
                        text='Ticket No. #' + unique,
                        font=('Arial bold', 18),
                        text_color='black')
ticket_num.pack()
info_holder.pack()
frame1.pack(pady=10)
frame1.pack_propagate(False)

proceed_img = ctk.CTkImage(light_image=Image.open("icons/proceed.png"), size=(30, 30))
proceed_button = ctk.CTkButton(master=window,
                               text='Proceed',
                               font=('Arial', 20),
                               fg_color='#008ECC',
                            width=200,
                            height=43,
                            corner_radius=18,
                            command=go_main,
                            image=proceed_img)
proceed_button.pack(pady=10)

window.mainloop()