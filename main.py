from time import time as t
from time import sleep as slp
from random import randint as r
from os import system as s
import json

def Generate(type,size,length):
	q = ""
	if type == "add":
		for i in range(length):
			q += str(r(1,size))
			if i != length-1:
				q += " + "
		return (q,eval(q))
	elif type == "sub":
		for i in range(length):
			q += str(r(1,size))
			if i != length-1:
				q += " - "
		return (q,eval(q))
	elif type == "mult":
		for i in range(length):
			q += str(r(1,size))
			if i != length-1:
				q += " * "
		return (q,eval(q))
	elif type == "div":
		nlist = []
		for i in range(length):
			l = True
			while l:
				a = str(r(1,size))
				if len(nlist) != 0:
					if (int(nlist[-1]) % int(a) == 0):
						l = False
						nlist.append(a)
				else:
					l = False
					nlist.append(a)

		for j in range(len(nlist)):
			q += str(nlist[j])
			if j != len(nlist)-1 :
				q += " / "
		return (q,eval(q)) 

default = {"size": 15,
		   "noOfQuestions": 10,
		   "length":2
		  }
type = ["add","sub","mult","div"]
settings = {}

inkey = input("Press [any] to start and [r] to reset.  ")
if inkey == "r":
	with open("settings.json",'w') as f:
				json.dump(default,f)


with open("settings.json",'r') as f:
	settings = json.load(f)


for i in range(settings["noOfQuestions"]):
	rtype = type[r(0,len(type)-1)]
	qset = Generate(rtype,settings["size"],settings["length"])
	print(qset[0])
	time = t()
	answer = float(input("Answer:"))
	time = t() - time
	if answer == float(qset[1]):
		print("Correct!, Time Taken:"+str(time))
	else:
		print("Wrong!, Correct Answer:"+str(qset[1]))

	slp(3)
	s("clear")




