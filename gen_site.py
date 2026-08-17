#!/usr/bin/env python3
import os
os.chdir(os.path.join(os.path.dirname(__file__), "website"))

FONT = ('<link rel="preconnect" href="https://fonts.googleapis.com" />\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet" />')

ICONS = {
  "home":  '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/>',
  "flag":  '<path d="M5 21V4"/><path d="M5 4h11l-1.5 4L16 12H5"/>',
  "route": '<circle cx="6" cy="19" r="2.5"/><circle cx="18" cy="5" r="2.5"/><path d="M8.5 19H15a3 3 0 0 0 0-6H9a3 3 0 0 1 0-6h6.5"/>',
  "image": '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="8.5" cy="9.5" r="1.5"/><path d="m21 16-5-5L5 21"/>',
  "wind":  '<path d="M3 8h11a3 3 0 1 0-3-3"/><path d="M3 13h15a3 3 0 1 1-3 3"/><path d="M3 18h7"/>',
  "heart": '<path d="M12 20s-7-4.5-9.5-9C1 8 2.5 4.5 6 4.5c2 0 3.2 1.2 4 2.3.8-1.1 2-2.3 4-2.3 3.5 0 5 3.5 3.5 6.5C19 15.5 12 20 12 20Z"/>',
  "info":  '<circle cx="12" cy="12" r="9"/><path d="M12 11v5"/><circle cx="12" cy="7.8" r="0.6" fill="currentColor" stroke="none"/>',
  "mail":  '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
}

NAV = [
  ("index.html",     "Home",                "home"),
  ("sfida.html",      "La Sfida",            "flag"),
  ("percorso.html",   "Il Percorso",         "route"),
  ("fotogallery.html","Galleria",            "image"),
  ("news.html",       "Il Turbo Catamarano", "wind"),
  ("partner.html",    "Partner",             "heart"),
  ("info.html",       "Info",                "info"),
  ("contatti.html",   "Contatti",            "mail"),
]

FB = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">'
      '<path d="M14 9h3V5h-3c-2.2 0-4 1.8-4 4v2H7v4h3v6h4v-6h3l1-4h-4V9c0-.6.4-1 1-1z"/></svg>')
MAILICON = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="2"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>')

def icon(name):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>'

def sidebar(active):
    links = "\n".join(
        f'      <a href="{href}"{" class=\"active\"" if href==active else ""}>{icon(ic)}<span>{label}</span></a>'
        for href, label, ic in NAV)
    return f'''<aside class="sidebar">
    <a class="side-brand" href="index.html"><img src="img/logo.png" alt="Padus Solar Challenge" /></a>
    <nav class="side-nav">
{links}
    </nav>
    <div class="side-foot">
      <div class="side-social">
        <a href="https://www.facebook.com/Padussolarchallenge" target="_blank" rel="noopener" aria-label="Facebook">{FB}</a>
        <a href="mailto:g.gigliobianco@fastpiu.it" aria-label="Email">{MAILICON}</a>
      </div>
      <p>&copy; Padus Solar Challenge<br />Cremona &middot; Venezia &middot; Po</p>
    </div>
  </aside>
  <div class="scrim"></div>
  <div class="topbar">
    <a href="index.html"><img src="img/logo.png" alt="Padus Solar Challenge" /></a>
    <button class="nav-toggle" aria-label="Menu"><span></span></button>
  </div>'''

FOOTER = '''<footer class="site-footer">
      <div class="wrap">
        <div class="footer-inner">
          <div class="footer-links">
            <a href="sfida.html">La Sfida</a>
            <a href="percorso.html">Il Percorso</a>
            <a href="fotogallery.html">Galleria</a>
            <a href="news.html">Il Turbo Catamarano</a>
            <a href="partner.html">Partner</a>
            <a href="contatti.html">Contatti</a>
          </div>
          <a href="https://www.facebook.com/Padussolarchallenge" target="_blank" rel="noopener">Facebook</a>
        </div>
        <div class="copy">&copy; Padus Solar Challenge &mdash; competizione internazionale di barche solari, da Cremona a Venezia andata e ritorno lungo il Po.</div>
      </div>
    </footer>'''

def page(filename, active, title, desc, main_html, extra_head=""):
    html = f'''<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<meta name="robots" content="ALL" />
<link rel="shortcut icon" href="favicon.ico" />
{FONT}
<link rel="stylesheet" href="assets/style.css" />{extra_head}
</head>
<body>

  {sidebar(active)}

  <div class="content">
    <main>
{main_html}
    </main>
    {FOOTER}
  </div>

<script src="assets/main.js"></script>
</body>
</html>
'''
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)

