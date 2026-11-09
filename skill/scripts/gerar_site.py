# Gera o site novo do Teacher Pedro: home + 4 páginas de serviço.
import os, sys
from urllib.parse import quote

OUT = sys.argv[1] if len(sys.argv) > 1 else "site"
WA = "5519997159133"
IG = "https://ig.me/m/teacherpedrogrt"
IGP = "https://instagram.com/teacherpedrogrt"
BASE = "https://teacherpedrogrt.github.io/"
LOCAL = "Presencial em Mogi Guaçu, Mogi Mirim e Araras • Online"

def wa(msg):
    return f"https://wa.me/{WA}?text={quote(msg)}"

# ---------------------------------------------------------------- CSS
CSS = r"""
:root{--c:#F7F4EA;--a:#1F3A8F;--a2:#2A4BB5;--v:#C6F135;--txt:#24305c;--papel:#FFFDF6;--terra:#C8553D;
--grao:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .11 0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
--M:Montserrat,system-ui,sans-serif;--N:Nunito,system-ui,sans-serif;--mono:'Courier Prime','Courier New',monospace}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--c);color:var(--txt);font-family:var(--N);font-weight:600;font-size:17px;line-height:1.55;-webkit-font-smoothing:antialiased;overflow-x:hidden}
body::after{content:"";position:fixed;inset:0;background-image:var(--grao);pointer-events:none;mix-blend-mode:multiply;z-index:60}
a{color:inherit}
img,svg{max-width:100%}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}
section{position:relative;overflow:hidden;padding:64px 0}
.creme{background-color:var(--c);color:var(--txt);background-image:radial-gradient(rgba(31,58,143,.13) 1.3px,transparent 1.6px);background-size:22px 22px}
.azul{background-color:var(--a);color:var(--c);background-image:radial-gradient(rgba(247,244,234,.13) 1.3px,transparent 1.6px);background-size:22px 22px}
.verde{background:var(--v);color:var(--a)}
p{margin:0 0 14px}
b,strong{font-family:var(--M);font-weight:800;letter-spacing:-.01em}

/* rótulo pequeno (estilo VOLT) */
.label{display:inline-flex;align-items:center;gap:8px;font-family:var(--M);font-weight:800;font-size:12.5px;letter-spacing:.16em;text-transform:uppercase;margin:0 0 16px}
.label::before{content:"";width:9px;height:9px;border-radius:50%;background:var(--v);box-shadow:0 0 0 2px var(--a)}
.azul .label::before{box-shadow:0 0 0 2px var(--c)}
.verde .label::before{background:var(--a);box-shadow:none}
/* título em duas partes: linha forte + caixa de destaque */
.blk{font-family:var(--M);font-weight:900;text-transform:uppercase;font-size:clamp(28px,7.4vw,52px);line-height:1.12;letter-spacing:-.025em;margin:0 0 22px;max-width:16em}
.blk span{background:var(--a);color:var(--c);padding:0 10px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.azul .blk span{background:var(--v);color:var(--a)}
.verde .blk span{background:var(--a);color:var(--c)}
.intro{font-size:18px;max-width:36em}

/* topo e navegação */
.nav{position:sticky;top:0;z-index:45;background:var(--a);color:var(--c);border-bottom:2px solid rgba(247,244,234,.14)}
.nav .wrap{display:flex;align-items:center;justify-content:space-between;gap:14px;min-height:64px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;font-family:var(--M);font-weight:900;font-size:15px;letter-spacing:.02em;text-transform:uppercase}
.logo svg{width:42px;height:42px;flex:none}
.menu{display:none;gap:4px;font-family:var(--M);font-weight:800;font-size:12.5px;letter-spacing:.06em;text-transform:uppercase}
.menu a{text-decoration:none;padding:8px 12px;border-radius:99px}
.menu a:hover,.menu a[aria-current]{background:rgba(247,244,234,.12)}
.nav .cta{background:var(--v);color:var(--a);text-decoration:none;font-family:var(--M);font-weight:800;font-size:12px;letter-spacing:.04em;text-transform:uppercase;padding:9px 14px;border-radius:99px;white-space:nowrap}
.chips-nav{display:flex;gap:8px;overflow-x:auto;padding:0 20px 12px;scrollbar-width:none;font-family:var(--M);font-weight:800;font-size:11.5px;letter-spacing:.06em;text-transform:uppercase}
.chips-nav::-webkit-scrollbar{display:none}
.chips-nav a{flex:none;text-decoration:none;border:2px solid rgba(247,244,234,.35);border-radius:99px;padding:5px 12px}
.chips-nav a[aria-current]{background:var(--v);color:var(--a);border-color:var(--v)}

.hero{padding:44px 0 72px}
.hero-grid{display:grid;gap:40px;align-items:center}
.hero h1{font-family:var(--M);font-weight:900;text-transform:uppercase;font-size:clamp(36px,10.4vw,70px);line-height:1.02;letter-spacing:-.035em;margin:0 0 22px}
.hero h1 span{background:var(--v);color:var(--a);padding:0 8px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.hero .sub{font-size:19px;max-width:30em;margin-bottom:28px}
.btns{display:grid;gap:12px;max-width:440px}
.btn{display:flex;align-items:center;justify-content:center;gap:10px;min-height:56px;border-radius:99px;padding:14px 18px;font-family:var(--M);font-weight:800;font-size:clamp(13px,3.6vw,15px);text-align:center;text-decoration:none;text-transform:uppercase;transition:transform .15s}
.btn:hover{transform:translateY(-2px)}
.btn svg{width:22px;height:22px;flex:none}
.btn.v{background:var(--v);color:var(--a);box-shadow:0 10px 24px -10px rgba(0,0,0,.45)}
.btn.o{border:2px solid currentColor}
.btn.a{background:var(--a);color:var(--c)}
.local{margin-top:20px;font-size:15px;opacity:.88}
.feat{display:flex;flex-wrap:wrap;gap:8px;margin-top:26px}
.feat span{border:2px solid rgba(247,244,234,.4);border-radius:99px;padding:5px 12px;font-family:var(--M);font-weight:700;font-size:11.5px;letter-spacing:.05em;text-transform:uppercase}

/* faixa campanha */
.faixa{display:none;background:var(--v);color:var(--a);padding:12px 0;text-align:center;font-family:var(--M);font-weight:800;font-size:13.5px;line-height:1.45}
.faixa a{text-decoration:underline;text-underline-offset:3px;text-transform:uppercase;white-space:nowrap}

/* faixa de palavras correndo */
.marq{background:var(--v);color:var(--a);border-top:3px solid var(--a);border-bottom:3px solid var(--a);overflow:hidden;padding:14px 0}
.marq-in{display:flex;width:max-content;animation:corre 32s linear infinite}
.marq span{font-family:var(--M);font-weight:900;font-size:22px;text-transform:uppercase;letter-spacing:-.01em;white-space:nowrap;padding-right:22px}
.marq span::after{content:"✦";margin-left:22px}
@keyframes corre{to{transform:translateX(-50%)}}

/* colagem: objetos de papel */
.colbox{position:relative;height:310px}
.colagem{position:absolute;left:50%;top:0;width:480px;height:420px;transform:translateX(-50%) scale(.72);transform-origin:top center}
.obj{position:absolute;box-shadow:0 18px 30px -16px rgba(0,0,0,.55);color:var(--a)}
.mono{font-family:var(--mono)}
.pass{display:flex;width:300px;border-radius:14px;overflow:hidden;background:var(--papel)}
.pass-main{padding:16px 18px;flex:1}
.pass small{display:block;font-family:var(--M);font-weight:800;font-size:9.5px;letter-spacing:.14em}
.pass strong{display:block;white-space:nowrap;font-family:var(--M);font-weight:900;font-size:36px;letter-spacing:-.02em;line-height:1.1;margin:6px 0}
.pass-stub{background:var(--v);width:78px;border-left:2px dashed var(--a);display:grid;place-content:center;text-align:center}
.pass-stub b{font-size:34px;line-height:1}
.recibo{width:220px;background:var(--papel);padding:16px 16px 26px;font-family:var(--mono);font-size:13px;line-height:1.55;-webkit-mask:linear-gradient(#000 0 0) top/100% calc(100% - 10px) no-repeat,conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) bottom/16px 10px repeat-x;mask:linear-gradient(#000 0 0) top/100% calc(100% - 10px) no-repeat,conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) bottom/16px 10px repeat-x}
.recibo .rt{text-align:center;font-weight:700;letter-spacing:.2em;border-bottom:1px dashed var(--a);padding-bottom:6px;margin-bottom:8px}
.recibo p{margin:0;white-space:nowrap}
.passaporte{width:150px;height:205px;background:var(--a);border-radius:10px 14px 14px 10px;color:var(--c);display:grid;place-items:center;text-align:center;font-family:Georgia,serif;letter-spacing:.2em;font-size:13px;padding:20px 10px;border:2px solid var(--c)}
.passaporte i{display:block;width:56px;height:56px;border:2px solid #E8D9A8;border-radius:50%;margin:6px auto;color:#E8D9A8;font-style:normal;font-size:24px;line-height:52px}
.cracha{width:200px;background:var(--papel);border-radius:14px;overflow:hidden;text-align:center;border:3px solid var(--a)}
.cracha .top{background:var(--a);color:var(--c);padding:12px 8px 8px;font-family:var(--M);font-weight:900;font-size:26px;letter-spacing:.04em;line-height:1}
.cracha .top small{display:block;font-size:11px;letter-spacing:.12em;font-weight:800;margin-top:4px}
.cracha .nome{display:block;font-family:var(--mono);font-style:italic;font-size:30px;padding:16px 8px 18px;color:var(--a)}
.cracha .furo{width:44px;height:8px;border-radius:9px;background:var(--c);margin:0 auto 8px;border:2px solid rgba(247,244,234,.5)}
.convite{width:240px;background:var(--papel);border-radius:14px;padding:14px 16px;border-left:10px solid var(--v)}
.convite small{font-family:var(--M);font-weight:800;font-size:10px;letter-spacing:.14em;display:block}
.convite b{display:block;font-size:20px;margin:4px 0 2px;text-transform:uppercase}
.convite span{font-size:13px;color:var(--txt)}
.convite .rsvp{display:flex;gap:8px;margin-top:10px}
.convite .rsvp i{font-style:normal;font-family:var(--M);font-weight:800;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;border:2px solid var(--a);border-radius:99px;padding:3px 10px}
.convite .rsvp i:first-child{background:var(--a);color:var(--c)}
.prova{width:250px;background:var(--papel);padding:16px 18px 18px;background-image:repeating-linear-gradient(transparent 0 25px,rgba(31,58,143,.14) 25px 26px);font-family:var(--mono);font-size:13px;line-height:26px}
.prova .pt{font-family:var(--M);font-weight:900;font-size:16px;letter-spacing:.06em;display:flex;justify-content:space-between;line-height:1.3;margin-bottom:6px}
.prova p{margin:0}
.prova u{text-decoration-color:var(--v);text-decoration-thickness:4px;text-underline-offset:2px;font-style:italic}
.gabarito{width:220px;background:var(--papel);padding:14px 16px;font-family:var(--M);font-weight:800}
.gabarito .gt{font-weight:900;font-size:13px;letter-spacing:.14em;border-bottom:2px solid var(--a);padding-bottom:6px;margin-bottom:8px}
.gab-l{display:flex;align-items:center;gap:7px;font-size:11px;margin:5px 0}
.gab-l em{font-style:normal;width:22px}
.gab-l i{width:18px;height:18px;border:2px solid var(--a);border-radius:50%;font-style:normal;font-size:9px;display:grid;place-items:center}
.gab-l i.x{background:var(--a);color:var(--a)}
.sel{width:110px}
.carimbo{font-family:var(--M);font-weight:900;font-size:15px;letter-spacing:.08em;text-transform:uppercase;border:3px solid currentColor;border-radius:8px;padding:6px 10px;background:rgba(255,253,246,.92);box-shadow:none}
.carimbo.ok{color:#2f7a3e}
.carimbo.t{color:var(--terra)}
.marca-mao{position:absolute;pointer-events:none;overflow:visible}

/* cards de público (estilo VOLT, com "EX.:") */
.publico{display:grid;gap:16px;margin-top:10px}
.pub{position:relative;display:flex;flex-direction:column;background:var(--papel);border:3px solid var(--a);border-radius:24px;padding:24px 22px 22px;text-decoration:none;box-shadow:0 18px 34px -24px rgba(0,0,0,.6);transition:transform .18s}
.pub:hover{transform:translateY(-4px) rotate(-.4deg)}
.pub .tag{align-self:flex-start;font-family:var(--M);font-weight:800;font-size:11px;letter-spacing:.12em;text-transform:uppercase;background:var(--a);color:var(--c);border-radius:99px;padding:4px 10px;margin-bottom:14px}
.pub h3{font-family:var(--M);font-weight:900;font-size:clamp(24px,6.4vw,30px);line-height:1.05;letter-spacing:-.02em;text-transform:uppercase;color:var(--a);margin:0 0 10px}
.pub p{font-size:16px;margin:0 0 14px}
.pub .ex{font-size:14.5px;border-top:2px dashed rgba(31,58,143,.35);padding-top:12px;margin-top:auto}
.pub .ex b{font-size:12px;letter-spacing:.12em}
.pub .ir{display:inline-flex;align-items:center;gap:8px;margin-top:14px;font-family:var(--M);font-weight:800;font-size:13px;letter-spacing:.04em;text-transform:uppercase;color:var(--a)}
.pub .ir::after{content:"→";transition:transform .18s}
.pub:hover .ir::after{transform:translateX(4px)}
.pub.v{background:var(--v)}
.pub.a{background:var(--a);color:var(--c);border-color:var(--a)}
.pub.a h3,.pub.a .ir{color:var(--v)}
.pub.a .tag{background:var(--v);color:var(--a)}
.pub.a .ex{border-color:rgba(247,244,234,.3)}
.pub .ico{position:absolute;right:14px;top:14px;width:64px;transform:rotate(8deg)}

/* quem sou */
.quem-grid{display:grid;gap:34px;align-items:start}
.tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:20px}
.tags span{background:var(--v);color:var(--a);border-radius:99px;padding:5px 14px;font-family:var(--M);font-weight:800;font-size:12px;letter-spacing:.04em;text-transform:uppercase}
.creme .tags span{background:var(--a);color:var(--c)}
.citacao{position:relative;background:var(--papel);color:var(--a);border-radius:6px;padding:30px 26px 26px;transform:rotate(-1.5deg);box-shadow:0 22px 40px -22px rgba(0,0,0,.6);font-family:var(--M);font-weight:900;text-transform:uppercase;font-size:clamp(24px,6vw,34px);line-height:1.08;letter-spacing:-.02em}
.citacao::before{content:"";position:absolute;top:-14px;left:50%;width:110px;height:28px;transform:translateX(-50%) rotate(2deg);background:rgba(198,241,53,.85)}
.citacao mark{background:var(--v);color:var(--a);padding:0 6px}
.citacao small{display:block;margin-top:16px;font-family:var(--N);font-weight:700;font-size:15px;letter-spacing:0;text-transform:none;color:var(--txt)}

/* blocos numerados grandes (estilo VOLT) */
.nums{display:grid;gap:14px;margin-top:10px;counter-reset:n}
.num{counter-increment:n;position:relative;border-top:3px solid currentColor;padding:18px 0 6px}
.num::before{content:"0" counter(n);display:block;font-family:var(--M);font-weight:900;font-size:clamp(54px,14vw,84px);line-height:.9;letter-spacing:-.05em;color:var(--a);margin-bottom:10px}
.azul .num::before{color:var(--v)}
.num h3{font-family:var(--M);font-weight:900;font-size:20px;text-transform:uppercase;letter-spacing:-.01em;margin:0 0 6px}
.num p{margin:0;font-size:16px}

/* método */
.lema{font-family:var(--M);font-weight:900;text-transform:uppercase;font-size:clamp(32px,9vw,62px);line-height:1;letter-spacing:-.03em;margin:4px 0 24px}
.lema mark{background:var(--v);color:var(--a);padding:0 8px}
.metodo-grid{display:grid;gap:30px}
.passos{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:10px}
.passos li{display:grid;grid-template-columns:40px 1fr;gap:12px;align-items:start;background:rgba(247,244,234,.07);border:2px solid rgba(247,244,234,.22);border-radius:18px;padding:14px 16px}
.passos .n{font-family:var(--M);font-weight:900;font-size:26px;line-height:1;color:var(--v)}
.passos h3{margin:0 0 2px;font-family:var(--M);font-weight:800;font-size:16px;text-transform:uppercase;letter-spacing:.02em}
.passos p{margin:0;font-size:15px;opacity:.92}
.aulas{display:grid;gap:14px}
.ficha{background:var(--papel);color:var(--a);border-radius:4px;padding:18px 18px 16px;font-family:var(--mono);font-size:14px;box-shadow:0 20px 34px -20px rgba(0,0,0,.6)}
.ficha:nth-child(1){transform:rotate(-1.2deg)}
.ficha:nth-child(2){transform:rotate(1deg)}
.ficha .ft{display:flex;justify-content:space-between;align-items:baseline;gap:10px;font-family:var(--M);font-weight:900;font-size:14px;letter-spacing:.08em;text-transform:uppercase;border-bottom:2px solid var(--a);padding-bottom:8px;margin-bottom:8px}
.ficha .ft small{font-weight:800;font-size:10.5px;letter-spacing:.12em;background:var(--v);padding:3px 8px;border-radius:99px;white-space:nowrap}
.ficha ol{margin:0;padding:0 0 0 22px}
.ficha li{padding:3px 0;border-bottom:1px dashed rgba(31,58,143,.25)}
.ficha li:last-child{border:0}
.ficha .leg{font-family:var(--N);font-size:13.5px;color:var(--txt);margin:10px 0 0}
.ficha .mo{display:grid;gap:8px;margin:0;padding:0;list-style:none}
.ficha .mo li{border:0;display:grid;grid-template-columns:auto 1fr;gap:10px;align-items:baseline}
.ficha .mo b{font-family:var(--M);font-size:11px;letter-spacing:.1em;background:var(--a);color:var(--c);padding:3px 8px;border-radius:99px;white-space:nowrap}

/* dores */
.dores{display:grid;gap:14px;margin-top:8px}
.dor{position:relative;background:var(--papel);border-radius:20px 20px 20px 4px;padding:20px 22px;border:3px solid var(--a);font-family:var(--M);font-weight:800;font-size:18px;line-height:1.3;color:var(--a);box-shadow:0 16px 28px -22px rgba(0,0,0,.6)}
.dor:nth-child(2){border-radius:20px 20px 4px 20px;background:var(--v)}
.virada{margin-top:30px;font-family:var(--M);font-weight:900;text-transform:uppercase;font-size:clamp(22px,5.8vw,34px);line-height:1.12;letter-spacing:-.02em;max-width:22em;color:var(--a)}
.virada mark{background:var(--v);color:var(--a);padding:0 6px;box-decoration-break:clone;-webkit-box-decoration-break:clone}

.situ{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 0}
.situ span{border:2px solid currentColor;border-radius:99px;padding:6px 13px;font-family:var(--M);font-weight:800;font-size:12.5px;letter-spacing:.04em;text-transform:uppercase}
.split{display:grid;gap:34px;align-items:start}

/* como funciona */
.etapas{list-style:none;margin:0;padding:0;counter-reset:e;display:grid;gap:14px}
.etapas li{counter-increment:e;position:relative;background:var(--c);color:var(--txt);border-radius:22px;padding:18px 18px 18px 70px;box-shadow:0 14px 28px -18px rgba(0,0,0,.5)}
.etapas li::before{content:counter(e);position:absolute;left:16px;top:16px;width:40px;height:40px;border-radius:50%;background:var(--a);color:var(--v);font-family:var(--M);font-weight:900;font-size:20px;display:grid;place-items:center}
.etapas h3{margin:0 0 4px;font-family:var(--M);font-weight:800;font-size:15px;letter-spacing:.02em;text-transform:uppercase;color:var(--a)}
.etapas p{margin:0;font-size:15px}

/* valores */
.cards{display:grid;gap:16px;margin-top:6px}
.card{background:#fff;border-radius:24px;padding:22px;box-shadow:0 20px 40px -24px rgba(0,0,0,.45);border:3px solid var(--a)}
.card.dest{background:var(--v)}
.card .tit{font-family:var(--M);font-weight:900;font-size:22px;text-transform:uppercase;color:var(--a);margin:0 0 2px;letter-spacing:-.01em}
.card .desc{font-size:15px;margin:0 0 16px;color:var(--txt)}
.precos{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.preco{background:var(--c);border-radius:16px;padding:14px 12px;color:var(--a)}
.card.dest .preco{background:rgba(255,255,255,.65)}
.preco .freq{font-family:var(--M);font-weight:800;font-size:12px;letter-spacing:.08em;text-transform:uppercase;opacity:.8}
.preco .val{font-family:var(--M);font-weight:900;font-size:34px;line-height:1.05;letter-spacing:-.03em;white-space:nowrap}
.preco .val small{font-size:15px;margin-right:2px;letter-spacing:0}
.preco .mes{font-size:13px}
.card.combina{background:var(--a);color:var(--c);border-color:var(--a)}
.card.combina .tit{color:var(--v)}
.card.combina .desc{color:var(--c)}
.obs{font-size:14.5px;margin-top:18px}
.info{display:grid;gap:12px;margin-top:22px;align-items:start}
.formato{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.formato div{border:3px solid var(--a);border-radius:18px;padding:14px;text-align:center;color:var(--a);background:rgba(255,253,246,.7)}
.formato b{display:block;font-size:15px;text-transform:uppercase}
.formato span{font-size:13.5px}
.horas{display:grid;gap:8px}
.hora{display:flex;justify-content:space-between;align-items:center;gap:12px;background:#fff;color:var(--a);border-radius:16px;padding:13px 16px;border:2px solid var(--a)}
.hora b{font-size:14px;text-transform:uppercase}
.hora span{font-family:var(--M);font-weight:900;font-size:19px;letter-spacing:-.02em;white-space:nowrap}
.hora.off{background:transparent;border-style:dashed}

/* perguntas frequentes */
.faq{display:grid;gap:10px;margin-top:8px;max-width:820px}
.faq details{background:rgba(247,244,234,.07);border:2px solid rgba(247,244,234,.25);border-radius:18px;padding:0 18px}
.faq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:14px;padding:16px 0;font-family:var(--M);font-weight:800;font-size:16px;text-transform:uppercase;letter-spacing:.01em}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";flex:none;width:30px;height:30px;border-radius:50%;background:var(--v);color:var(--a);display:grid;place-items:center;font-size:20px;transition:transform .2s}
.faq details[open] summary::after{transform:rotate(45deg)}
.faq details p{margin:0 0 16px;font-size:16px;opacity:.95}

/* final */
.final{padding-bottom:40px}
.final-grid{display:grid;gap:30px;align-items:center}
.assina{margin-top:34px;font-family:var(--M);font-weight:900;text-transform:uppercase;font-size:15px;letter-spacing:.04em}
.assina span{background:var(--a);color:var(--v);padding:3px 9px}
.azul .assina span{background:var(--v);color:var(--a)}
.rodape{background:#162b6b;color:var(--c);padding:40px 0 110px;font-size:14px}
.rod-grid{display:grid;gap:26px}
.rodape .logo{margin-bottom:10px}
.rodape h4{font-family:var(--M);font-weight:800;font-size:12px;letter-spacing:.14em;text-transform:uppercase;margin:0 0 10px;opacity:.7}
.rodape ul{list-style:none;margin:0;padding:0;display:grid;gap:6px}
.rodape a{text-decoration:none}
.rodape a:hover{text-decoration:underline}
.copy{margin-top:26px;opacity:.6;font-size:13px}

.ico{position:absolute;pointer-events:none}
.ico svg{width:100%;height:auto;display:block;overflow:visible}

/* botão flutuante (celular) */
.flut{position:fixed;left:50%;bottom:16px;transform:translateX(-50%);width:calc(100% - 32px);max-width:440px;z-index:40;opacity:0;pointer-events:none;transition:opacity .25s}
.flut.on{opacity:1;pointer-events:auto}
.flut .btn{background:var(--v);color:var(--a);box-shadow:0 12px 30px -8px rgba(0,0,0,.55);border:2px solid var(--a)}

@media (min-width:760px){
 .wrap{padding:0 32px}
 section{padding:96px 0}
 .publico{grid-template-columns:1fr 1fr}
 .dores{grid-template-columns:repeat(3,1fr)}
 .nums{grid-template-columns:repeat(3,1fr);gap:30px}
 .etapas{grid-template-columns:1fr 1fr}
 .cards{grid-template-columns:1fr 1fr}
 .info{grid-template-columns:1fr 1fr}
 .aulas{grid-template-columns:1fr 1fr}
 .rod-grid{grid-template-columns:1.4fr 1fr 1fr}
 .chips-nav{padding:0 32px 12px}
 .colbox{height:400px}
 .colagem{transform:translateX(-50%) scale(.92)}
}
@media (min-width:980px){
 .menu{display:flex}
 .chips-nav{display:none}
 .hero{padding:72px 0 100px}
 .hero-grid{grid-template-columns:1.15fr .85fr}
 .colbox{height:440px}
 .colagem{transform:translateX(-50%) scale(1.02)}
 .quem-grid,.split,.final-grid{grid-template-columns:1.1fr .9fr;gap:60px}
 .metodo-grid{grid-template-columns:.9fr 1.1fr;gap:60px}
 .flut{display:none}
 .rodape{padding-bottom:40px}
 .publico.home{grid-template-columns:repeat(6,1fr)}
 .publico.home .pub:nth-child(1),.publico.home .pub:nth-child(2){grid-column:span 3;min-height:300px}
 .publico.home .pub:nth-child(3),.publico.home .pub:nth-child(4){grid-column:span 3}
}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.btn,.flut,.pub{transition:none}.marq-in{animation:none}}
"""

