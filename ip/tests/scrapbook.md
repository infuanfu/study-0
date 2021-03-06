## compare mean absolute error of two images, output name of images alongside calculated metric

compare -metric MAE img/black.png img/gray50.png -format "%[d]/%[f] %[o]" null: 2>&1 | tr '\n' ' '

## parse video file into individual images

ffmpeg -i inputfile.avi -f image2 image-%3d.jpeg

## generate pairs of consecutive files to compare

ls > dirlist
len=$(wc -l dirlist)

head -n $(echo $len-1|bc) dirlist > f1
tail -n $(echo $len-1|bc) dirlist > f2
paste f1 f2 >f3


## run commands with param pairs

xargs -0 -I '{}' -n 1 sh -c 'compare -metric MAE $1 -format "%[d]/%[f] %[o]" null: 2>&1 | tr "\n" "\t"' -- {} < <(tr \\n \\0 <f3)

## unpack into individual lines per comparison
xargs -0 -I '{}' -n 1 sh -c 'compare -metric MAE $1 -format "%[d]/%[f] %[o]" null: 2>&1 | tr "\n" "\t"' -- {} < <(tr \\n \\0 <f3) | sed "s/\t\t/\n/g"

## histogram data
http://www.imagemagick.org/Usage/files/#histogram

## get color count
convert  ngeop/image-0002.png  -define histogram:unique-colors=true -format %c histogram:info:-|sort -n|tail -n 4|awk '{print $1 $6}'

## create color patch image
convert -size 200x50 xc:white 
	-fill #color -draw 'rectangle x1,y1 x2,y2'
	-fill #color -draw 'rectangle x1,y1 x2,y2'
	-fill #color -draw 'rectangle x1,y1 x2,y2'
	image.png


sh -c "convert -size 1280x50 xc:black $(convert  frames/00100.png  -colors 16 -define histogram:unique-colors=true -format %c histogram:info:-|sort -rn|../histbin_to_magickdraw.pl) patch.png" && eog patch.png