# ------------------------------------------------------------------ HOME
home = '''<section class="hero">
        <div class="hero-slides">
          <div class="slide on" style="background-image:url('img/Foto1.jpg')"></div>
          <div class="slide" style="background-image:url('img/Foto2.jpg')"></div>
          <div class="slide" style="background-image:url('img/Foto3.jpg')"></div>
        </div>
        <div class="wrap">
          <span class="route-chip">&#127774; <b>Cremona</b> &rarr; Venezia &rarr; <b>Cremona</b> &middot; 600 km</span>
          <span class="eyebrow">Competizione internazionale di barche solari</span>
          <h1>Sfida il grande fiume, alimentato solo dal Sole.</h1>
          <p>Equipaggi e mezzi sperimentali risalgono e discendono il Po tra Cremona e Venezia: una gara di endurance dove vincono strategia, ingegno ed energia pulita.</p>
          <div class="btn-row">
            <a class="btn btn-primary" href="sfida.html">Scopri la sfida</a>
            <a class="btn btn-ghost" href="percorso.html">Vedi il percorso</a>
          </div>
        </div>
      </section>

      <section>
        <div class="wrap">
          <div class="stats">
            <div class="stat"><div class="num">600 km</div><div class="label">Percorso totale, andata e ritorno</div></div>
            <div class="stat"><div class="num">2 citt&agrave;</div><div class="label">Da Cremona a Piazza San Marco</div></div>
            <div class="stat"><div class="num">45&deg;</div><div class="label">Parallelo seguito lungo il Po</div></div>
            <div class="stat"><div class="num">100%</div><div class="label">Energia solare a bordo</div></div>
          </div>
        </div>
      </section>

      <section class="alt">
        <div class="wrap">
          <div class="section-head">
            <span class="eyebrow">Esplora</span>
            <h2>Tre modi per vivere la Padus Solar Challenge</h2>
            <p class="lead">Dalla filosofia della gara al lungo tracciato sul Po, fino ai catamarani sperimentali nati attorno all'evento.</p>
          </div>
          <div class="cards">
            <a class="card" href="sfida.html">
              <div class="card-media"><img src="img/img-sfida.jpg" alt="La sfida" /></div>
              <div class="card-body"><span class="tag">La Gara</span><h3>La Sfida</h3>
                <p>Traiettorie sul fiume, orientamento dei pannelli, gestione dell'energia e delle batterie: 300 km in discesa e la durissima risalita controcorrente.</p>
                <span class="card-link">Leggi la storia &rarr;</span></div>
            </a>
            <a class="card" href="percorso.html">
              <div class="card-media"><img src="img/percorso.jpg" alt="Il percorso" /></div>
              <div class="card-body"><span class="tag">Il Tracciato</span><h3>Il Percorso</h3>
                <p>Circa 600 km lungo il corso del Po, da Cremona a Venezia andata e ritorno, tra conche, correnti e acque della laguna.</p>
                <span class="card-link">Guarda la mappa &rarr;</span></div>
            </a>
            <a class="card" href="news.html">
              <div class="card-media"><img src="foto_cat/DSCN0440.JPG" alt="Il Turbo Catamarano" /></div>
              <div class="card-body"><span class="tag">Il Progetto</span><h3>Il Turbo Catamarano</h3>
                <p>&laquo;Controvento&raquo;: un catamarano ad aeromotore e propulsore Voith&nbsp;Schneider capace di avanzare dritto contro vento.</p>
                <span class="card-link">Scopri il progetto &rarr;</span></div>
            </a>
          </div>
        </div>
      </section>

      <section>
        <div class="wrap">
          <div class="section-head"><span class="eyebrow">Galleria</span><h2>Dall'alba di Cremona alla laguna di Venezia</h2></div>
          <div class="gallery">
            <figure data-lightbox="fotogallery/B/5B.jpg" data-caption="Partenza!"><img src="fotogallery/S/5S.jpg" alt="Partenza" /></figure>
            <figure data-lightbox="fotogallery/B/7B.jpg" data-caption="Argo in navigazione"><img src="fotogallery/S/7S.jpg" alt="In navigazione" /></figure>
            <figure data-lightbox="fotogallery/B/10B.jpg" data-caption="Tramonto sul grande fiume"><img src="fotogallery/S/10S.jpg" alt="Tramonto sul Po" /></figure>
            <figure data-lightbox="fotogallery/B/17B.jpg" data-caption="Ecco Argo a Venezia!"><img src="fotogallery/S/17S.jpg" alt="Argo a Venezia" /></figure>
          </div>
          <div style="margin-top:26px"><a class="btn btn-ghost" href="fotogallery.html">Apri la galleria completa</a></div>
        </div>
      </section>

      <section class="alt">
        <div class="wrap">
          <div class="section-head"><span class="eyebrow">Con il sostegno di</span><h2>Partner e patrocini</h2>
            <p class="lead">La manifestazione &egrave; resa possibile grazie ai partner e alle istituzioni che la patrocinano.</p></div>
          <p class="subhead">Partner</p>
          <div class="logo-grid" style="margin-bottom:40px">
            <a class="logo-tile" href="http://www.asvea.e-cremona.it" target="_blank" rel="noopener"><img src="img/partner-1.jpg" alt="ASVEA" /></a>
          </div>
          <p class="subhead">Manifestazione patrocinata da</p>
          <div class="logo-grid">
            <div class="logo-tile"><img src="img/patrocini-1.jpg" alt="Patrocinio" /></div>
            <div class="logo-tile"><img src="img/patrocini-2.jpg" alt="Patrocinio" /></div>
            <div class="logo-tile"><img src="img/patrocini-3.jpg" alt="Patrocinio" /></div>
            <div class="logo-tile"><img src="img/patrocini-4.jpg" alt="Patrocinio" /></div>
            <div class="logo-tile"><img src="img/logo-patroc-5.jpg" alt="Patrocinio" /></div>
          </div>
          <div style="margin-top:28px"><a class="btn btn-ghost" href="partner.html">Tutti i partner</a></div>
        </div>
      </section>

      <section>
        <div class="wrap"><div class="cta">
          <h2>Vuoi partecipare o saperne di pi&ugrave;?</h2>
          <p>Scrivici per informazioni su iscrizione, regolamento e partecipazione alla Padus Solar Challenge.</p>
          <a class="btn btn-primary" href="mailto:g.gigliobianco@fastpiu.it">Contattaci</a>
        </div></div>
      </section>'''

