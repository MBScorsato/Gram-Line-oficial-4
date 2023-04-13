from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.shortcuts import render, redirect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random


def recuperar_senha(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/index/plataforma')
        return render(request, 'recuperar_senha.html')

    elif request.method == 'POST':
        # senha = 'eibrutfknhhwjxbi'
        if request.user.is_authenticated:
            return redirect('/index/plataforma')

        # Obter o email informado pelo usuário
        email = request.POST.get('para')

        # Verificar se o usuário com o email informado existe no banco de dados
        try:
            User = get_user_model()
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.add_message(request, constants.ERROR, 'Este email não está cadastrado')
            return render(request, 'recuperar_senha.html')

        # Sorteio de nova senha
        nova_senha = str(random.randint(100000, 999999))

        # Atualização da senha
        user.set_password(nova_senha)
        user.save()

        # Envio do email com a nova senha
        assunto = "Recuperação de senha"
        corpo = f"Sua nova senha é: {nova_senha}. Lembre-se de alterá-la o quanto antes."
        de = 'gramline.recuperacao.de.senha@gmail.com'
        senha = 'eibrutfknhhwjxbi'

        msg = MIMEMultipart()
        msg['From'] = de
        msg['To'] = email
        msg['Subject'] = assunto
        msg.attach(MIMEText(corpo, 'html'))

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(de, senha)
        s.sendmail(de, email, msg.as_string())
        s.quit()

        messages.add_message(request, constants.SUCCESS, 'Confira sua nova senha no seu email')

        print('Email enviado com sucesso!')
    return render(request, 'recuperar_senha.html')

