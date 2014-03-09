#!/bin/sh
# generates a list of pairs of consecutive files (alphabetical sorting)
# this list can be used as parameters to eg compare consecutive frames in a later step
#
# usage:
# 	mk_consecutive_frame_list.sh tests/frames
#

DIRLIST=$(mktemp)
FIRST=$(mktemp)
SECOND=$(mktemp)
PAIRS=$(mktemp)

echo ${DIRLIST} ${FIRST} ${SECOND} ${PAIRS}

find $1 -name '*png' |sort > ${DIRLIST}
len=$(cat ${DIRLIST} | wc -l)

head -n $(echo "${len}-1"|bc) ${DIRLIST} > ${FIRST}
tail -n $(echo "${len}-1"|bc) ${DIRLIST} > ${SECOND}
paste ${FIRST} ${SECOND} >${PAIRS}

cat ${PAIRS}

rm ${DIRLIST} ${FIRST} ${SECOND} ${PAIRS}