page("index.html", "index.html",
     "Padus Solar Challenge &mdash; Competizione internazionale di barche solari",
     "Padus Solar Challenge, la competizione internazionale delle migliori barche solari attrezzate per gare di endurance da Cremona a Venezia andata e ritorno.",
     home,
     extra_head='\n<meta name="google-site-verification" content="XplVyS7RTZhFHiRjY05QHFVnP1HGB97feNQ2UwV0iNA" />')

# ------------------------------------------------------------------ SFIDA
sfida = '''<div class="page-hero"><div class="wrap">
        <span class="eyebrow">La Sfida</span>
        <h1>Una gara di ingegno sul grande fiume</h1>
        <p>200 km in favore di corrente fino a Piazza San Marco, poi la parte pi&ugrave; lunga e difficile: 320 km di risalita controcorrente verso il vero traguardo, Cremona.</p>
      </div></div>

      <section><div class="wrap split">
        <div class="article">
          <h3>La Sfida</h3>
          <p>La competizione vede cimentarsi i diversi equipaggi che partono con i loro mezzi sperimentali da Cremona con l'obiettivo di essere i primi ad arrivare a piazza San Marco, lungo il 45&deg; parallelo fino alla citt&agrave; lagunare 200 km pi&ugrave; ad Est in favore di corrente, e successivamente fare ritorno a Cremona, vero traguardo dell'impresa.</p>
          <h3>L'avventura</h3>
          <p>I 300 km tortuosi di acqua dolce, la posizione del Sole, il traffico, le ombre delle nubi e delle rive, le conche di Volta Grimana, le acque mosse della laguna. &Egrave; una complessa questione di scelta delle traiettorie nel fiume Po, di orientamento dei pannelli, di gestione dell'energia solare e delle batterie.</p>
          <p>Le varie norme del Regolamento complicano ulteriormente la vita al pilota ed al team che via radio acquisisce dati, li rielabora e pianifica le strategie di condotta della gara.</p>
          <p>Tutta l'energia ottenuta dal Sole viene gestita al meglio per ottenere i minori tempi di percorrenza sul lunghissimo percorso. Ma non finisce qui. L'esperienza acquisita in discesa deve essere messa a frutto per affrontare la prova pi&ugrave; difficile.</p>
          <p>Chi &egrave; risultato vincitore sul traguardo di Venezia &egrave; solo ad un terzo dell'impresa. Ora rimane la parte pi&ugrave; lunga e difficile: la risalita controcorrente per 320 chilometri fino al traguardo di Cremona.</p>
        </div>
        <div class="media sticky"><img src="img/img-sfida.jpg" alt="La sfida sul Po" /></div>
      </div></section>

      <section class="alt"><div class="wrap">
        <div class="stats">
          <div class="stat"><div class="num">200 km</div><div class="label">Discesa in favore di corrente fino a Venezia</div></div>
          <div class="stat"><div class="num">320 km</div><div class="label">Risalita controcorrente verso Cremona</div></div>
          <div class="stat"><div class="num">Volta Grimana</div><div class="label">Le conche da attraversare</div></div>
          <div class="stat"><div class="num">San Marco</div><div class="label">Il giro di boa in laguna</div></div>
        </div>
      </div></section>

      <section><div class="wrap"><div class="cta">
        <h2>Segui l'impresa</h2>
        <p>Scopri il tracciato completo lungo il Po e le immagini della prima edizione.</p>
        <a class="btn btn-primary" href="percorso.html">Vedi il percorso</a>
      </div></div></section>'''
