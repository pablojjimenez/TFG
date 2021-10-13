# Trabajo de Fin de Grado: *Computación y optimización en la nube: implementación de aplicaciones de datos abiertos en la nube*


| Autor | Tutor |
|:---:|:---:|
| [Pablo Jiménez Jiménez](https://github.com/pablojj1808) | [Juan Julian Merelo Guervos](https://github.com/JJ) |

## Motivación
Quiero saber como han evolucionado las causas de muerte de la población para ayudar a que el SNS se adapte a estos cambios y sea capaz de realizar cribados preventivos más inteligentes para mejorar la calidad de vida de las personas.

## Objetivos
Crear un sistema que sea capaz de extraer, transformar y cargar los datos de los que disponemos. 

1. El sistema ha de realizar **una visualización dinámica de datos:** que nos permita comunicar de forma sencilla y visual la información a través de gráficos.

2. **Calcular medidas estadísticas centralizadas.**

3. **Realizar posibles redicciones futuras.**

Todo esto será ofrecido por un sistema web escalable dando la posibilidad de ser personalizado por el usuario así como incluir una API que pueda ser usada por usuarios más avanzdos. 



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
