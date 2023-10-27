import customtkinter as ctk
import retrieve
import os
from PIL import Image
import subprocess
import time

def main():
    def cancel_ticket():
        ticket_num = ticket_entry.get()
        retrieve.cancel_bus_ticket(ticket_num)
        thank()
    
    def proceed():
        subprocess.Popen(['python', 'main.py'])
        time.sleep(3)
        window.destroy()
    
    def thank():
        cancel_label.destroy()
        frame1.destroy()
        label = ctk.CTkLabel(master=window,
                            text='Your ticket has now been cancelled!!\nPlease proceed...',
                            font=('Arial bold', 25),
                            text_color='white')
        label.pack(pady=50)
        cancel_button = ctk.CTkButton(master=window,
                                  text='Proceed',
                                  font=('Arial bold', 15),
                                  width=200,
                                  height=40,
                                  corner_radius=200,
                                  fg_color='#0E4D92',
                                  command=proceed)
        cancel_button.pack()
        
        
        
    window = ctk.CTk()
    SCREEN_WIDTH = window.winfo_screenwidth()
    WIDTH = 700
    HEIGHT = 650
    window.geometry(f'{WIDTH}x{HEIGHT}+{int(SCREEN_WIDTH/2)-int(WIDTH/2)}+10')
    window.configure(fg_color='#181460')
    window.title('Bus Reservation Convenience Kiosk Ticket Cancellation')
    # enter ticket number
    neon_blue = '#58c1f6'
    frame3 = ctk.CTkFrame(master=window,
                          fg_color='transparent',
                          width=400,
                          height=500,)
    cancel_img = ctk.CTkImage(light_image=Image.open("icons/cancel.png"), size=(50, 50))
    cancel_label = ctk.CTkLabel(master=frame3,
                                text='',
                                image=cancel_img)
    cancel_label.pack(side='left')
    cancel_label = ctk.CTkLabel(master=frame3,
                                text='Cancel Ticket',
                                font=('Arial', 20))
    cancel_label.pack(side='left')
    frame3.pack(pady=20)
    frame1 = ctk.CTkFrame(master=window,
                          fg_color='#242172',
                          width=400,
                          height=500)
    spacer0 = ctk.CTkFrame(master=frame1,
                          fg_color='transparent',
                          height=50)
    spacer0.pack()
    
    
    ticket_img = ctk.CTkImage(light_image=Image.open("icons/ticket.png"), size=(30, 30))
    fram = ctk.CTkFrame(master=frame1,
                          fg_color='transparent')
    ticket_label = ctk.CTkLabel(master=fram, text='', fg_color='transparent', image=ticket_img)
    ticket_label.pack(pady=10, side='left')
    ticket_label = ctk.CTkLabel(master=fram, text='Ticket Number: ', fg_color='transparent', font=('Arial bold', 20))
    ticket_label.pack(pady=10, side='left')
    fram.pack()
    ticket1_label = ctk.CTkLabel(master=frame1, text='Example - 987654', fg_color='transparent', font=('Arial italic', 14))
    ticket1_label.pack(padx=15, pady=10)
    ticket_entry = ctk.CTkEntry(master=frame1, 
                            font=('Arial', 18),
                            fg_color='#0E4D92',
                            border_color=neon_blue,
                            height=55,
                            width=350,
                            corner_radius=10,
                            placeholder_text='# Enter 6-digit number')
    ticket_entry.pack()
    spacer = ctk.CTkFrame(master=frame1,
                          fg_color='transparent',
                          height=10)
    spacer.pack()
    frame2 = ctk.CTkFrame(master=frame1,fg_color='white', height=100,
                          width=350)
    ticket2_label = ctk.CTkLabel(master=frame2, text='Please note that this is non-refundable!!\nConsider before cancelling your ticket...', 
                                 fg_color='transparent', font=('Arial italic', 16),
                                 text_color='black')
    ticket2_label.pack(padx=15,anchor='center', pady=15)
    frame2.pack(pady=20)
    frame2.pack_propagate(False)
    confirm_img = ctk.CTkImage(light_image=Image.open("icons/confirm.png"), size=(30, 30))
    cancel_button = ctk.CTkButton(master=frame1,
                                  text='Confirm',
                                  font=('Arial bold', 15),
                                  width=200,
                                  height=40,
                                  corner_radius=200,
                                  fg_color='#008ECC',
                                  command=cancel_ticket,
                                  text_color='white',
                                  image=confirm_img)
    cancel_button.pack()
    cancel_button.pack_propagate(False)
    
    frame1.pack()
    frame1.pack_propagate(False)
    window.mainloop()

if __name__ == '__main__':
    main()