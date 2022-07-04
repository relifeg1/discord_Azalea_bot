import sqlite3


connection = sqlite3.connect("Team.db")
#cursor = connection.cursor()


mycursor = connection.cursor()

#mycursor.execute("SELECT * FROM team WHERE name = '%s'")


sql = "SELECT * FROM team WHERE name = ? "

data = input('Choose one of Them : '),


mycursor.execute(sql , data)
result = mycursor.fetchone()


# for x in result:
#     print(x)

print(result)






#cursor.execute("CREATE TABLE employee(name TEXT,link TEXT,description TEXT)")
# cursor.execute("SELECT * FROM team")

# selectone = input("Chose Team :")

# _Show = cursor.fetchall()

# for row in _Show:
#     print("id:",row[0],"--", "name:",row[1])
#connection.close
