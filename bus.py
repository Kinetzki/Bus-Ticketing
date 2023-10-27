import argparse
import retrieve
from PIL import Image
import subprocess
import time

def main(available_buses):
    import customtkinter as ctk
    
    
    def get_text_value(num):
        bus_num, bus_name, date = num
        n = bus_num.split('Bus number: ')[1]
        #os.system(f'python seat.py "{bus_name}" "{n}" "{date}" "{args.name}"')
        subprocess.Popen(['python', 'seat.py', bus_name, n, date, args.name])
        time.sleep(2.4)
        window.destroy()
    
    def go_back():
        #os.system('python book.py')
        subprocess.Popen(['python', 'book.py'])
        time.sleep(2.2)
        window.destroy()

    window = ctk.CTk()
    
    SCREEN_WIDTH = window.winfo_screenwidth()
    WIDTH = 700
    HEIGHT = 650
    bgcolor = '#181460'
    window.geometry(f'{WIDTH}x{HEIGHT}+{int(SCREEN_WIDTH/2)-int(WIDTH/2)}+{10}')
    window.title('Bus Reservation Convenience Kiosk')
    window.configure(fg_color=bgcolor)
    
    window_frame = ctk.CTkFrame(master=window, width=WIDTH*.9, height=HEIGHT*.75, fg_color=bgcolor)
    title_label = ctk.CTkLabel(master=window, 
                        text='Choose bus of your choice', 
                        font=('Arial bold', 20),
                        bg_color='transparent')
    title_label.pack(padx=15, pady=15)
    
    scroll = ctk.CTkScrollableFrame(master=window_frame, width=WIDTH*.9, fg_color='#242172', height=HEIGHT*.75,
                                    scrollbar_button_color='#58c1f6')
    back_img = ctk.CTkImage(light_image=Image.open("icons/back.png"), size=(30, 30))
    back = ctk.CTkButton(master=window,
                         text='Back',
                         font=('Arial bold', 15),
                         height=40, width=200, 
                            text_color='white', 
                            corner_radius=25,
                            command=go_back,
                            image=back_img,fg_color='#008ECC')
    
    scroll.pack(pady=20)
    if len(available_buses) == 0:
        no_available = ctk.CTkLabel(master=scroll,
                                    text='NO AVAILABLE BUSES FOR THE DESTINATION FROM YOUR TERMINAL',
                                    font=('Arial bold', 17))
        no_available.pack()
    else:
        for i in available_buses:
            num = retrieve.get_bus_number(i)
            depart = retrieve.get_departure(i)
            price = retrieve.get_price(i)
            seat = retrieve.get_available_seats(i, args.date)
            air = retrieve.get_air(i)
            # Each bus frame
            bus_frame = ctk.CTkFrame(master=scroll,
                                    width=800, 
                                    height=130,
                                    fg_color='#111E6C')
            # Inner frame
            inner_frame1 = ctk.CTkFrame(master=bus_frame,
                                        fg_color='transparent')
            bus_name = ctk.CTkLabel(master=inner_frame1, 
                                font=('Arial bold', 15),
                                bg_color='transparent',
                                text=i)
            bus_name.pack(anchor='nw', padx=15, pady=5)
            departure = ctk.CTkLabel(master=inner_frame1, 
                                text='Time of departure: ' + depart, 
                                font=('Arial', 10),
                                bg_color='transparent')
            departure.pack(anchor='nw', padx=15)
            arrival = ctk.CTkLabel(master=inner_frame1,
                                text='Time of arrival: n/a',
                                font=('Arial', 10),
                                bg_color='transparent')
            arrival.pack(anchor='nw', padx=15)
            fare = ctk.CTkLabel(master=inner_frame1, 
                                text='Fare Price: ' + price, 
                                font=('Arial', 19),
                                bg_color='transparent')
            fare.pack(anchor='nw', padx=15)
            inner_frame1.pack(side='left', padx=15)
            
            inner_frame2 = ctk.CTkFrame(master=bus_frame,
                                        fg_color='transparent')
            
            bus_number = ctk.CTkLabel(master=inner_frame2, 
                                font=('Arial', 10),
                                bg_color='transparent',
                                text=f'Bus number: {num}')
            bus_number.pack(anchor='nw', padx=15)
            seats = ctk.CTkLabel(master=inner_frame2, 
                                text='No. of Available Seats: ' + seat, 
                                font=('Arial', 10),
                                bg_color='transparent')
            seats.pack(anchor='nw', padx=15)
            aircon = ctk.CTkLabel(master=inner_frame2, 
                                text='Air-Conditioned (yes/no): ' + air, 
                                font=('Arial', 10),
                                bg_color='transparent')
            aircon.pack(anchor='nw', padx=15)
            inner_frame2.pack(side='left', anchor='sw', pady=5)
            check = ctk.CTkButton(master=bus_frame, text='Book', command=lambda num=(bus_number.cget('text'), i, args.date): get_text_value(num),
                                text_color='white',
                                corner_radius=14,
                                fg_color='#58c1f6')
            check.pack(anchor='e', side='right', padx=30)
            
            bus_frame.pack(padx=15, pady=20, anchor='nw')
            bus_frame.pack_propagate(False)
    
    #Time of departure,arrival, fare, available seats, air-conditioned(y/n), company name
    window_frame.pack()
    back.pack()
    window.mainloop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=str)
    parser.add_argument("destination", type=str)
    parser.add_argument("date", type=str)
    parser.add_argument("name", type=str)
    args = parser.parse_args()
    buses = retrieve.get_available_buses(args.source, args.destination, args.date)
    main(buses)