page("sfida.html", "sfida.html", "La Sfida &mdash; Padus Solar Challenge",
     "La Sfida della Padus Solar Challenge: da Cremona a Venezia e ritorno, tra traiettorie sul Po, gestione dell'energia solare e la difficile risalita controcorrente.",
     sfida)

# ------------------------------------------------------------------ PERCORSO
percorso = '''<div class="page-hero"><div class="wrap">
        <span class="eyebrow">Il Percorso</span>
        <h1>Circa 600 km lungo il corso del Po</h1>
        <p>La sfida si estende da Cremona a Venezia andata e ritorno, seguendo il grande fiume fino alla laguna e ritorno controcorrente.</p>
      </div></div>

      <section><div class="wrap">
        <figure data-lightbox="img/percorso.jpg" data-caption="Il percorso da Cremona a Venezia lungo il Po" style="margin:0;max-width:900px;cursor:zoom-in">
          <img src="img/percorso.jpg" alt="Mappa del percorso da Cremona a Venezia lungo il Po" style="border-radius:var(--radius);box-shadow:var(--shadow);width:100%" />
        </figure>
      </div></section>

      <section class="alt"><div class="wrap">
        <div class="stats">
          <div class="stat"><div class="num">~600 km</div><div class="label">Percorso complessivo, andata e ritorno</div></div>
          <div class="stat"><div class="num">Cremona</div><div class="label">Partenza e traguardo finale</div></div>
          <div class="stat"><div class="num">Venezia</div><div class="label">Giro di boa a Piazza San Marco</div></div>
          <div class="stat"><div class="num">Fiume Po</div><div class="label">Lungo il 45&deg; parallelo</div></div>
        </div>
      </div></section>'''
page("percorso.html", "percorso.html", "Il Percorso &mdash; Padus Solar Challenge",
     "Il percorso della Padus Solar Challenge: circa 600 km lungo il corso del Po, da Cremona a Venezia andata e ritorno.",
     percorso)

# ------------------------------------------------------------------ GALLERIA
shots = [
 (1,"17/6/2012 &mdash; In una calda mattina di giugno ha inizio l'avventura di Argo","Ha inizio l'avventura di Argo"),
 (2,"La meccanica di Argo","La meccanica di Argo"),
 (3,"Gli ultimi controlli prima della partenza del 1&ordm; Padus Solar Challenge","Gli ultimi controlli"),
 (4,"Un saluto prima di partire!","Un saluto prima di partire!"),
 (5,"Partenza!","Partenza!"),
 (6,"Passaggio sotto il ponte di Cremona","Il ponte di Cremona"),
 (7,"Argo in navigazione","Argo in navigazione"),
 (8,"... sulla spiaggia","... sulla spiaggia"),
 (9,"... ci si ferma per una notte sotto le stelle","Una notte sotto le stelle"),
 (10,"Tramonto sul grande fiume","Tramonto sul grande fiume"),
 (11,"Navigazione","Navigazione"),
 (12,"Navigazione","Navigazione"),
 (13,"Argo nella conca di Volta Grimana","Nella conca di Volta Grimana"),
 (14,"Conca di Volta Grimana","Conca di Volta Grimana"),
 (15,"Marina di Chioggia","Marina di Chioggia"),
 (16,"La prua della barca appoggio puntata su San Marco","Puntando su San Marco"),
 (17,"Ecco Argo a Venezia!","Ecco Argo a Venezia!"),
 (18,"La voce dei giornali locali","La voce dei giornali locali"),
 (19,"La voce dei giornali locali","La voce dei giornali locali"),
 (20,"Approdo di Castelmassa","Approdo di Castelmassa"),
 (21,"Il percorso controcorrente procede alla grande!","Risalita controcorrente"),
 (22,"Argo in arrivo a Casalmaggiore, prima dell'ultimo tratto verso la meta finale.","In arrivo a Casalmaggiore"),
 (23,"Questa sera si cena ...","Questa sera si cena&hellip;"),
 (24,"Argo in salita, alla volta di Cremona","Alla volta di Cremona"),
 (25,"I festeggiamenti dell'arrivo","I festeggiamenti dell'arrivo"),
 (26,"I festeggiamenti dell'arrivo","I festeggiamenti dell'arrivo"),
 (27,"I festeggiamenti dell'arrivo","I festeggiamenti dell'arrivo"),
]
figs = "\n".join(
 f'            <figure data-lightbox="fotogallery/B/{n}B.jpg" data-caption="{cap}"><img src="fotogallery/S/{n}S.jpg" alt="{short}" loading="lazy" /><figcaption>{short}</figcaption></figure>'
 for n, cap, short in shots)
