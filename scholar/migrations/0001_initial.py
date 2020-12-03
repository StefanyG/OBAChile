# Generated by Django 2.2.10 on 2020-11-18 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('last_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id_a', models.TextField(blank=True, db_column='Id_A', primary_key=True, serialize=False, unique=True)),
                ('nombre_autor', models.TextField(db_column='Nombre_Autor')),
                ('cargo', models.TextField(db_column='Cargo')),
                ('dominio', models.TextField(db_column='Dominio')),
                ('citas', models.TextField(db_column='Citas')),
                ('intereses', models.TextField(db_column='Intereses')),
                ('links', models.TextField(db_column='Links')),
                ('año_desde', models.IntegerField(blank=True, db_column='Año_Desde', null=True)),
                ('hindex_todo', models.IntegerField(blank=True, db_column='Hindex_todo', null=True)),
                ('hindex_desde', models.IntegerField(blank=True, db_column='Hindex_Desde', null=True)),
                ('todas_citas', models.IntegerField(blank=True, db_column='Todas_Citas', null=True)),
                ('citas_desde', models.IntegerField(blank=True, db_column='Citas_Desde', null=True)),
                ('id_institucion', models.TextField(blank=True, db_column='Id_Institucion', null=True)),
            ],
            options={
                'db_table': 'Autor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AutorPaper',
            fields=[
                ('a_id', models.IntegerField(blank=True, db_column='A_id', primary_key=True, serialize=False)),
                ('paper_id', models.TextField(db_column='Paper_Id')),
                ('autorpaper_id', models.TextField(db_column='AutorPaper_Id')),
                ('autor_id', models.TextField(db_column='Autor_Id')),
                ('titulo_paper', models.TextField(db_column='Titulo_Paper')),
                ('autores_paper', models.TextField(db_column='Autores_Paper')),
                ('revista', models.TextField(db_column='Revista')),
                ('revista_sp', models.TextField(db_column='Revista_sp')),
                ('revista_m', models.TextField(db_column='Revista_m')),
                ('citado_por', models.TextField(db_column='Citado_Por')),
                ('año', models.TextField(db_column='Año')),
                ('link_paper', models.TextField(db_column='Link_Paper')),
            ],
            options={
                'db_table': 'Autor_Paper',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('autor_id', models.TextField(blank=True, db_column='Autor_Id', null=True)),
                ('year_hist', models.TextField(blank=True, db_column='Year_hist', null=True)),
                ('citas_hist', models.TextField(blank=True, db_column='Citas_hist', null=True)),
            ],
            options={
                'db_table': 'Citas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Coautores',
            fields=[
                ('id', models.IntegerField(blank=True, db_column='Id', primary_key=True, serialize=False)),
                ('coautor_id', models.TextField(blank=True, db_column='Coautor_Id', null=True)),
                ('coautor', models.TextField(blank=True, db_column='Coautor', null=True)),
                ('institucion', models.TextField(blank=True, db_column='Institucion', null=True)),
                ('dominio', models.TextField(blank=True, db_column='Dominio', null=True)),
                ('a_id', models.TextField(blank=True, db_column='A_Id', null=True)),
            ],
            options={
                'db_table': 'Coautores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Instituciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institutiontypeid', models.IntegerField(blank=True, db_column='InstitutionTypeID', null=True)),
                ('institutiontype', models.TextField(blank=True, db_column='InstitutionType', null=True)),
                ('institutionacronymid', models.TextField(blank=True, db_column='InstitutionAcronymID', null=True)),
                ('institutionacronym', models.TextField(blank=True, db_column='InstitutionAcronym', null=True)),
                ('institutionid', models.IntegerField(blank=True, db_column='InstitutionID', null=True)),
                ('institution', models.TextField(blank=True, db_column='Institution', null=True)),
                ('students', models.IntegerField(blank=True, db_column='Students', null=True)),
                ('googlescholarid', models.TextField(blank=True, db_column='GoogleScholarID', null=True)),
            ],
            options={
                'db_table': 'Instituciones',
                'managed': False,
            },
        ),
    ]
