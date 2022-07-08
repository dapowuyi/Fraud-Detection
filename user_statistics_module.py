#Here are the different functions required to use the loaded dictionary 

#Function 1 - The Maximum and minimum transactions of a given user


def minMax(myDict, user):
    
    try:
        #create an new list
        newList = []
        #loop thrugh the nested dictionary to obtain amount
        for TransID, values in myDict[user].items():
        
            Amt = myDict[user][TransID][1]
        #append amount to the list
            newList.append(Amt)
            
        #Get the min and max values of amount
        maxAmt = max(newList)
        minAmt = min(newList)
        
        #return the minium and maximum amounts
        return (minAmt, maxAmt)
    except:
        return(0,0)


def locationCentroid(myDict, user):
    try:
    #create two empty lists
        xList = []
        yList = []
    
    #initiate two varaiables to get total of both x and y cor-ordinates
        xtotal = 0
        ytotal = 0

    #loop through dictionary to obtain the  x and y coordinates
        for TransID, values in myDict[user].items():
            x = myDict[user][TransID][2]
            y = myDict[user][TransID][3]
    
    #append the coordinates to the respective lists
            xList.append(x)
            yList.append(y)
    #Get the sum of both the x and y coordinates
            xtotal = xtotal + x
            ytotal = ytotal + y
    
    #Get the number of values in each list
        xLength = len(xList)
        yLength = len(yList)
    
    #divide the mean by the number of values and round to 2 decimal places
        x_coord = round(xtotal/xLength, 2)
        y_coord = round(ytotal/yLength, 2)
    
    #return the centroid
        return(x_coord, y_coord)
    except:
        return(0,0)


def distance(myDict, user):
    #request for the specific transaction
    transID = input("Please, input the TransactionID: ")
    
    #call the location centroid function
    (x1, y1) = locationCentroid(myDict, user)

    #loop through dictionary to get x and y coordinates
    for TransID, vs in myDict[user].items():
        x2 = myDict[user][TransID][2]
        y2 = myDict[user][TransID][3]
    
    #calculate the distance
    transactionDist = (((x1 - x2) ** 2) + ((y1 - y2) **2) ** 0.5)
    #dist = tranDist ** 0.5
    return transactionDist



def stndDev(myDict, user):
    #create an empty list
    amtList = []
    
    #initiate a varaible to store the total amount
    total = 0
    
    #loop through dictionry to obtain amount
    for TransID, values in myDict[user].items():
        Amt = myDict[user][TransID][1]
        
        #append amount to list 
        amtList.append(Amt)
        
        #sum the amount
        total = total + Amt
    #get the length of the list
    amtLength = len(amtList)

    #obtain the mean
    mean = total/amtLength
    print("The mean of the transactions performed by user ", user, "is ", round(mean, 2))

    total2 = 0
    
    #loop over the list and calculate standard deviation
    for v in amtList:
        sqr = (v - mean)** 2
        total2 = total2 + sqr
    mean2 = total2/amtLength
    sdeviation = mean2 ** 0.5
    return round(sdeviation, 2)

       
def variance(myDict, user):
    #create empty list and initiae variable to hold sum of amount
    amtList = []
    total = 0
    
    #loop through the dictiionary to obtain amount
    for TransID, values in myDict[user].items():
        Amt = myDict[user][TransID][1]
    #append amount to list and sum up the amount. Also obtain length of list
        amtList.append(Amt)
        total = total + Amt
    amtLength = len(amtList)

    #calculate the mean
    mean = total/amtLength

    
    total2 = 0
    
    #loop through the list and calculate variance
    for v in amtList:
        sqr = (v - mean)** 2
        total2 = total2 + sqr
    variance = total2/amtLength
    return variance


def fraudulent(myDict, user):

    #loop through the nested dictionary to obtain details of fraudulent transactions
    print("The following transactions are fraudulent", "\n")
    for TransID, values in myDict[user].items():
        fraud = myDict[user][TransID][4]
        Amt = myDict[user][TransID][1]
        description = myDict[user][TransID][0]
        x = myDict[user][TransID][2]
        y = myDict[user][TransID][3]
    #check if the transaction is fraudulent and print details of such transaction to the console
        if fraud == "true":
            print("TransID:", TransID, ", Amount:", Amt, ", Description:", description, ", x-coordinates:", x, ", y-coordinates: ", y, "\n")
        #return fraud
    

       
       



