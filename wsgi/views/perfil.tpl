<html> 
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
<form class="form-container" action="/resultadoperfil" method="post">
<input name="idperfil" type="text" class="search-field"/>
<div class="submit-container">
<br></br>
<input type="submit" value="Buscar" class="submit" />
<input type="reset" value="Restablecer" name="B2">
</div>
<h3><font COLOR=white>Ó</font></h3>
<div id="search-form">
<h3><font COLOR=white>NICK:</font></h3>
<form class="form-container" action="/resultadoperfil2" method="post">
<input name="nick" type="text" class="search-field"/>
<div class="submit-container">
<br></br>
<input type="submit" value="Buscar" class="submit" />
<input type="reset" value="Restablecer" name="B2">
</div>

</p> 
<br></br>
<b2><p align="left"><font face="Tahoma" size="2">Buscador de perfiles para steam 2016</font></p></b2>
<br></br>
<h3><font color=white> ID de usuarios de prueba: 76561198192569242, 76561198124490617, 76561198095333001 </font></h3>

<div id="botones"> 
<a href="http://gamesapi-hezparust.rhcloud.com/"><img class="inicio" src="/static/images/perfil1.png" onmouseover="this.style.opacity=1;this.filters.alpha.opacity='100';" onmouseout="this.style.opacity=0.8;this.filters.alpha.opacity='20';"/></a> 
<div id="botones"> 
<a href="http://gamesapi-hezparust.rhcloud.com/steam"><img class="inicio2" src="/static/images/perfil2.png" onmouseover="this.style.opacity=1;this.filters.alpha.opacity='100';" onmouseout="this.style.opacity=0.8;this.filters.alpha.opacity='20';"/></a> 
</div> 
</body> 
</html> 