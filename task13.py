me = {2, 6, 8, 10, 11, 13, 17, 20, 23, 30}

Tom = {3, 6, 7, 11, 13, 14, 16, 17, 27, 30}
Bill = {1, 2, 6, 8, 10, 11, 14, 19, 25, 27}
Alice = {5, 7, 11, 19, 22, 25, 26, 27, 28, 30}

total_me_with_tom = len(me | Tom)
total_me_with_bill = len(me | Bill)
total_me_with_alice = len(me | Alice)

print(total_me_with_tom)
print(total_me_with_bill)
print(total_me_with_alice)




