#bin/bash
dpkg-scanpackages repo/debs > repo/Packages
rm repo/Packages.gz
rm repo/Packages.bz2
gzip -c9 repo/Packages > repo/Packages.gz
bzip2 -c9 repo/Packages > repo/Packages.bz2
echo 'sucess!'
