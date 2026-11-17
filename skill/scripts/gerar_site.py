# Gera o site da bio do Teacher Pedro (versão de dezembro/2026): uma página só, inglês para viajar e para o trabalho.
# Uso: python3 skill/scripts/gerar_site.py .   (na raiz do repositório)
# Gera: index.html (home) e redirecionamentos para a home em viagem/, trabalho/, reforco/ e vestibular/ (páginas antigas).
import os, sys, urllib.parse

OUT = sys.argv[1] if len(sys.argv) > 1 else "site"
WA = "5519997159133"
IG = "https://ig.me/m/teacherpedrogrt"
IGP = "https://instagram.com/teacherpedrogrt"
BASE = "https://teacherpedrogrt.github.io/"
LOCAL = "Presencial em Mogi Guaçu, Mogi Mirim e Araras • Online"
MSG = "Oi Pedro! Vim pelo site e quero saber da aula experimental."

# Campanha: faixa no topo até a data (AAAA-MM-DD). Sem campanha, FAIXA = None.
FAIXA = {"ate": "2026-11-30",
         "texto": "Black Friday · Primeira mensalidade com desconto até 30/11",
         "msg": "Oi Pedro! Vim pelo site e quero saber da Black Friday.",
         "link": "Quero aproveitar"}

def wa(msg):
    return f"https://wa.me/{WA}?text={urllib.parse.quote(msg)}"

