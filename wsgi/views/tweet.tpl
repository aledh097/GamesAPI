<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Twitteando...</title>
  </head>
  <body>
    <p>Mensaje: </p>
    <form action="/twittear" method="post">
      <p><textarea name="tweet" id="textbox" rows="3" cols="50"></textarea></p>
      <p><input type="submit" class="button" value="Enviar tweet" /></p>
    </form>
    <a href="/twitter_logout">Desconectar</a>
  </body>
</html>