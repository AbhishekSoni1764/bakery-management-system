import time, sys, os
import pandas as pd
import matplotlib.pyplot as plt

msg = "WELCOME TO GUPTA Departmental Store"
for char in msg:
    sys.stdout.write(char)
    time.sleep(0.05)
time.sleep(0.3)
print()
n = 0
n7 = input('Enter Your Name:\n')
while n != 6:
    print("****************************************************")
    print("Enter '1' to access inventory: ")
    time.sleep(0.03)
    print("Enter '2' to update inventory: ")
    time.sleep(0.03)
    print("Enter '3' to generate sales report: ")
    time.sleep(0.03)
    print("Enter '4' to get gross profit: ")
    time.sleep(0.03)
    print("Enter '5' to exit store: ")
    time.sleep(0.03)
    n = int(input("Enter the number from the assigned tasks: "))
    if n == 1:
        df = pd.read_csv('inventory.csv')
        print(df)
    elif n == 2:
        os.system("start inventory.csv")
    elif n == 3:
        df = pd.read_csv("inventory.csv")
        df.plot(kind='bar',
                color=['red', 'blue', 'yellow', 'green', 'cyan', 'pink', 'magenta'],
                edgecolor='Black', linewidth=1, width=0.8)
        ticks = df.index.tolist()
        plt.xticks(ticks, df.Goods)
        plt.title('MONTHLY SALES REPORT')
        plt.ylabel('Sales(quantity)')
        plt.grid(True)
        plt.show()
    elif n == 4:
        c1 = int(input("enter number of milk items sold: "))
        c2 = int(input("enter number of medicine sold: "))
        c3 = int(input("enter number of bread sold: "))
        c4 = int(input("enter number of biscuits sold: "))
        c5 = int(input("enter number of vegetables sold: "))
        c6 = int(input("enter number of stationery sold: "))
        c7 = int(input("enter number of bags sold: "))
        netprofit = c1 * 50 + c2 * 25 + c3 * 40 + c4 * 20 + c5 * 15 + c6 * 35 + c7 * 500
        print('Net Profit is Rs', netprofit)
    elif n == 5:
        print("THANK YOU", n7, "FOR VISITING.......")
else:
    print('VALUE ERROR! PLEASE CHECK')
