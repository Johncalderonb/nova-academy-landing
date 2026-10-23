# NOVA ACADEMY · Landing page

Página de captación para la primera cohorte de **NOVA ACADEMY**, una formación práctica en inteligencia artificial para emprendedores, dueños de negocio y profesionales que quieren aplicar la IA a su trabajo.

La página presenta el programa, muestra el precio y lleva al visitante a un formulario de interés. Un asesor contacta luego a cada persona registrada.

## El programa en breve

| | |
|---|---|
| Formato | 8 clases prácticas en vivo, de 60 minutos |
| Modalidad | Virtual |
| Acompañamiento | Chat de soporte grupal |
| Certificación | Campuslands, sujeta a los requisitos académicos |
| Inversión | $600.000 COP por participante |
| Inicio previsto | 9 de noviembre de 2026 |

## Secciones de la página

1. **Portada:** mensaje principal y botón al formulario.
2. **Datos clave:** 8 clases, 60 minutos, virtual y certificado.
3. **Para quién:** pestañas para tres perfiles (idea de negocio, negocio activo, empleado o profesional).
4. **Propuesta de valor:** aplicar la IA, no coleccionar herramientas.
5. **¿Es para ti?:** autocalificación y requisitos.
6. **Qué incluye:** clases, chat de soporte y certificación.
7. **Programa:** línea de tiempo con las 8 sesiones.
8. **Herramientas:** agrupadas por necesidad.
9. **Formador.**
10. **Inversión:** precio y lo que incluye.
11. **Preguntas frecuentes.**
12. **Registro:** formulario de interés.

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
├── bg-tech.jpg                Fondo geométrico de marca (optimizado)
├── logo-mark.png              Isotipo de NOVA ACADEMY
├── logo-full-transparent.png  Logo completo
├── logo-small.jpg             Logo en formato pequeño
├── imagen logo.jpeg           Imagen para compartir en redes (Open Graph)
└── foto.jpg                   Foto del formador
```

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
