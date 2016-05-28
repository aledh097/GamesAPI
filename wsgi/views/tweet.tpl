<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Twitteando...</title>
    <link rel="stylesheet" href="/static/css/resultadonoticia.css" />
  </head>
  <body>
    <font size="6" color="white"><p align="middle">Mensaje: </p></font>
    <br></br>
    <form action="/twittear" method="post">
      <p align="middle"><textarea name="tweet" id="textbox" rows="3" cols="50"></textarea></p>
      <p align="middle"><input type="submit" class="button" value="Enviar tweet" /></p>
    </form>
    <p align="middle"><a href="/twitter_logout"><font size="2" color="blue">Desconectar</font></a></p>
  </body>
</html>