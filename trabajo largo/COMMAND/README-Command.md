# COMMAND
>Es un patrón de diseño el cual permite convertir una solicitud en un objeto independiente el cual contendrá la información total de esta solicitud. 
>Este patrón se utiliza normalmente cuando queremos parametrizar algún objeto con operaciones, o en su defecto cuando deseamos programar una ejecución que se encuentra en una cola de operaciones.
>Su estructuración se lleva a cabo de la siguiente manera: La clase emisora, que se encarga de inicializar las solicitudes, esta cuenta con un campo predeterminado que almacena las referencias de un objeto de comando para que así este pueda activar ese comando en vez de tener que enviar una solicitud directa al receptor.
>La interfaz de comando, la cual se encarga de declarar un método único para la ejecución del comando.
>Luego están los comandos concretos, estos implementan varios tipos de solicitudes, en pocas palabras tienen que hacer un llamado a uno de los objetos. Y para poder ejecutar esta parte se necesitan de unos parámetros en el objeto receptor los cuales se pueden declarar como campos de comando concreto.
> Después está la clase receptora, que es la que contiene una parte lógica del negocio, en esta clase la mayoría de los objetos pueden ejercer un papel de receptor.
>Y por último el cliente, el cual se encarga de crear y configurar los objetos definidos de los comandos concretos, y para esto debe  entregar todos los parámetros de la solicitud y una vez obtenidos los resultados estos pueden asociarse con varios emisores.
>image.png