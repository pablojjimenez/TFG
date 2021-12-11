#!/bin/sh

xelatex proyecto.tex
biber proyecto
xelatex proyecto.tex