CSS = r"""
:root{--c:#F7F4EA;--c2:#EFEBDD;--a:#1F3A8F;--v:#C6F135;--t:#24305c;--l:rgba(31,58,143,.18);
--M:"Archivo",system-ui,sans-serif;--N:"Inter",system-ui,sans-serif;--mono:"JetBrains Mono",ui-monospace,monospace;
--grao:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .07 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--c);color:var(--t);font-family:var(--N);font-weight:400;font-size:17px;line-height:1.65;-webkit-font-smoothing:antialiased}
body::after{content:"";position:fixed;inset:0;background-image:var(--grao);pointer-events:none;mix-blend-mode:multiply;z-index:50}
a{color:inherit}
.wrap{max-width:1040px;margin:0 auto;padding:0 20px}
section{padding:72px 0;border-top:1px solid var(--l)}
p{margin:0 0 14px}
b,strong{font-family:var(--M);font-weight:800;color:var(--a)}

/* rótulo pequeno (eyebrow) */
.eyebrow{display:inline-flex;align-items:center;gap:8px;font-family:var(--M);font-weight:700;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--a);margin:0 0 16px}
.eyebrow::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--v);box-shadow:0 0 0 2px var(--a)}
h1,h2,h3{font-family:var(--M);color:var(--a);text-transform:uppercase;margin:0}
h2{font-weight:900;font-size:clamp(28px,7.4vw,46px);line-height:1.05;letter-spacing:-.02em;margin-bottom:18px;max-width:18em}
h3{font-weight:800;font-size:16px;letter-spacing:.02em;line-height:1.25}
mark{background:var(--v);color:var(--a);padding:0 .14em;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.intro{max-width:36em;font-size:18px}

/* topo */
.nav{position:sticky;top:0;z-index:40;background:rgba(247,244,234,.92);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border-bottom:1px solid var(--l)}
.nav .wrap{display:flex;align-items:center;justify-content:space-between;height:64px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;font-family:var(--M);font-weight:900;font-size:15px;letter-spacing:.02em;color:var(--a);text-transform:uppercase}
.logo svg{width:38px;height:38px}
.nav .cta{font-family:var(--M);font-weight:800;font-size:12px;letter-spacing:.06em;text-transform:uppercase;text-decoration:none;color:var(--a);border:2px solid var(--a);border-radius:99px;padding:8px 14px}
.faixa{display:none;background:var(--a);color:var(--c);text-align:center;font-family:var(--M);font-weight:700;font-size:13px;line-height:1.4;padding:10px 0}
.faixa a{color:var(--v);text-transform:uppercase;white-space:nowrap}

.hero{border-top:0;padding:56px 0 64px}
.hero h1{font-weight:900;font-size:clamp(38px,11vw,76px);line-height:1;letter-spacing:-.03em;margin:0 0 22px;max-width:11em}
.hero .sub{font-size:19px;max-width:30em;margin-bottom:28px}
.btns{display:grid;gap:12px;max-width:420px}
.btn{display:flex;align-items:center;justify-content:center;gap:10px;min-height:56px;border-radius:99px;padding:14px 16px;font-family:var(--M);font-weight:800;font-size:clamp(13px,3.6vw,15px);text-transform:uppercase;text-decoration:none;text-align:center;transition:transform .15s}
.btn:active{transform:scale(.98)}
.btn svg{width:22px;height:22px;flex:none}
.btn.v{background:var(--v);color:var(--a);border:2px solid var(--a);box-shadow:0 4px 0 var(--a)}
.btn.o{border:2px solid var(--a);color:var(--a)}
.btn.c{border:2px solid var(--c);color:var(--c)}
.feat{display:flex;flex-wrap:wrap;gap:6px 18px;margin-top:26px;padding:0;list-style:none;font-family:var(--M);font-weight:700;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--a)}
.feat li::before{content:"✦ ";color:var(--a)}

/* pra quem é */
.duo{display:grid;gap:14px;margin:28px 0 22px}
.box{border:2px solid var(--a);border-radius:20px;padding:22px;background:var(--c)}
.box .tag{display:inline-block;font-family:var(--M);font-weight:800;font-size:11px;letter-spacing:.12em;text-transform:uppercase;background:var(--a);color:var(--c);border-radius:99px;padding:4px 10px;margin-bottom:12px}
.box h3{font-size:20px;margin-bottom:8px}
.box p{margin:0 0 10px;font-size:16px}
.box .ex{margin:0;padding-top:10px;border-top:1px dashed var(--l);font-size:15px}
.chave{font-family:var(--M);font-weight:800;color:var(--a);font-size:clamp(18px,4.8vw,22px);line-height:1.35;max-width:26em;margin:0}

/* como funciona */
.passos{list-style:none;margin:28px 0 0;padding:0;display:grid;gap:0}
.passos li{display:grid;grid-template-columns:64px 1fr;gap:14px;padding:22px 0;border-top:1px solid var(--l)}
.passos li:last-child{border-bottom:1px solid var(--l)}
.passos .n{font-family:var(--M);font-weight:900;font-size:40px;line-height:.9;color:var(--a);-webkit-text-stroke:0}
.passos .n{background:var(--v);border-radius:10px;text-align:center;padding:6px 0;height:max-content}
.passos h3{font-size:18px;margin-bottom:6px}
.passos p{margin:0;font-size:16px}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
.chips span{border:1.5px solid var(--a);color:var(--a);border-radius:99px;padding:2px 10px;font-family:var(--M);font-weight:700;font-size:11px;letter-spacing:.06em;text-transform:uppercase}

/* material */
.kit{list-style:none;margin:26px 0 0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:10px}
.kit li{border:2px solid var(--a);border-radius:18px;padding:16px}
.kit h3{font-size:14px;margin-bottom:6px}
.kit p{margin:0;font-size:14px;line-height:1.45}
.classroom{display:grid;grid-template-columns:44px 1fr;gap:14px;align-items:center;margin-top:16px;background:var(--v);border:2px solid var(--a);border-radius:18px;padding:16px 18px;color:var(--a)}
.classroom h3{font-size:15px;margin-bottom:4px}
.classroom p{margin:0;font-size:15px;line-height:1.5}
.gc{width:44px;height:44px;border-radius:12px;background:var(--a);color:var(--v);display:grid;place-items:center}
.gc svg{width:26px;height:26px}

/* quem sou */
.quem{display:grid;gap:22px}
.citacao{border-left:4px solid var(--v);padding:6px 0 6px 18px;font-family:var(--M);font-weight:800;color:var(--a);font-size:clamp(18px,4.8vw,22px);line-height:1.35;text-transform:uppercase}
.citacao small{display:block;margin-top:10px;font-family:var(--N);font-weight:600;font-size:15px;text-transform:none;color:var(--t)}

/* valores */
.planos{display:grid;gap:16px;margin-top:28px}
.plano{border:2px solid var(--a);border-radius:22px;padding:24px;background:var(--c);display:flex;flex-direction:column}
.plano.dest{background:var(--a);color:var(--c)}
.plano.dest h3,.plano.dest .val,.plano.dest .freq{color:var(--c)}
.plano .selo{align-self:flex-start;font-family:var(--M);font-weight:800;font-size:11px;letter-spacing:.12em;text-transform:uppercase;background:var(--v);color:var(--a);border-radius:99px;padding:4px 10px;margin-bottom:12px}
.plano h3{font-size:22px;margin-bottom:6px}
.plano .desc{font-size:15px;margin:0 0 18px}
.linha{display:flex;align-items:baseline;justify-content:space-between;gap:12px;padding:12px 0;border-top:1px solid var(--l)}
.plano.dest .linha{border-top-color:rgba(247,244,234,.25)}
.freq{font-family:var(--M);font-weight:800;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--a)}
.val{font-family:var(--M);font-weight:900;font-size:34px;line-height:1;letter-spacing:-.03em;color:var(--a);white-space:nowrap}
.val small{font-size:15px;letter-spacing:0;margin-right:2px}
.mensal{font-family:var(--M);font-weight:700;font-size:11px;letter-spacing:.12em;text-transform:uppercase;opacity:.8;margin:2px 0 18px}
.plano .btn{margin-top:auto}
.info{display:grid;gap:8px;margin-top:22px;font-family:var(--M);font-weight:700;font-size:13px;letter-spacing:.04em;text-transform:uppercase;color:var(--a)}

/* perguntas */
.faq{margin-top:24px;border-top:1px solid var(--l)}
.faq details{border-bottom:1px solid var(--l)}
.faq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:16px;padding:18px 0;font-family:var(--M);font-weight:800;font-size:15px;color:var(--a)}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font-size:24px;line-height:1;color:var(--a);flex:none;transition:transform .2s}
.faq details[open] summary::after{transform:rotate(45deg)}
.faq details p{margin:0 0 18px;font-size:16px;max-width:40em}

/* chamada final */
.final{border-top:0;padding:24px 0 72px}
.bloco{background:var(--a);color:var(--c);border-radius:28px;padding:44px 24px;position:relative;overflow:hidden}
.bloco .eyebrow{color:var(--c)}
.bloco h2{color:var(--c)}
.bloco p{max-width:34em}
.bloco .btns{margin-top:24px}
.bloco .globo{position:absolute;width:170px;right:-50px;bottom:-50px;opacity:.14}
.lema{margin-top:26px;font-family:var(--M);font-weight:900;font-size:14px;letter-spacing:.04em;text-transform:uppercase}
.lema span{background:var(--v);color:var(--a);padding:2px 8px}

footer{border-top:1px solid var(--l);padding:28px 0 110px;font-size:14px}
footer .wrap{display:grid;gap:10px}
footer a{color:var(--a);font-weight:800;text-decoration:none}

.flut{position:fixed;left:50%;bottom:16px;transform:translateX(-50%);width:calc(100% - 32px);max-width:520px;z-index:45;opacity:0;pointer-events:none;transition:opacity .25s}
.flut.on{opacity:1;pointer-events:auto}
.flut .btn{background:var(--v);color:var(--a);border:2px solid var(--a);box-shadow:0 10px 26px -8px rgba(0,0,0,.45)}

/* tipografia (referência Fisio & Movimento): Archivo larga nos títulos, Inter no texto, JetBrains Mono nos rótulos */
h1,h2,.passos .n,.val{font-stretch:125%;font-weight:800}
h3,.logo,.btn,.nav .cta,.box .tag,.chave,.citacao,.plano .selo,.freq,.faq summary,.lema,.faixa,b,strong{font-stretch:112%}
h3,.btn,.faq summary,.chave,.citacao{font-weight:700}
b,strong{font-weight:700}
.eyebrow,.feat,.chips span,.mensal,.info{font-family:var(--mono);font-weight:500;font-stretch:normal}
.eyebrow{font-size:12px;letter-spacing:.18em}
.chips span{font-size:11px;letter-spacing:.04em}
.citacao small,.box p,.passos p,.kit p,.plano .desc,.faq details p{font-weight:400}

@media (min-width:760px){
 .kit{grid-template-columns:repeat(4,1fr)}
 .duo{grid-template-columns:1fr 1fr}
 .planos{grid-template-columns:1fr 1fr}
 .quem{grid-template-columns:1.3fr 1fr;align-items:center}
 .btns{grid-template-columns:auto auto;justify-content:start;max-width:none}
 .btns .btn{padding:14px 28px;white-space:nowrap}
 .bloco{padding:64px 56px}
 .flut{display:none}
}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.btn,.flut,.faq summary::after{transition:none}}
"""