# ---------------------------------------------------------------- símbolos
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
 <symbol id="i-chat" viewBox="0 0 260 220"><g stroke="#1F3A8F" stroke-width="8" stroke-linejoin="round"><path d="M20 20h150a16 16 0 0 1 16 16v70a16 16 0 0 1-16 16H80l-40 32v-32H20z" fill="#F7F4EA"/><path d="M110 92h114a16 16 0 0 1 16 16v60a16 16 0 0 1-16 16h-14v30l-36-30h-64a16 16 0 0 1-16-16z" fill="#C6F135"/></g><text x="98" y="80" text-anchor="middle" font-family="Montserrat" font-weight="900" font-size="34" fill="#1F3A8F">hi!</text><text x="170" y="150" text-anchor="middle" font-family="Montserrat" font-weight="900" font-size="34" fill="#1F3A8F">hey!</text></symbol>
 <symbol id="i-bag" viewBox="0 0 220 260"><g stroke="#1F3A8F" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"><path d="M80 50V22h60v28" fill="none"/><rect x="30" y="50" width="160" height="180" rx="18" fill="#F7F4EA"/><path d="M75 50v180M145 50v180" fill="none"/><rect x="30" y="118" width="160" height="34" fill="#C6F135"/><circle cx="62" cy="240" r="10" fill="#1F3A8F"/><circle cx="158" cy="240" r="10" fill="#1F3A8F"/></g></symbol>
 <symbol id="i-togo" viewBox="0 0 200 240"><g stroke="#1F3A8F" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"><rect x="38" y="20" width="124" height="26" rx="8" fill="#F7F4EA"/><path d="M48 46h104l-14 176a10 10 0 0 1-10 9H72a10 10 0 0 1-10-9z" fill="#F7F4EA"/><path d="M53 100h94l-6 64H59z" fill="#C6F135"/></g><text x="100" y="142" text-anchor="middle" font-family="Montserrat" font-weight="900" font-size="26" fill="#1F3A8F">TO GO</text></symbol>
 <symbol id="i-mala" viewBox="0 0 240 200"><g stroke="#1F3A8F" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"><path d="M88 46V24h64v22" fill="none"/><rect x="18" y="46" width="204" height="138" rx="16" fill="#C6F135"/><path d="M18 96h204" fill="none"/><rect x="104" y="84" width="32" height="24" rx="4" fill="#F7F4EA"/></g></symbol>
 <symbol id="i-lapis" viewBox="0 0 260 80"><g stroke="#1F3A8F" stroke-width="7" stroke-linejoin="round"><path d="M40 14h170v52H40z" fill="#C6F135"/><path d="M210 14l40 26-40 26z" fill="#F7F4EA"/><path d="M238 33l12 7-12 7z" fill="#1F3A8F"/><rect x="10" y="14" width="30" height="52" rx="6" fill="#F7F4EA"/><path d="M40 40h170" fill="none"/></g></symbol>
 <symbol id="i-wa" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4a.5.5 0 0 0 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.6-.3Z"/></symbol>
 <symbol id="i-ig" viewBox="0 0 24 24"><path fill="currentColor" d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10Zm0 8.2a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4ZM17.3 5.5a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4ZM12 3.8c2.7 0 3 0 4 .1 2.7.1 4 1.4 4.1 4.1.1 1 .1 1.3.1 4s0 3-.1 4c-.1 2.7-1.4 4-4.1 4.1-1 .1-1.3.1-4 .1s-3 0-4-.1c-2.7-.1-4-1.4-4.1-4.1-.1-1-.1-1.3-.1-4s0-3 .1-4C4 5.3 5.3 4 8 3.9c1-.1 1.3-.1 4-.1ZM12 2c-2.7 0-3.1 0-4.1.1C4.2 2.3 2.3 4.2 2.1 7.9 2 8.9 2 9.3 2 12s0 3.1.1 4.1c.2 3.7 2.1 5.6 5.8 5.8 1 .1 1.4.1 4.1.1s3.1 0 4.1-.1c3.7-.2 5.6-2.1 5.8-5.8.1-1 .1-1.4.1-4.1s0-3.1-.1-4.1c-.2-3.7-2.1-5.6-5.8-5.8C15.1 2 14.7 2 12 2Z"/></symbol>
