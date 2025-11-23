import fpdf
import json

with open("./order.json") as order_file:

    proc_order = json.load(order_file)
    print(proc_order)

lab5_w7 = proc_order["lab5_w7"]
lab6_w8 = proc_order["lab6_w8"]


pdf = fpdf.FPDF()

