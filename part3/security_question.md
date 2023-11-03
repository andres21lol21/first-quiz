Control de Acceso Roto (A01:2021): se deberia usar un sistema de control de acceso bastante fuerte y basado en jararquias donde solo las personas que realmente necesiten acceder a sierta informacion tengan ese debido acceso deacuerdo a sus requerimiento sin permitir el acceso a terceros para asegurarnos de que solo los usuarios autorizados puedan acceder a los datos y funciones relevantes. Por ejemplo, los empleados de atención al cliente no deberían tener el mismo nivel de acceso que los ingenieros de software.

Fallas Criptográficas (A02:2021): es muy importante usar cifrado para los datos ya que nos brindaria un plus en cuanto a la seguridad de los datos. Esto es especialmente importante ya que estás almacenando contraseñas, direcciones y numeros de teléfono.

Inyección (A03:2021):se debe definir bastante bien las longitudes y los tipos de datos que se permiten para la base de datos . Debes asegurarte de que cualquier entrada del usuario se sanea adecuadamente antes de usarla en una consulta SQL.

Diseño Inseguro (A04:2021): se deben tener en cuenta los riesgos de seguridad en cada parte de la aplicacion  y asegurarse de evitar correr la mayor tasa de riesgo posible . Por ejemplo, podrias implementar la autenticación de dos factores para los usuarios.

Configuración de Seguridad Incorrecta (A05:2021): se debe asegurar de que la infraestructura de AWS y Kubernetes esté configurada de manera segura. Esto incluye cosas como asegurarte de que todos los servicios y contenedores tengan los permisos mínimos necesarios para funcionar de acuerdo a sus requerimientos .

Componentes Vulnerables y Desactualizados (A06:2021): Debes mantener tus sistemas y bibliotecas actualizados para protegerte contra vulnerabilidades conocidas ya que se pueden aprovechar de siertas vulnerabilidades que muchas veces ya son corregidas en parches de actualizaciones. Esto incluye tu base de datos MySQL, tu backend de Python y tu frontend de Next.js.

Identificación y Autenticación Inseguras (A07:2021): se deberian implementar mecanismos de autenticación e identificación seguros para tener una mayor seguridad a la hora de ingresar o realizar algun movimiento. Esto podría incluir el uso de contraseñas seguras, autenticación de dos factores y bloqueo de cuentas después de varios intentos de inicio de sesión fallidos.

Vulnerabilidades de Software y Hardware (A08:2021): es bastante importante mantener los sistemas y hardware actualizados para protegerte contra vulnerabilidades conocidas al igual que la ubicacion y el aceeso de los mismo a personas no deseadas. Esto incluye tanto tu infraestructura de AWS y Kubernetes como tus dispositivos móviles y servidores.

Server-Side Request Forgery (A09:2021): Debes proteger tu aplicación contra ataques de falsificación de solicitudes en el lado del servidor. Esto podría implicar la implementación de políticas de CORS estrictas y la validación de todas las solicitudes entrantes.

Registro y Monitoreo Insuficientes (A10:2021): Debes implementar un sistema de registro y monitoreo robusto para detectar y responder a incidentes de seguridad de manera oportuna para actuar lo mas pronto posible ante cualquier eventualidad y evitemos correr el mayor riesgo posible. Esto podría incluir la configuración de alertas automáticas para actividades sospechosas y la revisión regular de los registros de seguridad.