import pandas as pd


def grade(avg):
   if avg>60:
        return "pass 1st"
   elif avg>49:
        return "Pass  2nd"
   elif avg>33:
       return "Pass 3rd"
   else:
       return "fail"
   
# Roll No.,Name,hindi,English,Math,Science]
# def readExcel():\
df = pd.read_csv("student.csv")
Rollno = df["Rollno"]
name = df["Name"]
hindi = df["hindi"]
English = df["English"]
Math = df["Math"]


df["total"]=hindi+English+Math
total=df["total"]
# print(total)
df["avg"]=(total/300)*100
df['grade']=df['avg'].apply(grade)
print(df)


# print(df["avg"])
# df["pass"]=df["avg"]>=50
# for a in df["avg"]:
#    print(a)
# print(df["grade"])
# if df["avg"]>60:
#     df["grade"]="first"
# elif df["avg"]>49:
#     df['grade']="Second"
# elif df["avg"]>33:
#     df['grade']="Third"
# else:
#     df["grade"]="Fail"
   
# print(df["grade"])

# print(df["grade"])
# print(df)


# Rollno,name,hindi,English,Math
# total=hindi+English+Math
# for i in range(len(Rollno)):

   # n=df.loc[i]
   # avg=n['avg']
   # if avg<50:
   #    n["grade"]="fail"
   # else:
   #    n["grade"]="pass"
   # print(n['grade'])
   # print("______________________")

# print(df)
# print(total)
# print(a)



# Rollno,name,hindi,Engish,Math=readExcel()
# print(Rollno,name,hindi,English,Math)
# print(df.to_string())