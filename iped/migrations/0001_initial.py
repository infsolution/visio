# Generated by Django 2.1.5 on 2019-01-30 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Padaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('endereco', models.CharField(max_length=80)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=10)),
                ('favoritos', models.ManyToManyField(to='iped.Cliente')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='padaria', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('descricao', models.CharField(max_length=256)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('fabricacao', models.DateTimeField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('padaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='iped.Padaria')),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
                ('closed', models.BooleanField(default=False)),
                ('dateFinish', models.DateTimeField(blank=True, null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='compras', to='iped.Cliente')),
                ('padaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendas', to='iped.Padaria')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='produto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='produto', to='iped.Produto'),
        ),
        migrations.AddField(
            model_name='item',
            name='venda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='iped.Venda'),
        ),
    ]