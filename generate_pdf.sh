#!/bin/sh

xelatex doc/proyecto.tex
biber proyecto
xelatex doc/proyecto.tex