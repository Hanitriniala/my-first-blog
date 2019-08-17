from django.shortcuts import render

from django.http import HttpResponse, Http404

def sitraka(request):

    return HttpResponse("""

<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>sitraka</title>:
  <link rel="stylesheet" href="style.css">
  <script src="script.js"></script>
</head>
<body>
  ...
  <!-- Le reste du contenu -->
  <H1 style ="color:red" > Blog de Sitraka  </H1> 

  <p> Bla bla bla </p>
  ...
</body>
</html>
    """)







    # HTML
