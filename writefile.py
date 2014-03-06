#!/usr/bin/python env
#Write the install shell script

import string

def writeShell(s,config,src):
    """
     Write the part for installation of a script
    """
    script=string.Template("""#!/bin/bash
tmpdir=$$(pwd)
sed -n -e '1,/^exit 0$$/!p' $$0> "$${tmpdir}/${name}.tar.gz" 2>/dev/null
tar zxvf ${name}.tar.gz
rm ${name}.tar.gz
exit 0
""")
    src_script=string.Template("""#!/bin/bash
tmpdir=$$(pwd)/tmp_dir
mkdir $$tmpdir
sed -n -e '1,/^exit 0$$/!p' $$0> "$${tmpdir}/${name}.tar.gz" 2>/dev/null
cd $$tmpdir
tar zxvf ${name}.tar.gz
rm ${name}.tar.gz                
./configure $config
make
make install
make clean
echo "${tmpdir} can be removed"                               
exit 0
""")
    filename=s
    scriptname=''.join([filename,'.sh'])
    f=open(scriptname,'w')
    r={'name':filename,'config':config}
    if src:
        f.write(src_script.substitute(r))
    else:
        f.write(script.substitute(name=r['name']))
    f.close()
    return scriptname