SYMBOLS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
 <defs>
  <filter id="stk" x="-20%" y="-20%" width="140%" height="140%">
   <feMorphology in="SourceAlpha" operator="dilate" radius="7" result="d"/>
   <feFlood flood-color="#ffffff"/><feComposite in2="d" operator="in" result="w"/>
   <feGaussianBlur in="d" stdDeviation="6" result="b"/><feOffset in="b" dy="8" result="o"/>
   <feFlood flood-color="#000" flood-opacity=".22"/><feComposite in2="o" operator="in" result="s"/>
   <feMerge><feMergeNode in="s"/><feMergeNode in="w"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
 </defs>
 <symbol id="globo" viewBox="0 0 360 360"><circle cx="180" cy="180" r="150" fill="#1F3A8F"/><g fill="none" stroke="#F7F4EA" stroke-width="7" opacity=".9"><ellipse cx="180" cy="180" rx="150" ry="150"/><ellipse cx="180" cy="180" rx="100" ry="150"/><ellipse cx="180" cy="180" rx="45" ry="150"/><path d="M30 180h300M44 115h272M44 245h272M78 70h204M78 290h204"/></g><rect x="26" y="150" width="308" height="62" fill="#C6F135" stroke="#1F3A8F" stroke-width="6" transform="rotate(-4 180 181)"/><text x="180" y="193" text-anchor="middle" font-family="Montserrat, sans-serif" font-weight="900" font-size="34" fill="#1F3A8F" letter-spacing="-1" transform="rotate(-4 180 181)">TEACHER PEDRO</text></symbol>
 <symbol id="i-wa" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4a.5.5 0 0 0 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.6-.3Z"/></symbol>
 <symbol id="i-ig" viewBox="0 0 24 24"><path fill="currentColor" d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10Zm0 8.2a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4ZM17.3 5.5a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4ZM12 3.8c2.7 0 3 0 4 .1 2.7.1 4 1.4 4.1 4.1.1 1 .1 1.3.1 4s0 3-.1 4c-.1 2.7-1.4 4-4.1 4.1-1 .1-1.3.1-4 .1s-3 0-4-.1c-2.7-.1-4-1.4-4.1-4.1-.1-1-.1-1.3-.1-4s0-3 .1-4C4 5.3 5.3 4 8 3.9c1-.1 1.3-.1 4-.1ZM12 2c-2.7 0-3.1 0-4.1.1C4.2 2.3 2.3 4.2 2.1 7.9 2 8.9 2 9.3 2 12s0 3.1.1 4.1c.2 3.7 2.1 5.6 5.8 5.8 1 .1 1.4.1 4.1.1s3.1 0 4.1-.1c3.7-.2 5.6-2.1 5.8-5.8.1-1 .1-1.4.1-4.1s0-3.1-.1-4.1c-.2-3.7-2.1-5.6-5.8-5.8C15.1 2 14.7 2 12 2Z"/></symbol>
