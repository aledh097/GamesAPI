<html> 
<script>
function generateReportA(){
   document.forms['search_form_results'].action = '/resultadoperfil';
   document.forms['search_form_results'].submit();
}

function generateReportB(){
   document.forms['search_form_results'].action = '/resultadoperfil2';
   document.forms['search_form_results'].submit();
}
</script>
<head> 
<title>Buscador de ultima noticia</title> 
<link rel="stylesheet" href="/static/css/perfil.css" />
</head> 
</html>

<body> 
<h1><font COLOR=white>Buscar perfil de un jugador de Steam en concreto mediante su "ID/NICK"</font></h1>
<h2><font COLOR=white>Busca su Nick : <a href="https://steamcommunity.com/search/users/
" ><font color="9a82ff  ">Aqui</a><font COLOR=white> 
<div id="search-form">
<h3><font COLOR=white>ID:</font></h3>
<form class="form-container" formaction="/resultadoperfil" action="/resultadoperfil" method="post">
<input name="idperfil" type="text" class="search-field"/>
<div class="submit-container">
<br></br>
<input type="submit" value="Buscar" class="submit" />
<input type="reset" value="Restablecer" name="B2">
</div>
<h3><font COLOR=white>Ó</font></h3>

<form formaction="/resultadoperfil2" action="/resultadoperfil2" method="get">
  NICK: <input type="text" name="nick"><br>
  <button type="submit">Buscar</button>
</form>

<form name="search_form_results" action="/resultadoperfil" method="POST">
  <input type="submit" name="submit_report"  value="A"/>
      <input type="button" name="submit_reportD"  value="Generate a Report for Dean"   onclick="generateReportA();" />
            <input type="button" name="submit_reportA"  value="Generate a Report for ACS"  onclick="generateReportB();" />
</form>

</p> 
<br></br>
<b2><p align="left"><font face="Tahoma" size="2">Buscador de perfiles para steam 2016</font></p></b2>
<br></br>

<div id="botones"> 
<a href="http://gamesapi-hezparust.rhcloud.com/"><img class="inicio" src="/static/images/perfil1.png" onmouseover="this.style.opacity=1;this.filters.alpha.opacity='100';" onmouseout="this.style.opacity=0.8;this.filters.alpha.opacity='20';"/></a> 
<div id="botones"> 
<a href="http://gamesapi-hezparust.rhcloud.com/steam"><img class="inicio2" src="/static/images/perfil2.png" onmouseover="this.style.opacity=1;this.filters.alpha.opacity='100';" onmouseout="this.style.opacity=0.8;this.filters.alpha.opacity='20';"/></a> 
</div> 
</body> 
</html> 