</svg>"""

def sticker(sym, vb, cls_style):
    return f'<div class="ico" style="{cls_style}" aria-hidden="true"><svg viewBox="{vb}" filter="url(#stk)"><use href="#{sym}"/></svg></div>'

# marcas feitas à mão (SVG solto)
def circulo(style, cor="#C6F135"):
    return f'<svg class="marca-mao" style="{style}" viewBox="0 0 200 80" aria-hidden="true"><path d="M30 44C26 18 120 6 168 22s12 44-60 48S20 62 34 30" fill="none" stroke="{cor}" stroke-width="6" stroke-linecap="round"/></svg>'
def seta(style, cor="#C6F135"):
    return f'<svg class="marca-mao" style="{style}" viewBox="0 0 120 120" aria-hidden="true"><path d="M14 20c40-6 74 20 80 72M78 78l16 16 14-22" fill="none" stroke="{cor}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def estrela(style, cor="#C6F135"):
    return f'<svg class="marca-mao" style="{style}" viewBox="0 0 100 100" aria-hidden="true"><path d="M50 8l11 28 30 2-23 19 8 30-26-17-26 17 8-30L9 38l30-2z" fill="none" stroke="{cor}" stroke-width="6" stroke-linejoin="round"/></svg>'
def check(style, cor="#1F3A8F"):
    return f'<svg class="marca-mao" style="{style}" viewBox="0 0 100 80" aria-hidden="true"><path d="M10 44l26 24L90 10" fill="none" stroke="{cor}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></svg>'

# objetos
PASS = '<div class="pass"><div class="pass-main"><small>Boarding pass · Gate B12</small><strong>GRU → JFK</strong><small>Seat 23A · Boarding 21:40</small></div><div class="pass-stub"><small>Zone</small><b>3</b></div></div>'
def recibo(titulo, linhas):
    ls = "".join(f"<p>{l}</p>" for l in linhas)
    return f'<div class="recibo"><p class="rt">{titulo}</p>{ls}</div>'
PASSAPORTE = '<div class="passaporte"><div>PASSPORT<i>✦</i>TRAVEL<br>DOCUMENT</div></div>'
CRACHA = '<div class="cracha"><div class="top"><div class="furo"></div>HELLO<small>my name is</small></div><span class="nome">you</span></div>'
CONVITE = '<div class="convite"><small>Invite · 10:00 AM</small><b>Job interview</b><span>Video call · 45 min</span><div class="rsvp"><i>Accept</i><i>Decline</i></div></div>'
CONVITE2 = '<div class="convite"><small>Meeting · Monday 9:00</small><b>Weekly sync</b><span>Your turn to present</span><div class="rsvp"><i>Accept</i><i>Maybe</i></div></div>'
PROVA = '<div class="prova"><div class="pt"><span>ENGLISH TEST</span><span>#2</span></div><p>Name: __________</p><p>1. Complete:</p><p>Yesterday I <u>went</u> to school.</p><p>2. She <u>doesn\'t</u> like coffee.</p><p>3. Read and answer...</p></div>'
def gabarito(titulo="ANSWER SHEET"):
    linhas = []
    marcadas = [2, 0, 3, 1, 4]
    for i, m in enumerate(marcadas):
        bol = "".join(f'<i class="{"x" if j == m else ""}">{"ABCDE"[j]}</i>' for j in range(5))
        linhas.append(f'<div class="gab-l"><em>{i+1:02d}</em>{bol}</div>')
    return f'<div class="gabarito"><div class="gt">{titulo}</div>{"".join(linhas)}</div>'

def pos(html, style):
    # posiciona um objeto dentro da colagem
    return html.replace('class="', f'style="{style}" class="obj ', 1)

def colagem(itens):
    return '<div class="colbox" aria-hidden="true"><div class="colagem">' + "".join(itens) + "</div></div>"

# ---------------------------------------------------------------- partes comuns
PAGES = [("", "Início"), ("viagem/", "Viagem"), ("trabalho/", "Trabalho"), ("reforco/", "Reforço escolar"), ("vestibular/", "Vestibular e ENEM")]

def head(title, desc, canonical):
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{BASE}{canonical}">
<meta property="og:locale" content="pt_BR">
<meta name="theme-color" content="#1F3A8F">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Ccircle cx='32' cy='32' r='30' fill='%231F3A8F'/%3E%3Cpath d='M2 32h60M32 2v60' stroke='%23F7F4EA' stroke-width='3'/%3E%3Crect x='4' y='26' width='56' height='12' fill='%23C6F135' stroke='%231F3A8F' stroke-width='2' transform='rotate(-4 32 32)'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800;900&family=Nunito:wght@600;700;800&family=Courier+Prime:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>{CSS}</style>
"""

