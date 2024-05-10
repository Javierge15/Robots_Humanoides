# ROBOTS HUMANOIDES
Este repositorio se empleará para subir el proyecto realizado de la asignatura 'Robots Humanoides', del Máster en Robótica y Automatización en la UC3M.

## ENTREGABLE
El entregable consiste principalmente en modificar el tamaño del robot, teniendo en cuenta el apellido del alumno y a partir de ahí hacer que camine de manera correcta modificando algunos parámetros del código proporcionado. Se deberá corregir el avance del robot tanto en el plando **sagital** como en el plano **frontal**.

## PROCEDIMIENTO
### Modificación del tamaño del robot
Para la realización del trabajo será necesario modificar el valor de `HEIGHT`:
```bash
HEIGHT = 0.2 * len("SustituyeEstoPorTuPrimerApellido")
```
Que en mi caso será:
```bash
HEIGHT = 0.2 * len("Gomez")
```
Dando como resultado `HEIGHT = 1`

### Primer 1/12 - Avance en el plano SAGITAL
Script disponible [AQUI](Sagital_JGE.py)

Se han realizado cambios en los parámetros `self.zmp_x`, `self.zmp_x_change`, y parámetros de visualización.

El video se puede ver en el siguiente enlace [VIDEO PLANO SAGITAL](https://youtu.be/qRpz5R4lhLk)

### Segundo 1/12 - Avance en el plano FRONTAL
Script disponible [AQUI](Frontal_JGE.py)

Se han realizado cambios en los parámetros `self.zmp_y`, `self.zmp_time_change`, y parámetros de visualización.

El video se puede ver en el siguiente enlace [VIDEO PLANO SAGITAL](https://youtu.be/h9Fzvx-ElCU)

## EXTRAS
Los extras realizados son los siguientes:
- GitHub con la documentación y el procedimiento del trabajo realizado.
- Videos subidos a YouTube
- Plano sagital con la gravedad de la Luna
- Plano frontal con la gravedad de Júpiter

### - Plano sagital con la gravedad de la Luna
La gravedad en la Luna es aproximadamente 1/6 de la gravedad en la Tierra. Esto significa que la gravedad en la Luna es alrededor de 1.63 m/s².

Se ha cambiado el parámetro `G` al valor `G = 1.63`

Esto hace que todos los otros parámetros tengan que cambiar también para mantener el equilibrio del robot.

Script disponible [AQUI](Sagital_Luna_JGE.py)

El video se puede ver en el siguiente enlace [VIDEO PLANO SAGITAL LUNA](https://youtu.be/aZsN3ZFZQcE)


### - Plano frontal con la gravedad de Júpiter
Júpiter, el planeta más grande de nuestro sistema solar, tiene una gravedad aproximadamente 2.5 veces mayor que la de la Tierra. Esto significa que la gravedad en Júpiter es de alrededor de 24.5 m/s².

Se ha cambiado el parámetro `G` al valor `G = 24.5`

Esto hace que todos los otros parámetros tengan que cambiar también para mantener el equilibrio del robot.

Script disponible [AQUI](Frontal_Jupiter_JGE.py)

El video se puede ver en el siguiente enlace [VIDEO PLANO FRONTAL JUPITER](https://youtu.be/r8oo8D7KRpk)

