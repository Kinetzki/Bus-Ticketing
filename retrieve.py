import mysql.connector
import datetime
import time 

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="kinet",
    database="testdatabase"
)

mycursor = db.cursor()

def get_available_buses(source, destination, date):
    mycursor.execute(f"select Bus_name from bus where Source_terminal = '{source}' AND Destination_terminal = '{destination}'")
    buses = [str(i).replace("',)", "").replace("('", "") for i in mycursor]
    available = []
    for i in buses:
        mycursor.execute(f"select * from {date} where Bus_name= '{i}'")
        bus = [str(i).replace("',)", "").replace("('", "") for i in mycursor]
        if len(bus) >= int(get_number_of_seats(i)):
            pass 
        else:
            available.append(i)
    return available


def get_number_of_seats(number):
    mycursor.execute(f"select Available_seats from bus where Bus_name= '{number}'")
    num = [str(i) for i in mycursor]
    return num[0].replace("(", "").replace(",)", "")

def get_destinations():
    mycursor.execute("SELECT Destination_terminal from bus")
    destinations = list(set([str(i).replace("',)", "").replace("('", "") for i in mycursor]))
    return destinations

def get_sources():
    mycursor.execute("SELECT Source_terminal from bus")
    sources = list(set([str(i).replace("',)", "").replace("('", "") for i in mycursor]))
    return sources

def get_buses():
    mycursor.execute("SELECT Bus_name from bus")
    buses = list(set([str(i).replace("',)", "").replace("('", "") for i in mycursor]))
    return buses

def get_price(bus_name):
    mycursor.execute(f"select Fare_price from bus where Bus_name = '{bus_name}'")
    return [str(i) for i in mycursor][0].replace(",)", "").replace("(", "")

def get_air(bus_name):
    mycursor.execute(f"select Air_conditioned from bus where Bus_name = '{bus_name}'")
    return [str(i) for i in mycursor][0].replace("',)", "").replace("('", "")

def get_source(bus_name):
    mycursor.execute(f"select Source_terminal from bus where Bus_name = '{bus_name}'")
    return [str(i) for i in mycursor][0].replace("',)", "").replace("('", "")

def get_destination(bus_name):
    mycursor.execute(f"select Destination_terminal from bus where Bus_name = '{bus_name}'")
    return [str(i) for i in mycursor][0].replace("',)", "").replace("('", "")

def get_departure(bus_name):
    mycursor.execute(f"select Departure from bus where Bus_name = '{bus_name}'")
    return [str(i) for i in mycursor][0].replace("',)", "").replace("('", "")

def get_bus_number(bus_name):
    mycursor.execute(f"select Bus_number from bus where Bus_name = '{bus_name}'")
    return [str(i) for i in mycursor][0].replace("',)", "").replace("('", "")

def get_available_seat_numbers(bus_name, date):
    mycursor.execute(f"select Seat_number from {date} where Bus_name = '{bus_name}'")
    taken = [str(i).replace("',)", "").replace("('", "") for i in mycursor]
    available = []
    for i in range(1, int(get_number_of_seats(bus_name))+1):
        if str(i) in taken:
            pass 
        else:
            available.append(str(i))
    return available

def get_available_seats(bus_name, date):
    mycursor.execute(f"select Seat_number from {date} where Bus_name = '{bus_name}'")
    taken = [str(i).replace("',)", "").replace("('", "") for i in mycursor]
    available = []
    for i in range(1, int(get_number_of_seats(bus_name))+1):
        if str(i) in taken:
            pass 
        else:
            available.append(str(i))
    return str(len(available))

def update_tables():
    today = datetime.datetime.strptime(datetime.datetime.now().strftime('%m_%d_%y'), "%m_%d_%y")
    dates = [(today + datetime.timedelta(days=x)).strftime('%m_%d_%y') for x in range(1, 11)]
    yesterday = (today - datetime.timedelta(days=1)).strftime('%m_%d_%y')
    mycursor.execute("SHOW TABLES")
    tables = [str(x).replace("',)", "").replace("('", "") for x in mycursor]
    if yesterday in tables:
        mycursor.execute(f"DROP TABLE {yesterday}")
    for i in dates:
        if i == 'bus' or i in tables:
            pass
        else:
            mycursor.execute(f"CREATE TABLE {i} (Bus_name varchar(255), Ticket_number varchar(255), Departure varchar(255), Seat_number varchar(255))")
        time.sleep(0.1)

def get_date_tables():
    mycursor.execute(f"SHOW TABLES")
    tables = []
    for i in mycursor:
        i = str(i).replace("',)", "").replace("('", "")
        if i == 'bus' or i == 'tickets':
            pass 
        else:
            tables.append(i)
    return tables

def book_ticket(date, bus_name, ticket_num, departure, seat_num):
    formula = "INSERT INTO " + date + "(Bus_name, Ticket_number, Departure, Seat_number) \
        VALUES(%s, %s, %s, %s)"
    vals = (bus_name, ticket_num, departure, seat_num)
    mycursor.execute(formula, vals)
    
    db.commit()

def record_ticket(bus_num, bus_name, ticket_num, date, fare, name, time):
    formula = "INSERT INTO tickets(Bus_number, Bus_name, Ticket_number, Date, Fare_price, Name, Time) \
VALUES(%s, %s, %s, %s, %s, %s, %s)"
    vals = (bus_num, bus_name, ticket_num, date, fare, name, time)
    mycursor.execute(formula, vals)
    
    db.commit()
    
def add_bus(bus_name, bus_num, bus_company, destination, source, fare, seats_num, air, departure, clock):
    formula = "INSERT INTO bus(Bus_name, Bus_number, Bus_company, Destination_terminal, Source_terminal, Fare_price, Available_seats, Air_conditioned, Availability, Departure, Clock) \
VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    vals = (bus_name, bus_num, bus_company, destination, source, fare, seats_num, air, 'BOARDING', departure, clock)
    mycursor.execute(formula, vals)
    
    db.commit()

def get_booking(bus_name, date):
    mycursor.execute(f"SELECT * from {date} where Bus_name = '{bus_name}'")
    bookings = list(set([str(i).replace("',)", "").replace("('", "") for i in mycursor]))
    return bookings

def remove_bus(bus_name):
    mycursor.execute(f"DELETE FROM bus where Bus_name = '{bus_name}'")
    db.commit()
    mycursor.execute(f"DELETE FROM tickets where Bus_name = '{bus_name}'")
    db.commit()

def cancel_bus_ticket(ticket_num):
    mycursor.execute(f"SELECT Date from tickets where Ticket_number = '{ticket_num}'")
    date = [str(i).replace("',)", "").replace("('", "") for i in mycursor][0]
    mycursor.execute(f"DELETE FROM {date} where Ticket_number = '{ticket_num}'")
    db.commit()
    mycursor.execute(f"DELETE FROM tickets where Ticket_number = '{ticket_num}'")
    db.commit()

def get_ticket_count(date):
    mycursor.execute(f"SELECT * from {date}")
    count = len([i for i in mycursor])
    return count

def get_all_tickets():
    mycursor.execute(f"SELECT * from tickets")
    count = len([i for i in mycursor])
    return count

def set_new_price(bus_name, price):
    mycursor.execute(f"UPDATE bus set Fare_price = '{price}' where Bus_name = '{bus_name}'")
    db.commit()
