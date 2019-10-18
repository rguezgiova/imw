# UT1-A4: Sirviendo aplicaciones Php y Python

## Sitio Web 1
Tenemos que acceder a la página **http://php.alu4240.me**, para ello vamos a `/etc/nginx/sites-available` y creamos el fichero **php.alu4240.me** con lo siguiente:

![Creación fichero](img/1.png)

Ahora creamos el enlace del fichero anteriormente creado a `/etc/nginx/sites-enabled` para "activarla".

![Creación enlace](img/2.png)

Creamos en nuestro home de usurio dentro de **webapps** la carpeta `php`, aquí dentro irán los ficheros que compondrán nuestra página.

Lo siguiente es descargar el archivo **demo_php.zip** que lo encontraremos en la práctica, después de descargarlo lo descomprimimos.

![Descarga fichero y descomprimir](img/3.png)

Este es el resultado que se mostrará en nuestra página al acceder.

![Resultado final](img/4.png)

## Sitio Web 2
Para el segundo sitio web tendremos que acceder a la página **http://now.alu4240.me**, como anteriormente nos dirigimos a `/etc/nginx/sites-available`, creamos el fichero **now.alu4240.me** y le añadimos lo siguiente:

![Creación fichero](img/5.png)

Creamos el enlace del fichero anteriormente creado a `/etc/nginx/sites-enabled` para "activarla".

![Creación enlace](img/6.png)

Vamos a nuestro home, dentro de **webapps**, creamos la carpeta `now`, dentro de esta lanzamos los siguiente para crear el entorno virtual que usaremos, primero instalamos **flask**.

![Instalación flask](img/7.png)

Y luego **pytz**.

![Instalación pytz](img/8.png)

Creamos el fichero **main.py** que este nos monstrará el día y la hora de nuestra región geográfica.

![Creación main.py](img/9.png)

Ahora lanzaremos **uwsgi** para comprobar que lo hecho anteriormente funciona.

![Instalación pytz](img/10.png)

Como vemos funciona correctamente, pero lo que queremos es que lo hecho en el paso anterior se produzca automáticamente y no tener nosotros que lanzar el comando cada vez.

![Comprobación 1](img/18.png)

Para que se active automáticamente primero crearemos este script con lo siguiente:

![Creacion scipt](img/11.png)

Le daremos permisos de ejecución al script que acabamos de crear.

![Otorgar permisos](img/12.png)

Usaremos **Supervisor** que es un servicio que hará lo que queremos.

Vamos a los ficheros de configuración personalizados en `/etc/supervisor/conf.d` y ahí creamos **now.conf**, dentro de él escribimos la configuración para lanzar el script creado anteriormente.

![Creacion fichero supervisor](img/13.png)

## Comprobaciones
Ahora comprobaremos lo que hace los siguientes comandos:

El siguiente comando nos muestra el estado de todas las configuraciones creadas en `/etc/supervisor/conf.d`

![Comando status](img/14.png)

El siguiente comando para el fichero **now** que creamos anteriormente.

![Comando stop](img/15.png)

El siguiente comando inicia el fichero **now** que creamos anteriormente.

![Comando start](img/16.png)

El siguiente comando reinicia el fichero **now** que creamos anteriormente.

![Comando restart](img/17.png)
