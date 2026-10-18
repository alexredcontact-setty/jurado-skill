# Jurado · skill de Claude Code

Monta un juicio donde 12 clientes deciden si compran tu oferta, antes de lanzarla.

Porque tu entorno y Claude te dicen que sí a todo. Y un «sí» que nunca paga no te sirve.

1. **Dos abogados**: uno defiende que se vende y otro que nadie la compra.
2. **12 jurados** votan COMPRO o NO COMPRO **sin ver el voto de los demás**. Cada uno es un cliente distinto: la que mira
   cada euro, el que no acaba cursos, tu competencia, el escéptico quemado…
3. **El juez decide**: lánzala, ajústala o no la lances. Y te da **3 cambios** para darle la vuelta, con cuántos votos mueve cada uno.

Te deja una sentencia visual con el marcador, los cambios y los 12 votos razonados.

Hecha por [Setty](https://setty.es): el setter con IA que contesta a cada lead en menos de un minuto.

## Instalación

```bash
git clone https://github.com/alexredcontact-setty/jurado-skill.git ~/.claude/skills/jurado
```

Solo necesitas [Claude Code](https://claude.com/claude-code) y Python 3 (en Mac ya viene).

## Uso

Abre Claude Code y escribe **`/jurado`**. Cuéntale tu oferta (o pásale tu landing, tu PDF o tu guion de venta) y en
unos minutos tienes la sentencia en `~/Jurado/<tu-oferta>/sentencia.html`. Cuando apliques los cambios, pídele el
**segundo juicio** con el mismo jurado.

Mejor un «no» del jurado hoy… que el silencio después de enseñar la oferta.

¿La oferta ya está lista? El siguiente cuello de botella es contestar a tiempo: [setty.es](https://setty.es).
