"""
app config starts here#
"""
import sys

# Define the prices and special offers
prices = {
    'Soup': 0.65,
    'Bread': 0.80,
    'Milk': 1.30,
    'Apples': 1.00
}

special_offers = {
    'Apples': (0.10, '10% off'),
    'Soup_Bread': (0.40,
                   'Buy 2 tins of soup and get a loaf of bread for half price'
                   )
}


def calculate_discount(item_counts):
    discount = 0
    if 'Soup' in item_counts and 'Bread' in item_counts:
        soup_count = item_counts['Soup']
        bread_count = item_counts['Bread']
        sets_of_offer = min(soup_count // 2, bread_count)
        discount += sets_of_offer * special_offers['Soup_Bread'][0]
        print(f'Soup_Bread {special_offers["Soup_Bread"][1]}: £{discount:.2f}')

    if 'Apples' in item_counts:
        apples_count = item_counts['Apples']
        discount += apples_count * special_offers['Apples'][0]
        print(f'Apples {special_offers["Apples"][1]}: £{discount:.2f}')

    return discount


def price_basket(basket):
    item_counts = {}
    subtotal = 0

    for item in basket:
        if item in prices:
            item_counts[item] = item_counts.get(item, 0) + 1
            subtotal += prices[item]
        else:
            print(f"Warning: {item} is not a valid item and will be ignored.")

    print(f'Subtotal: £{subtotal:.2f}')

    if not item_counts:
        print('(No offers available)')
        print(f'Total price: £{subtotal:.2f}')
    else:
        discount = calculate_discount(item_counts)
        total_price = subtotal - discount
        print(f'Total price: £{total_price:.2f}')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: PriceBasket item1 item2 item3 ...")
    else:
        # Exclude script name and non-item arguments
        basket = sys.argv[1:]
        price_basket(basket)
