#!/usr/bin/python env

#subprocess for packaging, optparse for install
import subprocess
import optparse
from writefile import writeShell
import sys
import fileinput

pkgname=sys.argv[1]
tarballname=''.join([pkgname,'.tar.gz'])
subprocess.call(['tar','zcvf',tarballname,pkgname])

scriptname=writeShell(pkgname)
installfile_name=scriptname[:-3]+'_install.sh'
with open(installfile_name,'w') as ifn:
    for line in fileinput.input([scriptname,tarballname]):
        ifn.write(line)

subprocess.call(['rm',tarballname])
subprocess.call(['rm',scriptname])

