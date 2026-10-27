---
name: teacher-pedro-sites
description: Cria e altera os sites do Teacher Pedro (inglês para viagem) e publica no GitHub Pages - o site da bio do Instagram e páginas novas como landing page de campanha (Black Friday, volta às aulas), página da aula experimental, página de turma, página de evento ou de material. Use sempre que o Teacher Pedro pedir site, página, landing page, link da bio, "página para a campanha", mudar preço, horário, cidade, bio, texto, botão ou campanha do site, aplicar a logo, tirar uma página do ar ou publicar, mesmo que ele não diga "skill". Não use para posts de Instagram (skill teacher-pedro-marketing) nem para aulas (skill teacher-pedro-aulas).
---

# Teacher Pedro · Sites

Você cria e mantém as páginas do Teacher Pedro. Toda página tem um objetivo só: **levar a pessoa a chamar no WhatsApp ou no direct**. Todas seguem o mesmo visual do site da bio, que o Pedro aprovou.

## Arquivos
- `references/conteudo.md`: **fonte única** dos dados (contato, bio, método, valores, horários, aula experimental, campanha). Leia sempre.
- `references/paginas.md`: lista das páginas publicadas, endereço e status. Atualize a cada página criada, alterada ou removida.
- `references/padrao-visual.md`: cores, fontes, componentes prontos e regras de escrita aprovadas. Leia antes de criar ou mudar layout.
- `assets/site-bio.html`: cópia do site da bio publicado (página raiz). Serve de catálogo de todas as seções.
- `assets/modelo-pagina.html`: esqueleto para página nova (topo, como funciona, valores, contato, botão flutuante), com `[COLCHETES]` para trocar.
- `scripts/conferir.js`: prints por seção em 390 px. Avisa rolagem horizontal e fonte que não carregou.

## Onde as páginas moram
- Repositório: `pedro2004teixeira-lab/teacher-pedro-site`, branch `main`. GitHub Pages já está ativo.
- Site da bio: `index.html` na raiz → https://pedro2004teixeira-lab.github.io/teacher-pedro-site/
- Página nova: pasta própria com `index.html` → `https://pedro2004teixeira-lab.github.io/teacher-pedro-site/<pasta>/`
- Nome da pasta: curto, minúsculo, sem acento, com hífen (`black-friday`, `aula-experimental`, `turma-eua-2027`).
- A pasta `skill/` do repositório guarda uma cópia desta skill. Mantenha atualizada quando mudar a skill.

## Criar uma página nova
1. Entenda o pedido. Se faltar algo essencial, pergunte **uma coisa por vez**: objetivo da página (qual ação a pessoa deve fazer), público, oferta/condição, prazo, texto obrigatório. Nunca preencha preço, prazo ou condição por conta própria.
2. Mostre ao Pedro um roteiro curto (seções e títulos) antes de construir, se a página for nova no formato. Para variações de algo já aprovado, siga direto.
3. Copie `assets/modelo-pagina.html` para `<pasta>/index.html` no repositório. Troque todos os `[COLCHETES]` (confira com `grep -n "\[" <pasta>/index.html`). Reaproveite seções de `site-bio.html` quando servirem.
4. Ajuste a mensagem do WhatsApp para a página (ex.: `Oi Pedro! Vim pela página da Black Friday.`), codificada para URL, em **todos** os links `wa.me` da página.
5. Página de campanha com prazo: use a faixa `#faixa` com `data-ate`, e diga no texto até quando vale.
6. Confira (abaixo), publique, atualize `paginas.md` e entregue.

## Alterar uma página
1. Leia `conteudo.md`, `paginas.md` e o trecho da página que vai mudar.
2. Se o dado é geral (preço, horário, contato, cidade, aula experimental), mude em `conteudo.md` **e em todas as páginas que mostram esse dado** (`grep -rn "R\$ 280\|wa.me" --include=index.html`).
3. Siga as regras de `padrao-visual.md`. Confira, publique e entregue.

## Conferir antes de publicar
`node scripts/conferir.js <pasta>/index.html <saída>/` e **olhe os prints**: texto atrás de adesivo, título quebrando feio, botão em duas linhas, rolagem horizontal, `[COLCHETES]` esquecidos, letra minúscula no início de frase.

## Publicar
1. Repositório na sessão: se não estiver, use a ferramenta de adicionar repositório (ou peça ao Pedro para conectar em https://claude.ai/connect-github).
2. `git fetch origin main` e rebase se preciso. Commit em português ("site: <o que mudou>") e `git push origin main`.
3. Confirme a publicação com `gh run list -R pedro2004teixeira-lab/teacher-pedro-site -L 1` (deve aparecer `pages build and deployment` com `success`). O ambiente do Claude pode não conseguir abrir `github.io`; nesse caso, diga isso e peça ao Pedro para abrir o link no celular.
4. Leva 1 a 2 minutos para atualizar. Se der 404 logo depois, é só esperar.

Sem acesso ao GitHub: entregue o `index.html` e explique o upload pelo site (Add file → Upload files, na pasta certa).

## Remover uma página
Só com pedido do Pedro. Apague a pasta, publique, marque como removida em `paginas.md` e avise que o link deixa de funcionar (inclusive em posts antigos).

## Fidelidade
- Não invente preço, prazo, desconto, bônus, garantia, depoimento, número de alunos, formação ou resultado. Se faltar, marque a lacuna e pergunte.
- Valores de campanha antiga nunca são reaproveitados sem confirmação.
- Sugestões novas (seção de depoimentos, perguntas frequentes, domínio próprio, formulário) vão marcadas como **proposta**.
- Logo: só aplique depois que o Pedro decidir entre selo sol e globo. Até lá, o texto "Teacher Pedro".
- Se existir a skill `teacher-pedro-marketing`, a voz e a marca dela valem aqui também.

## Fechamento
Termine com: o que foi feito, link da página, print do celular, o que ficou pendente. Curto e em português.
