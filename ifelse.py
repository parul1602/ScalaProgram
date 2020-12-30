Indian = ["samosa", "daal", "dhokla"]
Chinese = ["Mancurian", "Fried rice"]
Italian = ["pizza","pasta"]
dish = input("What dish you want")
if dish in Indian:
    print("Its Indian")
elif dish in Chinese:
    print("Its chinese")
elif dish in Italian:
    print("Its Italian")
else:
    print("not in cusin")
