# Generated by Django 4.2.1 on 2024-02-07 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(verbose_name='Формулировка вопроса')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questions', to='categories.category', verbose_name='Тема вопроса')),
            ],
        ),
    ]
