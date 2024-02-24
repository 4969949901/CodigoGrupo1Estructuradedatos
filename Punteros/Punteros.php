<?php


// Definimos una función que modifica el valor de una variable usando una referencia
function modificar(&$variable, $nuevo_valor)
{
    $variable = $nuevo_valor;
}

// Definimos una variable
$mi_variable = 10;

// Imprimimos el valor original
echo "Valor original de mi_variable: " . $mi_variable . "<br>";

// Llamamos a la función modificar para cambiar el valor de la variable
modificar($mi_variable, 20);

// Imprimimos el nuevo valor
echo "Nuevo valor de mi_variable después de modificar: " . $mi_variable . "\n";


