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

### Extras