galleria = f'''<div class="page-hero"><div class="wrap">
        <span class="eyebrow">Galleria</span>
        <h1>L'avventura di Argo</h1>
        <p>Dalla partenza di Cremona all'arrivo a Venezia e ritorno: le immagini della prima Padus Solar Challenge. Clicca su una foto per ingrandirla.</p>
      </div></div>

      <section><div class="wrap">
        <div class="gallery">
{figs}
        </div>
      </div></section>'''
page("fotogallery.html", "fotogallery.html", "Galleria &mdash; Padus Solar Challenge",
     "Galleria fotografica della Padus Solar Challenge: l'avventura di Argo da Cremona a Venezia e ritorno lungo il Po.",
     galleria)

# ------------------------------------------------------------------ PARTNER
partner = '''<div class="page-hero"><div class="wrap">
        <span class="eyebrow">Partner &amp; Patrocini</span>
        <h1>Chi rende possibile la sfida</h1>
        <p>La Padus Solar Challenge nasce grazie al sostegno dei partner e delle istituzioni che patrocinano la manifestazione.</p>
      </div></div>

      <section><div class="wrap">
        <div class="section-head"><span class="eyebrow">Partner</span><h2>I nostri partner</h2></div>
        <div class="logo-grid">
          <a class="logo-tile" href="http://www.asvea.e-cremona.it" target="_blank" rel="noopener"><img src="img/partner-1.jpg" alt="ASVEA" /></a>
          <div class="logo-tile"><img src="img/partner-2.jpg" alt="Partner" /></div>
          <div class="logo-tile"><img src="img/partner-3.jpg" alt="Partner" /></div>
          <div class="logo-tile"><img src="img/partner-4.jpg" alt="Partner" /></div>
          <div class="logo-tile"><img src="img/partner-5.jpg" alt="Partner" /></div>
          <div class="logo-tile"><img src="img/partner-6.jpg" alt="Partner" /></div>
        </div>
      </div></section>

      <section class="alt"><div class="wrap">
        <div class="section-head"><span class="eyebrow">Patrocini</span><h2>Manifestazione patrocinata da</h2></div>
        <div class="logo-grid">
          <div class="logo-tile"><img src="img/patrocini-1.jpg" alt="Patrocinio" /></div>
          <div class="logo-tile"><img src="img/patrocini-2.jpg" alt="Patrocinio" /></div>
          <div class="logo-tile"><img src="img/patrocini-3.jpg" alt="Patrocinio" /></div>
          <div class="logo-tile"><img src="img/patrocini-4.jpg" alt="Patrocinio" /></div>
          <div class="logo-tile"><img src="img/logo-patroc-5.jpg" alt="Patrocinio" /></div>
        </div>
      </div></section>'''
page("partner.html", "partner.html", "Partner &mdash; Padus Solar Challenge",
     "I partner e i patrocini della Padus Solar Challenge, la competizione internazionale di barche solari da Cremona a Venezia e ritorno.",
     partner)

# ------------------------------------------------------------------ INFO
info = '''<div class="page-hero"><div class="wrap">
        <span class="eyebrow">Info</span>
        <h1>Iscrizione e regolamento</h1>
        <p>Informazioni pratiche per partecipare alla Padus Solar Challenge.</p>
      </div></div>

      <section><div class="wrap"><div class="notice">
        <h3>Pagina in allestimento</h3>
        <p>Presto in rete le informazioni sull'iscrizione ed il regolamento.</p>
        <p style="margin-bottom:0">Nel frattempo puoi contattarci a <a href="mailto:g.gigliobianco@fastpiu.it">g.gigliobianco@fastpiu.it</a>.</p>
      </div></div></section>'''
page("info.html", "info.html", "Info &mdash; Padus Solar Challenge",
     "Informazioni sull'iscrizione e sul regolamento della Padus Solar Challenge.", info)

