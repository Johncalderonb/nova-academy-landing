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
├── bg-tech.jpg                Fondo geométrico de marca (optimizado)
├── logo-mark.png              Isotipo de NOVA ACADEMY
├── logo-full-transparent.png  Logo completo
├── logo-small.jpg             Logo en formato pequeño
├── imagen logo.jpeg           Imagen para compartir en redes (Open Graph)
├── foto.jpg                   Foto del formador
└── assets/
    ├── perfil-idea.jpg        Foto del perfil "idea de negocio"
    ├── perfil-negocio.jpg     Foto del perfil "negocio activo"
    ├── perfil-empresa.jpg     Foto del perfil "trabajo en una empresa"
    └── credits.json           Autor, licencia y fuente de cada foto
```

### Créditos de imágenes

Las fotos de los perfiles vienen de Wikimedia Commons. El enlace "Créditos de imágenes" del pie de la página lleva a esta lista. Todas fueron redimensionadas.

- [“Woman writing on a notebook with a pen”](https://commons.wikimedia.org/wiki/File:Woman_writing_on_a_notebook_with_a_pen.jpg), Kristin Hardwick, [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.es).
- [“Bags for sale, Street scene in Cartagena, Colombia”](https://commons.wikimedia.org/w/index.php?curid=63455027), Joe Ross, [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/).
- [“Toong Coworking Space in Hanoi”](https://commons.wikimedia.org/w/index.php?curid=63785226), Ann0611, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

Son fotos ilustrativas del entorno de cada perfil, no de participantes del programa. Si se reemplazan por fotos propias, se puede quitar el enlace del pie.

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
