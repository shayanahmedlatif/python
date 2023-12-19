import math

auction_list = {}

while True:
  if input("Welcome! Are you ready for a new auction? Y/N? ").lower() in ["y", "yes"]:
    bid_number = len(auction_list) + 1
    while True:
      member_name = input("What is your name? ")
      while True:
        try:
          bid_amount = math.ceil(float(input("What is your bid amount? ")))
          if bid_amount <= 100:
            print("Minimum bid amount is $101. Try again.")
            continue
          break
        except ValueError:
          print("Invalid input, try again.")
          continue
      break
    auction_list[f"Bidder_{bid_number}"] = {"Bidder name": member_name, "Bid amount": bid_amount}
    bid_number += 1
    while True:
      if input("Is there any other bidder Y/N").lower() not in ["y", "yes"]:
        # clear()
        print("Auction Results")
        # A loop to print all the information within a dictionary.
        #  for bidder_id, info in auction_list.items():
          # print(f"{bidder_id}: {info['Bidder name']} bid is ${info['Bid amount']}")
        # print("Goodbye.")
        # print(auction_list)
        max_bidder = None
        max_bid_amount = float('-inf')
        for max_bidder_id, max_info in auction_list.items():
          bid_amount = max_info['Bid amount']
          if bid_amount > max_bid_amount:
            max_bid_amount = bid_amount
            max_bidder = max_bidder_id
        if max_bidder is not None:
          print(f"{max_info['Bidder name']} have the highest bid of {max_info['Bid amount']} among all.")
        else:
          print("No bid found.")
        break
      else:
        member_name = input("Who is the next bidder? ")
        while True:
          try:
            bid_amount = math.ceil(float(input("What is your bid amount? ")))
            if bid_amount <= 100:
              print("Minimum bid amount is $100. Try again.")
              continue
            break
          except ValueError:
            print("Invalid input, try again.")
        auction_list[f"Bidder_{bid_number}"] = {"Bidder name": member_name, "Bid amount": bid_amount}
        bid_number += 1
  else:
    print("Wrong choice! try again.")
    continue
  break 