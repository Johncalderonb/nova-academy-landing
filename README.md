# NOVA ACADEMY · Landing page

Página de captación para la primera cohorte de **NOVA ACADEMY**, una formación práctica en inteligencia artificial para emprendedores, dueños de negocio y profesionales que quieren aplicar la IA a su trabajo.

La página presenta el programa, muestra el precio y lleva al visitante a un formulario de interés. Un asesor contacta luego a cada persona registrada.

## El programa en breve

| | |
|---|---|
| Formación | 16 horas en vivo: 8 sesiones de 2 horas con el docente |
| Mentoría | 2 horas semanales de mentoría grupal |
| Modalidad | Virtual en vivo |
| Recursos | Plantillas y recursos prácticos, comunidad NOVA y canal de apoyo |
| Certificación | Campuslands, sujeta a los requisitos académicos |
| Inversión | $600.000 COP por participante |
| Inicio previsto | 9 de noviembre de 2026 |

La formación está a cargo de **Campuslands**, que imparte las sesiones con sus docentes y entrega la certificación. NOVA ACADEMY acompaña con la mentoría, la comunidad y el canal de apoyo.

## Precio y promoción

El valor de la formación es $1.000.000 COP. Hay un precio especial de **$600.000 COP pagando hasta el 10 de noviembre de 2026**, que la página destaca con cuenta regresiva, barra superior y el valor regular tachado. Al vencer, la página muestra sola el precio regular y retira la promoción. La fecha se cambia en el objeto `PROMO` al final de `index.html` (y en `gracias.html`).

## Master class

La página invita a la master class gratuita del viernes 30 de octubre de 2026 a las 6:30 p. m. (Colombia), con barra superior, sección propia, cuenta regresiva y enlace a Google Calendar. El acceso se entrega en el grupo de WhatsApp. Todo se oculta solo cuando termina el evento; la fecha se cambia en el objeto `MASTERCLASS` al final de `index.html` y en `CONFIG` de `gracias.html`.

## Secciones de la página

1. **Portada:** mensaje principal y botón al formulario.
2. **Datos clave:** 16 horas, 8 sesiones, 2 horas de mentoría semanal y precio.
3. **Para quién:** pestañas con foto para tres perfiles (idea de negocio, negocio activo, empleado o profesional).
4. **Propuesta de valor:** aplicar la IA, no coleccionar herramientas.
5. **¿Es para ti?:** autocalificación y requisitos.
6. **Programa:** línea de tiempo con las 8 sesiones.
7. **Herramientas:** agrupadas por necesidad.
8. **Formador.**
9. **Inversión:** $600.000 COP y seis beneficios incluidos, con llamado a inscribirse.
10. **Preguntas frecuentes.**
11. **Registro:** formulario de interés.

## Tecnología

Es un sitio estático: un solo archivo `index.html`, sin proceso de compilación.

- [Tailwind CSS](https://tailwindcss.com/) desde CDN
- Íconos [Phosphor](https://phosphoricons.com/) desde CDN
- Tipografías Outfit y Work Sans (Google Fonts)
- JavaScript sin librerías para el menú, las pestañas, las animaciones al hacer scroll y el formulario
- Diseño adaptable a móvil, tablet y escritorio, y respeta la opción del sistema para reducir el movimiento

## Estructura

```
├── index.html                 Página completa (HTML, estilos y scripts)
├── gracias.html               Página tras el registro: comunidad de WhatsApp y master class
└── assets/                    Todas las imágenes que usa la página
    ├── fondo-tecnologico.jpg  Fondo geométrico de marca (optimizado)
    ├── logo-nova.png          Isotipo de NOVA
    ├── og-nova.jpg            Imagen para compartir en redes (Open Graph)
    ├── nova-campuslands.webp  Logo NOVA con Campuslands (portada)
    ├── campuslands-*.webp     Logos de Campuslands (formador)
    ├── masterclass.webp       Afiche de la master class
    ├── perfil-idea.jpg        Foto del perfil "idea de negocio"
    ├── perfil-negocio.jpg     Foto del perfil "negocio activo"
    ├── perfil-empresa.jpg     Foto del perfil "trabajo en una empresa"
    └── credits.json           Autor, licencia y fuente de cada foto
```

### Créditos de imágenes

Las fotos de los perfiles son de dominio público ([CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.es)), así que no requieren crédito en la página. Se listan aquí como referencia:

- [“Woman writing on a notebook with a pen”](https://commons.wikimedia.org/wiki/File:Woman_writing_on_a_notebook_with_a_pen.jpg), Kristin Hardwick.
- [“Two men at coffee shop counter”](https://commons.wikimedia.org/w/index.php?curid=61713768), Jazmin Quaynor.
- [“Businessman working and writing notes in office”](https://commons.wikimedia.org/wiki/File:Businessman_working_and_writing_notes_in_office_(Unsplash).jpg), JESHOOTS.COM.

Son fotos ilustrativas del entorno de cada perfil, no de participantes del programa.

## Ver la página en tu computador

Abre `index.html` en el navegador, o sírvela con un servidor local:

```bash
python -m http.server 5510
```

Luego entra a <http://localhost:5510>.

## Formulario

El formulario envía los datos a una hoja de Google Sheets mediante un Google Apps Script publicado como aplicación web. La URL se configura en `index.html`, en el objeto `CONFIG.GOOGLE_SCRIPT_URL`.

Campos que envía: `fecha`, `nombre`, `whatsapp`, `correo`, `negocio`, `etapa`, `asistencia` (horario de contacto preferido), `objetivo` y `autorizacion`.

La hoja debe tener una columna con cada uno de esos nombres en la primera fila. No cambies los atributos `name` del formulario sin actualizar también la hoja.

Después de enviar, el visitante pasa a `gracias.html`, que lo invita a la comunidad de WhatsApp y a la master class con cuenta regresiva y botón para agregarla al calendario. Los enlaces y la fecha se cambian en el objeto `CONFIG` al final de `gracias.html` (`WHATSAPP_COMMUNITY_URL`, `MASTERCLASS_URL`, `MASTERCLASS_START`). Cuando la master class termina, su tarjeta se oculta sola.

> Apps Script no devuelve una respuesta legible desde el navegador. La página muestra el mensaje de éxito cuando no hay error de red, pero no puede confirmar que la fila se guardó.

## Publicación

La página está publicada con GitHub Pages desde la rama `main`:

**<https://johncalderonb.github.io/nova-academy-landing/>**

Cada cambio que se sube a `main` se publica solo en uno o dos minutos.

Si más adelante usas un dominio propio, actualiza en `index.html` las etiquetas `canonical`, `og:url`, `og:image` y `twitter:image`, que hoy apuntan a la dirección de GitHub Pages.

## Pendientes

- Confirmar el temario final de las 8 sesiones y la lista de herramientas con Campuslands.
- Confirmar días y horario de clase antes de mostrarlos.
- Confirmar los datos del formador y la autorización de su fotografía.
- Enlazar la política de tratamiento de datos en el formulario.
- Definir las condiciones del chat de soporte (horarios y tiempos de respuesta).

---

Formación con respaldo académico de Campuslands.
