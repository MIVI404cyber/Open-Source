"""
    @ Original Written By Raj
    @ Dont Forget Credit
    @ Github: https://github.com/MIVI404cyber
"""

import os,time
class Convrt:
	def __init__(self):
		self.line=(45*f'-')
		self.logo=('''\n\033[1;31m            ┏┓┏┓┳┓┓┏┏┓┳┓┏┳┓┏┓┳┓\n            ┃ ┃┃┃┃┃┃┣ ┣┫ ┃ ┣ ┣┫\n            ┗┛┗┛┛┗┗┛┗┛┛┗ ┻ ┗┛┛┗\033[0m''')
	def Main(self):
		os.system('clear')
		print(self.logo)
		print(self.line)
		print(f' [1] Convert Headers')
		print(f' [2] Convert Data')
		print(f' [0] Exit Tool')
		print(self.line)
		XX=input(f' [~] Choice Option: ')
		if XX in ['1','a','A']:
			self.Head()
		elif XX in ['2','b','B']:
			self.Data()
		elif XX in ['0','c','C']:
			exit()
		else:
			self.Main()
	def Head(self):
		os.system('clear')
		print(self.logo)
		print(self.line)
		x = int(input(" [~] How Many Lines Of Headers To Add?: "))
		print(self.line)
		fil=input(' [~] Headers Output Path: ')
		print(self.line)
		try:os.remove(fil)
		except:pass
		file=open(fil,'a')
		print("\t    PASTE LINES BELOW")
		print(self.line)
		file.write('#convert by raj\n#dont forget credit\n\nheaders={\n')
		for i in range(x):
			xx = input()
			nk = xx.split(":")[0]
			bk2 = xx.split(":")[1]
			first = f"'{nk}'"
			last = f"'{bk2}'"
			if i+1 == x:file.write('    '+first+str(":")+last+",\n}"+"\n")
			else:file.write('    ' + first + str(":")+last+","+"\n")
		file.close()
		time.sleep(1)
		print(self.line)
		print(f' [~] Headers Convert Successfully ')
		print(self.line)
		input('\n [~] Press Enter To Main Menu')
		self.Main()
	def Data(self):
		os.system('clear')
		print(self.logo)
		print(self.line)
		fil=input(' [~] Data Output Path: ')
		print(self.line)
		try:os.remove(fil)
		except:pass
		file=open(fil,'a')
		file.write('#convert by raj\n#dont forget credit\n\ndata={\n')
		xx = input(' [~] Paste Data: ')
		dd = xx.split('&')
		for x in dd:
			file.write("    '"+x.replace('=',"': '")+"',\n")
		file.write('}')
		file.close()
		print(self.line)
		time.sleep(1)
		print(f' [~] Data Convert Successfully ')
		print(self.line)
		input('\n [~] Press Enter To Main Menu')
		self.Main()
		

if __name__ == '__main__':
	os.system('clear')
	os.system('git pull')
	time.sleep(1)
Convrt().Main()