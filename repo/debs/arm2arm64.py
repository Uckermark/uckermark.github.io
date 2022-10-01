import os
import sys


args = sys.argv
deb = args[1]
path = args[2]
dataf = []

def patch_control():
	print("> patching architecture...")
        with open(path + 'DEBIAN/control', 'r') as f:
		control = f.read()
		control = control.replace(' iphoneos-arm', ' iphoneos-arm64')
	with open(path + 'DEBIAN/control', 'w') as f:
		f.write(control)
	print("> patching architecture... done", end='\r')


def unpack_deb():
	print("> unpacking deb...")
	os.system('mkdir ' + path)
	os.system('dpkg-deb -R ' + deb + ' ' + path)
	os.system('rm ' + path + deb)
	print("> unpacking deb... done", end='\r')


def get_files():
	return os.listdir(path)

def rm_root():
	print("> creating rootless fs...")
	os.system('mkdir ' + path + 'var')
	os.system('mkdir ' + path + 'var/jb')
	print("> creating rootless fs... done", end='\r')
	print("> moving files to rootless...")
	for file in get_files():
		dfile = path + file
		if not "DEBIAN" is in file:
			os.system('mv ' + dfile + ' ' + path + 'var/jb/')
		os.system('rm -r ' + dfile)
	print("> moving files to rootless... done", end='\r')

		
if len(args) == 3:
	unpack_deb()
	rm_root()
	patch_control()
	os.system('dpkg -b ' + dir + ' ' + deb)
else:
	print("Error: 2 arguments expected!")
	print("Usage: arm.py <deb> <tempdir>")