</svg>"""

def head():
    t = "Teacher Pedro · Inglês pra viajar e pro trabalho"
    d = ("Aulas de inglês personalizadas pra quem quer viajar ou precisa do inglês no trabalho. "
         "Presencial em Mogi Guaçu, Mogi Mirim e Araras, ou online. Aula experimental gratuita.")
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{BASE}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:type" content="website">
<meta property="og:url" content="{BASE}">
<meta property="og:locale" content="pt_BR">
<meta name="theme-color" content="#F7F4EA">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Ccircle cx='32' cy='32' r='30' fill='%231F3A8F'/%3E%3Cpath d='M2 32h60M32 2v60' stroke='%23F7F4EA' stroke-width='3'/%3E%3Crect x='4' y='26' width='56' height='12' fill='%23C6F135' stroke='%231F3A8F' stroke-width='2' transform='rotate(-4 32 32)'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,500..900&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>{CSS}</style>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"LocalBusiness","name":"Teacher Pedro - Professor de Inglês","description":"{d}","url":"{BASE}","telephone":"+55-19-99715-9133","areaServed":["Mogi Guaçu","Mogi Mirim","Araras"],"sameAs":["{IGP}"],"openingHoursSpecification":[{{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"20:00"}},{{"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"08:00","closes":"12:00"}}]}}</script>
</head>"""

