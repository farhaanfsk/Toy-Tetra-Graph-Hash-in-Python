from posixpath import split
import textwrap
import numpy as np

#assign values
char={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
num={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25 }


 


def menu():
	print("\n Toy Tetra Graph Hash")
	print("-----------------------\n")
	msg=input("enter the message :")
	hashing(msg)
	

def hashing(msg):
	arr = textwrap.fill(msg, 16)
	arr = arr.split("\n")
	temp = [0,0,0,0]

	for i in arr:
		matriz = pre_processing(i)
		t1 = round1(matriz)
		t2 = round2(matriz)
		temp = hash(t1,t2,temp[0])
	
	print(temp[1])


def pre_processing(msg):
	l=len(msg)
	if(l<16):
		for i in range(l,16):
			msg = msg + 'a'
	arr = np.array([[]])

	for i in msg:
		arr = np.append(arr,num[i])

	a=arr.reshape(4,4)
	return a

def round1(matriz):
																		#round1
	print("\nThe value after round1 is : \n")
	t1=matriz.sum(axis=0)%26
	print(t1)
	return t1


def round2(matriz):
																		#round2
	c1 = c2 = c3 = c4 = matriz
	c1=np.roll(c1[0],3)
	c2=np.roll(c2[1],2)
	c3=np.roll(c3[2],1)
	c4=np.fliplr(c4)
	c4=np.roll(c4[3],4)

	t2=(c1+c2+c3+c4)%26
	print("\nThe value after round2 is :\n")
	print(t2)
	return t2
                                                                       #Hash calculation
def hash(t1, t2, temp):
	t=(t1+t2)%26
	t=(t+temp)%26
	a2 = np.array([])
	for i in t:
		a2 = np.append(a2,char[i])
	return [t, a2]



menu()