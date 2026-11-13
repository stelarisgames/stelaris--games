# Site Stelaris Games (GitHub Pages)

## Como publicar
1. No repositório, **mantenha** o arquivo `CNAME`.
2. Copie para a raiz do repositório: `index.html`, as pastas `assets/`, `img/`, `conserto-ps5/`,
   `conserto-xbox/`, `conserto-controle-drift/`, `conserto-switch/`, `privacidade/`,
   `sitemap.xml` e `robots.txt`. Substitua o `index.html` antigo.
3. Faça commit e push. O GitHub Pages publica em poucos minutos.
(As imagens antigas, como logo-stelaris.png e hero-consoles.jpg, não são mais usadas e podem ser apagadas.)

## Imagens (pasta img/)
- `logo.png`: isotipo principal com fundo transparente. `favicon.png`: ícone da aba.
- `hero-fachada.webp` e `tecnica.webp`: fachada e bancada.
- `antes-*.webp` / `depois-*.webp`: fotos tratadas (nitidez e fundo desfocado), 1000x1000.
- `rv-*.webp`: avaliações do Google recortadas.

## Rastreamento
Edite `assets/config.js` e coloque o ID do Google Tag Manager (GTM-XXXXXXX).
Eventos no dataLayer: whatsapp_header, whatsapp_hero, whatsapp_card, whatsapp_wizard, whatsapp_sticky,
whatsapp_local, whatsapp_mapa, ligar_sticky, rota_hero, rota_local, wizard_step, mapa_ponto.

## Edições
Textos, horários e serviços ficam em `build.py` (opcional: `python3 build.py` regenera as páginas).
