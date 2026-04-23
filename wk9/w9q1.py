prices = list(map(float, input("Enter daily closing prices: ").split()))

if len(prices) == 0:
    print("No prices entered")
else:
    max_price = prices[0]
    min_price = prices[0]

    for price in prices:
        if price > max_price:
            max_price = price
        if price < min_price:
            min_price = price

    print("Maximum price:", max_price)
    
    print("Minimum price:", min_price)
    