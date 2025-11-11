import os
from dotenv import load_dotenv
load_dotenv()

gst=float(os.getenv("GST_rate"))

def amount(order):
    total=0
    for items,price,quan in order:
        print(items,":  ₹",price," ",quan)
        total+=price*quan
    tax = total * gst
    grand_total = total + tax
    return grand_total

