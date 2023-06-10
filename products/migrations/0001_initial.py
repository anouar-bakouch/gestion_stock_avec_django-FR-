# Generated by Django 4.2.2 on 2023-06-10 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nCom', models.IntegerField(max_length=50)),
                ('dateCom', models.DateField()),
                ('montantCde', models.FloatField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nFact', models.IntegerField(max_length=50)),
                ('dateFact', models.DateField()),
                ('montantFact', models.FloatField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nFr', models.IntegerField(max_length=50)),
                ('Societe', models.CharField(max_length=50)),
                ('tel', models.IntegerField(max_length=14)),
                ('email', models.EmailField(max_length=50)),
                ('adresse', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RefProd', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('marque', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Livraison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nBon', models.IntegerField(max_length=50)),
                ('qteLiv', models.IntegerField(max_length=50)),
                ('prixLiv', models.FloatField(max_length=50)),
                ('RefFact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.facture')),
                ('RefProd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.produit')),
            ],
        ),
        migrations.AddField(
            model_name='facture',
            name='nFr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.fournisseur'),
        ),
        migrations.CreateModel(
            name='Devis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nDevis', models.IntegerField(max_length=50)),
                ('dateDevis', models.DateField()),
                ('montant', models.FloatField(max_length=50)),
                ('nFr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.fournisseur')),
            ],
        ),
        migrations.CreateModel(
            name='DetailDevis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qteProd', models.IntegerField(max_length=50)),
                ('prixProd', models.FloatField(max_length=50)),
                ('RefProd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.produit')),
                ('nDevis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.devis')),
            ],
        ),
        migrations.CreateModel(
            name='DetailCommande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qteCde', models.IntegerField(max_length=50)),
                ('prixProd', models.FloatField(max_length=50)),
                ('RefProd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.produit')),
                ('nCom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.commande')),
            ],
        ),
        migrations.AddField(
            model_name='commande',
            name='nFr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.fournisseur'),
        ),
        migrations.AddField(
            model_name='commande',
            name='refDevis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.devis'),
        ),
    ]
