#!/bin/sh

if [ $# -lt 2 ]; then
    echo Usage: $0 INPUTDIR OUTPUTDIR
    exit 2
fi

INPUTDIR=$1
OUTPUTDIR=$2

if [ ! -d $OUTPUTDIR ]; then
    mkdir $OUTPUTDIR
fi

for htmlfiles in $(ls $INPUTDIR/*); do
    OUTPUTFILE=$(basename $htmlfiles | perl -pe 's/.*\.\K.*/org/g')
    pandoc -f html -t org $htmlfiles -o $OUTPUTDIR/$OUTPUTFILE
done
