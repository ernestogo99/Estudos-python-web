from django.shortcuts import render



#pagina principal
def index(request):
    return render(request,'galeria/index.html')

def imagem(request):
    return render(request,'galeria/imagem.html')