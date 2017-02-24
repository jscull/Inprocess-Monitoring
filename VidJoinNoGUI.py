import os, re
import subprocess

def main(dir1, dir2, outname):
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
	main('C\\B00237_EOL', 'C\\B00237_EOL_1', 'B00237_EOL')