/**
 * Recibe las inscripciones de masterclass.html y las guarda en la hoja
 * "Inscritos Master Class NOVA - 20 nov 2026".
 *
 * Cómo activarlo (una sola vez):
 *  1. Abre la hoja en Google Sheets.
 *  2. Menú Extensiones > Apps Script. Borra lo que haya y pega este archivo completo.
 *  3. Guarda (icono de disquete).
 *  4. Botón Implementar > Nueva implementación > tipo "Aplicación web".
 *       Ejecutar como: Yo
 *       Quién tiene acceso: Cualquier usuario
 *  5. Autoriza los permisos que pide Google y copia la URL que termina en /exec.
 *  6. Pega esa URL en masterclass.html, en CONFIG.MASTERCLASS_SCRIPT_URL.
 *
 * Las columnas se llenan por nombre (fila 1), así que puedes reordenarlas sin romper nada.
 */
function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    const data = JSON.parse(e.postData.contents || '{}');
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
    const headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
    const row = headers.map(h => {
      const v = data[String(h).trim()];
      return v === undefined || v === null ? '' : String(v).slice(0, 500);
    });
    sheet.appendRow(row);
    return ContentService.createTextOutput(JSON.stringify({ ok: true }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ ok: false, error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}

/** Permite comprobar en el navegador que la implementación está activa. */
function doGet() {
  return ContentService.createTextOutput('Inscripciones Master Class NOVA: activo');
}
