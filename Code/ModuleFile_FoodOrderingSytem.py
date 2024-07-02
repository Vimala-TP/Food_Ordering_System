#Module file of Food Ordering
def ServiceMenu():
    print("""\n---Services Available---
1.Select Food
2.Display Bill
3.Exit""")
    return int(input("Select the option what you wanted to do = "))
def FoodMenu():
    print("""\n---Food Menu---
1.Statars
2.Rice
3.Pasta
4.To move to Service Menu""")
    return int(input("\nEnter you choice = "))
def StartarsMenu():
    print("""\n----Statars---
1.Paneer Manchurian    = 150Rs
2.Babycorn Manchurian  = 160Rs
3.Gobi Manchurian      = 100Rs
4.Babycorn chilly      = 170Rs
5.To move to Food Menu""")
    print("\nTo Add enter \"+quantity_required\" and to remove \"-quantity_required\"")
def RiceMenu():
    print("""\n----Rice Items---
1.Veg Biriyani  = 150Rs
2.Fried Rice    = 120Rs
3.Gobi Rice     = 150Rs
4.Ghee Rice     = 120Rs
5.To move to Food Menu""")
    print("\nTo Add enter \"+quantity_required\" and to remove \"-quantity_required\"")
def PastaMenu():
    print("""\n----Pasta Items---
1.Mac and cheese Pasta  = 180Rs
2.Veg Maceroni          = 150Rs
3.Penne Alfredo         = 140Rs
4.Red sauce Pasta       = 120Rs
5.To move to Food  Menu""")
    print("\nTo Add enter \"+quantity_required\" and to remove \"-quantity_required\"")
