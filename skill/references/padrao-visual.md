# Padrão visual e de escrita dos sites

Aprovado pelo Pedro em 27/10/2026 no site da bio. Toda página nova segue isto.

## Base
- Página única, pensada para celular (conferir em 390 px), conteúdo com largura máxima de 560 px (`.wrap`).
- Arquivo autossuficiente: CSS, ícones SVG e script dentro do próprio `index.html`. Fontes pelo Google Fonts.
- Fontes: Montserrat (títulos, botões, etiquetas) e Nunito (texto). **Sempre** com reserva sem serifa: `Montserrat,system-ui,sans-serif`. Sem isso, o título aparece com serifa quando a fonte não carrega.
- Textura de grão de papel por cima de tudo (`body::after`).

## Cores
| Nome | Hex | Uso |
|---|---|---|
| Creme | `#F7F4EA` | fundo, cards |
| Azul | `#1F3A8F` | cor principal |
| Verde | `#C6F135` | destaque, botão principal |
| Texto | `#24305c` | texto corrido em fundo claro |

Seções alternam fundo **azul / creme / verde**. Nunca duas seguidas iguais.

## Escrita
- Toda frase começa com letra maiúscula, inclusive etiquetas e valores ("Por mês", "Até 12h").
- Em MAIÚSCULAS (via CSS `text-transform:uppercase`): títulos de seção (`.blk`, `h1`), botões e links de WhatsApp/Instagram (`.btn`, `.pill`, link da `#faixa`), etiquetas (`.tags`, `.situ`), títulos de etapas e cards (`.etapas h3`, `.card .tit`, `.passos h3`), rótulos (`.label`) e horários (`.hora`).
- Nunca `text-transform:lowercase`.
- Depois de dois-pontos, minúscula (regra do português), a menos que o Pedro peça outra coisa.
- Separador entre itens curtos: `•` (ex.: "Presencial em Mogi Guaçu e Araras • Online").
- Voz: "amigo que já viajou", frases curtas, "você", sem promessa e sem cara de IA.
- Botão precisa caber em **uma linha** em 390 px. Se não couber, encurte o texto.

## Componentes prontos (em `assets/site-bio.html`)
| Componente | Classe | Para quê |
|---|---|---|
| Faixa de campanha | `#faixa[data-ate]` | aviso no topo que some sozinho depois da data |
| Topo | `.hero` + `h1 span` | título grande com uma palavra na caixa verde |
| Botões | `.btn.v` (verde), `.btn.o` (contorno), `.btns` | WhatsApp e Direct, sempre os dois |
| Título de seção | `.label` + `.blk span` | rótulo pequeno + título em caixas |
| Etiquetas | `.tags`, `.situ` | listas curtas em pílulas |
| Passos numerados | `.passos` | método, sequência curta em fundo azul |
| Etapas | `.etapas` | "como funciona", cards creme numerados |
| Preços | `.cards .card` (+ `.dest` em verde) + `.precos .preco` | modalidades e valores |
| Formato | `.formato` | presencial/online lado a lado |
| Horários | `.horas .hora` (+ `.off`) | dias e horários |
| Adesivo | `.ico` + `<use href="#i-...">` | um por seção, canto superior direito, sem cobrir texto |
| Lema | `.lema mark` / `.assina span` | "inglês é treino, não matéria." |
| Botão flutuante | `#flut` | WhatsApp fixo no celular entre o topo e o contato |

Adesivos disponíveis no arquivo: `i-liberty`, `i-pass`, `i-bag`, `i-chat`, `i-togo`. Outros (águia, hambúrguer, táxi, Empire State, Golden Gate, bandeira, etiqueta %, lupa) estão em `assets/templates/artes_base.html` da skill `teacher-pedro-marketing`. Copie o `<symbol>` para a página se precisar.

## Regras visuais vindas do Pedro
- Sem fotos do Pedro. Adesivos no lugar.
- Imagens de filmes, séries ou pessoas só se o Pedro enviar.
- No máximo um adesivo por seção.
