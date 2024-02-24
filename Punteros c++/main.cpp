#include <iostream>

int main() {
    // Puntero a entero
    int numero = 10;
    int *puntero_entero = &numero;

    // Puntero a double
    double decimal = 3.14;
    double *puntero_double = &decimal;

    // Puntero a string
    std::string cadena = "Hola, mundo!";
    std::string *puntero_string = &cadena;

    // Accediendo y modificando los valores a través de los punteros
    *puntero_entero = 20;
    *puntero_double = 6.28;
    *puntero_string = "Hola de nuevo, mundo!";

    // Imprimiendo los valores
    std::cout << "Valor entero: " << numero << std::endl;
    std::cout << "Valor double: " << decimal << std::endl;
    std::cout << "Valor string: " << cadena << std::endl;
}
