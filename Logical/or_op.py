#or operator using different persons

exam=False
sports=True
print("exam : ",exam)
print("sports: ",sports)

#dhoni

dhoni={'exam':True,'sports':True}
print(dhoni)
exam=dhoni['exam']
print(exam)
sports=dhoni['sports']
print(sports)
res=exam or sports
print("dhoni is eligible for gov job: ",res)

#siraj

siraj={'exam':False,'sports':True}
print(siraj)
exam=siraj['exam']
print(exam)
sports=siraj['sports']
print(sports)
res=exam or sports
print("siraj is eligible for gov job: ",res)

#Ansari

Ansari={'exam':True,'sports':False}
print(Ansari)
exam=Ansari['exam']
print(exam)
sports=Ansari['sports']
print(sports)
res=exam or sports
print("Ansari is eligible for gov job: ",res)

#Ganesh

Ganesh={'exam':False,'sports':False}
print(Ganesh)
exam=Ganesh['exam']
print(exam)
sports=Ganesh['sports']
print(sports)
res=exam or sports
print("Ganesh is eligible for gov job: ",res)

