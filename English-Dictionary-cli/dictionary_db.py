import mysql.connector

conn = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cur = conn.cursor()
word = input("Enter a word to search: ")
query = cur.execute(f"SELECT * from Dictionary WHERE Expression = '{word}'")
results = cur.fetchall()

if results:
    for line in results:
        print(line[1])
else:
    print("No result found")

#Get all rows where the value of the column Expression starts with r
# cur.execute("SELECT * from Dictionary WHERE EXPRESSION LIKE 'r%'")
# Get all rows where the value of the column Expression starts with rain
# "SELECT * FROM Dictionary WHERE Expression  LIKE 'rain%'"
# All rows where the length of the value of the column Expression is less than four characters:
# "SELECT * FROM Dictionary WHERE length(Expression) < 4"
# All rows where the length of the value of the column Expression is four characters:
# "SELECT * FROM Dictionary WHERE length(Expression) = 4"
# All rows where the length of the value of the column Expression is greater than 1 but less than 4 characters:
# "SELECT * FROM Dictionary WHERE length(Expression) > 1 AND length(Expression) < 4"
