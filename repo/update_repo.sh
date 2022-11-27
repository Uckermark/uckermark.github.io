#bin/bash
cd repo/debs/
dpkg-scanpackages debs > ../Packages
cd ..
rm Packages.gz
rm Packages.bz2
gzip -c9 Packages > Packages.gz
bzip2 -c9 Packages > Packages.bz2
echo 'sucess!'
