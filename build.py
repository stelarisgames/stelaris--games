import os, json
DOM="https://stelarisgames.com.br"
WA="5521996151748"
CNPJ="49.789.226/0001-02"
HOURS="Seg a sex, 10h às 18h · Sáb, 10h às 15h"
RVH={"alexsandra":(493,"Alexsandra Barbosa"),"bruno":(760,"Bruno Abdon"),"juan":(387,"Juan Corvan"),"henrique":(541,"Henrique"),"jeff":(1081,"JeffFeliciano"),"speed":(280,"Speedlegends"),"hugo":(280,"Hugo M"),"betas":(203,"BETAS FF"),"samuel":(316,"Samuel Victor")}
RV={"":["alexsandra","bruno","juan"],"conserto-ps5/":["henrique","juan","hugo"],"conserto-xbox/":["speed","hugo","bruno"],"conserto-controle-drift/":["henrique","alexsandra","speed"],"conserto-switch/":["jeff","alexsandra","betas"]}
CAP={"ps5-fonte":"Limpeza da fonte do PS5","ps5-cooler":"Limpeza do cooler do PS5","dualsense":"Limpeza do controle DualSense","xbox-one":"Xbox One: limpeza completa","controle-xbox":"Controle Xbox One: limpeza"}
PR={"":["ps5-fonte","ps5-cooler","dualsense","xbox-one","controle-xbox"],"conserto-ps5/":["ps5-fonte","ps5-cooler","dualsense"],"conserto-xbox/":["xbox-one","controle-xbox"],"conserto-controle-drift/":["dualsense","controle-xbox"],"conserto-switch/":[]}
def c(t,d,m=None,h=None): return dict(t=t,d=d,m=m,h=h)
PAGES=[
dict(slug="",name="Home",dev=None,
 title="Assistência técnica de videogames em Bangu | Stelaris Games",
 desc="Conserto de PS5, PS4, Xbox, Switch e controles em Bangu. Diagnóstico técnico, transparência e garantia de até 3 meses. Real Shopping, 2º piso.",
 h1="Assistência técnica de videogames em Bangu",
 lead="Consoles, controles e notebooks com diagnóstico técnico, registro em foto e vídeo e garantia de até 3 meses nos serviços elegíveis.",
 msg="Olá! Vim pelo site da Stelaris Games e quero um orçamento.",
 cards=[c("PlayStation","PS5, PS4, PS3 e PS2: placa, HDMI, limpeza, superaquecimento.",h="conserto-ps5/"),
 c("Xbox","Series X/S, One e 360: reparo, limpeza e troca de componentes.",h="conserto-xbox/"),
 c("Nintendo Switch","Switch V1/V2, Lite e OLED, além de 3DS e 2DS.",h="conserto-switch/"),
 c("Controles","DualSense, DualShock, Xbox e Joy-Con: drift, botões e gatilhos.",h="conserto-controle-drift/"),
 c("Manutenção preventiva","Limpeza interna, pasta térmica e metal líquido do PS5.",m="Olá! Quero um orçamento de limpeza e manutenção preventiva."),
 c("Armazenamento e sistema","Troca de HD e SSD, upgrade e reinstalação de sistema.",m="Olá! Quero um orçamento de armazenamento ou sistema.")],
 rev=["henrique","juan","isabelle"]),
dict(slug="conserto-ps5/",name="PS5",dev="PS5",
 title="Conserto de PS5 em Bangu | Orçamento grátis | Stelaris Games",
 desc="Conserto de PS5 em Bangu: não liga, sem imagem, HDMI, superaquecimento e reparo de placa. Orçamento grátis e garantia de até 3 meses.",
 h1="Conserto de PS5 em Bangu, com orçamento grátis",
 lead="Seu PS5 não liga, está sem imagem ou esquenta demais? Diagnosticamos, mostramos o problema em foto e vídeo e consertamos com garantia de até 3 meses nos serviços elegíveis.",
 msg="Olá! Meu PS5 precisa de conserto. Pode me passar um orçamento?",
 cards=[c("Não liga ou desliga sozinho","Diagnóstico de fonte e placa, curtos-circuitos e circuitos de alimentação.",m="Olá! Meu PS5 não liga ou desliga sozinho. Quero um orçamento."),
 c("Sem imagem ou HDMI com defeito","Troca da entrada HDMI e substituição do CI HDMI.",m="Olá! Meu PS5 está sem imagem ou com problema no HDMI. Quero um orçamento."),
 c("Superaquecimento e barulho","Limpeza completa, pasta térmica e manutenção do metal líquido.",m="Olá! Meu PS5 esquenta e faz barulho. Quero um orçamento de limpeza."),
 c("Controle DualSense","Drift, analógicos Hall Effect ou TMR, botões e gatilhos.",m="Olá! Meu controle de PS5 está com defeito. Quero um orçamento."),
 c("SSD e sistema","Upgrade de armazenamento, reinstalação e correção de falhas de inicialização.",m="Olá! Quero SSD ou reinstalação de sistema no meu PS5."),
 c("Reparo de placa","Componentes SMD, VRM e MOSFETs, chipset e reballing em consoles compatíveis.",m="Olá! Meu PS5 precisa de reparo de placa. Quero um orçamento.")],
 rev=["henrique","juan","isabelle"]),
dict(slug="conserto-xbox/",name="Xbox",dev="Xbox",
 title="Conserto de Xbox em Bangu | Series X/S, One e 360 | Stelaris Games",
 desc="Conserto de Xbox Series X/S, One e 360 em Bangu: não liga, sem imagem, superaquecimento e controles. Orçamento grátis.",
 h1="Conserto de Xbox em Bangu, com orçamento grátis",
 lead="Xbox Series X/S, One ou 360 com defeito? Fazemos diagnóstico técnico e reparo com transparência, registro em foto e vídeo e garantia de até 3 meses nos serviços elegíveis.",
 msg="Olá! Meu Xbox precisa de conserto. Pode me passar um orçamento?",
 cards=[c("Não liga ou desliga","Fontes de alimentação, circuitos de energia e curtos.",m="Olá! Meu Xbox não liga ou desliga sozinho. Quero um orçamento."),
 c("Sem imagem ou HDMI","Troca de entrada HDMI e substituição do CI HDMI.",m="Olá! Meu Xbox está sem imagem. Quero um orçamento."),
 c("Superaquecimento e ruído","Limpeza interna, pasta térmica, coolers e ventoinhas.",m="Olá! Meu Xbox esquenta e faz barulho. Quero um orçamento."),
 c("Controle Xbox","Drift, botões, gatilhos LB, RB, LT e RT, conectores.",m="Olá! Meu controle de Xbox está com defeito. Quero um orçamento."),
 c("HD, SSD e sistema","Troca de HD ou SSD, upgrade e reinstalação de sistema.",m="Olá! Quero trocar o HD/SSD ou reinstalar o sistema do meu Xbox."),
 c("Reparo de placa","Diagnóstico de placa-mãe, componentes SMD e reballing em consoles compatíveis.",m="Olá! Meu Xbox precisa de reparo de placa. Quero um orçamento.")],
 rev=["juan","isabelle","victor"]),
dict(slug="conserto-controle-drift/",name="Controles",dev="Controle",
 title="Conserto de controle com drift em Bangu | Stelaris Games",
 desc="Conserto de controle com drift em Bangu: DualSense, DualShock, Xbox e Joy-Con. Analógicos Hall Effect e TMR. Orçamento grátis.",
 h1="Conserto de controle com drift em Bangu",
 lead="Drift, botão travado ou gatilho falhando? Reparamos DualSense, DualShock, Xbox e Joy-Con. Defeitos simples, como o drift, costumam sair no mesmo dia.",
 msg="Olá! Meu controle está com drift. Pode me passar um orçamento?",
 cards=[c("Drift nos analógicos","Correção do drift e troca por analógicos convencionais (ALPS).",m="Olá! Meu controle está com drift. Quero um orçamento."),
 c("Hall Effect e TMR","Instalação de analógicos Hall Effect ou TMR, mais duráveis.",m="Olá! Quero instalar analógicos Hall Effect/TMR no meu controle."),
 c("Botões e gatilhos","Reparo e troca de botões e gatilhos L1, L2, R1, R2, LB, RB, LT e RT.",m="Olá! Meu controle está com botão ou gatilho com defeito. Quero um orçamento."),
 c("Carregamento","Troca de conectores de carregamento USB-C.",m="Olá! Meu controle não carrega. Quero um orçamento."),
 c("Áudio P2","Troca de conectores de áudio P2.",m="Olá! O áudio P2 do meu controle não funciona. Quero um orçamento."),
 c("Placa do controle","Reparos em placas eletrônicas de controles.",m="Olá! Meu controle precisa de reparo de placa. Quero um orçamento.")],
 rev=["henrique","gabriel","isabelle"]),
dict(slug="conserto-switch/",name="Switch",dev="Nintendo Switch",
 title="Conserto de Nintendo Switch em Bangu | Stelaris Games",
 desc="Conserto de Nintendo Switch V1/V2, Lite e OLED em Bangu: sem imagem, carregamento, Joy-Con e placa. Orçamento grátis.",
 h1="Conserto de Nintendo Switch em Bangu",
 lead="Switch V1/V2, Lite ou OLED com problema? Diagnóstico técnico, peças novas quando aplicável e garantia de até 3 meses nos serviços elegíveis.",
 msg="Olá! Meu Nintendo Switch precisa de conserto. Pode me passar um orçamento?",
 cards=[c("Sem imagem","Diagnóstico de vídeo e substituição de componentes danificados.",m="Olá! Meu Switch está sem imagem. Quero um orçamento."),
 c("Não carrega","Troca de conector USB-C e circuitos de alimentação.",m="Olá! Meu Switch não carrega. Quero um orçamento."),
 c("Joy-Con com drift","Correção de drift e reparo de botões dos Joy-Con.",m="Olá! Meu Joy-Con está com drift. Quero um orçamento."),
 c("Superaquecimento","Limpeza interna, pasta térmica e troca de cooler.",m="Olá! Meu Switch esquenta demais. Quero um orçamento."),
 c("Sistema e inicialização","Correção de falhas de boot e erros de software.",m="Olá! Meu Switch tem erro de sistema. Quero um orçamento."),
 c("Reparo de placa","Reparos em placa eletrônica e componentes SMD.",m="Olá! Meu Switch precisa de reparo de placa. Quero um orçamento.")],
 rev=["isabelle","juan","henrique"]),
]
FAQ=[("O orçamento é grátis?","Sim. A avaliação é sem compromisso e você só segue com o reparo se aprovar."),
("Quanto tempo leva o conserto?","Varia conforme o defeito. Problemas simples, como reinstalação de sistema e drift, entregamos no mesmo dia. Nos demais casos, informamos o prazo no orçamento."),
("Qual é a garantia?","Garantia de até 3 meses nos serviços elegíveis. As condições ficam registradas no seu atendimento."),
("Posso mandar foto ou vídeo antes de ir à loja?","Pode. Envie pelo WhatsApp e adiantamos o diagnóstico."),
("Vocês mostram o que foi feito no aparelho?","Sim. Fazemos registros em foto e vídeo do serviço, para você acompanhar com transparência."),
("Quais aparelhos vocês atendem?","PS5, PS4, PS3, PS2, Xbox Series X/S, One e 360, Switch V1/V2, Lite e OLED, 3DS, 2DS, PSP, PS Vita, controles e notebooks."),
("Qual é o horário de atendimento?",HOURS+".")]
PAIRS=[("limpeza","Limpeza e manutenção"),("hdmi","Troca de HDMI"),("controle","Reparo de controle")]
GTM=""   # coloque aqui o ID do Google Tag Manager, ex.: "GTM-XXXXXXX"
CSS=open("assets/style.css",encoding="utf-8").read()
JS=open("assets/app.js",encoding="utf-8").read()
def xray(p):
    dv=p["dev"] or "console"
    st="controle" if p["dev"]=="Controle" else "console"
    C=[("HDMI","Sem imagem ou HDMI","Troca da entrada HDMI e substituição do CI HDMI.",84,22),("Fonte","Não liga","Fontes de alimentação, circuitos de alimentação e curtos-circuitos.",19,73),("Cooler","Barulho e superaquecimento","Limpeza interna, pasta térmica, metal líquido do PS5, coolers e ventoinhas.",47,46),("SSD","SSD e sistema","Troca de HD e SSD, upgrade e reinstalação de sistema.",82,73),("Placa","Reparo de placa","Componentes SMD, VRM e MOSFETs, chipset, NAND e reballing em consoles compatíveis.",19,29)]
    K=[("Analógico","Drift","Correção do drift e analógicos ALPS, Hall Effect ou TMR.",39,65),("Gatilhos","Gatilhos","Reparo de L1, L2, R1, R2, LB, RB e LT/RT.",31,20),("Botões","Botões","Reparo e substituição de botões.",75,46),("USB-C","Carregamento","Troca de conectores de carregamento.",50,25),("Áudio P2","Áudio P2","Troca de conectores de áudio P2.",50,77)]
    def hs(L,k): return "".join('<button class="hot" type="button" aria-pressed="false" style="left:%d%%;top:%d%%" data-t="%s" data-d="%s" data-m="%s"><span>%s</span></button>'%(x,y,t,d,e("Olá! Defeito: %s (%s). Quero um orçamento."%(t,k if k!="console" else dv)),l) for l,t,d,x,y in L)
    sv1='<svg viewBox="0 0 400 260" role="img" aria-label="Esquema interno de um console"><rect class="pcb" x="10" y="10" width="380" height="240" rx="18"/><path class="tr" d="M110 75H190M120 110H150M75 110V160M120 190H150M230 120H290M300 76V170M250 190H290M190 175V230H330"/><rect class="blk" x="300" y="40" width="70" height="36" rx="6"/><rect class="blk" x="30" y="160" width="90" height="60" rx="8"/><rect class="blk" x="290" y="170" width="80" height="40" rx="6"/><rect class="blk" x="40" y="40" width="70" height="70" rx="8"/><circle class="blk" cx="190" cy="120" r="55"/><g class="fan"><path d="M190 120c-10-40 20-50 28-20zM190 120c40-10 50 20 20 28zM190 120c10 40-20 50-28 20zM190 120c-40 10-50-20-20-28z"/></g></svg>'
    sv2='<svg viewBox="0 0 400 260" role="img" aria-label="Esquema de um controle"><path class="pcb" d="M110 70Q60 70 40 190Q30 235 70 230Q100 225 125 180L275 180Q300 225 330 230Q370 235 360 190Q340 70 290 70Z"/><rect class="blk" x="95" y="46" width="60" height="16" rx="6"/><rect class="blk" x="245" y="46" width="60" height="16" rx="6"/><rect class="blk" x="184" y="60" width="32" height="12" rx="4"/><circle class="blk" cx="155" cy="170" r="22"/><circle class="blk" cx="245" cy="170" r="22"/><circle class="blk" cx="105" cy="120" r="14"/><circle class="blk" cx="300" cy="105" r="9"/><circle class="blk" cx="320" cy="125" r="9"/><circle class="blk" cx="280" cy="125" r="9"/><circle class="blk" cx="300" cy="145" r="9"/><rect class="blk" x="190" y="196" width="20" height="10" rx="5"/></svg>'
    return '<section id="mapa"><div class="wrap"><h2>Toque no ponto com defeito</h2><p class="lead">Veja o que reparamos em cada parte do aparelho e peça o orçamento direto.</p><div class="xr"><div><div class="tabs" role="tablist"><button class="tab" role="tab" data-v="console" aria-selected="%s">Console</button><button class="tab" role="tab" data-v="controle" aria-selected="%s">Controle</button></div><div class="dev" data-v="console"%s>%s%s</div><div class="dev" data-v="controle"%s>%s%s</div></div><div class="hp" aria-live="polite"><small>Selecione um ponto</small><h3 id="hp-t"></h3><p id="hp-d"></p><a class="btn btn-wa" id="hp-a" href="https://wa.me/%s" data-track="whatsapp_mapa">Pedir orçamento</a></div></div></div></section>'%(str(st=="console").lower(),str(st=="controle").lower(),"" if st=="console" else " hidden",sv1,hs(C,"console"),"" if st=="controle" else " hidden",sv2,hs(K,"Controle"),WA)
