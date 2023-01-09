f=open("names.txt", "r+")

count=1
try: 
  while True:
    contents=f.readline().strip().split()
    
    fname=contents[0]
    lname=contents[-1]
    
    first=(fname + lname)
    second=(fname[0] + lname)
    third=(fname + lname[0])
    fourth=(fname + "." + lname)
    
    with open("NewNames.txt", 'a+') as b:
      b.write(f"""Name #{count}

{first}
{second}
{third}
{fourth}

""")
      count+=1
    if contents=="":
      break
  f.close()
  b.close()
except:
  print("The script has completed. Check file for results.")
