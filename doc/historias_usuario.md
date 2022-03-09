# Diseño de la aplicación

Para redactar las historias de usuario no podemos perder de vista los usuarios candidatos a utilizar el trabajo. Someramente:
1. Periodísta.
2. Programadora.

Las necesidades de cada uno de ellos se detallan en el readme del repositorio.

## Historias de usuario
#### [HU01] Como triubunal tengo que poder leer de forma ordenada y estructurada la memoria (para poder asignarle buena nota al alumno).
(provoca la fase de documentación y análisis)

- De esta HU01 se derivan las issues que correponden a la realización de los capítulos de la memoria y tareas asociadas.

#### [UH02] Como programadora quiero poder trabajar con los datos de mortandad unificados (para poder crear aplicaciones específicas).
(provoca la codificación de la lógica de negocio)

_issues derivadas:_
- El código que se añada al proyecto tiene que cumplir unos estándares (CI lint).
- CI para correr los tests y asegurar la calidad del código.
- Implementar un modelo de datos que satisfaga el dominio del problema.
- Diseñar los estados inválidos del dominio (excepciones).
- Ofrecer todas las variables disponibles.
- Ofrecer la clasificación de todas las enfermedades disponibles.
- Como programadora quiero poder trabajar con datos ordenados y paginados.
- Ofrecer toda la información a través de un servicio restful.
- . . .


#### [UH03] Como periodísta quiero poder predecir la evolución de los fallecimientos de una enfermedad (para poder realizar informes críticos al SNS).
(provoca la codificación de la lógica de negocio)

_issues derivadas:_
- . . .

#### [UH04] Como periodísta quiero poder acceder a una web donde poder interactuar con todos estos datos (para poder escribir mejores artículos).
(no veo que provoque la codificación de la lógica de negocio)

> Esta HU serviría para satisfacer, si lo alcanzo, el último milestone de crear un frontend.
