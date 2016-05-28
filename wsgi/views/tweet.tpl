<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Twitteando...</title>
  </head>
  <body>
    <p>Mensaje: </p>
    <form action="/twittear" method="post">
    <textarea name="comentarios" rows="10" cols="40">Buenas Twitter, estoy echándole un vistazo al perfil de: {{nick}}, gracias a la web http://gamesapi-hezparust.rhcloud.com/</textarea>

    <p><input type="submit" class="button" value="Enviar tweet" /></p>
    </form>
    <a href="/">Desconectar</a>
  </body>
</html>