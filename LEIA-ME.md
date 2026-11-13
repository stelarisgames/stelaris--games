# Site Stelaris Games (GitHub Pages)

## Como publicar (importante)
Envie **todas** as pastas e arquivos deste pacote para a **raiz** do repositório, mantendo o `CNAME`:

- `index.html`
- `conserto-ps5/`, `conserto-xbox/`, `conserto-controle-drift/`, `conserto-switch/`, `privacidade/`
- **`img/`  (todas as fotos e o logo: sem esta pasta as imagens não aparecem)**
- `sitemap.xml`, `robots.txt`

O CSS e o JavaScript já estão dentro de cada página; a pasta `assets/` e o `build.py` são só para edição e
não são necessários para o site funcionar.

## Como conferir se deu certo
Depois do deploy (1 a 3 minutos), abra no navegador:
- https://stelarisgames.com.br/img/logo.png  (deve mostrar o logo)
- https://stelarisgames.com.br/conserto-ps5/  (deve abrir a página completa, com cores e botões)
Se o logo der "404", a pasta `img/` não foi enviada ou está dentro de outra pasta.
Se a página abrir sem cores, force a atualização (Ctrl+F5) ou limpe o cache.

## Rastreamento
Em `build.py`, preencha `GTM=""` com o ID do Google Tag Manager e rode `python3 build.py`.
Eventos no dataLayer: whatsapp_header, whatsapp_hero, whatsapp_card, whatsapp_wizard, whatsapp_sticky,
whatsapp_local, whatsapp_mapa, ligar_sticky, rota_hero, rota_local, wizard_step, mapa_ponto.
