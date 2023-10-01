while True:
    try:
        #define the variable bg as the user input for the budget
        bg = float(input("What's your budget? ")) 
        #define another variable s equal to bg
        s = bg
    #we want the input to be in the float format. if it isn't, then we print a ValueError asking user to provide a valid input.
    except ValueError:
        print("Print the number as an amount")
        continue
    #if the input satisfies all these conditions, we break out of this loop
    else:
        break
#define the format of the output within the variable a
a = {"name":[], "quant":[], "price":[]}
#define a variable b with the list of all values of a in it
b = list(a.values())

#name of the product
na = b[0]
#quantity of the product
qu = b[1]
#price of the product
pr = b[2]

while True:
    try:
        #define a variable ch asking the user for whether they want to add a product or if they want to exit
        ch = int(input("1.Add\n2.Exit\nEnter your choice:"))
    #if the user inputs any other option than 1 or 2, print a ValueError prompting the user to choose just one of the two options
    except ValueError:
         print("\nERROR: Choose only digits from the given option")
         continue
    #if the user decides to add a product and if the budget is not negative,
    else:
        if ch == 1 and s>0:
            #define a variable pn for the product name
            pn = input("Enter product name: ")
            #define a variable q for the quantity
            q = input("Enter Quantity: ")
            #define a variable p for the price of the product
            p = float(input("Enter price of the product: "))

            #if the price of the product is greater than the budget, tell the user that they can't buy it and then continue with the else function
            if p > s:
                print("\nCan't buy. Price of the products exceeds the budget")
                continue
            else:
                #now once the user adds a product to the grocery list, print the amount left after buying the desired product
                if pn in na:
                    ind = na.index(pn)
                    qu.remove(qu[ind])
                    pr.remove(pr[ind])
                    qu.insert(ind, q)
                    pr.insert(ind, p)

                    s = bg-sum(pr)

                    print("\nAmount left", s)
                else:
                    #??
                    na.append(pn)
                    qu.append(q)
                    pr.append(p)

                    s = bg-sum(pr)
        #if the difference of the price of the products and the budget becomes 0, tell the user that they don't have any money left           
        elif s<=0:
            print("\nNo Budget")
        else:
            #if the user still has some money left, break out of this loop and print the final amount left
            break
    print("Amount Left: Rs.", s)
    
    #if the amount left after buying all the specified products is still enough to buy some additional quantity of any of the products listed, prompt the user that they can still buy one more.
    if s in pr:
        print("\nAmount left can buy you a", na[pr.index(s)])
    
    #in the end, print the final grocery list
    print("\n\nGrocery List")

    #len(na) refers to the length of the number of names in the grocery list
    #then, for every item in the list, print the quantity of the item, the name of the item and the total price(of the total quantity) of the item
    for i in range(len(na)):
        print(qu[i], na[i], "-", "Rs.", pr[i], "\n")