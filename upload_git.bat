git add .
git commit -a -m %1
git push -u origin pelican
rem "pelican content -o output -s publishconf.py"
ghp-import output -r origin -b master
git push origin master
git checkout pelican