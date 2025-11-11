import csv
from databaseconn import get_connection
from bill import amount

conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM food")
menu = cursor.fetchall()

print("------ MENU ------")
for row in menu:
    print(row)

print("\nEnter the items you want to order:")

order = [] 

while True:
    dish = input("Item name: ")
    quan = int(input("Enter quantity:"))

    cursor.execute("SELECT items,price FROM food WHERE items = %s", (dish,))
    result = cursor.fetchone()

    if result:
        items,price=result
        order.append((items,price,quan))
        print(f"{dish} added to order")
    else:
        print("Enter a valid item")

    choice = input("Do you want to order more (yes/no): ").lower()

    if choice == "no":
        break
    elif choice == "yes":
        continue
    else:
        print("Invalid choice, exiting order")
        break

print("\n------ YOUR ORDER ------")
for item,price,quan in order:
    print(item," ",quan)


print("\n------ YOUR bill ------")

grand_total=amount(order)
print("Grand Total : ₹",grand_total)

cursor.execute(
    "INSERT INTO bills (total) VALUES (%s)", (grand_total,)
)
conn.commit()
f=open("bill.csv","w",newline="")
writer=csv.writer(f)
writer.writerow (["item","price","quantity"])
for items,price,quan in order:
    writer.writerow([items,price,quan])
writer.writerow([])
writer.writerow(["Grand Total", "", grand_total])


cursor.close()
conn.close()