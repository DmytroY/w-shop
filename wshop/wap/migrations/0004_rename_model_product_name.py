# Generated by Django 4.0.6 on 2022-08-02 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wap', '0003_alter_product_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='model',
            new_name='name',
        ),
    ]