# ------------------------------------------------------------------ CONTATTI
contatti = '''<div class="page-hero"><div class="wrap">
        <span class="eyebrow">Contatti</span>
        <h1>Mettiti in contatto</h1>
        <p>Per informazioni sulla manifestazione, sulla partecipazione o sui progetti collegati.</p>
      </div></div>

      <section><div class="wrap"><div class="contact-card">
        <div class="row">
          <div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></div>
          <div><div class="k">Email</div><div class="v"><a href="mailto:g.gigliobianco@fastpiu.it">g.gigliobianco@fastpiu.it</a></div></div>
        </div>
        <div class="row">
          <div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M14 9h3V5h-3c-2.2 0-4 1.8-4 4v2H7v4h3v6h4v-6h3l1-4h-4V9c0-.6.4-1 1-1z"/></svg></div>
          <div><div class="k">Social</div><div class="v"><a href="https://www.facebook.com/Padussolarchallenge" target="_blank" rel="noopener">facebook.com/Padussolarchallenge</a></div></div>
        </div>
        <div class="row">
          <div class="ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 12-9 12s-9-5-9-12a9 9 0 0 1 18 0Z"/><circle cx="12" cy="10" r="3"/></svg></div>
          <div><div class="k">Dove</div><div class="v">Cremona &mdash; lungo il fiume Po</div></div>
        </div>
      </div></div></section>'''
page("contatti.html", "contatti.html", "Contatti &mdash; Padus Solar Challenge",
     "Contatti della Padus Solar Challenge, la competizione internazionale di barche solari da Cremona a Venezia e ritorno.", contatti)

# ------------------------------------------------------------------ NEWS
cat_photos = [
 ("foto_cat/5.jpeg","Il catamarano Controvento sul Po"),
 ("foto_cat/DSCN0440.JPG","Il catamarano sollevato dalla gru"),
 ("foto_cat/4.jpeg","Dettaglio dell'aeromotore ad asse verticale"),
 ("foto_cat/1.jpeg","Le ali e le palette del catamarano"),
 ("foto_cat/2.jpeg","Il catamarano Controvento"),
 ("foto_cat/3.jpeg","Il catamarano Controvento"),
 ("foto_cat/DSCN0448.JPG","Il catamarano Controvento"),
]
cat_figs = "\n".join(
 f'            <figure data-lightbox="{src}" data-caption="{cap}"><img src="{src}" alt="{cap}" loading="lazy" /><figcaption>{cap}</figcaption></figure>'
 for src, cap in cat_photos)
