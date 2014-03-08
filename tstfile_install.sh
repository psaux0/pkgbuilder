#!/bin/bash
tmpdir=$(pwd)/tmp_dir
mkdir $tmpdir
sed -n -e '1,/^exit 0$/!p' $0> "${tmpdir}/tstfile.tar.gz" 2>/dev/null
cd $tmpdir
tar zxvf tstfile.tar.gz
rm tstfile.tar.gz                
./configure l
make
make install
make clean
echo "${tmpdir} can be removed"                               
exit 0
� 8S ��M
� @a�����'�
]�h��o�m�-.t����<����v_/j �&1��h�݆P�e�7ɋHp�X��S:�\�k�eٴV���ϟ��-�Xh���_�8���_��D����N�o�ø]����Lr����o�����L�=�g8��q3����_�?��ߏ���_��?�          z� ���p (  