def faixa():
    if not FAIXA:
        return ""
    return f"""<!-- CAMPANHA: aparece só até data-ate. Para desligar, FAIXA = None no script. -->
<div class="faixa" id="faixa" data-ate="{FAIXA['ate']}"><div class="wrap">{FAIXA['texto']} · <a href="{wa(FAIXA['msg'])}" target="_blank" rel="noopener">{FAIXA['link']} →</a></div></div>"""

def btn(cls, msg_or_url, txt, icon="i-wa", ident=""):
    href = msg_or_url if msg_or_url.startswith("http") else wa(msg_or_url)
    i = f' id="{ident}"' if ident else ""
    return f'<a class="btn {cls}"{i} href="{href}" target="_blank" rel="noopener"><svg aria-hidden="true"><use href="#{icon}"/></svg>{txt}</a>'

PLANOS = [
    {"nome": "Individual", "desc": "Só você e eu. A aula no seu ritmo e no seu objetivo.",
     "precos": [("1x por semana", "280"), ("2x por semana", "400")], "dest": False},
    {"nome": "Em grupo", "desc": "Até 5 pessoas. Pra treinar com amigos, família ou colegas de trabalho.",
     "precos": [("1x por semana", "200"), ("2x por semana", "320")], "dest": True},
]

def plano(p):
    linhas = "".join(f'<div class="linha"><span class="freq">{f}</span><span class="val"><small>R$</small>{v}</span></div>' for f, v in p["precos"])
    selo = '<span class="selo">Treino junto</span>' if p["dest"] else ""
    b = btn("v", f"Oi Pedro! Vim pelo site e quero saber das aulas {'em grupo' if p['dest'] else 'individuais'}.", "Quero esse formato")
    return f"""<div class="plano{' dest' if p['dest'] else ''}">
    {selo}<h3>{p['nome']}</h3>
    <p class="desc">{p['desc']}</p>
    {linhas}
    <p class="mensal">(Valor mensal) · Aulas de 60 minutos</p>
    {b}
   </div>"""

FAQ = [
    ("Como é a aula experimental?", "É gratuita e dura 30 minutos. A gente conversa sobre pra que você precisa do inglês, eu vejo seu nível e descubro onde você trava. Daí sai o plano das suas aulas."),
    ("Serve pra viagem e pro trabalho ao mesmo tempo?", "Serve. O que muda são as situações que a gente treina: check-in e restaurante, ou reunião e entrevista. O jeito de treinar é o mesmo, e muita gente precisa dos dois."),
    ("As aulas são presenciais ou online?", "Os dois. Presencial em Mogi Guaçu, Mogi Mirim e Araras, ou online de onde você estiver."),
    ("Vou usar livro?", "Não. O material é montado pro seu objetivo e muda conforme você avança."),
]

