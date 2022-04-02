# Pasos para el diseño de la arquitectura software

## DDD
### Domain
Quiero programar con las mejores prácticas de diseño posibles teniendo en mente siempre el princpio de **diseño dirigido por el dominio**. 

He programado las **entidades** del problema que mantendrán su identidad a lo largo del ciclo de vida y los **objeto-valor** que no son más que objetos asigandos a un atriubuto de las entidades. Tienen también un papel fundamental porque pueden servir para gestionar todo el conjunto de objetos.
De esta primera parte del diseño se obtienen los tests del dominio que verifican su integridad y sus estados inválidos (normalmente mediante el uso de excepciones)

### Repositorios
Nuestras entidades nunca van a ser útiles en solitoria sino que normalmente las aplicaciones almancenan colecciones interelacionadas de estas. El concepto de **repositorio** sirve para abstraer las operaciones específicas de infraestructura de como se listan las colecciones de datos con la BBDD y sirven de *contrato* para acceder a las colecciones de datos.
Este concepto es fundamental junto con la inyección de dependencias para escribir y mockear tests correctamente.

### Servicios
En la mayoría de problemas necesitamos realizar operaciones que no pertenecen conceptualmente a ningún modelo del dominio específico. La capa de servicio es el lugar para realizar normalmente este tipo de operaciones.
Suelen tener inyectado los repositorios de los modelos que necesitan acceder. 


## Referencias

- [Apply Domain-Driven Design to microservices architecture](https://www.ibm.com/garage/method/practices/code/domain-driven-design/)
- [Domain Driven Design: principios, beneficios y elementos](https://medium.com/@jonathanloscalzo/domain-driven-design-principios-beneficios-y-elementos-primera-parte-aad90f30aa35)
- [JJ Curso-tdd](https://github.com/JJ/curso-tdd/blob/master/temas/dise%C3%B1o.md)