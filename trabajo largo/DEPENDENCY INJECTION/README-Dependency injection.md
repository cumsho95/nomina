# DEPENDENCY INJECTION
>Es un patrón de diseño el cual sirve para suministrar objetos a una clase, sin necesidad de que la clase tenga que hacerlo. En pocas palabras este patrón es el encargado de extraer esa (responsabilidad) de tener que crear las instancias del componente para luego tener que ponerlo en otro.
>Su estructuración principal sería esta :
>image.png
>Aquí podemos ver cómo se crean unas dependencias al servicio de impresión, ya que el servicio de impresión está dependiendo de otros servicio y de esta menar las responsabilidades de cada uno son más claras, de esto se trata la (inyección de dependencia).