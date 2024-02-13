import sqlite3
import bcrypt

conn = sqlite3.connect("users.db")
c = conn.cursor()

# Get username and validate
while True:
    username = input("Please enter your username: ")
    qry = f"SELECT * FROM USERS WHERE USERID='{username}'"
    c.execute(qry)
    result = c.fetchone()

    if result:
        userid, hashed = result
        break
    else:
        print("Invalid username")

print(f"Hello there {userid}")

while True:
    entered_password = input("Please enter your password: ")

    if bcrypt.checkpw(entered_password.encode(), hashed.encode()):
        print("Welcome!")
        break
    else:
        print("The entered password is incorrect!")

