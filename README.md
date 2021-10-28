# LFP_Proyecto2_201905515
En este repositorio se trabajará el proyecto 2 de Lenguajes Formales y de Programación, segundo semestre 2021

|   #   |   Token   |   Descripcion   |   Tipo de Dato   |  ER   |
| ------------- | ------------- || ------------- || ------------- || ------------- |
| 1  | Reservada  || Este token representa una palabra reservada   | String  | L+  |
| 2  | Cadena  || Este token representa una línea de texto que puede optar por todos los caracteres   | String  | “(^”)*”  |
| 3  | Digito  || Este token representa un digito entero  | Int[0,9]  | D+  |
| 4  | Letra  || El carácter que puede formar un comando  | String  | L+  |
| 5  | Real  || Este token representa una variable real o decimal  | float  | D+|R?  |
| 6  | Símbolos  || Este token representa los tokens de los símbolos que pueden presentarse durante el análisis léxico  | String  | S?  |
| 7  | Comandos  || Este token representa las instrucciones que se pueden realizar dentro del análisis    | String  | (L+)(S)(“(^”)*”)(S+)  |
| 8  | $  || Este token representa el final de la ejecución  | String  | $?  |