while read line ; do

	ary=( $(echo ${line} | sed 's/\./ /g') )

	echo ${ary[0]}${ary[1]}

	echo ${ary[0]:0:1}${ary[1]}

	echo ${ary[0]}${ary[1]:0:1}

	echo ${ary[0]}.${ary[1]}

done < names.txt
