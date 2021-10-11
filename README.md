# Trabajo de Fin de Grado: *Computación y optimización en la nube: implementación de aplicaciones de datos abiertos en la nube*


| Autor | Tutor |
|:---:|:---:|
| [Pablo Jiménez Jiménez](https://github.com/pablojj1808) | [Juan Julian Merelo Guervos](https://github.com/JJ) |

## Motivación
Se quiere conocer de forma clara y concisa las causas de fallecimiento, en función de distitos factores (geográficos, género, fecha, edades), para poder predecir a futuro la evolución de la población y poder mejorar la toma de decisiones, como la realización de cribados más inteligentes en el SNS u otros cuerpos competentes.


## Objetivos
Mejorar el entendimiento de los datos recogidos sobre defunciones en España según causa de muerte. Lo que puede ayudar a la mejora de la vida de las personas, conectando esta fuente de iformación a otras que desbordan el objetivo de este trabajo.

### ¿Cómo?
Mediante técnicas estadísticas y computacionales que nos permiten extraer información de los datos almacenados.

1. **Mediante la visualización dinámica de datos:** que nos permite comunicar de forma sencilla y visual la información a través de gráficos.

2. **Mediante el cálculo de medidas estadísticas centralizadas.**

3. **Mediante posibles predicciones futuras.**

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
