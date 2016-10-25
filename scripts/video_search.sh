#!/bin/bash
# Searches for video files recursively from the current folder
# Lists found files in 'search_results'

deps=("mediainfo" "bc")
dpkg -s "${deps[@]}" >/dev/null 2>&1 || { echo "To install needed packages please run: apt-get install ${deps[@]}"; exit; }

fnum=$(find . -type f | wc -l)
fcur=0
count=0

echo "Looking through $fnum files"
> "search_results"

for f in `find . -type f`
do
 	let "fcur++"
	prog=$(echo "scale=2; ($fcur/$fnum)*100" | bc -l)
	echo -ne "$prog%%\r"

	ret=$(mediainfo $f 2>/dev/null | grep "Video")
	if [ "$ret" != "" ]
		then
			echo -e "\\n$f"
			echo "$f" >> "search_results"
			let "count++"
	fi
done
echo "Found $count video files"
