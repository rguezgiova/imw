<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Fondo random</title>
    </head>
    <body>
      <?php
          $red = mt_rand(0, 255);
          $green = mt_rand(0, 255);
          $blue = mt_rand(0, 255);
          echo ("<body style='background-color: rgb($red, $green, $blue);'> </body>")
      ?>
    </body>
</html>
