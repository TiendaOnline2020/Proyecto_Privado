# Generated by Django 3.0.3 on 2020-02-25 00:40

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('telefono', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('numero_dni', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('region', models.CharField(choices=[('Amazonas', 'Amazonas'), ('Ancash', 'Ancash'), ('Apurimac', 'Apurimac'), ('Arequipa', 'Arequipa'), ('Ayacucho', 'Ayacucho'), ('Cajamarca', 'Cajamarca'), ('Callao', 'Callao'), ('Cusco', 'Cusco'), ('Huancavelica', 'Huancavelica'), ('Huanuco', 'Huanuco'), ('Ica', 'Ica'), ('Junin', 'Junin'), ('La libertad', 'La libertad'), ('Lambayeque', 'Lambayeque'), ('Lima', 'Lima'), ('Loreto', 'Loreto'), ('Madre de dios', 'Madre de dios'), ('Moquegua', 'Moquegua'), ('Pasco', 'Pasco'), ('Piura', 'Piura'), ('Puno', 'Puno'), ('San martin', 'San martin'), ('Tacna', 'Tacna'), ('Tumbes', 'Tumbes'), ('Ucayali', 'Ucayali')], max_length=255, verbose_name='Region Encargada')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