news = f'''<div class="page-hero"><div class="wrap">
        <span class="eyebrow">Il Turbo Catamarano &middot; 30/05/2020</span>
        <h1>Catamarano &laquo;Controvento&raquo;</h1>
        <p>Un catamarano dotato di aeromotore ad asse verticale direttamente connesso a un propulsore tipo Voith Schneider, in grado di procedere dritto contro vento.</p>
      </div></div>

      <section><div class="wrap">
        <div class="section-head"><span class="eyebrow">Video</span><h2>Il catamarano in azione</h2></div>
        <div class="videos">
          <div class="video"><iframe src="https://www.youtube.com/embed/IMmfteyIWEY" title="Controvento &mdash; video 1" loading="lazy" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
          <div class="video"><iframe src="https://www.youtube.com/embed/f1k1MAl3RkQ" title="Controvento &mdash; video 2" loading="lazy" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
          <div class="video"><iframe src="https://www.youtube.com/embed/LGn3uY2xCt4" title="Controvento &mdash; video 3" loading="lazy" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
        </div>
      </div></section>

      <section class="alt"><div class="wrap">
        <div class="article" style="max-width:78ch;margin:0 auto">
          <h3>Controvento</h3>
          <p>Controvento &egrave; il nome di questo catamarano, obiettivo del progetto &egrave; costruire un catamarano in grado di avanzare dritto contro vento. La possibilit&agrave; teorica di questo concetto &egrave; gi&agrave; stata ampiamente dimostrata da Hammit (1) e altri. Nessuno oggi si meraviglia pi&ugrave; del fatto che una barca a vela possa avanzare controvento bordeggiando; ma pu&ograve; una barca a vela avanzare diritta contro vento su una rotta parallela alla direzione del vento? Con una attrezzatura tradizionale no, nemmeno con una ala rigida, con un aeromotore forse s&igrave;, ed &egrave; quello che voglio dimostrare.</p>
          <p>Un aeromotore (anche detto mulino a vento) &egrave; una macchina che trasforma l'energia eolica in energia meccanica o in energia elettrica; queste macchine sono oggi ampiamente collaudate e caratterizzano alcuni paesaggi di comune osservazione; ci sono installazioni sperimentali di aeromotori su piattaforme galleggianti e prototipi di barche mosse da aeromotore, in queste realizzazioni l'aeromotore aziona un'elica immersa. Gli aeromotori possono essere ad asse orizzontale o verticale, i primi sono molto pi&ugrave; diffusi e sono le eliche che comunemente vediamo percorrendo le strade, fra i secondi ci sono il Darrieus (2) (molto efficiente ma non parte da solo) e la cicloturbina (3), quest'ultima richiede un meccanismo che regola l'incidenza della pala nei vari punti della circonferenza.</p>
          <p>Un catamarano dotato di elica aerea ad asse orizzontale collegata con un'elica immersa &egrave; gi&agrave; stato costruito col nome Revelation (4) (vedi foto); il risultato &egrave; una velocit&agrave; media a tutte le andature inferiore alla vela tradizionale, facilit&agrave; di manovra, avanza dritto contro vento a velocit&agrave; inferiore alla Velocity Made Good di una barca tradizionale col vantaggio di non richiedere la larghezza di acqua necessaria a bordeggiare. Nella navigazione in mare aperto l'affidabilit&agrave; &egrave; pi&ugrave; importante del massimo rendimento; la barca a vela tradizionale &egrave; pi&ugrave; affidabile di un aeromotore con parti in movimento; il catamarano Controvento ha il vantaggio di poter essere utilizzato sia nella modalit&agrave; aeromotore sia nella modalit&agrave; profili alari fissi; nelle andature che vanno dalla bolina larga in gi&ugrave; conviene quest'ultima modalit&agrave;.</p>
          <p>Nel campo della propulsione navale oltre alla comune elica ad asse orizzontale &egrave; noto il propulsore ad asse verticale detto Voith-Schneider; l'accoppiamento di un'elica aerea ad asse orizzontale con un'elica immersa richiede 2 giunti ad ingranaggi conici e un albero di trasmissione verticale; al contrario un aeromotore ad asse verticale e un propulsore VS possono essere accoppiati senza ingranaggi; il fisico H. M. Barkla ha fatto notare questo vantaggio (5).</p>
          <p>Lo stesso Barkla ha inventato il linear water-wind mill (6): si tratta di un'ala destinata a captare il vento calettata sullo stesso asse di una paletta immersa, questo complesso ad asse verticale &egrave; libero di scorrere in un binario orizzontale perpendicolare alla direzione del vento idealmente posto sulla superficie dell'acqua; una volta che a questo profilo aero-idrodinamico viene impressa una velocit&agrave; iniziale i profili trovano un angolo di equilibrio e l'ala cammina generando energia. Nelle andature che vanno dalla bolina larga alla poppa l'imbarcazione a vela o ala rigida ottiene una velocit&agrave; superiore all'imbarcazione dotata di aeromotore; nell'andatura contro vento la barca a vela necessita di una certa larghezza del passaggio per bordeggiare; l'imbarcazione dotata di aeromotore non ha bisogno di larghezza del passaggio; l'ideale sarebbe utilizzare la propulsione che deflette il vento nelle andature dal traverso al largo e la propulsione ad aeromotore controvento. Il catamarano Controvento &egrave; in grado di sommare questi due vantaggi.</p>
          <p>Prima di Controvento ho costruito un catamarano lungo 6 metri dotato di cicloturbina conica alta 8 metri e propulsore VS; la cicloturbina &egrave; stata provata nella galleria del vento del Politecnico di Torino nell'ambito di un programma di ricerca finanziato dal C.N.R. La meccanica della trasmissione &egrave; abbastanza complessa e i risultati sperimentali incerti. (7) Pi&ugrave; recentemente ho costruito un modello del catamarano Controvento costituito da 2 scafi e 2 traverse; nello spazio quadrato compreso fra gli scafi e le traverse &egrave; alloggiato un binario circolare, all'interno di questo binario circola una struttura prismatica costituita da 2 triangoli orizzontali e 3 assi verticali; ai vertici del triangolo inferiore sono fissati 3 carrelli composti da 3 ruote ciascuno che abbracciano il binario; gli elementi verticali sono costituiti da un'ala in aria e da una paletta in acqua, ala e paletta sono calettate sullo stesso asse; ogni complesso ala-paletta si comporta come il linear water-wind mill, le ali nell'aria si assestano da sole al migliore angolo di incidenza e analogamente le palette nell'acqua trovano il migliore angolo di incidenza; nel complesso l'aeromotore capta l'energia del vento e le palette forniscono una spinta in avanti in direzione contraria a quella del vento.</p>
          <p>Il vantaggio di questo catamarano rispetto ad altre imbarcazioni dotate di aeromotore &egrave; quello di poter essere utilizzato anche in modalit&agrave; di deviazione del vento come una vela o ala; infatti bloccando la rotazione dell'aeromotore abbiamo 3 ali che sfruttano il vento come vele alari e tre palette in acqua che svolgono funzione antideriva. La velocit&agrave; media di una barca a vela (flessibile o ad ala rigida) tradizionale a tutte le andature &egrave; superiore a quella di imbarcazione ad aeromotore, quest'ultima ha il vantaggio di poter avanzare anche nell'angolo morto. Il catamarano &laquo;Controvento&raquo; pu&ograve; essere utilizzato in modalit&agrave; aeromotore oppure in modalit&agrave; tradizionale sommando cos&igrave; i vantaggi di entrambe le modalit&agrave;.</p>
          <p class="byline"><strong>Giuseppe Gigliobianco</strong> &mdash; Cremona<br /><a href="mailto:g.gigliobianco@fastpiu.it">g.gigliobianco@fastpiu.it</a></p>
        </div>
      </div></section>

      <section><div class="wrap">
        <div class="section-head"><span class="eyebrow">Galleria del progetto</span><h2>Il catamarano da vicino</h2></div>
        <div class="gallery">
{cat_figs}
        </div>
      </div></section>

      <section class="alt"><div class="wrap">
        <div class="article" style="max-width:82ch;margin:0 auto">
          <h3>A self trimming vertical axis windmill propelled catamaran</h3>
          <p>The "Linear wind/water mill propeller" was first presented by Professor H. M. Barkla in the XII symposium of the American Institute of Aeronautics and Astronautics (S. Francisco, October 1982). This is a mast with sail and keel without hull. Obviously this "thing" cannot float, so it is set onto a truck and the truck runs onto a rail above the surface of the water and the rail is at square angle with the true wind. This "mill" yields a thrust directed against the wind.</p>
          <p>Subsequently Barkla proposed a "vertical axis turbine propeller for ship propulsion" (Wind Engineering, London 1984, Vol 8, No 4). In this work Barkla proposes to put together three "mills" rotating around a central shaft, this shaft being coupled to a Voith Schneider propeller in the water; the blades of the Voith Schneider propeller are trimmed via rods and cranks by an eccentric.</p>
          <p>In the first video a full size catamaran can be seen equipped with a vertical axis windmill and a Voith Schneider propeller. This cat is presented in AYRS 102, 1986. (Thanks to my friend Paolo Carotta who helped in projecting and building.)</p>
          <p>Since then I have worked to lighten the craft; I have eliminated the central shaft, eccentric, rods and cranks; each wing is fastened to a mast with its blade and the three masts are enclosed in a truss that rotates into a circular rail; each wing-blade complex is self trimming; in conclusion we have three linear mills running in circle. This craft was presented at the 17th AIAA symposium (Stanford, CA 1987). In the last video the catamaran is equipped with six wings but the improvement is not that great. (Thanks to Mario Tomatis for the videos and photos.)</p>
          <p>I hope to build a full size craft in the future.</p>
          <p class="byline"><strong>Giuseppe Gigliobianco</strong> &mdash; Cremona</p>
        </div>
      </div></section>

      <section><div class="wrap">
        <div class="article" style="max-width:82ch">
          <h3>Bibliografia</h3>
          <ol class="refs">
            <li>Hammit A. G. &mdash; Optimum wind propulsion, proceedings of the 1st AIAA symposium, april 1969.</li>
            <li>P. South and R. Rangi &mdash; &laquo;Comparison between three analytical models of a Darrieus wind turbine&raquo;, 2nd International Symposium on Wind Energy Systems (SISWES), october 1978, Amsterdam.</li>
            <li>N. D. Ham and H. M. Drees &mdash; Analytical and experimental evaluation of Cycloturbine aerodynamic performance; Wind Technology Journal, fall and winter 1978.</li>
            <li>AYRS 105 &mdash; High speed sailing, october 1989.</li>
            <li>H. M. Barkla &mdash; The Vertical-Axis Turbine/Propeller for Ship Propulsion, Wind Engineering Vol. 8, No. 4 (1984).</li>
            <li>Barkla H. M. &mdash; The linear wind/water-mill propeller, Proceedings of the XII AIAA symposium, october 1982, S. Francisco.</li>
            <li>Giuseppe Gigliobianco &mdash; A vertical axis windmill propelled catamaran, The Ancient Interface XVI, 16th AIAA Symposium on the aero/hydronautics of sailing, october 1986.</li>
            <li>G. Gigliobianco &mdash; A Self Trimming Vertical Axis Windmill Propelled Catamaran, The Ancient Interface XVII, 17th AIAA Symposium on the aero/hydronautics of sailing, october 1987.</li>
          </ol>
        </div>
      </div></section>'''
page("news.html", "news.html", "Il Turbo Catamarano &laquo;Controvento&raquo; &mdash; Padus Solar Challenge",
     "Controvento: un catamarano dotato di aeromotore ad asse verticale e propulsore Voith Schneider, in grado di avanzare dritto contro vento. Progetto di Giuseppe Gigliobianco.",
     news)

print("done")