def schema():
    return """<script type="application/ld+json">{"@context":"https://schema.org","@type":"LocalBusiness","name":"Teacher Pedro - Professor de Inglês","description":"Aulas de inglês para viagem, trabalho, reforço escolar e vestibular. Presencial em Mogi Guaçu, Mogi Mirim e Araras, ou online.","url":"https://teacherpedrogrt.github.io/","telephone":"+55-19-99715-9133","areaServed":["Mogi Guaçu","Mogi Mirim","Araras"],"sameAs":["https://instagram.com/teacherpedrogrt"],"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"20:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"08:00","closes":"12:00"}]}</script>"""

def rel(atual, destino):
    # caminho relativo entre páginas
    prefixo = "../" if atual else ""
    return prefixo + destino if destino else (prefixo or "./")

def nav(atual, msg, cta="Aula experimental"):
    links = "".join(
        f'<a href="{rel(atual, p)}"{" aria-current=\"page\"" if p == atual else ""}>{n}</a>'
        for p, n in PAGES[1:])
    chips = "".join(
        f'<a href="{rel(atual, p)}"{" aria-current=\"page\"" if p == atual else ""}>{n}</a>'
        for p, n in PAGES[1:])
    return f"""<header class="nav">
 <div class="wrap">
  <a class="logo" href="{rel(atual, '')}" aria-label="Teacher Pedro, página inicial"><svg viewBox="0 0 360 360" aria-hidden="true"><use href="#globo"/></svg></a>
  <nav class="menu" aria-label="Serviços">{links}</nav>
  <a class="cta" href="{wa(msg)}" target="_blank" rel="noopener">{cta}</a>
 </div>
 <nav class="chips-nav" aria-label="Serviços">{chips}</nav>
</header>"""

