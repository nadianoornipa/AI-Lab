sales_data = [
    {"Product": "Book", "Revenue": 1000},
    {"Product": "Paper", "Revenue": 250},
    {"Product": "Color", "Revenue": 1200},
    {"Product": "Pencil Box", "Revenue": 300},
    {"Product": "Canvas", "Revenue": 2500},
    {"Product": "Pen", "Revenue": 50},
]

total_revenue = {}
for entry in sales_data:
    product = entry["Product"]
    revenue = entry["Revenue"]
    if product in total_revenue:
        total_revenue[product] += revenue
    else:
        total_revenue[product] = revenue

print(total_revenue) 
