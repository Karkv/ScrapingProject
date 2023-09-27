
import pandas as pd
from sklearn.metrics import balanced_accuracy_score


def readfromexcel():
    df = pd.read_excel("UBI.xlsx", index_col=0)

    return df
def show(accno):
    df=readfromexcel()
    
    n=df.loc[accno]
    return n

def GetBalance(accno):
    try:
        df = readfromexcel()
        x = df[['balance']]
        return x.loc[accno][0]
    except:
        return None


def ChangeBalance(accno, newbalance):
    try:
        newdata = {'accno': [accno],

                   'balance': [newbalance]
                   }
        newdata = pd.DataFrame(newdata, index=newdata["accno"])
        print(newdata)
        df = readfromexcel()
        df.update(newdata)

        SaveToExcel(df)
        return True
    except:
        return False


def CloseAccount(accno):
    try:
        df = readfromexcel()
        df = df.drop(accno)
        print(df)
        SaveToExcel(df)
        return True
    except:
        return False


def NewAccount(accno, name, balance):
    # try:
    newdata = {
        "accno": accno,
        'balance': balance,
        "name": name


    }
    df = readfromexcel()
    print(newdata)
    df.loc[accno] = newdata
    print('df', df)
    SaveToExcel(df)
    return True
    # except:
    return False


def depositBalance(accno, newBalance):
    currentbalance = GetBalance(accno)
    balance = currentbalance+newBalance
    ChangeBalance(accno, balance)

def WithdrawBalance(accno, newBalance):
    currentbalance = GetBalance(accno)
    balance = currentbalance-newBalance
    ChangeBalance(accno, balance)


def SaveToExcel(df):
    # df=readfromexcel()
    df.to_excel("UBI.xlsx")

# accno = int(input("Enter the account Numbner"))
# name = input("Enter the name: ")
# Balance = int(input("Enter the Balance:"))


# x = NewAccount(accno, name, Balance)
# print(x)
# print(readfromexcel())
while True:
    print("0-Exit,1-New Account, 2-Deposit,3-Withdraw,4-Check Balance,5-Close\n")
    option = int(input())
    if option == 0:
        break
    if option == 1:
        print("New")
        accno = input("Enter the account No.:")
        name = input("Enter the name:")
        newBalance = int(input("Enter the Balance:"))

        NewAccount(accno, name, newBalance)
        continue
    if option == 2:
        print("Deposit")
        accno = input("Enter the account no.")
        newBalance = int(input("Enter the deposite Balance"))
        x = depositBalance(accno, newBalance)
        print(x)
        continue
    if option == 3:
        print("Withdraw")
        accno=input("Enter the account Number:")
        newBalance=int(input("Enter the withdrow money:"))
        p=WithdrawBalance(accno,newBalance)
        print(p)
        continue
    if option == 4:
        print("Check Balance")
        accno=input("Enter the account no.")
        print(SaveToExcel.loc[accno])
        continue
    if option == 5:
        print("Close")
        accno=input("Enter the account number for close")
        CloseAccount(accno)
        print("CLose account")
        continue
    print("Invalid Option")


print(readfromexcel())