def faixa(ativa):
    if not ativa:
        return ""
    return f"""<!-- CAMPANHA: aparece só até a data em data-ate (AAAA-MM-DD). Para desligar, apague o bloco. -->
<div class="faixa" id="faixa" data-ate="2026-11-30">
 <div class="wrap">Black Friday · Primeira mensalidade com desconto até 30/11 · Individual a partir de R$ 230 · Grupo a partir de R$ 150 · <a href="{wa('Oi Pedro! Vim pelo site e quero saber da Black Friday.')}" target="_blank" rel="noopener">Quero aproveitar →</a></div>
</div>"""

def botoes(msg, txt1="Quero uma aula experimental", txt2="Me chama no direct", ident=""):
    i = f' id="{ident}"' if ident else ""
    return f"""<div class="btns"{i}>
   <a class="btn v" href="{wa(msg)}" target="_blank" rel="noopener"><svg aria-hidden="true"><use href="#i-wa"/></svg>{txt1}</a>
   <a class="btn o" href="{IG}" target="_blank" rel="noopener"><svg aria-hidden="true"><use href="#i-ig"/></svg>{txt2}</a>
  </div>"""

def marquee(palavras):
    s = "".join(f"<span>{p}</span>" for p in palavras)
    return f'<div class="marq" aria-hidden="true"><div class="marq-in">{s}{s}</div></div>'

ETAPAS_ESCOLA = [("A gente combina", "Conteúdo, dias, horários e valores, de acordo com o que o aluno precisa."), ("Aula no ritmo do aluno", "Diagnóstico do que ele já sabe, explicação e exercícios até fazer sentido."), ("Treino até a prova", "O mesmo conteúdo em situações diferentes, até ele resolver sem ajuda.")]

def etapas(passo1, resto=None):
    if resto:
        lis = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in resto)
        return f'<ol class="etapas"><li><h3>Você me chama</h3><p>{passo1}</p></li>{lis}</ol>'
    return f"""<ol class="etapas">
   <li><h3>Você me chama</h3><p>{passo1}</p></li>
   <li><h3>Aula experimental gratuita</h3><p>30 minutos pra eu entender seu objetivo, ver seu nível e descobrir onde você trava.</p></li>
   <li><h3>Plano feito pra você</h3><p>Material montado pro seu objetivo, não um livro igual pra todo mundo.</p></li>
   <li><h3>Treino toda semana</h3><p>Aulas de 60 minutos que alternam construção (vocabulário e estruturas) e prática real (simulações das suas situações).</p></li>
  </ol>"""

FORMATO = """<div class="formato">
     <div><b>Presencial</b><span>Mogi Guaçu, Mogi Mirim e Araras</span></div>
     <div><b>Online</b><span>De onde você estiver</span></div>
    </div>"""
HORAS = """<div class="horas">
     <div class="hora"><b>Segunda a sexta</b><span>8H ÀS 20H</span></div>
     <div class="hora"><b>Sábado</b><span>8H ÀS 12H</span></div>
     <div class="hora off"><b>Domingo</b><span>OFF</span></div>
    </div>"""

def valores(msg_combina, obs):
    return f"""<section class="valores creme" id="valores">
 <div class="wrap">
  <p class="label">Modalidades e valores</p>
  <h2 class="blk">Escolhe <span>seu formato</span></h2>
  <div class="cards">
   <div class="card">
    <p class="tit">Individual</p>
    <p class="desc">Só você e eu. Aula no seu ritmo e no seu objetivo.</p>
    <div class="precos">
     <div class="preco"><div class="freq">1x por semana</div><div class="val"><small>R$</small>280</div><div class="mes">Por mês</div></div>
     <div class="preco"><div class="freq">2x por semana</div><div class="val"><small>R$</small>400</div><div class="mes">Por mês</div></div>
    </div>
   </div>
   <div class="card dest">
    <p class="tit">Em grupo</p>
    <p class="desc">Até 5 pessoas. Pra treinar com amigos, família ou colegas de trabalho.</p>
    <div class="precos">
     <div class="preco"><div class="freq">1x por semana</div><div class="val"><small>R$</small>200</div><div class="mes">Por mês</div></div>
     <div class="preco"><div class="freq">2x por semana</div><div class="val"><small>R$</small>320</div><div class="mes">Por mês</div></div>
    </div>
   </div>
  </div>
  <p class="obs">{obs}</p>
  <div class="info">
   {FORMATO}
   {HORAS}
  </div>
 </div>
</section>"""

def rodape(atual, msg):
    links = "".join(f'<li><a href="{rel(atual, p)}">{n}</a></li>' for p, n in PAGES)
    return f"""<footer class="rodape">
 <div class="wrap">
  <div class="rod-grid">
   <div>
    <a class="logo" href="{rel(atual, '')}"><svg viewBox="0 0 360 360" aria-hidden="true"><use href="#globo"/></svg>Teacher Pedro</a>
    <p>Aulas de inglês personalizadas. {LOCAL}.</p>
   </div>
   <div><h4>Objetivos</h4><ul>{links}</ul></div>
   <div><h4>Contato</h4><ul>
    <li><a href="{wa(msg)}" target="_blank" rel="noopener">WhatsApp (19) 99715-9133</a></li>
    <li><a href="{IGP}" target="_blank" rel="noopener">Instagram @teacherpedrogrt</a></li>
   </ul></div>
  </div>
  <p class="copy">© <span id="ano">2026</span> Teacher Pedro · Inglês é treino, não matéria.</p>
 </div>
</footer>"""

def flut(msg, txt="Quero uma aula experimental"):
    return f"""<div class="flut" id="flut" aria-hidden="true">
 <a class="btn" tabindex="-1" href="{wa(msg)}" target="_blank" rel="noopener"><svg aria-hidden="true"><use href="#i-wa"/></svg>{txt}</a>
</div>
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
</html>"""

def final(titulo_html, texto, msg, extra=""):
    return f"""<section class="final azul" id="contato">
 <div class="wrap">
  <div class="final-grid">
   <div>
    <p class="label">Bora treinar?</p>
    <h2 class="blk">{titulo_html}</h2>
    <p class="intro">{texto}</p>
    {botoes(msg, "Chamar no WhatsApp", "Mandar direct")}
    <p class="local">{LOCAL}</p>
    <p class="assina"><span>Inglês é treino, não matéria.</span></p>
   </div>
   <div>{extra}</div>
  </div>
 </div>
</section>"""

