import psycopg2
import csv

yourpassword = 'kazbek'  # Ensure to secure your password appropriately

def insert_from_csv(file_path):
    conn = psycopg2.connect(f"dbname=dev user=postgres password={yourpassword}")
    cur = conn.cursor()
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)",
                row
            )
    conn.commit()
    cur.close()
    conn.close()

def insert_via_console():
    conn = psycopg2.connect(f"dbname=dev user=postgres password={yourpassword}")
    cur = conn.cursor()
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    cur.execute(
        "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)",
        (first_name, last_name, phone)
    )
    conn.commit()
    cur.close()
    conn.close()

def update_phonebook(first_name, new_phone):
    conn = psycopg2.connect(f"dbname=dev user=postgres password={yourpassword}")
    cur = conn.cursor()
    cur.execute(
        "UPDATE phonebook SET phone = %s WHERE first_name = %s",
        (new_phone, first_name)
    )
    conn.commit()
    cur.close()
    conn.close()

def query_phonebook(first_name):
    conn = psycopg2.connect(f"dbname=dev user=postgres password={yourpassword}")
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (first_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def delete_from_phonebook(by, value):
    conn = psycopg2.connect(f"dbname=dev user=postgres password={yourpassword}")
    cur = conn.cursor()
    cur.execute(f"DELETE FROM phonebook WHERE {by} = %s", (value,))
    conn.commit()
    cur.close()
    conn.close()

def main():
    while True:
        print("\nPhoneBook Application")
        print("1. Insert from CSV")
        print("2. Insert via console")
        print("3. Update phone number")
        print("4. Query by first name")
        print("5. Delete record")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            file_path = input("Enter CSV file path: ")
            insert_from_csv(file_path)
        elif choice == '2':
            insert_via_console()
        elif choice == '3':
            first_name = input("Enter the first name of the person to update: ")
            new_phone = input("Enter the new phone number: ")
            update_phonebook(first_name, new_phone)
        elif choice == '4':
            first_name = input("Enter the first name to query: ")
            query_phonebook(first_name)
        elif choice == '5':
            by = input("Delete by 'first_name' or 'phone'? ")
            value = input("Enter the value: ")
            delete_from_phonebook(by, value)
        elif choice == '6':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()