def e(s): return s.replace("&","&amp;").replace('"',"&quot;")
def page(p):
    b="/"
    u=DOM+"/"+p["slug"]
    cards="".join(('<article class="card"><h3>%s</h3><p>%s</p><a %s>%s</a></article>'%(x["t"],x["d"],
      ('href="%s%s" data-track="nav_servico"'%(b,x["h"])) if x["h"] else ('href="https://wa.me/%s" data-msg="%s" data-track="whatsapp_card"'%(WA,e(x["m"]))),
      "Ver página" if x["h"] else "Orçar este serviço")) for x in p["cards"])
    rev="".join('<figure class="rv"><img src="%simg/rv-%s.webp" width="640" height="%d" alt="Avaliação 5 estrelas de %s no Google" loading="lazy"></figure>'%(b,k,RVH[k][0],RVH[k][1]) for k in RV[p["slug"]])
    pr=PR[p["slug"]]
    ba="".join('<figure class="cmp" style="--p:50%%"><img src="%simg/depois-%s.webp" alt="Depois: %s" width="1000" height="1000" loading="lazy"><img class="top" src="%simg/antes-%s.webp" alt="Antes: %s" width="1000" height="1000" loading="lazy"><span class="tg l">Antes</span><span class="tg r">Depois</span><input type="range" min="0" max="100" value="50" aria-label="Comparar antes e depois: %s"><figcaption>%s</figcaption></figure>'%(b,k,CAP[k],b,k,CAP[k],CAP[k],CAP[k]) for k in pr)
    ba_sec=('<section class="alt" id="antes-depois"><div class="wrap"><h2>Antes e depois</h2><p class="lead">Arraste para comparar. Fotos reais de serviços feitos na Stelaris.</p><div class="cmps">%s</div></div></section>'%ba) if pr else ""
    faq="".join("<details><summary>%s</summary><p>%s</p></details>"%f for f in FAQ)
    dev=' data-device="%s"'%p["dev"] if p["dev"] else ""
    ld=json.dumps({"@context":"https://schema.org","@type":"LocalBusiness","name":"Stelaris Games","url":DOM+"/","telephone":"+55 21 99615-1748","image":DOM+"/img/hero-fachada.webp","address":{"@type":"PostalAddress","streetAddress":"Rua Francisco Real, 1950, Loja 213, Real Shopping","addressLocality":"Rio de Janeiro","addressRegion":"RJ","addressCountry":"BR"},"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"10:00","closes":"18:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"10:00","closes":"15:00"}]},ensure_ascii=False)
    L=[("","Início"),("conserto-ps5/","PS5"),("conserto-xbox/","Xbox"),("conserto-controle-drift/","Controles"),("conserto-switch/","Switch")]
    nav="".join('<a href="/%s"%s>%s</a>'%(sl,' aria-current="page"' if sl==p["slug"] else "",n) for sl,n in L)+'<a href="#local">Como chegar</a>'
    return f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p["title"]}</title><meta name="description" content="{e(p["desc"])}">
