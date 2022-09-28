import os
os.system('dpkg-scanpackages ./debs > Packages')
os.system('rm Packages.gz')
os.system('rm Packages.bz2')
os.system('gzip -c9 Packages > Packages.gz')
os.system('bzip2 -c9 Packages > Packages.bz2')
print("finished!")
