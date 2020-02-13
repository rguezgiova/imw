<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Michis random</title>
    </head>
    <body>
        <?php
            $number = rand(1, 2);
            if($number == 1){echo '<img src="img/michi1.jpg"/>';}
            if($number == 2){echo '<img src="img/michi2.jpg"/>';}
        ?>
    </body>
</html>
