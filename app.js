(function(){
  var C=window.STELARIS||{},WA=C.whatsapp||"5521996151748";
  window.dataLayer=window.dataLayer||[];
  if(C.gtm){window.dataLayer.push({"gtm.start":Date.now(),event:"gtm.js"});var s=document.createElement("script");s.async=true;s.src="https://www.googletagmanager.com/gtm.js?id="+C.gtm;document.head.appendChild(s);}
  function wa(t){return "https://wa.me/"+WA+"?text="+encodeURIComponent(t);}
  document.querySelectorAll("[data-msg]").forEach(function(a){a.href=wa(a.getAttribute("data-msg"));});
  document.addEventListener("click",function(e){var a=e.target.closest("[data-track]");if(a)dataLayer.push({event:a.getAttribute("data-track")});});
  document.querySelectorAll(".cmp input").forEach(function(r){r.addEventListener("input",function(){r.parentNode.style.setProperty("--p",r.value+"%");});});

  var tabs=document.querySelectorAll(".tab"),devs=document.querySelectorAll(".dev"),T=document.getElementById("hp-t");
  if(T){
    var D=document.getElementById("hp-d"),A=document.getElementById("hp-a");
    function pick(h){document.querySelectorAll(".hot").forEach(function(x){x.setAttribute("aria-pressed",x===h?"true":"false");});
      T.textContent=h.dataset.t;D.textContent=h.dataset.d;A.href=wa(h.dataset.m);dataLayer.push({event:"mapa_ponto",value:h.dataset.t});}
    document.querySelectorAll(".hot").forEach(function(h){h.onclick=function(){pick(h);};});
    function show(v){tabs.forEach(function(t){t.setAttribute("aria-selected",t.dataset.v===v?"true":"false");});
      devs.forEach(function(d){d.hidden=d.dataset.v!==v;});pick(document.querySelector('.dev[data-v="'+v+'"] .hot'));}
    tabs.forEach(function(t){t.onclick=function(){show(t.dataset.v);};});
    show(document.querySelector('.tab[aria-selected="true"]').dataset.v);
  }
  var box=document.getElementById("wz");if(!box)return;
  var preset=box.parentNode.getAttribute("data-device");
  var steps=[{k:"device",q:"Qual aparelho está com problema?",o:["PS5","PS4","Xbox","Nintendo Switch","Controle","Notebook"]},
    {k:"issue",q:"O que está acontecendo?",o:["Não liga","Sem imagem ou HDMI","Esquenta e faz barulho","Drift ou botão com defeito","SSD ou sistema","Outro problema"]},
    {k:"when",q:"Para quando você precisa?",o:["Hoje","Nesta semana","Sem pressa"]}];
  var st=preset?{i:1,a:{device:preset}}:{i:0,a:{}};
  function el(t,c,x){var n=document.createElement(t);if(c)n.className=c;if(x!==undefined)n.textContent=x;return n;}
  function render(){
    box.textContent="";var prog=el("div","prog");
    for(var p=0;p<3;p++)prog.appendChild(el("span",p<=Math.min(st.i,2)?"on":""));box.appendChild(prog);
    if(st.i<3){var S=steps[st.i];box.appendChild(el("div","q",S.q));var g=el("div","opts");
      S.o.forEach(function(o){var b=el("button","opt",o);b.type="button";b.onclick=function(){st.a[S.k]=o;st.i++;dataLayer.push({event:"wizard_step",step:S.k,value:o});render();};g.appendChild(b);});
      box.appendChild(g);
      if(st.i>(preset?1:0)){var back=el("button","back","Voltar");back.type="button";back.onclick=function(){st.i--;render();};box.appendChild(back);}
    }else{
      var r=el("div","result"),sm=el("div","summary");sm.appendChild(el("b","","Sua solicitação"));
      sm.appendChild(document.createTextNode(st.a.device+" · "+st.a.issue+" · Para: "+st.a.when));r.appendChild(sm);
      var msg="Olá! Vim pelo site da Stelaris Games.\nAparelho: "+st.a.device+"\nProblema: "+st.a.issue+"\nPrecisa para: "+st.a.when+"\nPode me passar um orçamento?";
      var a=el("a","btn btn-wa","Enviar no WhatsApp");a.href=wa(msg);a.target="_blank";a.rel="noopener";a.setAttribute("data-track","whatsapp_wizard");r.appendChild(a);
      r.appendChild(el("p","note","Você pode anexar foto ou vídeo do defeito na conversa."));
      var re=el("button","back","Refazer");re.type="button";re.onclick=function(){st=preset?{i:1,a:{device:preset}}:{i:0,a:{}};render();};r.appendChild(re);box.appendChild(r);}
  }
  render();
})();
