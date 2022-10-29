# DATA ACCESS OBJECT
>Es  un componente del software el cual cumple con suministrar una interfaz entre el dispositivo de almacenamiento de datos y la aplicación.
>Este patrón se utiliza mucho normalmente gracias a su fácil implementación, ya que provee unos beneficios claros, permite separar en su totalidad la lógica de acceso a datos de los objetos de negocio.
>Su estructuración es la siguiente: Business Object, el cual es que representa un objeto con su lógica de negocio.
>Data Access Object, este representa una capa de acceso a los datos que la fuente oculta y también lo detalles para la recuperación de datos.
>Transfer Object, este implementa el patrón de (DTO) que cumple la función de transmitir la información entre DAO y Business Service.
>Y por último tenemos al DataSource, el cual es el que representa de una manera abstracta la fuente de datos.
>image.png
