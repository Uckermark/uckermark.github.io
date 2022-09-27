import os

os.system('dpkg-scanpackages ./Files > Packages')

with open("Packages", 'r') as f:
	packages =  f.read()
packages = packages.replace("iphoneos-arm", "iphoneos-arm64")
# print(var)
os.system('rm Packages')
os.system('touch Packages')
with open("Packages", 'w') as f:
	f.write(packages)
print("Success!")
