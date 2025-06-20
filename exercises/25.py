age=int(input("enter your age"))

if (age > 18):
    print ("You can vote")
else:
    print("you will be able to participate after"+ str(18-age) + "years")