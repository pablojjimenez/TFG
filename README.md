# Trabajo de Fin de Grado: *Computación y optimización en la nube: implementación de aplicaciones de datos abiertos en la nube*


| Autor | Tutor |
|:---:|:---:|
| [Pablo Jiménez Jiménez](https://github.com/pablojj1808) | [Juan Julian Merelo Guervos](https://github.com/JJ) |




## Generación de documentación
Dentro del directorio `doc/`:

### Usando tu propia distribución Texlive
Para construir tu PDF usando tu distribución `TeXLive` instalada sigue los siguientes comandos:

``` sh
$ pdflatex proyecto.tex
$ bibtex proyecto
$ make
```

### Usando una imagen Docker
Ejecuta este comando en la terminal.
```sh
./latexdockercmd.sh pdflatex proyecto.tex
```

Para limpiar ficheros de compilación
```sh
make
```

## License

Este proyecto está publicado bajo la licencia [GNU General Public License v3](https://opensource.org/licenses/GPL-3.0)

------
[Inspirado en esta plantilla](https://github.com/JJ/plantilla-TFG-ETSIIT)
