# Generated by Django 4.2.4 on 2023-09-27 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("decks", "0007_alter_deck_clase_deck_alter_deck_imagen"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deck",
            name="clase_deck",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="decks.shadowverseclass",
            ),
        ),
    ]