<link rel="canonical" href="{u}"><meta name="theme-color" content="#1f2a6b">
<meta property="og:title" content="{e(p["title"])}"><meta property="og:description" content="{e(p["desc"])}"><meta property="og:image" content="{DOM}/img/hero-fachada.webp"><meta property="og:type" content="website"><meta property="og:url" content="{u}">
<link rel="icon" type="image/png" href="{b}img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@500;700&family=Figtree:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
<script type="application/ld+json">{ld}</script></head>
<body>
<header class="top"><div class="wrap bar"><a class="brand" href="{b or "./"}"><img src="{b}img/logo.png" alt="Stelaris Games" width="54" height="52"></a><nav aria-label="Principal">{nav}</nav>
<a class="btn btn-wa" href="https://wa.me/{WA}" data-msg="{e(p["msg"])}" data-track="whatsapp_header">Orçamento grátis</a></div></header>
<main>
<section class="hero"><div class="wrap hero-grid"><div>
<span class="pill">Real Shopping · Bangu, Rio de Janeiro</span><h1>{p["h1"]}</h1><p class="lead">{p["lead"]}</p>
<div class="cta-row"><a class="btn btn-wa" href="https://wa.me/{WA}" data-msg="{e(p["msg"])}" data-track="whatsapp_hero">Pedir orçamento no WhatsApp</a><a class="btn btn-ghost" href="https://maps.app.goo.gl/uSFVXtiMWQx1u5JZ9" target="_blank" rel="noopener" data-track="rota_hero">Como chegar</a></div>
<ul class="ticks"><li>Orçamento gratuito e sem compromisso</li><li>Garantia de até 3 meses nos serviços elegíveis</li><li>Registro em foto e vídeo do seu reparo</li></ul>
<img class="himg" src="{b}img/hero-fachada.webp" alt="Fachada da Stelaris Games no Real Shopping, Bangu" width="1200" height="900"></div>
<div class="wizard"{dev}><h2>Diga o problema em 3 toques</h2><p class="sub">Montamos a mensagem para você. O técnico responde já com o caminho do reparo.</p><div id="wz" aria-live="polite"></div></div></div></section>
<div class="trust"><div class="wrap trust-grid"><div><b>Nota 5★ no Google</b><span>Avaliações reais de clientes</span></div><div><b>Orçamento grátis</b><span>Você decide depois de saber o valor</span></div><div><b>Garantia até 3 meses</b><span>Nos serviços elegíveis</span></div><div><b>Loja física</b><span>{HOURS}</span></div></div></div>
{xray(p)}
<section id="servicos"><div class="wrap"><h2>{"O que consertamos" if not p["slug"] else "Defeitos que resolvemos"}</h2><p class="lead">Escolha o serviço e peça o orçamento já com o assunto certo.</p><div class="cards">{cards}</div></div></section>
<section class="alt" id="como-funciona"><div class="wrap"><h2>Como funciona o atendimento</h2><p class="lead">Sem surpresa na conta. Você aprova antes de qualquer reparo.</p><div class="steps">
<div class="step"><h3>Orçamento</h3><p>Você descreve o problema pelo WhatsApp ou na loja e recebe o diagnóstico com valor e prazo.</p></div>
<div class="step"><h3>Conserto</h3><p>Com a sua aprovação, o reparo começa. Usamos peças novas quando aplicável.</p></div>
<div class="step"><h3>Testes</h3><p>Testamos o aparelho para confirmar que o defeito foi resolvido.</p></div>
<div class="step"><h3>Entrega com garantia</h3><p>Você retira o aparelho com orientação de uso e garantia de até 3 meses nos serviços elegíveis.</p></div></div></div></section>
<section id="diferenciais"><div class="wrap"><h2>Por que escolher a Stelaris</h2><div class="cards cards4">
<article class="card"><h3>Diagnóstico técnico</h3><p>Identificamos a causa real antes de propor o reparo.</p></article>
<article class="card"><h3>Transparência</h3><p>Registramos o serviço em foto e vídeo para você ver o que foi feito.</p></article>
<article class="card"><h3>Peças novas</h3><p>Utilizamos peças novas quando aplicável.</p></article>
<article class="card"><h3>Garantia</h3><p>Garantia de até 3 meses nos serviços elegíveis.</p></article></div></div></section>
{ba_sec}
<section id="avaliacoes"><div class="wrap"><h2>Quem já consertou aqui recomenda</h2><p class="lead">Avaliações reais de clientes no Google.</p><div class="rev">{rev}</div></div></section>
<section class="alt" id="duvidas"><div class="wrap"><h2>Dúvidas frequentes</h2>{faq}</div></section>
<section id="local"><div class="wrap loc"><div><h2>Venha até a loja</h2><address class="addr">Rua Francisco Real, 1950, Loja 213, 2º piso<br>Real Shopping, Bangu, Rio de Janeiro, RJ<br>{HOURS}</address>
<div class="cta-row"><a class="btn btn-ghost" href="https://maps.app.goo.gl/uSFVXtiMWQx1u5JZ9" target="_blank" rel="noopener" data-track="rota_local">Abrir no Google Maps</a><a class="btn btn-wa" href="https://wa.me/{WA}" data-msg="Olá! Estou a caminho da loja. Vocês estão abertos agora?" data-track="whatsapp_local">Confirmar no WhatsApp</a></div></div>
<iframe class="map" title="Mapa da Stelaris Games" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Stelaris%20Games%20Assist%C3%AAncia%20T%C3%A9cnica%2C%20Rua%20Francisco%20Real%2C%201950%2C%20Loja%20213%2C%20Bangu%2C%20Rio%20de%20Janeiro%20RJ&amp;output=embed"></iframe></div></section>
</main>
<footer><div class="wrap"><b>Stelaris Games</b><span>CNPJ {CNPJ} · Rua Francisco Real, 1950, Loja 213, Real Shopping, Rio de Janeiro, RJ · (21) 99615-1748 · <a href="https://instagram.com/stelarisgames">@stelarisgames</a></span><span>© Stelaris Games. <a href="{b}privacidade/">Política de privacidade</a></span></div></footer>
<div class="sticky"><a class="btn btn-wa" href="https://wa.me/{WA}" data-msg="{e(p["msg"])}" data-track="whatsapp_sticky">Orçamento no WhatsApp</a><a class="btn btn-ghost" href="tel:+{WA}" data-track="ligar_sticky">Ligar</a></div>
<script>window.STELARIS={{gtm:"{GTM}",whatsapp:"{WA}"}};</script><script>{JS}</script></body></html>'''
def w(path,txt):
    os.makedirs(os.path.dirname(path) or ".",exist_ok=True); open(path,"w",encoding="utf-8").write(txt)
for p in PAGES: w(p["slug"]+"index.html",page(p))
priv='''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Política de privacidade | Stelaris Games</title><meta name="robots" content="noindex"><style>'''+CSS+'''</style></head><body><div class="wrap" style="padding:48px 0;max-width:760px"><p><a href="/">← Voltar ao site</a></p><h1>Política de privacidade</h1>
<p>A Stelaris Games (CNPJ %s) respeita a sua privacidade e a LGPD (Lei nº 13.709/2018).</p><h2>Dados que coletamos</h2><p>Ao iniciar uma conversa pelo WhatsApp, recebemos as informações que você enviar (nome, telefone, aparelho e descrição do problema). O site também pode usar ferramentas de medição, como Google Tag Manager, Google Ads e Meta Pixel, que registram dados de navegação, como páginas visitadas e cliques.</p><h2>Como usamos</h2><p>Usamos os dados para responder ao seu pedido, realizar o orçamento e o serviço, e medir o desempenho dos nossos anúncios. Não vendemos seus dados.</p><h2>Seus direitos</h2><p>Você pode solicitar acesso, correção ou exclusão dos seus dados pelo WhatsApp (21) 99615-1748.</p><p><i>Texto-modelo: recomendamos revisão por um profissional jurídico.</i></p></div></body></html>'''%CNPJ
w("privacidade/index.html",priv)
urls=[DOM+"/"+p["slug"] for p in PAGES]
w("sitemap.xml",'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join("<url><loc>%s</loc></url>\n"%u for u in urls)+"</urlset>\n")
w("robots.txt","User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n"%DOM)
