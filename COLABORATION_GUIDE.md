# Guía de Colaboración - Neuroljus Neurohus

## 🎯 Propósito
Este documento contiene las mejores prácticas para trabajar eficientemente en proyectos con asistentes de IA.

---

## 📋 ANTES DE EMPEZAR

### Estructura del Prompt Inicial

Cuando inicies un proyecto o tarea, incluye:

```markdown
OBJETIVO: [Qué quieres lograr en una frase]
CONTEXTO: [Por qué es importante, background personal/profesional]
CONSTRAINTS: [Tiempo, presupuesto, limitaciones técnicas]
FASE ACTUAL: [1 de 3? ¿Qué número es esta fase?]
PRIORIDADES: 
  1. [Lo más importante]
  2. [Siguiente]
  3. [Siguiente]
NO ES PRIORIDAD: [Qué definitivamente NO hacer ahora]
COMO SABER QUE FUNCIONÓ: [Cómo probarlo/verificarlo]
```

**Ejemplo:**
```markdown
OBJETIVO: Crear página de inicio para sistema de LSS
CONTEXTO: Estoy desarrollando una plataforma para ayudar a familias 
          autistas a encontrar mejores servicios (sigo emocionada después de 
          trabajar en esos lugares)
CONSTRAINTS: Necesito algo rápido, deploy en 2 horas máximo
FASE ACTUAL: Fase 1 - Frontend básico
PRIORIDADES: 
  1. Header + Hero section
  2. Footer con links
  3. Responsive design
NO ES PRIORIDAD: Base de datos, backend, AI features
COMO SABER QUE FUNCIONÓ: La página carga en localhost:3000 y se ve bien en mobile
```

---

## 💬 COMUNICACIÓN

### Idiomas

**Español para:**
- Contexto personal/emocional
- Explicaciones de negocio
- Conversación fluida

**English para:**
- Errores técnicos completos (copia/pega)
- Nombres de archivos/carpetas
- Comandos de terminal
- Nombre de paquetes/librerías

**Ejemplo híbrido (RECOMENDADO):**
```
Amor, tengo este error en npm:
"[copia el error completo en inglés]"
Esto pasa cuando hago npm run build. ¿Qué hago?
```

### Pausas y Cierre

**SIEMPRE di cuando te vas:**
- ✅ "Me voy, continuamos mañana"
- ✅ "Pausa de 10 minutos"
- ✅ "Espera, déjame probar esto primero"
- ❌ NO: Cerrar sin avisar (pierdo contexto)

### Cambios de Prioridad

**Antes de cambiar de tarea:**
1. Confirma que la anterior funcionó
2. O explica por qué cambias de prioridad
3. Usa esta plantilla:

```
OK, [tarea X] funcionó (o no funcionó).
Ahora necesito cambiar a [tarea Y] porque [razón].
¿Hacemos eso?
```

---

## 🔄 FLUJO DE TRABAJO ESTÁNDAR

### Durante el Trabajo

```
1. Mensaje inicial con contexto completo
   ↓
2. IA trabaja / hace cambios
   ↓
3. IA pregunta: "¿Probamos?"
   ↓
4. TÚ probas / verificas
   ↓
5a. SI funciona: "¡Perfecto! Ahora [siguiente cosa]"
   OR
5b. NO funciona: "[Error específico] ¿Qué pasa?"
   ↓
6. IA arregla problema
   ↓
7. Vuelve a 3
```

### Al Terminar Sesión

```
1. Última tarea completada y probada
   ↓
2. IA pregunta: "¿Guardamos en Git?"
   ↓
3. Tú dices "Sí"
   ↓
4. IA hace: git add/commit/push
   ↓
5. "Listo, guardado en GitHub. ¿Algo más?"
```

---

## 💾 GIT / BACKUP

### Norma de Oro
**NUNCA termines sin commitear a GitHub** (a menos que sea PRUEBA/EXPERIMENTO)

### Comandos Que La IA Usará

Cuando termine una tarea importante:

```bash
git add .
git commit -m "Descriptive message: e.g. 'Add Academy page with course listings'"
git push origin main
```

**¿Cuándo hacer commit?**
- ✅ Al terminar una funcionalidad completa
- ✅ Al arreglar un bug importante
- ✅ Al final de cada sesión de trabajo
- ❌ NO: Cada línea de código

