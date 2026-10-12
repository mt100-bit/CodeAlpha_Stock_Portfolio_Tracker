stock_prices  = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 200
}

total_portfolio = 0
portfolio = []

while True: 

  stock_name = input("Enter the stock name (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()
  if stock_name not in stock_prices:
    print("Invalid stock name. Please try again.")
    continue
  
  try:
    quantity = int(input("Enter the quantity: "))
  except ValueError:
    print("Please enter a valid whole number.")
    continue 
  if quantity <= 0:
    print("Quantity must be a positive number.")
    continue
  
  price = stock_prices[stock_name]

  total_investment = price * quantity

  portfolio.append({
    "stock": stock_name,
    "quantity": quantity,
    "price": price,
    "investment": total_investment
})
  
  total_portfolio += total_investment

  while True:
    again = input("Do you want to add another stock? (yes/no): ").lower()

    if again == "yes":
      break
    elif again == "no":
       break
    else:
      print("Invalid input. Please enter 'yes' or 'no'.")

  if again == "no":
      break

print("Total portfolio investment: $", total_portfolio)

while True:
    results = input("Do you want to save your results? (yes/no): ").lower()

    if results == "yes" or results == "no":
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

if results == "yes":
    with open("portfolio_results.txt", "w") as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("======================\n\n")

        for item in portfolio:
            file.write(f"Stock: {item['stock']}\n")
            file.write(f"Quantity: {item['quantity']}\n")
            file.write(f"Price per share: ${item['price']}\n")
            file.write(f"Investment: ${item['investment']}\n")
            file.write("----------------------\n")

        file.write(f"\nTotal portfolio investment: ${total_portfolio}\n")

    print("Results saved to portfolio_results.txt")
    