import os
import sys

def patch_control():
        with open(dir + 'DEBIAN/control', 'r') as f:
                control = f.read()
        control = control.replace(' iphoneos-arm', ' iphoneos-arm64')
        with open(dir + 'DEBIAN/control', 'w') as f:
                f.write(control)


args = sys.argv
deb = args[1]
dir = args[2]
dataf = []
os.system('mkdir ' + dir)
os.system('cp ' + deb + ' ' + dir)
os.system('ar xf ' + dir + deb + ' --output ' + dir)
files = os.listdir(dir)
for file in files:
	dfile = dir + file
	if file.startswith('data'):
		os.system('tar -xf ' + dfile + ' -C ' + dir)
		dataf = os.listdir(dir)
		os.system('mkdir ' + dir + 'var')
		os.system('mkdir ' + dir + 'var/jb')
		for f in dataf:
			if not f.startswith('DEBIAN') and not f.startswith('debian-binary') and not f.startswith('data') and not f.startswith('control') and 'deb' not in f and not f.startswith('var'):
				print(f)
				os.system('mv ' + dir + f + ' ' + dir + 'var/jb/')
		os.system('rm ' + dfile)
	elif file.startswith('control'):
		os.system('mkdir ' + dir + 'DEBIAN')
		os.system('tar -xf ' + dfile + ' -C ' + dir + 'DEBIAN')
		patch_control()
		os.system('rm ' + dfile)
os.system('rm ' + dir + deb)
os.system('dpkg -b ' + dir)