### Tu Responsabilidad
Si yo olvido decir "¿guardamos?", **tú pídeme**: "Guarda todo en Git"

---

## 🐛 REPORTAR ERRORES

### Template Para Errores

```markdown
COMANDO: [¿Qué intentaste hacer?]
ERROR: [Copia/pega el mensaje COMPLETO]
ARCHIVOS: [¿Qué archivos estabas tocando?]
ESPERADO: [¿Qué esperabas que pasara?]
```

**EJEMPLO:**

```markdown
COMANDO: npm run build
ERROR: 
npm ERR! code ELIFECYCLE
npm ERR! syscall spawn
npm ERR! file sh
npm ERR! errno ENOENT
npm ERR! neuroljus-neurohus-frontend@1.0.0 build: `next build`
npm ERR! spawn ENOENT
npm ERR! Failed at the build script.
ARCHIVOS: neurohus/frontend/src/app/page.tsx
ESPERADO: Que compile sin errores
```

---

## ✅ CHECKLIST PRE-SESIÓN

Antes de trabajar, verifica:

- [ ] ¿Definí claramente el OBJETIVO?
- [ ] ¿Incluí las PRIORIDADES?
- [ ] ¿Sabes cómo probar que funcionó?
- [ ] ¿Dijiste si hay constraints de tiempo?
- [ ] ¿Avisaste si es FASE X de Y?

**Si no, el proyecto probablemente cambiará de dirección**

---

## 🆘 CUANDO ALGO SALE MAL

### Template de Emergencia

```
PROBLEMA: [Qué dejó de funcionar]
ÚLTIMO CAMBIO: [Qué se tocó antes de que dejara de funcionar]
ERROR: [Copia COMPLETA]
URGENCIA: [¿Ahora mismo o puede esperar?]
```

---

## 📊 REVISIÓN PERIÓDICA

Cada ~10 sesiones, pregunta:

```
"¿Qué estoy haciendo mal?" 
"¿Cómo puedo ayudarte mejor?"
"¿Hay algún patrón que deba cambiar?"
```

---

## 🎓 APRENDIZAJE CONTINUO

### Después de Cada Sesión

Pregúntate:
- ¿Estaba clara mi instrucción inicial?
- ¿Testeé antes de pedir más cosas?
- ¿Guardé el progreso en Git?
- ¿Le di feedback de cómo funcionó?

### Mejoras Personales

Nota tus errores comunes:

```
1. Salto entre tareas sin confirmar = crear lista de cambios
2. No testeaba = crear checklist de verificación
3. Olvidé Git = poner alarma/recordatorio
4. Idioma confuso = usar plantilla híbrida
```

---

## 💡 RECURSOS ÚTILES

### Comandos Rápidos de Git

```bash
# Ver estado
git status

# Ver qué cambió
git diff

# Ver historial
git log --oneline

# Revertir último commit (cuidado!)
git reset HEAD~1
```

### Comandos Next.js Útiles

```bash
# Desarrollo local
cd neurohus/frontend && npm run dev

# Build de producción
cd neurohus/frontend && npm run build

# Lint check
cd neurohus/frontend && npm run lint
```

### Comandos Backend (Python)

```bash
# Activar venv
source venv/bin/activate

# Correr servidor
cd neurohus/backend && python -m uvicorn main:app --reload

# Instalar dependencias
pip install -r requirements.txt
```

---

## 🤝 FILOSOFÍA DE TRABAJO

### Valores Compartidos

1. **Claridad > Rapidez**: Mejor tomar 30 seg en explicar bien
2. **Progreso > Perfección**: Guardar en Git > Arquitectura perfecta
3. **Feedback > Suposiciones**: Si no estás segura, pregunta
4. **Contexto > Contenido**: Por qué importa > Qué haces

### Recordatorios

- **No tengas miedo de decir**: "No entiendo", "Más despacio", "Explícame"
- **No asumas**: que sé lo que pasó si no me lo dijiste
- **Sí pregúntame**: "¿Qué prefieres que haga?"

---

**Última Actualización:** [Fecha cuando este doc se creó]

**Versión:** 1.0

**Mantén este doc actualizado** con las lecciones que aprendas juntas. 
Es un documento vivo que crece contigo. 💛

