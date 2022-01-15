#Easter egg program 
import sys
fname = input('Enter a file name: ')
if fname == 'na na boo boo':
  print('%s - You have been punked'%(fname.upper()))
  sys.exit()

try:
	fhandle = open(fname)
except FileNotFoundError:
	print('File cannot be found')
	sys.exit(1)

count = 0
for line in fhandle:
  count += 1
print('There were %d subject lines in %s'%(count, fname))
