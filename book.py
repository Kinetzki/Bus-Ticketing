import datetime
import retrieve
from PIL import Image
import subprocess
import time

def main():
    import customtkinter as ctk
    date_1 = datetime.datetime.strptime(datetime.datetime.now().strftime('%m/%d/%y'), "%m/%d/%y")
    dates = [(date_1 + datetime.timedelta(days=x)).strftime('%m/%d/%y - %A') for x in range(1, 11)]

    def get_bus():
        s = source_box.get()
        d = dest_box.get()
        date = dates_box.get()
        date = date.split(' - ')[0].replace('/', '_')
        n = name_entry.get()
        #os.system(f'python bus.py "{s}" "{d}" "{date}" "{n}"')
        subprocess.Popen(['python', 'bus.py', s, d, date, n])
        time.sleep(1.8)
        window.destroy()

    window = ctk.CTk()
    SCREEN_WIDTH = window.winfo_screenwidth()
    SCREEN_HEIGHT = window.winfo_screenheight()
    WIDTH = 700
    HEIGHT = 650
    bgcolor = '#181460'
    window.geometry(f'{WIDTH}x{SCREEN_HEIGHT}+{int(SCREEN_WIDTH/2)-int(WIDTH/2)}+{0}')
    window.title('Bus Reservation Convenience Kiosk')
    window.configure(fg_color=bgcolor)
    terminals = retrieve.get_destinations()
    source = ['Batangas City Pier', 'Batangas Grand Terminal', 'SM Lipa Grand Terminal']
    header_frame = ctk.CTkFrame(master=window,
                          fg_color='#242172',
                          width=600,
                          height=50)
    header_frame.pack(pady=10)
    header_frame.pack_propagate(False)
    write_label = ctk.CTkLabel(master=header_frame, text='', fg_color='transparent', width=140)
    write_label.pack(side='left', anchor='center')
    write_img = ctk.CTkImage(light_image=Image.open("icons/writing.png"), size=(30, 30))
    write_label = ctk.CTkLabel(master=header_frame, text='', fg_color='transparent', image=write_img)
    write_label.pack(side='left', anchor='center', padx=10)
    label1 = ctk.CTkLabel(master=header_frame, text='Please fill out the entries below', font=('Arial bold', 20))
    label1.pack(anchor='center', pady=15,side='left')

    neon_blue = '#58c1f6'

    # Source destinations
    station_holder = ctk.CTkFrame(master=window, fg_color='transparent')
    source_label = ctk.CTkLabel(master=station_holder, text=f"Source Station:{' '*36} Destination:{' '*42} Date (m/d/y):", font=('Arial', 15))
    source_label.pack(anchor='nw', padx=10)

    source_box = ctk.CTkComboBox(master = station_holder,
                                values=source,
                                fg_color='#242172',
                                border_color= '#242172',
                                button_color= neon_blue,
                                width=200,
                                height=35,
                                dropdown_fg_color='#242172',
                                dropdown_text_color='white')
    source_box.pack(side='left', padx=10)
    dest_box = ctk.CTkComboBox(master = station_holder,
                                values=terminals,
                                fg_color='#242172',
                                border_color='#242172',
                                button_color=neon_blue,
                                width=200,
                                height=35,
                                dropdown_fg_color='#242172',
                                dropdown_text_color='white')
    dest_box.pack(side='left', padx=10)
    dates_box = ctk.CTkComboBox(master = station_holder,
                                values=dates,
                                fg_color='#242172',
                                border_color='#242172',
                                button_color=neon_blue,
                                width=180,
                                height=35,
                                dropdown_fg_color='#242172',
                                dropdown_text_color='white')
    dates_box.pack(padx=10)
    station_holder.pack(anchor='center', pady=15, padx=10)

    info_frame = ctk.CTkFrame(master=window,
                           fg_color="#242172",
                           width=450,
                           height=500)
    # Info Holder
    info_holder = ctk.CTkFrame(master=info_frame,
                            fg_color='transparent')

    # Name
    name_label = ctk.CTkLabel(master=info_holder, text='Name: ', fg_color='transparent', font=('Arial bold', 15))
    name_label.pack(anchor='nw', padx=15)
    name_entry = ctk.CTkEntry(master=info_holder, 
                            font=('Arial', 18),
                            fg_color='#0E4D92',
                            border_color=neon_blue,
                            height=35,
                            width=350,
                            corner_radius=10)
    name_entry.pack()
    name_caption = ctk.CTkLabel(master=info_holder, 
                                text='(Example: Juan A. Cruz)', 
                                fg_color='transparent', 
                                font=('Arial italic', 11))
    name_caption.pack(anchor='nw', padx=5)
    #Address
    address_label = ctk.CTkLabel(master=info_holder, text='Address: ', fg_color='transparent', font=('Arial bold', 15))
    address_label.pack(anchor='nw', padx=15)
    address_entry = ctk.CTkEntry(master=info_holder, 
                            font=('Arial', 18),
                            fg_color='#0E4D92',
                            border_color=neon_blue,
                            height=35,
                            width=350,
                            corner_radius=10)
    address_entry.pack()
    address_caption = ctk.CTkLabel(master=info_holder, 
                                text='(Street/Subdivision/City/Province)', 
                                fg_color='transparent', 
                                font=('Arial italic', 11))
    address_caption.pack(anchor='nw', padx=5)

    # Contact No
    contact_label = ctk.CTkLabel(master=info_holder, text='Contact No.: ', fg_color='transparent', font=('Arial bold', 15))
    contact_label.pack(anchor='nw', padx=15)
    contact_entry = ctk.CTkEntry(master=info_holder, 
                            font=('Arial', 18),
                            fg_color='#0E4D92',
                            border_color=neon_blue,
                            height=35,
                            width=350,
                            corner_radius=10)
    contact_entry.pack()
    contact_caption = ctk.CTkLabel(master=info_holder, 
                                text='(Example: 09565176896)', 
                                fg_color='transparent', 
                                font=('Arial italic', 11))
    contact_caption.pack(anchor='nw', padx=5)

    # Email
    email_label = ctk.CTkLabel(master=info_holder, text='E-mail (Optional): ', fg_color='transparent', font=('Arial bold', 15))
    email_label.pack(anchor='nw', padx=15)
    email_entry = ctk.CTkEntry(master=info_holder, 
                            font=('Arial', 18),
                            fg_color='#0E4D92',
                            border_color=neon_blue,
                            height=35,
                            width=350,
                            corner_radius=10)
    email_entry.pack()
    email_caption = ctk.CTkLabel(master=info_holder,
                                text='(Example: juancruz@gmail.com)',
                                fg_color='transparent',
                                font=('Arial italic', 11))
    email_caption.pack(anchor='nw', padx=5)

    info_holder.pack(padx=10, pady=15)
    next_img = ctk.CTkImage(light_image=Image.open("icons/next.png"), size=(25, 25))
    next_btn = ctk.CTkButton(master = info_frame,
                             text='Next',
                             font=('Arial bold', 20),
                             width=250,
                             fg_color='#008ECC',
                             height=40,
                             corner_radius=20,
                             command=get_bus,
                             image=next_img)
    next_btn.pack(pady=10)
    info_frame.pack(pady=20)
    info_frame.pack_propagate(False)
    window.mainloop()


if __name__ == '__main__':
    main()

