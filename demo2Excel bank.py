import pandas as pd 
from sklearn.metrics import balanced_accuracy_score

def readexcel():
    df=pd.read_excel('UBI.xlsx',index_col=0)

    return df

def NewAccount(accno,name,balance):
    newdata={
        "accno":accno,
        "balance":balance,
        "name":name
    }
    df = readexcel()
    print(newdata)
    df.loc[accno]=newdata
    print("new table",df)
    savetoexcel(df)
    return True

def show(accno):
    df=readexcel()
    x=df.loc[accno]
    return x

def GetBalance(accno):
    # try:
        df=readexcel()
        x=df["balance"]
        return int(x.loc[accno])
    # except:
        # return None
    

def changeBalance(accno,newbalance):
    try:
        newdata={
            'accno':[accno],
            'balance':[newbalance]

        }
        newdata=pd.DataFrame(newdata,index=newdata['accno'])
        print(newdata)
        df=readexcel()
        df.update(newdata)
        savetoexcel(df)
    except:
        return True


def depositBalance(accno,newbalance):
    currentbalance=GetBalance(accno)
    balance=currentbalance+newbalance
    changeBalance(accno,balance)

def withdrawBalance(accno,newbalance):
    currentbalance=GetBalance(accno)
    balance=currentbalance-newbalance
    if balance<0
    changeBalance(accno,balance)

def closeAccount(accno):
    try:
        df=readexcel()
        df=df.drop(accno)
        print(df)
        savetoexcel(df)
        return True
    except:
        return False

def savetoexcel(df):
    df.to_excel("UBI.xlsx")


# print(GetBalance(2))


# print(readexcel())

# print(show(1))


while True:
    print("0-Exit 1-New Account 2-Deposit 3-Withdrow, 4-check Balance 5-close")
    option=int(input("Choose what you want :"))
    if option==0:
        break
    if option==1:
        print("Creaet New Account")
        accno=int(input("enter the account number:"))
        name=input("Enter the name :")
        newBalance=int(input("Enter the Balance:"))
        NewAccount(accno,name ,newBalance)
        continue
    if option==2:
        print("Deposit")
        accno=int(input("Enter the your account number:"))
        newbalance=int(input("Enter the deposit money:"))
        x=depositBalance(accno,newbalance)
        print(x)
    if option==3:
        print("withdraw")
        accno=int(input("Enter the Account nUmber"))
        newbalance=int(input("Enter the withdraw Money"))
        p=withdrawBalance(accno,newbalance)
        print(p)
        continue
    if option ==4:
        print("checkaccount")
        accno=int(input("Enter the account Number"))
        x=show(accno)
        print(x)
