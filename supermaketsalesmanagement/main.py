import pandas as pd
df=pd.read_csv('supermarket_sales - Sheet1.csv',parse_dates=['Date'])
def showfirst():
    return df[0:5]
def showlast():
    return df[-5:]
def showcolumns():
    return df.columns
def summary():
    return df.describe()
def viewsales(branch):
    branchsort=df[df.Branch==branch]
    return pd.DataFrame({
        branch:[branchsort.Total.sum(), branchsort.cogs.sum(),branchsort['gross margin percentage'].mean(),branchsort['gross income'].mean(),branchsort.Rating.mean()]},
        index=['Total Sales','Total cogs','average gross margin percentage','average gross income','average rating'])
def abovecutoff(amount):
    return df[df.Total>amount]
def belowcutoff(amount):
    return (df[df.Total<amount] if not df[df.Total<amount].empty else 'Data not found')
def searchbypayment(method):
    return (df[df.Payment==method] if not df[df.Payment==method].empty else "Data not found")
def searchbyproduct(product):
    return (df[df['Product line']==product] if not df[df['Product line']==product].empty else "Data not found")
def displaysalesperday():
    grouped= df[['Total','Date','cogs','gross margin percentage','gross income','Rating']].groupby('Date')
    newdata={}
    for i,j in grouped:
        newdata[i]=[j['Total'].sum(), j['cogs'].sum(),j['gross margin percentage'].mean(),j['gross income'].mean(),j['Rating'].mean()]
    newdata=pd.DataFrame(newdata,index=['Total Sales','Total cogs','average gross margin percentage','average gross income','average rating'])
    return newdata
def displaysalespermonth():
    grouped= df[['Total','Date','cogs','gross margin percentage','gross income','Rating']].groupby(df['Date'].dt.month)
    newdata={}
    for i,j in grouped:
        newdata[i]=[j['Total'].sum(), j['cogs'].sum(),j['gross margin percentage'].mean(),j['gross income'].mean(),j['Rating'].mean()]
    return pd.DataFrame(newdata,index=['Total Sales','Total cogs','average gross margin percentage','average gross income','average rating'])
def averageratingperproduct():
    grouped= df[['Product line','Rating']].groupby('Product line')
    newdata={}
    for i,j in grouped:
        newdata[i]=[j['Rating'].mean()]
    return pd.DataFrame(newdata,index=['average rating'])
def displaysalespercity():
    grouped=df.groupby('City')
    for i,j in grouped:
        print(i, '\n', pd.DataFrame(j)[['Total','cogs','gross margin percentage','gross income','Rating']].describe())
    return None
def sortbyhighestsales():
    return df.sort_values(by='Total', ascending=False)
def sortbylowestsales():
    return df.sort_values(by='Total', ascending=True)
def sortbyquantity():
    return df.sort_values(by='Quantity', ascending=False)
def databyinvoice(invoice):
    return (df[df['Invoice ID']==invoice] if not df[df['Invoice ID']==invoice].empty else "Data not found")
def display():
    return df
if __name__=='__main__':
    while True:
        print('====== Super Market Sales Management =====')
        print('1. Show first 5 rows')
        print('2. Show last 5 rows')
        print('3. Show all column names')
        print('4. Show summary of all the dataset')
        print('5. View sales for a particular branch')
        print('6. Display sales above a specific amount')
        print('7. Display sales below a specific amount')
        print('8. Search by payment method')
        print('9. Search by product line')
        print('10. Display sales per day')
        print('11. Display sales per month')
        print('12. Average rating per product line')
        print('13. Sales summary per city')
        print('14. Sort the dataset by highest sales')
        print('15. Sort the dataset by lowest sales')
        print('16. Sort by quantity sold')
        print('17. Find all the data of a product by Invoice Id')
        print('18. Display whole dataset')
        print('19. Exit')
        print('==========================================')
        try:
            ch=int(input('Enter your choice:-  '))
            if ch==1:
                print(showfirst())
            elif ch==2:
                print(showlast())
            elif ch==3:
                for i in showcolumns():
                    print(i)
            elif ch==4:
                print(summary())
            elif ch==5:
                branch=input('Enter the branch you want to see the sales of:-  ')
                print(viewsales(branch.upper()))
            elif ch==6:
                amount=int(input('Enter the cutoff amount:-  '))
                print(abovecutoff(amount))
            elif ch==7:
                amount=int(input('Enter the cutoff amount:-  '))
                print(belowcutoff(amount))
            elif ch==8:
                method=input('Enter the payment method:-  ')
                print(searchbypayment(method.title()))
            elif ch==9:
                product=input('Enter the product line:-  ')
                print(searchbyproduct(product.capitalize()))
            elif ch==10:
                print(displaysalesperday())
            elif ch==11:
                print(displaysalespermonth())
            elif ch==12:
                print(averageratingperproduct())
            elif ch==13:
                displaysalespercity()
            elif ch==14:
                print(sortbyhighestsales())
            elif ch==15:
                print(sortbylowestsales())
            elif ch== 16:
                print(sortbyquantity())
            elif ch==17:
                invoice=input('Enter the invoice id:-  ')
                print(databyinvoice(invoice))
            elif ch==18:
                print(display())
            elif ch==19:
                print('Thank you for using our program')
                exit(0)
            else:
                print('Wrong input')
        except Exception as e:
            print(e)
            continue