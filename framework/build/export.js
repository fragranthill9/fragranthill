const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
(async () => {
  const outDir = '/home/user/fragranthill/framework/export';
  fs.mkdirSync(outDir, { recursive: true });
  const files = process.argv.slice(2);
  const browser = await chromium.launch();
  for (const f of files) {
    const base = path.basename(f, '.html');
    const html = fs.readFileSync(f, 'utf8');
    const doc = '<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"></head><body>' + html + '</body></html>';
    // PNG at 2x
    let page = await browser.newPage({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 2 });
    await page.setContent(doc, { waitUntil: 'networkidle' }); await page.waitForTimeout(800);
    await page.screenshot({ path: path.join(outDir, base + '.png'), fullPage: true });
    const h = await page.evaluate(() => document.documentElement.scrollHeight);
    await page.close();
    // PDF single page
    page = await browser.newPage({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 });
    await page.setContent(doc, { waitUntil: 'networkidle' }); await page.waitForTimeout(800);
    await page.emulateMedia({ media: 'screen' });
    await page.pdf({ path: path.join(outDir, base + '.pdf'), width: '1280px', height: (h + 2) + 'px', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
    console.log('exported', base, 'height', h);
    await page.close();
  }
  await browser.close();
})();
