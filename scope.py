

## Video de youtube: https://www.youtube.com/watch?v=-c0h05cluQA

## Ejemplo scope global: no se toma en cuenta la variable local.

variable = "Soy una variable Global" # Es una variable global

def funcion():
    variable= "Soy una variable local" #Es una variable local porque está dentro de la función.

print(variable) #El sistema imprime variable pero la Global dado que el print está fuera de la función def.

## Ejemplo 2, scope local: variables dentro de diferentes funciones son diferentes variables incluso si tienen el mismo nombre.

def funcion_uno():
    variable = "PHP"
    funcion_dos()
    print(variable)

def funcion_dos():
    variable = "Python"

funcion_uno

## Ejemplo 3: las variables globales sí pueden ser accedidas desde un ámbito local.

def local():
    print(mi_variable_global)

mi_variable_global = "Hola soy global"

print(mi_variable_global)
local()

## Ejemplo 4: Tomará como prioridad el parametro que se le está pasando a la función.

def local(mi_variable_global):
    print(mi_variable_global)

mi_variable_global = "Hola soy global"

print(mi_variable_global)
local("Soy un parametro") #Python tomará como prioridad el parametro "soy un parametro" que se le está pasando a la función def al ser local.

## Ejemplo 5: Modificar una variable global desde la variable local usando la palabra especial de python "Global".

def mi_funcion_local():
    global variable    # la palabra global indica que se usa la variable externa global y no la variable interna local de la función.
    variable = "Pero fui modificada desde la función"

variable = "Sou una variable Global" #Esta es una variable global
print(variable)
mi_funcion_local()
print(variable) #Aquí el sistema al haber llamado previamente a la función "mi_funcion_local" y ser cambiada, va a imprimir la variable modificada en local.

