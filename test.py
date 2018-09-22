#!/usr/bin/python3

def getSnack():
	return input("Snack: ")

def z1():
	print(getSnack()+getSnack())

def z2():
	bill=int(input("Wprowadź kwotę z rachunku: "))
	print("Napiwki: \t"+str(bill*0.15)+"\t"+str(bill*0.2))

z2()
