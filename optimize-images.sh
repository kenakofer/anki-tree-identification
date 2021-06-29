#!/bin/bash
MEDIA_DIR="./media"
ORIGINAL_SIZE_DIR="./original-size-media"
IMAGE_MAGICK_OPTIONS='-sampling-factor 4:2:0 -strip -quality 75 -interlace JPEG -colorspace sRGB -resize 700x700>'

type convert >/dev/null 2>&1 || { echo >&2 "I require convert, but it's not installed.  Aborting."; exit 1; }

## For all jpg/JPG files:
find "$MEDIA_DIR" -type f -iname "*.jpg" -print0 | sort -z | while IFS= read -r -d $'\0' file; do
    BASE=`basename "$file"`
    ORIGINAL_SIZE_FILE="$ORIGINAL_SIZE_DIR/$BASE"

    ## Don't reoptimize if we already have a backup from an earlier run of this script
    if [ -e "$ORIGINAL_SIZE_FILE" ]; then
        echo "Skipping $file..."

    else
        echo "Backing up and compressing $file"
        cp "$file" "$ORIGINAL_SIZE_FILE" || exit 1
        rm "$file" || exit 1
        convert $IMAGE_MAGICK_OPTIONS "$ORIGINAL_SIZE_FILE" "$file" || exit 1
    fi
done
