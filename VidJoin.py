import os, re
import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from shutil import copy

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
		directory = tk.filedialog.askopenfile()
		if pk == 1:
			self.entry_one.config(state='normal')
			self.entry_one.delete(0, 'end')
			self.entry_one.insert('end', directory.name)
			self.entry_one.config(state='readonly')
		elif pk == 2:
			self.entry_two.config(state='normal')
			self.entry_two.delete(0, 'end')
			self.entry_two.insert('end', directory.name)
			self.entry_two.config(state='readonly')
		# FINISH OFF GUI MAKE IT GRID LAYOUT, TAKE THE WHOLE PATH WITH ASKFILE
		# MOVE THE FILE TO THE VIDJOIN DIR AND TRY TO PURGE ALL TEMP FILE AFTER JOIN

	def main(self):
		dir1 = self.entry_one.get()
		dir2 = self.entry_two.get()

		wd = os.path.expanduser('~\Documents\VidJoin')
		if os.path.exists(wd) is False:
			os.mkdir(wd)

		output_name = outname

		ffmpegdir = 'C:\\Program Files\\FFMPEG'
		if os.path.exists(ffmpegdir) is False:
			print('FFMPEG Not detected, please install and place into Program Files to get this to work.\nExample: {}.'.format(ffmpegdir))
		ffmpeg = "C:\\Program Files\\FFMPEG\\bin\\ffmpeg.exe"

		file1_name = dir1.split('\\')[-1]
		file2_name = dir2.split('\\')[-1]
		
		items = get_info(dir1)
		file1_dir = items[0]
		file1_name = items[1]
		self.transport_files(file1_dir, file1_name, wd)

		items = get_info(dir2)
		file2_dir = items[0] 
		file2_name = items[1]
		self.transport_files(file2_dir, file2_name, wd)

		command1 = ffmpeg + ' -i ' + file1_name + ' -c copy -bsf:v h264_mp4toannexb -f mpegts medium1.ts'
		command2 = ffmpeg + ' -i ' + file2_name + ' -c copy -bsf:v h264_mp4toannexb -f mpegts medium2.ts'
		join_command = ffmpeg + ' -i "concat:medium1.ts|medium2.ts" -c copy -bsf:a aac_adtstoasc ' + output_name + '.mp4'

		os.chdir( wd )
		subprocess.call(command1)
		subprocess.call(command2)
		subprocess.call(join_command)

	def transport_files(self, file_dir, file_name, destination):
		os.chdir(file_dir)
		copy(file_name, destination)

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

def run_app():
	app = window()
	app.title('VidJoin')
	app.resizable(False, False)
	app.mainloop()

if __name__ == '__main__':
	run_app()