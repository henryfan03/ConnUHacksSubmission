<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>website</title>
    <script type="text/javascript" src="brython.js"></script>
    <script type="text/javascript" src="brython_stdlib.js"></script>
    <script type="text/javascript" src="requests.brython.js"></script>
  </head>
  <body onload="brython()">
    <script type="text/python" src="main.py" id="module"></script>
    <script type="text/python">
      from browser import document
      import module

      document.body <= module.test()
    </script>
    <div class="header">
      <div class="left">
        <a href="#"><img src="images\SAP.png" style="height: 70px;"></a>
      </div>
      <div class="right">
        <a href="#">Orders</a>
        <a href="#">Login</a>
      </div>
    </div>
