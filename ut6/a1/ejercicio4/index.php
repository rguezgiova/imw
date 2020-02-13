<!DOCTYPE html>
<html>
<head>
    <title>Tablas</title>
</head>
<body>
<form action="index.php" method="post">
    <table>
        <tr>
            <td>Introduzca el número de filas: </td>
            <td> <input type="text" name="rows" /> </td>
        </tr>
        <tr>
            <td>Introduzca el número de columnas: </td>
            <td> <input type="text" name="columns" /> </td>
        </tr>
        <tr>
            <td> <input type="submit" value="Enviar" /> </td>
        </tr>
    </table>
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
                        echo ("<td> Michi </td>");
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
