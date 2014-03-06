#!/usr/bin/python env
#Write the install shell script

import string

def writeShell(s):
    script=string.Template("""#!/bin/bash
tmpdir=$$(pwd)
sed -n -e '1,/^exit 0$$/!p' $$0> "$${tmpdir}/${name}.tar.gz" 2>/dev/null
cd $$tmpdir
tar zxvf ${name}.tar.gz
rm ${name}.tar.gz
exit 0
""")
    filename=s
    scriptname=''.join([filename,'.sh'])
    f=open(scriptname,'w')
    f.write(script.substitute(name=filename))
    f.close()
    return scriptname
