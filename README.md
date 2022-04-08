sudo docker build -t sisedgar/app_pythonedgar:v2 .


docker images
En otra ventana de terminal     sudo docker stats

sudo docker run --rm -p 5000:5000 sisedgar/app_pythonedgar:v2

Mantenerlo corriendo en segundo plano
sudo docker run -d --rm -p 5000:5000 sisedgar/app_pythonedgar:v2

Mantenerlo corriendo en segundo plano pero a los 5000 segundos se cierra
sudo docker run -d -p 5000:5000 sisedgar/app_pythonedgar:v2 sleep 5000

Para convertir una imagen en un contenedor hacemos esto:
sudo docker run -it sisedgar/app_pythonedgar:v2

Ejemplo de editar variables de entorno de un contenedor
docker run -e "APP=PandoraFMS" -e "VER=740" alpine echo "$APP $VER"

Ahora vamos a borrar una imagen asi:
sudo docker rmi images eefc0cb3ada9

En caso de querer saber cuantos contenedores tenemos activos debemos ejecutar este comando:
sudo docker ps

Pero si lo que queremos es ver todos los contenedores activos e inactivos debemos ejecutar:
sudo docker ps -a

Para detener un contenedor que aun este corriendo en docker debemos ejecutar este comando:
sudo docker stop eefc0cb3ada9

De igual forma para arrancar un contenedor detenido debemos ejecutar:
sudo docker start eefc0cb3ada9

Si queremos acceder a nuestro contenedor debemos ejecutar este comando:
sudo docker attach eefc0cb3ada9

Para eliminar un contenedor debemos ejecutar.
sudo docker rm eefc0cb3ada9

