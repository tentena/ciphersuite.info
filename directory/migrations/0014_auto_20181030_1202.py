# Generated by Django 2.1.2 on 2018-10-30 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0013_auto_20181030_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciphersuite',
            name='auth_algorithm',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='directory.AuthAlgorithm', verbose_name='authentication algorithm'),
        ),
        migrations.AlterField(
            model_name='ciphersuite',
            name='enc_algorithm',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='directory.EncAlgorithm', verbose_name='encryption algorithm'),
        ),
        migrations.AlterField(
            model_name='ciphersuite',
            name='hash_algorithm',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='directory.HashAlgorithm', verbose_name='hash algorithm'),
        ),
        migrations.AlterField(
            model_name='ciphersuite',
            name='kex_algorithm',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='directory.KexAlgorithm', verbose_name='key exchange algorithm'),
        ),
        migrations.AlterField(
            model_name='ciphersuite',
            name='protocol_version',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='directory.ProtocolVersion', verbose_name='protocol version'),
        ),
    ]
