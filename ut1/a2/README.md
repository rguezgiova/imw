# UT1-A2: Listado de directorios

## 1. Creación del directorio **shared**

Para ello primero en nuestro home de usuario vamos al directorio **webapps**
y dentro de él creamos el directorio **shared**, después de esto, haremos los enlaces simbólicos de los siguientes ficheros dentro de este:
* `/etc/apt/sources.list`
* `/etc/resolv.conf`
* `/etc/bash.bashrc`
* `/proc/cpuinfo`

![Creación directorio shared](img/1.png)

## 2. Activación de la ruta y recarga del servicio

Luego nos a la ruta `/etc/nginx/sites-available/` y añadimos el directorio que acabamos de crear al fichero `alu4240.me`.

![Ruta archivo alu4240.me](img/5.png)

Dentro del fichero añadimos lo siguiete:

![Infomación añadida al fichero](img/2.png)

Finalmente después de esto, recargamos el servicio **nginx** ya que no hace falta hacer enlace simbólico porque ya lo tenemos creado de la activdad anterior, usaremos el siguiente comando para reiniciarlo:

![Recarga del servicio](img/3.png)

## 3. Resultado final

Como resultado al acceder a la página web **http://alu4240.me/shared/** nos saldrá el listado de ficheros creado al principio

![Resultado final página web](img/4.png)
