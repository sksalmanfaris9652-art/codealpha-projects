
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}

print("=" * 45)
print("          STOCK PORTFOLIO TRACKER")
print("=" * 45)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

while True:
    print()

    stock_name = input("Enter stock name: ").strip().upper()

    if stock_name not in stock_prices:
        print("Invalid stock name. Please try again.")
        continue

    quantity = input("Enter quantity: ").strip()

    if not quantity.isdigit() or int(quantity) <= 0:
        print("Please enter a valid quantity.")
        continue

    quantity = int(quantity)

    # Add stock to portfolio
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    print(f"{quantity} shares of {stock_name} added.")

    # Ask whether the user wants another stock
    add_more = input(
        "Do you want to add another stock? (yes/no): "
    ).strip().lower()

    if add_more not in ("yes", "y"):
        break


# Calculate and display the result
print("\n" + "=" * 45)
print("             PORTFOLIO SUMMARY")
print("=" * 45)

total_investment = 0

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(
        f"{stock} : {quantity} shares × "
        f"${price} = ${investment}"
    )

print("-" * 45)
print(f"Total Investment Value: ${total_investment}")
print("=" * 45)

# Save portfolio details to a text file

with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("=" * 40 + "\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity

        file.write(
            f"{stock} : {quantity} shares × "
            f"${price} = ${investment}\n"
        )

    file.write("=" * 40 + "\n")
    file.write(f"Total Investment Value: ${total_investment}\n")

print("\nPortfolio saved successfully to portfolio.txt")