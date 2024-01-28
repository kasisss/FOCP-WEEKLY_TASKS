#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_user_input():
    while True:
        try:
            pizzas_ordered = int(input("How many pizzas ordered? "))
            if pizzas_ordered < 0:
                raise ValueError("Please enter a positive integer!")
            break
        except ValueError:
            print("Please enter a number!")

    while True:
        delivery_required = input("Is delivery required? (Y/N) ").upper()
        if delivery_required in ('Y', 'N'):
            break
        else:
            print('Please answer "Y" or "N".')

    while True:
        is_tuesday = input("Is it Tuesday? (Y/N) ").upper()
        if is_tuesday in ('Y', 'N'):
            break
        else:
            print('Please answer "Y" or "N".')

    while True:
        used_app = input("Did the customer use the app? (Y/N) ").upper()
        if used_app in ('Y', 'N'):
            break
        else:
            print('Please answer "Y" or "N".')

    return pizzas_ordered, delivery_required, is_tuesday, used_app


def calculate_total_price(pizzas_ordered, delivery_required, is_tuesday, used_app):
    pizza_price = 12
    delivery_cost = 2.5

    if is_tuesday == 'Y':
        pizza_price *= 0.5  # 50% discount on Tuesdays

    if delivery_required == 'Y' and pizzas_ordered >= 5:
        delivery_cost = 0  # Free delivery for 5 or more pizzas

    total_price = (pizza_price * pizzas_ordered) + delivery_cost

    if used_app == 'Y':
        total_price *= 0.75  # 25% additional discount for using the app

    return round(total_price, 2)


def main():
    print("BPP Pizza Price Calculator")
    print("==========================\n")

    pizzas_ordered, delivery_required, is_tuesday, used_app = get_user_input()

    total_price = calculate_total_price(pizzas_ordered, delivery_required, is_tuesday, used_app)

    print(f"\nTotal Price: £{total_price:.2f}.")


if __name__ == "__main__":
    main()


# In[ ]:




