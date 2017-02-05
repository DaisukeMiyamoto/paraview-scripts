#!/bin/bash -x

BLENDER=~/bin/blender-2.78a-linux-glibc211-x86_64/blender
BLENDER_OPT=--background

IMPORT_PYTHON=~/git/paraview-scripts/blender/import_x3d.py
EXPORT_FILENAME=~/work/blender/batch20170201.blend
IMAGE_FILENAME=~/work/blender/render20170127/frame####.png

${BLENDER} ${BLENDER_OPT} --python ${IMPORT_PYTHON} -- ${EXPORT_FILENAME}
${BLENDER} ${BLENDER_OPT} ${EXPORT_FILENAME} -o ${IMAGE_FILENAME} -j 10 -a

