import json


"""variables global"""
Memories_json=open("Memories_json.json","r")
Memories_json_str=Memories_json.read()


Accs=json.loads(Memories_json_str)["Accs"]
Datas=json.loads(Memories_json_str)["Datas"]

Comms={"ex":"exit from programm",
       "exlog":"go to Login\Register menu",
       "reg":"Register",
       "log":"Login",
       "ns(name)":"create new string",
       "pp(name)":"print you string",
       "prall":"print all you strings",
       "cl(name)":"clear you string",
       "dl(name)":"delete you string",
       "ed(name)":"edit you string",
       "help":"help in commands"
       }
Comms_noinpstr={"(help)":"help in commands",
                "(ex)":"exit from programm",
                "(exlog)":"go to Login\Register menu",
                "(ns(name))":"create new string",
                "(prall)":"print all you strings",
                "(log)":"Login",
                "(reg)":"Register",
}
inp=''
inp1=''
Psn=''
Lgn=''

"""funcs global"""
def Do_Comms_noinpstr(inpp, safe):
  if inpp in Comms_noinpstr or str(inpp[0]+inpp[1]+inpp[2])+"(name))" in Comms_noinpstr:
    if inpp=="(help)":hp_nis()
    if inpp=="(ex)":ex()
    if inpp=="(exlog)":exlog()
    if inpp=="(reg)":reg()
    if inpp=="(log)":log()
    if inpp=="(prall)" and safe==0:prall()
    if inpp[1]+inpp[2]=="ns" and safe==0:
      if inpp[3]!="(" or inpp[-2]!=")":
        print("SyntaxError: "+str(inpp))
        exlog()
      pname=''
      for i in range(4,len(inpp)-2):
        pname+=inpp[i]
      ns(pname)
    if inpp=="(prall)" and safe==1:print("You not Logined, login to print all you strings")
    if inpp[1]+inpp[2]=="ns" and safe==1:
      if inpp[3]!="(" or inpp[-2]!=")":
        print("SyntaxError: "+str(inpp))
        exlog()
      pname=''
      for i in range(4,len(inpp)-2):
        pname+=inpp[i]
      print('You not Logined, login to add "'+pname+'" to you account')
    exlog()
def Do_Comms(inp):
  if len(inp)>1:
    if inp in Comms or str(inp[0]+inp[1])+"(name)" in Comms:
      if inp=="help":hp()
      if inp=="ex":ex()
      if inp=="exlog":exlog()
      if inp=="reg":reg()
      if inp=="log":log()
      if inp=="prall":prall()
      if inp[0]+inp[1]=="ns":
        if inp[2]!='(' or inp[-1]!=')':
          print("SyntaxError: "+str(inp))
          reedit()
        pname=''
        for i in range(3,len(inp)-1):
          pname+=inp[i]
        ns(pname)
      if inp[0]+inp[1]=="pp":
        if inp[2]!='(' or inp[-1]!=')':
          print("SyntaxError: "+str(inp))
          reedit()
        pname=''
        for i in range(3,len(inp)-1):
          pname+=inp[i]
        pp(pname)
      if inp[0]+inp[1]=="cl":
        if inp[2]!='(' or inp[-1]!=')':
          print("SyntaxError: "+str(inp))
          reedit()
        pname=''
        for i in range(3,len(inp)-1):
          pname+=inp[i]
        cl(pname)
      if inp[0]+inp[1]=="dl":
        if inp[2]!='(' or inp[-1]!=')':
          print("SyntaxError: "+str(inp))
          reedit()
        pname=''
        for i in range(3,len(inp)-1):
          pname+=inp[i]
        dl(pname)
      if inp[0]+inp[1]=="ed":
        if inp[2]!='(' or inp[-1]!=')':
          print("SyntaxError: "+str(inp))
          reedit()
        pname=''
        for i in range(3,len(inp)-1):
          pname+=inp[i]
        ed(pname)
      reedit()
    else:
      Datas[Psn][name]=inp
      reedit()
  else:
    Datas[Psn][name]=inp
    reedit()
def register(n,p):
  Accs[n]=p
  Datas[p]={input("Add string name:"):"New string."}
  exlog()
def log():
  global Lgn
  global Psn
  global inp
  global inp1
  inp=input("Name:")
  Do_Comms_noinpstr(inp,1)
  while Accs.get(inp)==None:
    print("Name is not be!")
    inp=input("Name:")
    Do_Comms_noinpstr(inp,1)
  inp1=input("Password:")
  Do_Comms_noinpstr(inp,1)
  while Accs[inp]!=inp1:
    print("Not Logined!")
    inp1=input("Password:")
    Do_Comms_noinpstr(inp,1)
  Psn=inp1
  Lgn=inp
  print("Logined!")

def hp():
  for i in Comms:
    print(str(i)+": "+str(Comms[i]))
def hp_nis():
  for i in Comms_noinpstr:
    print(str(i)+": "+str(Comms_noinpstr[i]))
def prdata(d):
  for i in d:
    print(str(i)+": "+str(d[i]))

"""funcs loc commands"""
def reg():
  global inp
  global inp1
  inp=input("Name:")
  Do_Comms_noinpstr(inp,1)
  while Accs.get(inp)!=None:
    print("Name "+inp+" is be!")
    inp=input("Name:")
    Do_Comms_noinpstr(inp,1)
  register(inp,input("Password (no commands):"))
  print("Register!")

def ns(name):
  if Datas[Psn].get(name)==None:
    Datas[Psn][name]=""
  else:
    print("String "+name+" is be, not added")
    reedit()
def pp(name):
  if Datas[Psn].get(name)!=None:
    print(name+": "+str(Datas[Psn][name]))
  else:
    print("String "+name+" is not be, not printed")
  reedit()
def prall():
  for i in Datas[Psn]:
    print(str(i)+": "+Datas[Psn][i])
  reedit()
def cl(name):
  if Datas[Psn].get(name)!=None:
    Datas[Psn][name]=""
  else:
    print("String "+name+" is not be, not cleared")
  reedit()
def ed(name):
  global inp
  global inp1
  if Datas[Psn].get(name)!=None:
    print('Print "help" to help in commands.')
    while inp!="ex":
      inp=input()
      Do_Comms(inp)
  else:
    print("Not redacted")
    reedit()
def reedit():
  global inp
  global inp1
  inp=input("Name editable string: ")
  Do_Comms_noinpstr(inp,0)
  while Datas[Psn].get(inp)==None:
    print("String is not be")
    inp=input("Name editable string: ")
    Do_Comms_noinpstr(inp,0)
  ed(inp)
def dl(name):
  if Datas[Psn].get(name)!=None:
    Datas[Psn].pop(name)
  else:
    print("String "+name+" is not be, not deleted")
    reedit()
def ex():
  with open('Memories_json.json', 'w', encoding='utf-8') as f:
    json.dump({"Datas":Datas,"Accs":Accs}, f, ensure_ascii=False, indent=2)
  input("Press Enter")
  raise SystemExit(1)
def exlog():
  global inp
  global inp1
  print("Login=1\Register=0")
  if input("0 or 1?(no commands) ")=="0":
    reg()
  else:
    log()
    reedit()


if __name__ == "__main__":
  print('Print "(help)" to help in commands.')
  exlog()