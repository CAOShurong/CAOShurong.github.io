(() => {
  'use strict';
  const zh = document.documentElement.lang.startsWith('zh');
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#navigation');
  toggle?.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('is-open', open);
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && !document.querySelector('.nav-group.is-open') && toggle?.getAttribute('aria-expanded') === 'true') {
      toggle.setAttribute('aria-expanded', 'false'); nav.classList.remove('is-open'); toggle.focus();
    }
  });
  document.querySelectorAll('.submenu-toggle').forEach(button => {
    button.addEventListener('click', () => {
      const open = button.getAttribute('aria-expanded') !== 'true';
      document.querySelectorAll('.nav-group').forEach(group => {
        group.classList.remove('is-open'); group.querySelector('button').setAttribute('aria-expanded','false');
      });
      button.setAttribute('aria-expanded',String(open)); button.parentElement.classList.toggle('is-open',open);
    });
  });
  document.addEventListener('click', event => {
    if (!event.target.closest('.nav-group')) document.querySelectorAll('.nav-group').forEach(group => {
      group.classList.remove('is-open'); group.querySelector('button').setAttribute('aria-expanded','false');
    });
  });
  document.addEventListener('keydown', event => {
    if(event.key === 'Escape') document.querySelectorAll('.nav-group.is-open').forEach(group => {
      group.classList.remove('is-open'); const button=group.querySelector('button'); button.setAttribute('aria-expanded','false'); button.focus();
    });
  });
  const language = document.querySelector('.language-switch');
  language?.addEventListener('click', event => {
    try {
      localStorage.setItem('academic-language', zh ? 'en' : 'zh');
      sessionStorage.setItem('academic-scroll', JSON.stringify({route:document.body.dataset.route, y:window.scrollY}));
    } catch (_) {}
    if (location.hash) language.href += location.hash;
  });
  try {
    if (location.pathname === '/' && !location.search && localStorage.getItem('academic-language') === 'zh') location.replace('/zh/' + location.hash);
    const saved = JSON.parse(sessionStorage.getItem('academic-scroll') || 'null');
    if (saved?.route === document.body.dataset.route) {
      sessionStorage.removeItem('academic-scroll');
      window.addEventListener('load', () => { if(!location.hash) window.scrollTo(0,saved.y); }, {once:true});
    }
  } catch (_) {}
  document.querySelectorAll('.copy-cite').forEach(button => button.addEventListener('click', async () => {
    const text = button.parentElement.querySelector('pre').textContent;
    const status = button.parentElement.querySelector('.copy-status');
    try { await navigator.clipboard.writeText(text); status.textContent = zh ? '已复制' : 'Copied'; }
    catch (_) {
      const selection=window.getSelection(); const range=document.createRange(); range.selectNodeContents(button.parentElement.querySelector('pre')); selection.removeAllRanges(); selection.addRange(range);
      status.textContent=zh?'已选中，请复制文本或下载 .bib。':'Text selected. Copy it or download the .bib file.';
    }
  }));
  document.querySelectorAll('.paper-figure[href^="/assets/"], .figure-link[href^="/assets/"]').forEach(link => link.addEventListener('click', event => {
    event.preventDefault();
    const dialog = document.createElement('dialog');
    dialog.className = 'figure-dialog';
    dialog.setAttribute('aria-label', link.getAttribute('aria-label'));
    const close = document.createElement('button');
    close.className = 'button secondary'; close.textContent = zh ? '关闭 ×' : 'Close ×';
    const figure = link.querySelector('img').cloneNode(); figure.loading = 'eager';
    dialog.append(close, figure); document.body.append(dialog);
    close.addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', e => { if(e.target === dialog) dialog.close(); });
    dialog.addEventListener('close', () => { dialog.remove(); link.focus(); });
    dialog.showModal();
  }));
})();
