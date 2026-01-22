# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

portfolio = {}
total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))
    portfolio[stock] = quantity

# Calculate total investment
for stock, qty in portfolio.items():
    total_investment += stock_prices[stock] * qty

# Display result
print("\n📊 Portfolio Summary")
for stock, qty in portfolio.items():
    print(f"{stock} - Quantity: {qty}, Price: {stock_prices[stock]}")

print("\n💰 Total Investment Value:", total_investment)

# Optional file saving
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock} - Quantity: {qty}, Price: {stock_prices[stock]}\n")
        file.write(f"\nTotal Investment Value: {total_investment}")

    print("✅ Data saved to portfolio.txt")
