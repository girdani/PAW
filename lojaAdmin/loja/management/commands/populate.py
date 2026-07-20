from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from loja.models import Produto, Categoria, Fabricante
Usuario = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            usuario = Usuario.objects.get(username='giordanni')
        except Usuario.DoesNotExist:
            usuario = Usuario.objects.create_superuser(
                username='giordanni',
                email='g.giordanni@escolar.ifrn.edu.br',
                password='senha',
            )

        software, _ = Categoria.objects.get_or_create(Categoria='Software')
        hardware, _ = Categoria.objects.get_or_create(Categoria='Hardware')

        microsoft, _ = Fabricante.objects.get_or_create(Fabricante='Microsoft')
        dell, _ = Fabricante.objects.get_or_create(Fabricante='Dell')

        Produto.objects.get_or_create(
            categoria=software,
            fabricante=microsoft,
            Produto='Windows 11',
            destaque=False,
            promocao=True,
            msgPromocao='Não sai nunca de promoção!',
            preco=2000,
            image='windows-11.jpg'
        )
        Produto.objects.get_or_create(
            categoria=hardware,
            fabricante=dell,
            Produto='Monitor 24 polegadas',
            destaque=True,
            promocao=True,
            msgPromocao='Até próximo sábado!',
            preco=2000,
            image='monitor-24-polegadas.jpg'
        )