# ---------------------------------------------------------------- HOME
def home():
    msg = "Oi Pedro! Vim pelo site e quero saber da aula experimental."
    col = colagem([
        pos(PASS, "left:0;top:34px;transform:rotate(-6deg)"),
        pos(CONVITE, "right:0;top:196px;transform:rotate(5deg)"),
        pos(PROVA, "left:6px;top:200px;transform:rotate(-3deg) scale(.86);transform-origin:left top"),
        '<div class="ico" style="width:120px;right:14px;top:-6px;transform:rotate(10deg)"><svg viewBox="0 0 260 220" filter="url(#stk)"><use href="#i-chat"/></svg></div>',
        estrela("width:46px;left:52%;top:150px"),
    ])
    pubs = f"""<div class="publico home">
   <a class="pub v" href="viagem/">
    {sticker('i-mala', '0 0 240 200', 'width:74px;right:16px;top:16px;transform:rotate(8deg)')}
    <span class="tag">Destaque</span>
    <h3>Inglês para<br>viagem</h3>
    <p>Aeroporto, hotel, restaurante e os imprevistos do caminho, sem depender do tradutor.</p>
    <p class="ex"><b>EX.:</b> explicar no check-in que a sua reserva não aparece no sistema.</p>
    <span class="ir">Ver inglês para viagem</span>
   </a>
   <a class="pub a" href="trabalho/">
    {sticker('i-chat', '0 0 260 220', 'width:80px;right:16px;top:16px;transform:rotate(6deg)')}
    <span class="tag">Destaque</span>
    <h3>Inglês para<br>o trabalho</h3>
    <p>Entrevista, reunião, call e apresentação com o inglês que você já tem, funcionando.</p>
    <p class="ex"><b>EX.:</b> responder o "tell me about yourself" da entrevista sem travar.</p>
    <span class="ir">Ver inglês para trabalho</span>
   </a>
   <a class="pub" href="reforco/">
    <span class="tag">Escola</span>
    <h3>Reforço escolar</h3>
    <p>O conteúdo que está caindo na escola, explicado no ritmo do aluno e treinado até fazer sentido.</p>
    <p class="ex"><b>EX.:</b> entender quando usar o past simple antes da prova.</p>
    <span class="ir">Ver reforço escolar</span>
   </a>
   <a class="pub" href="vestibular/">
    <span class="tag">Vestibular</span>
    <h3>ENEM e vestibular</h3>
    <p>Interpretação de texto, vocabulário e estratégia pras questões de inglês.</p>
    <p class="ex"><b>EX.:</b> achar a resposta no texto mesmo sem saber todas as palavras.</p>
    <span class="ir">Ver ENEM e vestibular</span>
   </a>
  </div>"""
    faq = [
        ("Como é a aula experimental?", "É gratuita e dura 30 minutos. A gente conversa sobre pra que você precisa do inglês, eu vejo seu nível e descubro onde você trava. Daí sai o plano das suas aulas."),
        ("Quanto tempo dura cada aula?", "60 minutos, uma ou duas vezes por semana."),
        ("As aulas são presenciais ou online?", "Os dois. Presencial em Mogi Guaçu, Mogi Mirim e Araras, ou online de onde você estiver."),
        ("Tem aula em grupo?", "Tem. Turmas de até 5 pessoas, com a mesma estrutura das aulas individuais e mais espaço pra treinar com outras pessoas."),
        ("Vou usar livro?", "Não. O material é montado pro seu objetivo, seja viagem, trabalho, escola ou vestibular."),
        ("Quanto custa o reforço escolar e o preparatório para vestibular?", "Esses valores eu combino direto no WhatsApp, de acordo com o que o aluno precisa."),
    ]
    faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    body = f"""{head("Teacher Pedro · Aulas de inglês em Mogi Guaçu, Mogi Mirim, Araras e online",
        "Aulas de inglês personalizadas com o Teacher Pedro: viagem, trabalho, reforço escolar e vestibular. Presencial em Mogi Guaçu, Mogi Mirim e Araras, ou online. Aula experimental gratuita.", "")}
{schema()}
</head>
<body>
{SYMBOLS}
{faixa(True)}
{nav("", msg)}

<section class="hero azul" id="topo">
 <div class="wrap hero-grid">
  <div>
   <p class="label">Aulas de inglês · Mogi Guaçu, Mogi Mirim, Araras e online</p>
   <h1>Do “travo na hora de falar” ao <span>“resolvi sozinho”</span></h1>
   <p class="sub">Você já estudou inglês. Agora precisa aprender a usar. Aulas personalizadas pra viagem, trabalho, escola e vestibular, com treino das situações que você vai viver.</p>
   {botoes(msg, ident="cta-topo")}
   <div class="feat"><span>Aula experimental gratuita</span><span>Aulas de 60 minutos</span><span>Individual ou em grupo</span><span>Presencial ou online</span></div>
  </div>
  {col}
 </div>
</section>

{marquee(["Treino", "Conversa", "Repetição", "Decisão", "Autonomia", "Viagem", "Trabalho", "Escola", "Vestibular"])}

<section class="creme" id="objetivos">
 <div class="wrap">
  <p class="label">Pra que você precisa do inglês?</p>
  <h2 class="blk">Cada objetivo pede um treino. <span>Escolhe o seu.</span></h2>
  {pubs}
 </div>
</section>

<section class="azul" id="quem-sou">
 <div class="wrap quem-grid">
  <div>
   <p class="label">Quem sou</p>
   <h2 class="blk">Prazer, <span>sou o Pedro</span></h2>
   <p>Estudei inglês por 12 anos em escola de idiomas, desde os 12 anos de idade. E mesmo assim travava pra falar.</p>
   <p>Hoje eu sei que dava pra chegar no mesmo nível em bem menos tempo. Não porque eu era ruim, mas porque eu estudava inglês como matéria. Matéria você decora pra prova. Treino você repete até sair sozinho.</p>
   <p>Dou aula de inglês desde 2023 e sou estudante de fisioterapia. Fã de Marvel, filmes, séries e música, e muito disso entra nas aulas.</p>
   <div class="tags"><span>Professor desde 2023</span><span>Método próprio</span><span>Marvel</span><span>Filmes e séries</span><span>Música</span></div>
  </div>
  <div class="citacao">Você já estudou inglês. Agora precisa <mark>aprender a usar.</mark><small>É a minha história e a de quase todo aluno que chega pra mim.</small></div>
 </div>
</section>

<section class="creme" id="como-trabalho">
 <div class="wrap">
  <p class="label">Como eu trabalho</p>
  <h2 class="blk">Ouvir, entender <span>e resolver</span></h2>
  <p class="intro">Meu jeito de dar aula vem do raciocínio que eu uso na fisioterapia: primeiro eu ouço, depois identifico onde está o problema, e aí escolho as ferramentas certas pra resolver.</p>
  <div class="nums">
   <div class="num"><h3>Ouvir</h3><p>Pra que você precisa do inglês, o que já sabe e o que te deixa inseguro.</p></div>
   <div class="num"><h3>Identificar</h3><p>Onde exatamente você trava: vocabulário, listening, estrutura ou medo de errar.</p></div>
   <div class="num"><h3>Resolver</h3><p>Um plano com material feito pra você, ajustado conforme você avança.</p></div>
  </div>
 </div>
</section>

<section class="azul" id="metodo">
 <div class="wrap metodo-grid">
  <div>
   <p class="label">O método</p>
   <p class="lema">Inglês é <mark>treino</mark>, não matéria.</p>
   <p>Saber a regra não faz ninguém falar. O que faz você falar é praticar, errar, ajustar e tentar de novo, até a frase sair sem pensar. O treino segue quatro etapas:</p>
   <ol class="passos">
    <li><span class="n">1</span><div><h3>Modelo</h3><p>Você vê e ouve como se fala na situação real.</p></div></li>
    <li><span class="n">2</span><div><h3>Controle</h3><p>Treina com apoio até a estrutura ficar natural.</p></div></li>
    <li><span class="n">3</span><div><h3>Decisão</h3><p>Escolhe e adapta o que dizer, como acontece de verdade.</p></div></li>
    <li><span class="n">4</span><div><h3>Autonomia</h3><p>Resolve a situação sozinho, sem roteiro decorado.</p></div></li>
   </ol>
  </div>
  <div>
   <p class="label">A aula por dentro</p>
   <div class="aulas">
    <div class="ficha"><div class="ft">Aula de construção <small>1 · 3 · 5 · 7</small></div>
     <ol><li>Warm up</li><li>Language ladder</li><li>Useful structure</li><li>Repetition drills</li><li>Fluency training ou problem solving</li><li>Your turn</li></ol>
     <p class="leg">Vocabulário novo, estrutura e repetição em situações diferentes.</p></div>
    <div class="ficha"><div class="ft">Aula de prática real <small>2 · 4 · 6 · 8</small></div>
     <ol><li>Warm up</li><li>Recall</li><li>Fluency drill</li><li>Decision making ou role play</li><li>Your turn</li></ol>
     <p class="leg">Você usa o que construiu pra decidir, negociar e resolver.</p></div>
   </div>
  </div>
 </div>
</section>

<section class="verde" id="como-funciona">
 <div class="wrap">
  <p class="label">Como funciona</p>
  <h2 class="blk">Do primeiro “hi” <span>ao treino</span></h2>
  {etapas("No WhatsApp ou no direct. Me conta pra que você precisa do inglês e como ele está hoje.")}
 </div>
</section>

{valores("", "Aulas de 60 minutos. Reforço escolar e preparatório para vestibular têm valores combinados no WhatsApp.")}

<section class="azul" id="perguntas">
 <div class="wrap">
  <p class="label">Perguntas frequentes</p>
  <h2 class="blk">Ficou <span>alguma dúvida?</span></h2>
  <div class="faq">{faq_html}</div>
 </div>
</section>

<section class="final verde" id="contato">
 <div class="wrap">
  <div class="final-grid">
   <div>
    <p class="label">Bora treinar?</p>
    <h2 class="blk">O primeiro passo <span>é uma conversa</span></h2>
    <p class="intro">Me chama e me conta pra que você precisa do inglês. Eu te mando os horários da aula experimental gratuita de 30 minutos.</p>
    <div class="btns">
     <a class="btn a" href="{wa(msg)}" target="_blank" rel="noopener"><svg aria-hidden="true"><use href="#i-wa"/></svg>Chamar no WhatsApp</a>
     <a class="btn o" href="{IG}" target="_blank" rel="noopener"><svg aria-hidden="true"><use href="#i-ig"/></svg>Mandar direct</a>
    </div>
    <p class="local">{LOCAL}</p>
    <p class="assina"><span>Inglês é treino, não matéria.</span></p>
   </div>
   <div>{colagem([
        pos(PASSAPORTE, "left:8%;top:30px;transform:rotate(-8deg)"),
        pos(recibo("COFFEE · NYC", ["1 LATTE M ... 5.25", "OAT MILK .... 0.80", "TO GO", "NAME: YOU"]), "right:4%;top:70px;transform:rotate(6deg)"),
        '<div class="ico" style="width:110px;left:40%;top:230px;transform:rotate(-6deg)"><svg viewBox="0 0 200 240" filter="url(#stk)"><use href="#i-togo"/></svg></div>',
   ])}</div>
  </div>
 </div>
</section>

{rodape("", msg)}
{flut(msg)}"""
    return body

