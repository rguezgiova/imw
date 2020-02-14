<!DOCTYPE html>
<html>
<head>
    <title>Tablas</title>
</head>
<style>
  table td {width: 40px; height: 20px;}
</style>
<body>
<form action="index.php" method="post">
  <p>Introduzca el número de filas: <input type="text" name="rows" /></p>
  <p>Introduzca el número de columnas: <input type="text" name="columns" /></p>
  <p> <input type="submit" value="Enviar" /> </p>
</form>
<table border="1">
    <?php
        if (isset($_POST["rows"]) and isset($_POST["columns"])) {
            $rows = (int)$_POST["rows"];
            $columns = (int)$_POST["columns"];
            $number_rows = 1;
            $number_columns = 1;
            if ($rows >= 1 and $columns >= 1) {
                echo ("<p>$rows filas y $columns columnas.</p>");
                while ($number_rows <= $rows) {
                    $number_rows++;
                    echo("<tr>");
                    while ($number_columns <= $columns) {
                        $number_columns++;
                        echo ("<td></td>");
                    }
                    $number_columns = 1;
                    echo ("</tr>");
                }
            }
            else {
                echo ("<p>Introduzca un valor mayor que 0.</p>");
            }
        }
    ?>
</body>
</html>
