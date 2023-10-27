import customtkinter as tk
import retrieve
import subprocess
from PIL import Image
import time

# bg blue = #181460
neon_blue = '#58c1f6'
# light blue = #242172

def main():
    def book_a_ticket():
        subprocess.Popen(['python', 'book.py'])
        time.sleep(2.4)
        window.destroy()

    def cancel_a_ticket():
        subprocess.Popen(['python', 'cancel.py'])
        time.sleep(3)
        window.destroy()

    retrieve.update_tables()
    window = tk.CTk()
    SCREEN_WIDTH = window.winfo_screenwidth()
    WIDTH = 650
    HEIGHT = 690
    window.geometry(f'{WIDTH}x{HEIGHT}+{int(SCREEN_WIDTH/2)-int(WIDTH/2)}+2')
    window.title('Bus Reservation Convenience Kiosk')
    window.configure(fg_color='#181460')

    outer_frame = tk.CTkFrame(master=window,
                           fg_color="#242172",
                           width=450,
                           height=600)
    
    title_label = tk.CTkLabel(master = outer_frame, 
                            text='Bus Reservation Convenience Kiosk', 
                            font=('Arial bold', 22), 
                            text_color='#58c1f6',
                            fg_color='#242172')
    title_label.pack(pady=20)

    bus = tk.CTkImage(light_image=Image.open("icons/bus.png"), size=(250, 250))

    spacer = tk.CTkLabel(master=outer_frame, text='',image=bus, fg_color='transparent')
    spacer.pack(pady=30)
    book_img = tk.CTkImage(light_image=Image.open("icons/reservation.png"), size=(30, 30))
    book_ticket = tk.CTkButton(outer_frame, 
                            text='Book a ticket   ', 
                            font=('STHupo bold', 20), 
                            fg_color='#58c1f6', 
                            command=book_a_ticket, 
                            height=50, width=300, 
                            text_color='#181460', 
                            corner_radius=25,
                            image=book_img)
    book_ticket.pack(pady=10)
    cancel_ticket = tk.CTkButton(master = outer_frame, 
                                text='CANCEL A TICKET',
                                fg_color='#181460',
                                command=cancel_a_ticket,
                                height=40, width=220,
                                text_color='white',
                                corner_radius=20)
    cancel_ticket.pack()
    outer_frame.pack(pady=45)
    outer_frame.pack_propagate(False)
    window.mainloop()

if __name__ == '__main__':
    main()

# Create date tables- include seat numbers as columns, bus_number, bus seats vacant
# Create update date tables, remove date tables that are already done
# Check bus availability on certain date - Just minus 1 to each bus_seats available until 0, and also seat numbers
# Finish admin panel
# Generate qr
# Create ticket table (Name, date, time, ticket number, Bus name, Bus number, fair price)