from django.shortcuts import render
from controleEstoque.models import estoqueinsert, usuarioinsert
from django.contrib import messages
import mysql.connector
con = mysql.connector.connect(host='localhost', database='controleEstoque', user='usuario', password='1234')




def estoquerecord(request):
    if request.method=='POST':
        if request.POST.get('nome_pr') and  request.POST.get('qtde_pr') and request.POST.get('valor_pr'):
            saverecord=estoqueinsert()
            saverecord.nome_pr=request.POST.get('nome_pr')
            saverecord.qtde_pr=request.POST.get('qtde_pr')
            saverecord.valor_pr=request.POST.get('valor_pr')
            saverecord.save()
            messages.sucess(request, 'Produto Adionado com sucesso')
            return render(request, 'inicio.html')
    else :
            return render(request, 'inicio.html')
            messages.error(request, 'Erro ao adicionar produto')

def estoquedelete(request, cod_produto):
    saverecord=estoqueinsert()
    saverecord= get_object_or_404(task, pk=cod_produto)
    saverecord= delete()
    return render(request, 'inicio.html')
    
def estoqueconsultar(resquet):
    consulta_sql = "select * into table#tabela from cEstoque "
    cursor = con.cursor()
    return render(request, 'inicio.html')

def userrecord(request):
    if request.method=='POST':
        if request.POST.get('nome_user') and  request.POST.get('emai_user') and request.POST.get('senha_user') and request.POST.get('dn_user') and request.POST.get('sexo_user') and request.POST.get('end_user') and request.POST.get('end_n_user') and  request.POST.get('est_user'):
            saverecord=usuarioinsert()
            saverecord.nome_user=request.POST.get('nome_user')
            saverecord.email_user=request.POST.get('email_user')
            saverecord.senha_user=request.POST.get('senha_user')
            saverecord.dn_user=request.POST.get('dn_user')
            saverecord.sexo_user=request.POST.get('sexo_user')
            saverecord.end_user=request.POST.get('end_user')
            saverecord.end_n_user=request.POST.get('end_n_user')
            saverecord.est_user=request.POST.get('est_user')
            saverecord.save()
            messages.sucess(request, 'Usuario Adionado com sucesso')
            return render(request, 'cadastrp.html')
    else :
            return render(request, 'cadastro.html')
            messages.error(request, 'Erro ao adicionar usuario')



