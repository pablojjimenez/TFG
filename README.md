# Trabajo de Fin de Grado: *Computación y optimización en la nube: implementación de aplicaciones de datos abiertos en la nube*
---------
### Autor: [👨🏻‍💻 Pablo Jiménez Jiménez](https://github.com/pablojj1808)
### Tutor: [👨🏻‍💻 Juan Julian Merelo Guervos](https://github.com/JJ)
---------


## Documentation section
In `doc/` directory:

### Using your own Texlive distribution
You have to build the PDF file using a `TeXLive` distribution. Once it is installed you can execute the following commands:

``` sh
$ pdflatex proyecto.tex
$ bibtex proyecto
$ make
```

### Using Docker
Use theses steps for compiling using docker image.
```sh
./latexdockercmd.sh pdflatex proyecto.tex
```

Cleaning
```sh
make
```

------
[Inspired by this template](https://github.com/JJ/plantilla-TFG-ETSIIT)
