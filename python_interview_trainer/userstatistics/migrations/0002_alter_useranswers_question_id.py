# Generated by Django 4.2.1 on 2024-03-05 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
        ('userstatistics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswers',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions_for_user', to='questions.question', verbose_name='Вопросы'),
        ),
    ]