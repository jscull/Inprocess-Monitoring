import os, re
import shutil
import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

class window(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		tk.Tk.iconbitmap(self,default="C:/Users/jscull/Documents/code/MasterEmboss/lib/hieta_icon.ico")

		l = ttk.Label(self, text='Directory to Fix: ')
		l.pack(side='left', padx=2, pady=5)
		self.dir = ttk.Entry(self, width=50)
		self.dir.config(state='readonly')
		self.dir.pack(side='left', padx=2, pady=5)
		self.button = ttk.Button(self, text='...', command=self.get_dir)
		self.button.pack(side='left', padx=2, pady=5)
		self.start = ttk.Button(self, text='Fix!', command=lambda path=self.dir.get(): self.fix_dir(path))
		self.start.pack(side='left', padx=2, pady=5)
		self.end = ttk.Button(self, text='Quit', command=self.quit)
		self.end.pack(side='left', padx=2, pady=5)

	def get_dir(self):
		directory = tk.filedialog.askdirectory()
		self.dir.config(state='normal')
		self.dir.delete(0, 'end')
		self.dir.insert('end', directory)
		self.dir.config(state='readonly')

	def quit(self):
		self.destroy()

	def fix_dir(path):
		global wd
		wd = path
		print('Path: {}.'.format(path))
		items = os.listdir(path)
		old_items = [item for item in items]
		pattern = re.compile('[0-9]+')
		for count, item in enumerate(items):
			match = pattern.search(item)
			if match:
				num = match.group(0)
				try:
					match = pattern.search(items[count+1])
				except IndexError:
					break
				next_num = match.group(0)
				returned = is_consistent(num, next_num)
				if isinstance(returned, int):
					items = decrement_files(next_num, items, returned)
					#decrement_files(next_num, items, returned)
			else:
				print('Not matched, maybe found a DIR.')
		rename_items(items, old_items)

	def is_consistent(num1, num2):
		num1 = int(num1)
		num2 = int(num2)
		if num1 + 1 == num2:
			return 'Yes'
		else:
			inc = 2
			while True:
				if inc > 200:
					break
				if num1 + inc == num2:
					break
				else:
					inc += 1
			print('Difference of: {}.'.format(inc))
			return inc - 1

	def decrement_files(start_num, items, decrement):
		cached_num = ''
		index = 0

		for count, item in enumerate(items):
			if start_num in item:
				index = count
				break

		for i in range(index, len(items)):
			pattern = re.compile('[0-9]+')
			match = pattern.search(items[i])

			cur_num = int(match.group(0))

			if i != index:
				returned = is_consistent(cached_num, cur_num)
				if isinstance(returned, int):
					decrement = returned

			cached_num = cur_num
			newnum = cur_num - decrement

			new_file = items[i].replace(str(cur_num), str(newnum))
			items[i] = items[i].replace(str(cur_num), str(newnum))

		return items

	def rename_items(items, old_items):
		print('Items: {}.'.format(items))
		print('Backup: {}.'.format(old_items))
		nd_temp = wd.split('\\')
		nd_temp[-1] = nd_temp[-1]+' - Fixed'
		nd = '\\'.join(nd_temp)
		if os.path.exists(nd) is False:
			os.mkdir(nd)

		for i in range(0, len(items)):
			#os.rename(os.path.join(wd, old_items[i]), os.path.join(nd, items[i]))
			os.rename((wd+'\\'+old_items[i]), (nd+'\\'+items[i]))

def run_app():
	app = window()
	app.title('Fix My Dir!')
	app.resizable(False, False)
	app.mainloop()	

if __name__ == '__main__':
	run_app()