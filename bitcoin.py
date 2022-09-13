try:
    bitcoin_price = float(input("What is Bitcoin price today? "))
    how_much = float(input("How much $ do you have? "))
except Exception:
    print("You only need to input a number")
else:
    if bitcoin_price:
        print("You can buy: ", how_much/bitcoin_price, "BTC")
    else:
        print("You are mistaken. Bitcoin cannot be 0.")
