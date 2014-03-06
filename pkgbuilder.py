#!/usr/bin/python env

#subprocess for packaging, optparse for install
import subprocess

#a new version will be come with argparse (supported after python 2.7)
import optparse
from writefile import writeShell
import sys,os
import fileinput

bintype={'sh':'.sh','bin':'.bin','run':'.run'}

def produceScript(path,ftype,src):
    """
     produce compiled script, binary data, cannot be opened
    """
    pkgname=os.path.basename(path)
    tarballname=''.join([pkgname,'.tar.gz'])
    try:
	    subprocess.call(['tar','zcvf',tarballname,path])
    except e:
        print "Unknown error, cannot complie file"

    makeConfig=None
    if src:
        makeConfig=raw_input('Please enter configuration for makefile: ')

    scriptname=writeShell(pkgname,makeConfig,src)
    installfile_name=scriptname[:-3]+'_install'+bintype[ftype]
    with open(installfile_name,'w') as ifn:
        for line in fileinput.input([scriptname,tarballname]):
            ifn.write(line)

    subprocess.call(['rm',tarballname])
    subprocess.call(['rm',scriptname])

def main():
    parser = optparse.OptionParser('usage: %prog '+'-f <target file> -t <type> default="sh" --from-src <True or False>')
    parser.add_option('-f', dest='tgtPath', type='string', help='specify the target file path')
    parser.add_option('-t', dest='compileType', type='string', help='specify the type to complie into',default="sh")
    parser.add_option('--from-src', dest='fromsrc',action="store_true", help='specify whether needs to compile from source code',default=False)
    (options,args) = parser.parse_args()
    path=options.tgtPath
    ftype=options.compileType
    src=options.fromsrc


    if not os.path.exists(path):
        print "Error: Path doesn't exist"
        sys.exit(1)
    if ftype not in bintype:
        print "Error: Can only compile into bin,run or sh"
        sys.exit(1)
	
    try:
        produceScript(path,ftype,src)
    except TypeError:
        print "Error: wrong arguments type"
        parser.print_usage()

if __name__=="__main__":
    main()