shopping_cart = [{'name': 'apple', 'price_per_item': 0.21, 'number': 4}, {'name': 'banana', 'price_per_item': 0.12, 'number': 5}]

def receipt (items):
    for item in items:
        print (item)

def gross(shopping_cart):
    apple_cost = shopping_cart[0]['price_per_item'] * shopping_cart[0]['number']
    banana_cost = shopping_cart[1]['price_per_item'] * shopping_cart[1]['number']
    Gross_Cost = apple_cost + banana_cost
    return apple_cost,banana_cost,Gross_Cost

def sale(apple_cost, banana_cost):
    apple_cost_sale = apple_cost * 0.5
    Cost_after_sales = apple_cost_sale + banana_cost
    return Cost_after_sales

def tax(Cost_after_sales):
    sales_tax = 1.15
    net_cost = Cost_after_sales * sales_tax
    return net_cost

apple_cost, banana_cost, Gross_Cost = gross(shopping_cart)
print (f'Cost of basket before sales and tax {Gross_Cost}')

Cost_after_sales = sale(apple_cost, banana_cost)
print (f'Cost of basket after sales, but before tax {Cost_after_sales}')

net_cost = tax(Cost_after_sales)
print (f'Cost of basket after sales and tax {net_cost:.2f}')

receipt (shopping_cart)