# ---------------------------------------------------------------- PÁGINA DE SERVIÇO
def servico(s):
    msg = s["msg"]
    atual = s["pasta"]
    dores = "".join(f'<div class="dor">“{d}”</div>' for d in s["dores"])
    situ = "".join(f"<span>{t}</span>" for t in s["situ"])
    nums = "".join(f'<div class="num"><h3>{h}</h3><p>{p}</p></div>' for h, p in s["nums"])
    rot = s['ficha'].get('rot', 'Moment')
    mo = "".join(f"<li><b>{rot} {i+1}</b><span>{m}</span></li>" for i, m in enumerate(s["ficha"]["itens"]))
    ficha = f"""<div class="ficha"><div class="ft">{s['ficha']['titulo']} <small>{s['ficha']['tag']}</small></div>
     <ul class="mo">{mo}</ul>
     <p class="leg">{s['ficha']['leg']}</p></div>"""
    if s["preco"]:
        val = valores("", s["obs"])
    else:
        val = f"""<section class="valores creme" id="valores">
 <div class="wrap">
  <p class="label">Valores e horários</p>
  <h2 class="blk">Valores <span>combinados no WhatsApp</span></h2>
  <div class="split">
   <div>
    <p class="intro">{s['combina']}</p>
    <div class="btns"><a class="btn a" href="{wa(msg)}" target="_blank" rel="noopener"><svg aria-hidden="true"><use href="#i-wa"/></svg>Combinar no WhatsApp</a></div>
   </div>
   <div class="info" style="margin-top:0;grid-template-columns:1fr">
    {FORMATO}
    {HORAS}
   </div>
  </div>
 </div>
</section>"""
    outros = "".join(f'<a class="btn o" href="../{p}">{n}</a>' for p, n in PAGES[1:] if p != atual)
    return f"""{head(s['title'], s['desc'], atual)}
{schema()}
</head>
<body>
{SYMBOLS}
{faixa(s['preco'])}
{nav(atual, msg, 'Aula experimental' if s['preco'] else 'Chamar no WhatsApp')}

<section class="hero azul" id="topo">
 <div class="wrap hero-grid">
  <div>
   <p class="label">{s['eyebrow']}</p>
   <h1>{s['h1']}</h1>
   <p class="sub">{s['sub']}</p>
   {botoes(msg, s.get('flut', 'Quero uma aula experimental'), ident="cta-topo")}
   <div class="feat">{"".join(f"<span>{f}</span>" for f in s['feat'])}</div>
  </div>
  {s['colagem']}
 </div>
</section>

{marquee(s['marq'])}

<section class="creme" id="soa-familiar">
 <div class="wrap">
  <p class="label">Soa familiar?</p>
  <h2 class="blk">{s['dores_h2']}</h2>
  <div class="dores">{dores}</div>
  <p class="virada">{s['virada']}</p>
 </div>
</section>

<section class="azul" id="situacoes">
 <div class="wrap split">
  <div>
   <p class="label">O que a gente treina</p>
   <h2 class="blk">{s['situ_h2']}</h2>
   <p class="intro">{s['situ_txt']}</p>
   <div class="situ">{situ}</div>
  </div>
  <div class="aulas" style="grid-template-columns:1fr">{ficha}</div>
 </div>
</section>

<section class="creme" id="como-resolve">
 <div class="wrap">
  <p class="label">Como o treino resolve</p>
  <h2 class="blk">{s['nums_h2']}</h2>
  <div class="nums">{nums}</div>
 </div>
</section>

<section class="verde" id="como-funciona">
 <div class="wrap">
  <p class="label">Como funciona</p>
  <h2 class="blk">{s['como_h2']}</h2>
  {etapas(s['passo1'], None if s['preco'] else ETAPAS_ESCOLA)}
 </div>
</section>

{val}

{final(s['final_h2'], s['final_txt'], msg, '<p class="label">Outros objetivos</p><div class="btns">' + outros + '</div>')}

{rodape(atual, msg)}
{flut(msg, s.get('flut', 'Quero uma aula experimental'))}"""

