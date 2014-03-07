#!/usr/bin/python env
#Write the install shell script

import string

scripts={
    "non_src":string.Template("""#!/bin/bash
tmpdir=$$(pwd)
sed -n -e '1,/^exit 0$$/!p' $$0> "$${tmpdir}/${name}.tar.gz" 2>/dev/null
tar zxvf ${name}.tar.gz
rm ${name}.tar.gz
exit 0
"""),
    "with_src":string.Template("""#!/bin/bash
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
echo "$${tmpdir} can be removed"                               
exit 0
""")
}

def writeShell(s,**kargs):
    """
     Write the part for installation of a script
    """
    filename=s
    scriptname=''.join([filename,'.sh'])
    f=open(scriptname,'w')
    r={'name':filename,'config':config}
    if src:
        f.write(scripts['with_src'].substitute(r))
    else:
        f.write(scripts['non_src'].substitute(name=r['name']))
    f.close()
    return scriptname
