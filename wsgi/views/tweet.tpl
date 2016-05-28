<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Twitteando...</title>
    <link rel="stylesheet" href="/static/css/resultadonoticia.css" />
  </head>
  <body>
    <p align="middle">Mensaje: </p>
    <form action="/twittear" method="post">
      <p align="middle"><textarea name="tweet" id="textbox" rows="3" cols="50"></textarea></p>
      <p align="middle"><input type="submit" class="button" value="Enviar tweet" /></p>
    </form>
    <p align="middle"><a href="/twitter_logout">Desconectar</a></p>
  </body>
</html>