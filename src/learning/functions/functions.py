def calculate_total(prices, discount=0):  # efining a function to calculate the total price
    """
    Calculate the total price after applying a discount.
    :param prices: List of book proces
    :param discount: Discount to apply (default is 0%)
    :return: Total price after discount
    """
    subtotal = sum(prices)
    discounted_total = subtotal - (subtotal * discount / 100)
    return discounted_total


def add_extra_charges(total,
                      *args):  # Using *args to handle variable numbers of additional charges (e.g., tax, shipping)
    """
    Add extra charges like tax and shipping.
    :param total: Initial total price
    :param args: Variable extra charges (e.g., tax, shipping)
    :return: Final total after adding charges
    """
    for charge in args:
        total += charge
    return total


def display_summary(final_total, **kwargs):  # Using **kwargs to display additional information
    """
    Display a summary of the purchase.
    :param final_total: Final total price
    :param kwargs: Additional details like buyer name, date, etc.
    """
    print("\n--- Purchase Summary ---")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
    print(f"Final Total: \u20B9{final_total:.2f}") #\u20B9 unicode format for Indian Rupee


effective_discount = lambda price, percent: price - (
            price * percent / 100)  # Using a lambda function to calculate the effective discount for a quick operation

# Execute the functions
book_prices = [15.99, 25.50, 8.99, 12.00]
discount_percent = 10
extra_charges = [2.50, 5.00]  # Shipping, Tax

# Calculate the discounted total
total_after_discount = calculate_total(book_prices, discount_percent)
# Add extra charge
final_price = add_extra_charges(total_after_discount, *extra_charges)
# Display the summary
display_summary(final_price, firstname="Alice", lastname="Huang", date="2024-11-19")

# Quick Lambda Calculation
print("\nLambda Example:")
price = 50
percent_discount = 20
print(
    f"Price after {percent_discount}% discount: \u20B9{effective_discount(price, percent_discount):.2f}")  # 2f - output format 2 decimal places
