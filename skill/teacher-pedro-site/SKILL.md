---
name: teacher-pedro-site
description: Cria, atualiza e publica o site de uma página do Teacher Pedro (link da bio do Instagram) com quem sou, método, como funciona, modalidades, valores, horários e contato, no padrão visual da marca, hospedado no GitHub Pages. Use sempre que o Teacher Pedro pedir para mexer no site, na página da bio, no link da bio ou na landing page, por exemplo mudar preço, horário, cidade, bio ou texto, colocar ou tirar campanha (Black Friday, aula experimental), trocar o botão, aplicar a logo ou publicar o site, mesmo que ele não diga "skill".
---

# Teacher Pedro · Site da bio

Página única, pensada para celular, que transforma visita do Instagram em conversa no WhatsApp ou no direct. O objetivo é **vender aulas**.

## Arquivos
- `references/conteudo.md`: **fonte única** dos dados (contato, bio, método, valores, horários, campanha). Leia sempre antes de mexer.
- `assets/index.html`: o site completo, autossuficiente (CSS, adesivos SVG e script no próprio arquivo; fontes Montserrat e Nunito pelo Google Fonts).
- `scripts/conferir.js`: tira prints do site em 390 px (celular) para revisão.

Se existir a skill `teacher-pedro-marketing`, siga a marca e a voz dela (cores, adesivos, sem fotos do Pedro, tom "amigo que já viajou"). Os pontos essenciais já estão aplicados no `index.html`.

## Fluxo de uma alteração
1. Leia `references/conteudo.md` e o trecho do `assets/index.html` que vai mudar.
2. Altere **os dois**: o dado em `conteudo.md` e o texto no `index.html`. Preço aparece em `.preco .val`; horário em `.hora`; contato em todos os links `wa.me` e `ig.me` (procure e troque todos) e no texto "WhatsApp:".
3. Confira: `node scripts/conferir.js caminho/index.html pasta-saida/`. Olhe os prints: texto escondido atrás de adesivo, título quebrando feio, rolagem horizontal (o script avisa se a largura passar de 390).
4. Publique (abaixo) e mande ao Pedro o print e o link.

## Seções e onde ficam
| Seção | id | Fundo |
|---|---|---|
| Faixa de campanha | `#faixa` | verde |
| Topo + botões | `#topo` | azul |
| Quem sou | `#quem-sou` | creme |
| Método | `#metodo` | azul |
| Como funciona | `#como-funciona` | verde |
| Modalidades e valores | `#valores` | creme |
| Horários | `#horarios` | verde |
| Contato final | `#contato` | azul |

Regras de escrita aprovadas pelo Pedro (27/10/2026):
- Toda frase começa com letra maiúscula, inclusive em etiquetas e valores ("Por mês", "Até 12h", "Descanso"). Nada de `text-transform:lowercase`.
- Em MAIÚSCULAS (via CSS): títulos das seções (`.blk`), botões e links de WhatsApp/Instagram (`.btn`, `.pill`, link da faixa), etiquetas do "quem sou" (`.tags`), situações do método (`.situ`) e títulos das etapas (`.etapas h3`).
- Toda regra de fonte usa reserva sem serifa (`Montserrat,system-ui,sans-serif`), para não aparecer letra com serifa se o Google Fonts não carregar.
- Botões precisam caber em uma linha em 390 px; se o texto crescer, encurte o texto.

Mantenha a alternância de fundos. Cada seção tem no máximo um adesivo (`.ico`), posicionado no canto superior direito, sem cobrir texto.

## Campanhas
- A faixa `#faixa` só aparece até a data em `data-ate` (AAAA-MM-DD, horário de Brasília). Para uma nova campanha, troque o texto, o link do WhatsApp (mensagem específica, ex.: "quero saber da Black Friday") e a data.
- Sem campanha ativa, apague o bloco `#faixa` inteiro.
- **Nunca reaproveite valores de campanha antiga** sem o Pedro confirmar.

## Publicação no GitHub Pages
O site vai na raiz de um repositório do Pedro (ex.: `teacher-pedro-site`), como `index.html`.
1. Se o repositório não estiver na sessão, peça ao Pedro para conectar em https://claude.ai/connect-github e informe o nome.
2. Copie `assets/index.html` para a raiz do repositório, faça commit ("site: <o que mudou>") e push na branch `main`.
3. Na primeira vez, ative o Pages: com `gh` disponível, `gh api -X POST repos/<dono>/<repo>/pages -f "source[branch]=main" -f "source[path]=/"`; senão, peça ao Pedro: Settings → Pages → Branch `main` / root → Save.
4. Endereço: `https://<dono>.github.io/<repo>/`. Leva 1 a 2 minutos para atualizar.
5. Lembre o Pedro de colocar o link na bio, se ainda não colocou.

Sem acesso ao GitHub, entregue o `index.html` como arquivo e explique que ele pode subir pelo site do GitHub (Add file → Upload files).

## Fidelidade
- Não invente preço, horário, cidade, depoimento, número de alunos, formação ou condição (ex.: desconto, bônus ou garantia que não estejam em `conteudo.md`). Se faltar, marque a lacuna e pergunte.
- Texto em português do Brasil, frases curtas, com "você". Sem promessas ("fluente em 30 dias") e sem cara de IA.
- Sugestões novas (seção de depoimentos, perguntas frequentes, domínio próprio) vão como **proposta**.
- Logo: só aplique depois que o Pedro decidir entre selo sol e globo. Até lá, use o texto "teacher pedro".

## Fechamento
Termine com: o que mudou, link do site (ou o arquivo), print do celular e o que ficou pendente. Curto e em português.
