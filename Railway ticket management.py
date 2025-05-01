import mysql.connector

def connect_to_database():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_pass",
            database="trainmg"
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        exit(1)

def create_tables(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trains (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            seats INT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passengers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            train_id INT,
            FOREIGN KEY (train_id) REFERENCES trains(id)
        )
    """)

def insert_sample_trains(cursor):
    cursor.execute("SELECT COUNT(*) FROM trains")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO trains (name, seats) VALUES (%s, %s)", ("Rajdhani Express", 30))
        cursor.execute("INSERT INTO trains (name, seats) VALUES (%s, %s)", ("Shatabdi Express", 20))
        #you can add more trains here

def book_ticket(cursor, train_name, passenger_name):
    cursor.execute("SELECT id, seats FROM trains WHERE name = %s", (train_name,))
    result = cursor.fetchone()

    if result:
        train_id, available_seats = result
        if available_seats > 0:
            cursor.execute("INSERT INTO passengers (name, train_id) VALUES (%s, %s)", (passenger_name, train_id))
            cursor.execute("UPDATE trains SET seats = %s WHERE id = %s", (available_seats - 1, train_id))
            print("Ticket booked successfully!")
        else:
            print("Sorry, no available seats for the selected train.")
    else:
        print("Train not found.")

def display_trains(cursor):
    cursor.execute("SELECT * FROM trains")
    result = cursor.fetchall()

    if result:
        print("\n Available trains:")
        for train in result:
            print(f"ID: {train[0]} | Name: {train[1]} | Available Seats: {train[2]}")
    else:
        print("No trains available.")

def main():
    db_connection = connect_to_database()
    cursor = db_connection.cursor()

    create_tables(cursor)
    insert_sample_trains(cursor)

    display_trains(cursor)

    train_name = input("\nEnter train name to book: ")
    passenger_name = input("Enter passenger name: ")

    book_ticket(cursor, train_name, passenger_name)

    display_trains(cursor)
    db_connection.commit()
    cursor.close()
    db_connection.close()

if __name__ == "__main__":
    main()
