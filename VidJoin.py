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

		l = ttk.Label(self, text='Video 1: ')
		l.grid(row=0, column=0, padx=2, pady=5)
		self.entry_one = ttk.Entry(self, width=50)
		self.entry_one.config(state='readonly')
		self.entry_one.grid(row=0, column=1, padx=2, pady=5)
		self.button_one = ttk.Button(self, text='...', command=lambda pk=1: self.get_dir(pk))
		self.button_one.grid(row=0, column=2, padx=2, pady=5)

		l = ttk.Label(self, text='Video 2: ')
		l.grid(row=1, column=0, padx=2, pady=5)
		self.entry_two = ttk.Entry(self, width=50)
		self.entry_two.config(state='readonly')
		self.entry_two.grid(row=1, column=1, padx=2, pady=5)
		self.button_two = ttk.Button(self, text='...', command=lambda pk=2: self.get_dir(pk))
		self.button_two.grid(row=1, column=2, padx=2, pady=5)

		self.run = ttk.Button(self, text='Join Videos', command=self.main)
		self.run.grid(row=2, column=1, padx=2, pady=5)

	def get_dir(self, pk):
		directory = tk.filedialog.askdirectory()
		if pk == 1:
			self.entry_one.config(state='normal')
			self.entry_one.delete(0, 'end')
			self.entry_one.insert('end', directory)
			self.entry_one.config(state='readonly')
		elif pk == 2:
			self.entry_two.config(state='normal')
			self.entry_two.delete(0, 'end')
			self.entry_two.insert('end', directory)
			self.entry_two.config(state='readonly')
		# FINISH OFF GUI MAKE IT GRID LAYOUT, TAKE THE WHOLE PATH WITH ASKFILE
		# MOVE THE FILE TO THE VIDJOIN DIR AND TRY TO PURGE ALL TEMP FILE AFTER JOIN

	def main(self):
		dir1 = self.entry_one.get()
		dir2 = self.entry_two.get()

		output_name = outname
		ffmpeg = "C:\\Program Files\\FFMPEG\\bin\\ffmpeg.exe"
		#command  = 'copy /b "{}" + "{}" {}.mp4'.format(dir1, dir2, output_name)

		file1_name = dir1.split('\\')[-1]
		file2_name = dir2.split('\\')[-1]
		
		items = get_info(dir1)
		file1_dir = items[0]
		file1_name = items[1]

		items = get_info(dir2)
		file2_dir = items[0]
		file2_name = items[1]

		command1 = ffmpeg + ' -i ' + file1_name + ' -c copy -bsf:v h264_mp4toannexb -f mpegts medium1.ts'
		command2 = ffmpeg + ' -i ' + file2_name + ' -c copy -bsf:v h264_mp4toannexb -f mpegts medium2.ts'
		join_command = ffmpeg + ' -i "concat:medium1.ts|medium2.ts" -c copy -bsf:a aac_adtstoasc ' + output_name + '.mp4'

		os.chdir('C:\\Users\\Jscull\\Documents\\VidJoin')
		print('Command 1: {}.'.format(command1))
		print('Command 2: {}.'.format(command2))
		print('Command 3: {}.'.format(join_command))
		subprocess.call(command1)
		subprocess.call(command2)
		subprocess.call(join_command)

	def get_info(dir):
		path = ''
		file_name = ''
		dir_split = dir.split('\\')
		print('Dir_split: {}.'.format(dir_split))
		for count, segment in enumerate(dir_split):
			print('Segment: {}'.format(segment))
			if count == len(dir_split)-1:
				file_name = segment
			else:
				path += segment
		items = [path, file_name]
		return items

if __name__ == '__main__':
	