SERVICOS = [
 dict(pasta="viagem/",
  title="Inglês para viagem · Teacher Pedro · Mogi Guaçu, Mogi Mirim, Araras e online",
  desc="Aulas de inglês para viagem: aeroporto, hotel, restaurante, transporte, compras e imprevistos. Presencial em Mogi Guaçu, Mogi Mirim e Araras, ou online. Aula experimental gratuita.",
  msg="Oi Pedro! Vim pela página de viagem do site e quero saber da aula experimental.",
  eyebrow="Inglês para viagem",
  h1="Você não vai decorar frases. Vai <span>treinar</span> as situações que vai viver.",
  sub="Aeroporto, hotel, restaurante, transporte, compras e os imprevistos do caminho, do jeito que acontece lá fora.",
  feat=["Aula experimental gratuita", "Individual ou em grupo", "Presencial ou online"],
  colagem=colagem([
    pos(PASS, "left:0;top:10px;transform:rotate(-7deg)"),
    pos(PASSAPORTE, "right:2%;top:110px;transform:rotate(9deg)"),
    pos(recibo("THE CHECK", ["2 BURGERS .... 28.00", "2 SODAS ....... 6.00", "TAX ........... 3.02", "TIP  ________"]), "left:4%;top:160px;transform:rotate(-3deg)"),
    '<div class="carimbo ok obj" style="left:46%;top:118px;transform:rotate(-12deg)">Admitted</div>',
  ]),
  marq=["Aeroporto", "Imigração", "Hotel", "Restaurante", "Transporte", "Compras", "Imprevistos", "Conversa"],
  dores_h2="Os medos de quem <span>vai viajar</span>",
  dores=["E se o atendente não me entender?", "E se faltar a palavra bem na hora?", "Eu entendo quando leio, mas travo pra responder."],
  virada="Você não precisa saber todas as palavras. Precisa saber <mark>se virar com as que tem.</mark>",
  situ_h2="As situações <span>da sua viagem</span>",
  situ_txt="A gente treina o que você vai viver de verdade, e principalmente o que pode dar errado. Esqueceu a palavra? Você aprende a explicar de outro jeito: “the one with…”, “the thing for…”.",
  situ=["Imigração", "Check-in", "Pedir comida", "Transporte", "Compras", "Pedir ajuda", "Reclamar", "Conversar com gente nova"],
  ficha=dict(titulo="Role play · No hotel", tag="Exemplo", itens=["Fazer o check-in normal.", "A reserva não aparece no sistema.", "O quarto não é o que você pediu."], leg="Cada aula de prática real tem três momentos, do mais simples ao mais difícil."),
  nums_h2="Do roteiro <span>ao improviso</span>",
  nums=[("Ver como se fala", "Você ouve e vê a situação do jeito que ela acontece lá fora."), ("Treinar com apoio", "Repete a estrutura em situações diferentes até ela sair natural."), ("Resolver sozinho", "Role play sem roteiro, com imprevisto no meio. Igual à vida real.")],
  como_h2="Do primeiro “hi” <span>ao embarque</span>",
  passo1="No WhatsApp ou no direct. Me conta pra onde vai, quando vai e como está seu inglês hoje.",
  preco=True, obs="Aulas de 60 minutos. Vai viajar junto com alguém? A aula em grupo é uma ótima opção.",
  final_h2="Sua viagem <span>começa na primeira aula</span>",
  final_txt="Me chama e me conta pra onde você vai. Eu te mando os horários da aula experimental gratuita de 30 minutos."),

 dict(pasta="trabalho/",
  title="Inglês para o trabalho e entrevistas · Teacher Pedro · Mogi Guaçu e online",
  desc="Aulas de inglês para o trabalho: entrevista de emprego, reuniões, calls, apresentações e e-mails. Presencial em Mogi Guaçu, Mogi Mirim e Araras, ou online. Aula experimental gratuita.",
  msg="Oi Pedro! Vim pela página de trabalho do site e quero saber da aula experimental.",
  eyebrow="Inglês para o trabalho",
  h1="O inglês que você estudou, <span>funcionando</span> no trabalho.",
  sub="Entrevista, reunião, apresentação, e-mail e aquela call que você evita. Treino com o vocabulário que você já tem e o que a sua área pede.",
  feat=["Aula experimental gratuita", "Individual ou em grupo", "Presencial ou online"],
  colagem=colagem([
    pos(CONVITE, "left:0;top:16px;transform:rotate(-5deg)"),
    pos(CRACHA, "right:2%;top:60px;transform:rotate(7deg)"),
    pos(CONVITE2, "left:6%;top:200px;transform:rotate(3deg)"),
    estrela("width:44px;left:52%;top:10px"),
  ]),
  marq=["Entrevista", "Reunião", "Call", "Apresentação", "E-mail", "Small talk", "Opinião", "Negociação"],
  dores_h2="O que trava <span>no trabalho</span>",
  dores=["Entendo a reunião, mas na hora de falar eu travo.", "Conheço o tempo verbal, mas não sei quando usar.", "Fico ensaiando a frase e a conversa já passou."],
  virada="O inglês você já tem. O que falta é <mark>treino de usar</mark>, na pressão da vida real.",
  situ_h2="As situações <span>da sua rotina</span>",
  situ_txt="A aula parte do seu trabalho: sua área, as pessoas com quem você fala e onde o inglês aparece no seu dia.",
  situ=["Entrevista de emprego", "Se apresentar", "Reunião", "Call com cliente", "Apresentação", "E-mail", "Small talk", "Dar opinião"],
  ficha=dict(titulo="Role play · Job interview", tag="Exemplo", itens=["“Tell me about yourself.”", "Contar uma experiência do seu trabalho.", "Responder a pergunta que você não esperava."], leg="Cada aula de prática real tem três momentos, do mais simples ao mais difícil."),
  nums_h2="Da sua rotina <span>pra aula</span>",
  nums=[("Mapear sua rotina", "Quais situações do seu trabalho pedem inglês e qual vocabulário da sua área importa."), ("Treinar o que você vai usar", "Se apresentar, opinar, discordar, pedir esclarecimento, explicar um problema."), ("Simular", "Entrevista e reunião simuladas, com pergunta inesperada no meio.")],
  como_h2="Do primeiro “hi” <span>à reunião</span>",
  passo1="No WhatsApp ou no direct. Me conta o que você faz e onde o inglês aparece no seu trabalho.",
  preco=True, obs="Aulas de 60 minutos. Quer treinar com colegas da empresa? A aula em grupo é pra até 5 pessoas.",
  final_h2="Bora treinar <span>o inglês do seu trabalho?</span>",
  final_txt="Me chama e me conta o que você faz. Eu te mando os horários da aula experimental gratuita de 30 minutos."),

 dict(pasta="reforco/",
  title="Reforço escolar de inglês em Mogi Guaçu, Mogi Mirim e Araras · Teacher Pedro",
  desc="Aulas de reforço escolar de inglês: o conteúdo da escola explicado no ritmo do aluno e treinado até fazer sentido. Presencial em Mogi Guaçu, Mogi Mirim e Araras, ou online.",
  msg="Oi Pedro! Vim pela página de reforço escolar do site e quero combinar as aulas.",
  eyebrow="Reforço escolar de inglês",
  h1="Inglês da escola, sem <span>decoreba</span> na véspera da prova.",
  sub="Aulas de reforço pro conteúdo que está caindo na escola, explicado no ritmo do aluno e treinado até fazer sentido.",
  feat=["Conteúdo da escola", "Presencial ou online", "Valores no WhatsApp"],
  colagem=colagem([
    pos(PROVA, "left:2%;top:10px;transform:rotate(-5deg)"),
    check("width:70px;left:56%;top:96px"),
    '<div class="ico" style="width:200px;right:0;top:250px;transform:rotate(-10deg)"><svg viewBox="0 0 260 80" filter="url(#stk)"><use href="#i-lapis"/></svg></div>',
    pos(recibo("TO DO", ["[x] verb to be", "[x] present simple", "[ ] past simple", "[ ] test on friday"]), "right:2%;top:40px;transform:rotate(7deg)"),
  ]),
  marq=["Gramática", "Vocabulário", "Leitura", "Listening", "Prova", "Dúvida", "Treino", "Confiança"],
  dores_h2="O que acontece <span>perto da prova</span>",
  dores=["Estuda, mas na prova dá branco.", "Decora a regra e esquece na semana seguinte.", "A turma anda rápido e a dúvida vai acumulando."],
  virada="Regra decorada some. O que fica é o que foi <mark>treinado em situações diferentes.</mark>",
  situ_h2="O conteúdo <span>da escola</span>",
  situ_txt="A aula segue o que está caindo na escola. Pais e responsáveis: me contem a série, a escola e o conteúdo da próxima prova, e eu monto o treino a partir disso.",
  situ=["Gramática", "Tempos verbais", "Vocabulário", "Interpretação de texto", "Listening", "Revisão pra prova"],
  ficha=dict(titulo="Aula de reforço", tag="Como é", rot="Passo", itens=["Diagnóstico do que o aluno já sabe.", "Explicação no ritmo dele.", "Exercícios até o conteúdo fazer sentido."], leg="Cada aula parte da dúvida real do aluno, não de um livro igual pra todo mundo."),
  nums_h2="Da dúvida <span>ao “entendi”</span>",
  nums=[("Diagnóstico", "Ver o que o aluno já sabe e onde está a dúvida de verdade."), ("Explicação no ritmo dele", "Sem pressa, com exemplos que fazem sentido pro conteúdo e pra idade."), ("Treino até fazer sentido", "O conteúdo da prova em situações diferentes, não só a mesma frase repetida.")],
  como_h2="Do primeiro “hi” <span>à prova</span>",
  passo1="No WhatsApp ou no direct. Me conta a série, a escola e o conteúdo que está difícil.",
  preco=False,
  combina="Reforço muda muito de aluno pra aluno: conteúdo, frequência e época de prova. Por isso eu combino os valores direto no WhatsApp.",
  final_h2="Bora tirar a dúvida <span>antes da prova?</span>",
  final_txt="Me chama e me conta qual é o conteúdo e quando é a prova. A gente combina dias, horários e valores.",
  flut="Combinar no WhatsApp"),

 dict(pasta="vestibular/",
  title="Inglês para ENEM e vestibular · Teacher Pedro · Mogi Guaçu, Mogi Mirim, Araras e online",
  desc="Preparação de inglês para o ENEM e vestibulares: interpretação de texto, vocabulário e estratégia de prova. Presencial em Mogi Guaçu, Mogi Mirim e Araras, ou online.",
  msg="Oi Pedro! Vim pela página de vestibular do site e quero combinar as aulas.",
  eyebrow="Inglês para ENEM e vestibular",
  h1="Questão de inglês é <span>leitura</span>. E leitura se treina.",
  sub="Preparação para o ENEM e para vestibulares: interpretação de texto, vocabulário e estratégia pra resolver a questão sem traduzir palavra por palavra.",
  feat=["ENEM e vestibulares", "Presencial ou online", "Valores no WhatsApp"],
  colagem=colagem([
    pos(gabarito(), "left:2%;top:12px;transform:rotate(-6deg)"),
    pos(PROVA.replace("ENGLISH TEST", "READING").replace("#2", "Q.05").replace("<p>Name: __________</p><p>1. Complete:</p><p>Yesterday I <u>went</u> to school.</p><p>2. She <u>doesn't</u> like coffee.</p><p>3. Read and answer...</p>", "<p>The text suggests that...</p><p>(A) ...</p><p>(B) ...</p><p><u>(C) ...</u></p><p>(D) ...</p>"), "right:0;top:70px;transform:rotate(6deg)"),
    circulo("width:120px;right:12%;top:218px"),
    '<div class="ico" style="width:150px;left:6%;top:262px;transform:rotate(8deg)"><svg viewBox="0 0 260 80" filter="url(#stk)"><use href="#i-lapis"/></svg></div>',
  ]),
  marq=["Interpretação", "Vocabulário", "Cognatos", "Contexto", "Estratégia", "Tempo de prova", "ENEM", "Vestibular"],
  dores_h2="O que pesa <span>na hora da prova</span>",
  dores=["Leio o texto e não entendo metade das palavras.", "Perco tempo traduzindo palavra por palavra.", "Fico na dúvida entre duas alternativas."],
  virada="Você não precisa saber todas as palavras do texto. Precisa saber <mark>achar a resposta com as que tem.</mark>",
  situ_h2="O que cai <span>na prova</span>",
  situ_txt="O treino é feito em cima de textos e questões no formato do ENEM e dos vestibulares que você vai prestar.",
  situ=["Interpretação de texto", "Vocabulário", "Cognatos e falsos cognatos", "Inferência", "Gêneros textuais", "Gestão de tempo"],
  ficha=dict(titulo="Treino de leitura", tag="Exemplo", itens=["Vocabulário e estruturas do texto.", "Interpretação guiada, passo a passo.", "Questão no formato da prova, sozinho."], leg="Do apoio total até você resolver a questão sem ajuda."),
  nums_h2="Do texto difícil <span>à alternativa certa</span>",
  nums=[("Diagnóstico", "Onde você perde ponto: vocabulário, interpretação ou tempo."), ("Estratégia de leitura", "Cognatos, contexto e falsos amigos pra entender o texto sem traduzir tudo."), ("Treino no formato da prova", "Questões no estilo do ENEM e dos vestibulares, até você resolver sozinho.")],
  como_h2="Do primeiro “hi” <span>ao dia da prova</span>",
  passo1="No WhatsApp ou no direct. Me conta quais provas você vai prestar e quando.",
  preco=False,
  combina="A preparação muda conforme as provas que você vai prestar e quanto tempo falta. Por isso eu combino os valores direto no WhatsApp.",
  final_h2="Bora treinar <span>a leitura da prova?</span>",
  final_txt="Me chama e me conta quais provas você vai prestar. A gente combina dias, horários e valores.",
  flut="Combinar no WhatsApp"),
]

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(home())
for s in SERVICOS:
    d = os.path.join(OUT, s["pasta"])
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(servico(s))
print("ok")
