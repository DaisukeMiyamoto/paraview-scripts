#!/bin/bash -x
PVBATCH=~/bin/ParaView-5.2.0-Qt4-OpenGL2-MPI-Linux-64bit/bin/pvbatch
PVBATCH_OPT="--use-offscreen-rendering --mpi"
SCRIPT=~/git/paraview-scripts/load_items/make_sequential_snapshot.py

for ((i=0; i<200; i=i+1)); do
      $PVBATCH $PVBATCH_OPT $SCRIPT $i 1
done
