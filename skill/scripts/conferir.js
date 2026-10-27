// Tira prints do site na largura de celular para revisão.
// Uso: node conferir.js caminho/index.html pasta-saida/
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

(async () => {
  const [arquivo, saida = '.'] = process.argv.slice(2);
  if (!arquivo) { console.error('Uso: node conferir.js index.html pasta-saida/'); process.exit(1); }
  fs.mkdirSync(saida, { recursive: true });
  const navegador = await chromium.launch();
  const pagina = await navegador.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
  const erros = [];
  pagina.on('pageerror', e => erros.push(e.message));
  await pagina.goto('file://' + path.resolve(arquivo));
  await pagina.waitForTimeout(2500);

  const largura = await pagina.evaluate(() => document.documentElement.scrollWidth);
  if (largura > 390) console.warn(`ATENÇÃO: rolagem horizontal (${largura}px > 390px)`);
  if (!(await pagina.evaluate(() => document.fonts.check('900 20px Montserrat')))) console.warn('ATENÇÃO: fonte Montserrat não carregou');

  // um print por seção, mais fácil de revisar que a página inteira
  const secoes = await pagina.$$('section, #faixa');
  let n = 0;
  for (const s of secoes) {
    if (!(await s.isVisible())) continue;
    const id = (await s.getAttribute('id')) || `secao${n}`;
    await s.screenshot({ path: path.join(saida, `${String(n++).padStart(2, '0')}-${id}.png`) });
  }
  await pagina.screenshot({ path: path.join(saida, 'pagina-inteira.png'), fullPage: true });
  console.log(`${n} seções salvas em ${saida}`);
  if (erros.length) console.warn('Erros de script:', erros);
  await navegador.close();
})();
