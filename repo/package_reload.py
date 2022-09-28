import os
os.system('dpkg-scanpackages ./debs > Packages')

with open("Packages", 'r') as f:
	packages =  f.read()
packages = packages.replace(" iphoneos-arm", " iphoneos-arm64")
packages = packages.replace("iphoneos-arm6464", "iphoneos-arm64")
os.system('rm Packages')
os.system('touch Packages')
with open("Packages", 'w') as f:
	f.write(packages)
os.system('rm Packages.gz')
os.system('rm Packages.bz2')
os.system('gzip -c9 Packages > Packages.gz')
os.system('bzip2 -c9 Packages > Packages.bz2')
print("finished!")

# TODO: new debs have to change arch to iphoneos-arm64
# deb/control change architecture
