
# importing module
from pandas import *
import csv
amount =5
price =2

with open('names3.csv', 'w', newline='') as csvfile:
						fieldnames = ['Size', 'Amount','price','total']
						writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
						writer.writeheader()
						#writer.writerow({'Size': 'small', 'Amount': amount,'price':price})
						while True:
							print("welcome to our Asp Shop")

							#print("3-Exit")
							print("=========================")
							# choise= int(input("Enter your choise "))
							# mydic = {}
							my_dict = {'1-small':5 , '2-medium':10,'3-large':15}
							print(my_dict)
							choise= int(input("Enter your choise "))
							
							if(choise==1):
								amount= int(input("Enter the amount  "))
								price=(amount*my_dict['1-small'])
								print(price)
								writer.writerow({'Size': 'small', 'Amount': amount,'price':price})
							if(choise==2):
								amount= int(input("Enter the amount  "))
								price=(amount*my_dict['2-medium'])
								print(price)
								writer.writerow({'Size': 'medium', 'Amount': amount,'price':price})
							if(choise==3):
								amount= int(input("Enter the amount  "))
								price=(amount*my_dict['3-large'])
								print(price)
								writer.writerow({'Size': 'large', 'Amount': amount,'price':price})
							if(choise==4):
								print("bye")
								csvfile.close()
								
								data = read_csv("names3.csv")
 
# converting column data to list
							
								fc = data['price'].tolist()
								
								print('total', fc)
								sum = 0
								for x in fc:
									sum = sum + x

								print(sum)
								data = read_csv("names3.csv")
								data['tota']=sum
								exit()
								

				