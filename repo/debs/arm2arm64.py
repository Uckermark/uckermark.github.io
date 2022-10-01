import os
import sys


args = sys.argv
if len(args) == 2:
	deb = args[1]
path = "tmp-arm2arm64/"

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
	os.system('dpkg-deb -R ' + deb + ' ' + path + ' 1> /dev/null')
	print("> unpacking deb... done", end='\r')


def get_files():
	return os.listdir(path)

def rm_root():
	print("> creating rootless fs...")
	os.system('mkdir ' + path + 'var 2> /dev/null')
	os.system('mkdir ' + path + 'var/jb 2> /dev/null')
	print("> creating rootless fs... done", end='\r')
	print("> moving files to rootless...")
	for file in get_files():
		dfile = path + file
		if not "DEBIAN" in file and not "var" in file:
			os.system('mv ' + dfile + ' ' + path + 'var/jb/')
			os.system('rm -r ' + dfile)
	print("> moving files to rootless... done", end='\r')


if len(args) == 2:
	unpack_deb()
	rm_root()
	patch_control()
	os.system('dpkg -b ' + path + ' ' + deb + ' 1> /dev/null')
	os.system('rm -r ' + path)
else:
	print("Error: 1 arguments expected!")
	print("Usage: arm.py <deb>")
