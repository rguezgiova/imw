<!doctype html>
<html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Salario</title>
    </head>
    <body>
        <?php
            $name = $_POST["nombre"];
            $surname = $_POST["apellido"];
            $salary = $_POST["salario"];
            $age = $_POST["edad"];
            if (($salary >= 1000) and ($salary <= 2000)) {
                if ($age >= 45) {
               	    $totalsalary = $salary * 1.03;
                }
                else {
                    $totalsalary = $salary * 1.10;
                }
                echo ("$surname, $name tiene $age años y cobrará $totalsalary €");
            }
            elseif ($salary < 1000) {
                if ($age < 30 ) {
                    $totalsalary = 1100;
                }
                elseif ($age >= 30 and $age <= 45) {
                    $totalsalary = $salary * 1.03;
                }
                else {
                    $totalsalary = $salary * 1.15;
                }
                echo ("$surname, $name tiene $age años y cobrará $totalsalary €");
            }
            elseif ($salary > 2000){
                echo ("$surname, $name tiene $age años y cobrará $salary €");
            }
        ?>
    </body>
</html>
