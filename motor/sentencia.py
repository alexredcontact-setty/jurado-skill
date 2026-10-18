#!/usr/bin/env python3
"""Convierte sentencia.json en una sentencia visual (sentencia.html) y la abre.
   python3 sentencia.py ~/Jurado/<oferta>/"""
import html, json, os, subprocess, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent


def main():
    d = Path(sys.argv[1]).expanduser()
    s = json.loads((d / 'sentencia.json').read_text(encoding='utf-8'))
    e = lambda x: html.escape(str(x or ''))
    color = {'LÁNZALA': '#30D158', 'AJÚSTALA': '#FFB020', 'NO LA LANCES': '#FF453A'}.get(s['veredicto'], '#FFB020')
    votos = ''.join(
        f'<div class="voto {"si" if v["voto"] == "COMPRO" else "no"}"><div class="cab"><b>{e(v["jurado"])}</b>'
        f'<span>{e(v["voto"])}</span></div><p class="frase">«{e(v.get("frase"))}»</p>'
        f'<p class="obj"><i>{"Le convence" if v["voto"] == "COMPRO" else "Le frena"}:</i> {e(v.get("objecion"))}</p>'
        f'<p class="obj"><i>Compraría si:</i> {e(v.get("cambiaria_si"))}</p><p class="obj"><i>Pagaría:</i> {e(v.get("pagaria"))}</p></div>'
        for v in s.get('votos', []))
    cambios = ''.join(f'<li><b>{e(c["titulo"])}</b><p>{e(c["detalle"])}</p><span class="mueve">+{e(c.get("votos", "?"))} votos</span></li>'
                      for c in s.get('cambios', []))
    fichas = ''.join(f'<i class="f {"si" if v["voto"] == "COMPRO" else "no"}"></i>' for v in sorted(s.get('votos', []), key=lambda v: v['voto'] != 'COMPRO'))
    t = (AQUI.parent / 'ref' / 'sentencia.html').read_text(encoding='utf-8')
    for k, v in {'OFERTA': e(s.get('oferta')), 'VEREDICTO': e(s['veredicto']), 'COLOR': color, 'COMPRO': e(s.get('compro')),
                 'NOCOMPRO': e(s.get('no_compro')), 'RESUMEN': e(s.get('resumen')), 'CAMBIOS': cambios, 'VOTOS': votos,
                 'FICHAS': fichas, 'PRECIO': e(s.get('precio_jurado')), 'ARGUMENTO': e(s.get('mejor_argumento'))}.items():
        t = t.replace('{{' + k + '}}', v)
    out = d / 'sentencia.html'
    out.write_text(t, encoding='utf-8'); print(out)
    if '--no-abrir' in sys.argv: return
    if sys.platform == 'darwin': subprocess.run(['open', str(out)])
    elif os.name == 'nt': os.startfile(str(out))


if __name__ == '__main__':
    main()