def home():
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)
    return f"""{head()}
<body>
{SYMBOLS}
{faixa()}
<header class="nav"><div class="wrap">
 <a class="logo" href="./" aria-label="Teacher Pedro, início"><svg viewBox="0 0 360 360" aria-hidden="true"><use href="#globo"/></svg>Teacher Pedro</a>
 <a class="cta" href="{wa(MSG)}" target="_blank" rel="noopener">Aula grátis</a>
</div></header>

<section class="hero" id="topo">
 <div class="wrap">
  <p class="eyebrow">Inglês pra viajar e pro trabalho</p>
  <h1>Do “travo na hora de falar” ao <mark>“resolvi sozinho”</mark></h1>
  <p class="sub">Você já estudou inglês. Agora precisa aprender a usar. Aulas personalizadas pra quem vai viajar ou precisa do inglês no trabalho.</p>
  <div class="btns" id="cta-topo">
   {btn("v", MSG, "Quero uma aula experimental")}
   {btn("o", IG, "Me chama no direct", "i-ig")}
  </div>
  <ul class="feat"><li>Aula experimental grátis</li><li>Individual ou em grupo</li><li>Presencial ou online</li></ul>
 </div>
</section>

<section id="quem-sou">
 <div class="wrap quem">
  <div>
   <p class="eyebrow">Quem sou</p>
   <h2>Prazer, sou o Pedro</h2>
   <p>Estudei inglês por 12 anos em escola de idiomas e mesmo assim travava pra falar. Não porque eu era ruim, mas porque estudava inglês como matéria.</p>
   <p>Ensino inglês desde 2023 com um método próprio, criado por mim. Cada parte da aula tem base em evidências científicas e um objetivo: fazer você aprender do jeito que funciona melhor.</p>
   <p>Fã de Marvel, filmes, séries e música, e muito disso entra nas aulas.</p>
  </div>
  <p class="citacao">Matéria você decora pra prova. Treino você repete até sair sozinho.<small>É a minha história e a de quase todo aluno que chega pra mim.</small></p>
 </div>
</section>

<section id="pra-quem">
 <div class="wrap">
  <p class="eyebrow">Pra quem é</p>
  <h2>Você entende. <mark>Mas trava</mark> na hora de falar.</h2>
  <p class="intro">Lê, entende série com legenda, conhece os tempos verbais. Só que na hora de responder, a frase não sai.</p>
  <div class="duo">
   <div class="box"><span class="tag">Na viagem</span><h3>Se virar sem o tradutor</h3>
    <p>Aeroporto, hotel, restaurante e os imprevistos do caminho.</p>
    <p class="ex"><b>Ex.:</b> explicar no check-in que a sua reserva não aparece no sistema.</p></div>
   <div class="box"><span class="tag">No trabalho</span><h3>Falar sem travar</h3>
    <p>Reunião, call, entrevista e apresentação com o inglês que você já tem.</p>
    <p class="ex"><b>Ex.:</b> responder o "tell me about yourself" da entrevista.</p></div>
  </div>
  <p class="chave">O cenário muda. O treino é o mesmo: situações reais, repetidas até você resolver sozinho.</p>
 </div>
</section>

<section id="como-funciona">
 <div class="wrap">
  <p class="eyebrow">Como funciona</p>
  <h2>Inglês é <mark>treino</mark>, não matéria.</h2>
  <ol class="passos">
   <li><span class="n">01</span><div><h3>Aula experimental grátis</h3><p>30 minutos pra eu ouvir pra que você precisa do inglês, ver seu nível e descobrir onde você trava.</p><div class="chips"><span>30 minutos</span><span>Sem custo</span></div></div></li>
   <li><span class="n">02</span><div><h3>Plano feito pra você</h3><p>Material montado pro seu objetivo, não um livro igual pra todo mundo.</p><div class="chips"><span>Viagem</span><span>Trabalho</span><span>Os dois</span></div></div></li>
   <li><span class="n">03</span><div><h3>Treino toda semana</h3><p>Aulas de 60 minutos: você vê o modelo, treina com apoio, decide o que dizer e resolve sozinho.</p><div class="chips"><span>Modelo</span><span>Controle</span><span>Decisão</span><span>Autonomia</span></div></div></li>
  </ol>
 </div>
</section>

<section id="material">
 <div class="wrap">
  <p class="eyebrow">O material</p>
  <h2>Feito pra sua aula. <mark>Fica com você.</mark></h2>
  <p class="intro">Nada de livro igual pra todo mundo. Cada aula tem material próprio, montado pro seu objetivo e pro seu nível.</p>
  <ul class="kit">
   <li><h3>Apresentação da aula</h3><p>O que guia a aula, passo a passo.</p></li>
   <li><h3>Aula pra imprimir</h3><p>Os exercícios da aula no papel.</p></li>
   <li><h3>Flashcards</h3><p>Vocabulário e frases pra revisar e recortar.</p></li>
   <li><h3>Mapa mental</h3><p>A aula inteira resumida numa página.</p></li>
  </ul>
  <div class="classroom">
   <span class="gc" aria-hidden="true"><svg viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="10" r="2.4" fill="currentColor"/><path d="M7.5 16c.8-2 2.5-3 4.5-3s3.7 1 4.5 3" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8 21h8" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>
   <div><h3>Tudo no Google Classroom</h3><p>O plano do mês, os flashcards e o mapa mental ficam lá pra você revisar entre uma aula e outra.</p></div>
  </div>
 </div>
</section>


<section id="valores">
 <div class="wrap">
  <p class="eyebrow">Modalidades e valores</p>
  <h2>Escolhe seu formato</h2>
  <div class="planos">
   {"".join(plano(p) for p in PLANOS)}
  </div>
  <div class="info"><span>{LOCAL}</span><span>Segunda a sexta: 8H ÀS 20H</span><span>Sábado: 8H ÀS 12H</span></div>
 </div>
</section>

<section id="perguntas">
 <div class="wrap">
  <p class="eyebrow">Antes de começar</p>
  <h2>Perguntas frequentes</h2>
  <div class="faq">{faq}</div>
 </div>
</section>

<section class="final" id="contato">
 <div class="wrap">
  <div class="bloco">
   <p class="eyebrow">Bora treinar?</p>
   <h2>O primeiro passo é <mark>uma conversa</mark></h2>
   <p>Me chama e me conta pra que você precisa do inglês. Eu te mando os horários da aula experimental gratuita de 30 minutos.</p>
   <div class="btns">
    {btn("v", MSG, "Chamar no WhatsApp")}
    {btn("c", IG, "Mandar direct", "i-ig")}
   </div>
   <p class="lema"><span>Inglês é treino, não matéria.</span></p>
  </div>
 </div>
</section>

<footer><div class="wrap">
 <a class="logo" href="./"><svg viewBox="0 0 360 360" aria-hidden="true"><use href="#globo"/></svg>Teacher Pedro</a>
 <span>{LOCAL}</span>
 <span><a href="{wa(MSG)}" target="_blank" rel="noopener">WhatsApp (19) 99715-9133</a> · <a href="{IGP}" target="_blank" rel="noopener">@teacherpedrogrt</a></span>
 <span>© <span id="ano">2026</span> Teacher Pedro</span>
</div></footer>

<div class="flut" id="flut" aria-hidden="true">{btn("", MSG, "Quero uma aula experimental").replace('href=', 'tabindex="-1" href=', 1)}</div>
<script>
(function(){{
  var f=document.getElementById('faixa');
  if(f){{var ate=new Date(f.dataset.ate+'T23:59:59-03:00');if(new Date()<=ate)f.style.display='block';}}
  var a=document.getElementById('ano');if(a)a.textContent=new Date().getFullYear();
  var flut=document.getElementById('flut'),topo=document.getElementById('cta-topo'),fim=document.getElementById('contato');
  if(flut&&topo&&fim&&'IntersectionObserver' in window){{
    var vTopo=true,vFim=false;
    function upd(){{var on=!vTopo&&!vFim;flut.classList.toggle('on',on);flut.setAttribute('aria-hidden',on?'false':'true');flut.querySelector('a').tabIndex=on?0:-1;}}
    new IntersectionObserver(function(e){{vTopo=e[0].isIntersecting;upd();}}).observe(topo);
    new IntersectionObserver(function(e){{vFim=e[0].isIntersecting;upd();}}).observe(fim);
  }}
}})();
</script>
</body>
</html>
"""

# páginas antigas (viagem, trabalho, reforço, vestibular): viram atalho para a home (links antigos continuam funcionando)
REDIRECT = """<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Teacher Pedro</title><link rel="canonical" href="{base}"><meta http-equiv="refresh" content="0; url=../">
<meta name="robots" content="noindex"></head>
<body style="background:#F7F4EA;color:#1F3A8F;font-family:system-ui,sans-serif;padding:24px">
<p>Esta página agora faz parte do site principal. <a href="../">Ir para o início</a>.</p>
</body></html>
"""

with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(home())
for pasta in ("viagem", "trabalho", "reforco", "vestibular"):
    d = os.path.join(OUT, pasta)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(REDIRECT.format(base=BASE))
print("ok: index.html + redirecionamentos das páginas antigas")
