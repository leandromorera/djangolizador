# Generated by Django 4.0.6 on 2024-11-17 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.IntegerField()),
                ('clave', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'almacen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Areastaller',
            fields=[
                ('id', models.IntegerField()),
                ('idtaller', models.IntegerField()),
                ('clave', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'areastaller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.IntegerField()),
                ('idFamilia', models.IntegerField()),
                ('idSubfamilia', models.IntegerField()),
                ('nombre', models.CharField(max_length=255)),
                ('nombre_generico', models.CharField(max_length=255)),
                ('sku', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'articulos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArticulosServicios',
            fields=[
                ('id', models.IntegerField()),
                ('cantidad', models.CharField(max_length=255)),
                ('idservicios', models.IntegerField()),
                ('idarticulos', models.IntegerField()),
            ],
            options={
                'db_table': 'articulos_servicios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField()),
                ('group_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField()),
                ('content_type_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField()),
                ('last_login', models.DateTimeField()),
                ('is_superuser', models.BooleanField()),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('password', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleMttoActividades',
            fields=[
                ('id', models.IntegerField()),
                ('idmentenimientoo', models.IntegerField()),
                ('servicioexterno', models.BooleanField()),
                ('tiempoestimado', models.CharField(max_length=255)),
                ('idservicios', models.IntegerField()),
                ('tiemporeal', models.CharField(max_length=255)),
                ('clave', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'detalle_mtto_actividades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleMttoExterno',
            fields=[
                ('id', models.IntegerField()),
                ('iddetalle_mtto', models.IntegerField()),
                ('idroveedor', models.IntegerField()),
            ],
            options={
                'db_table': 'detalle_mtto_externo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('action_time', models.DateTimeField()),
                ('action_flag', models.IntegerField()),
                ('content_type_id', models.IntegerField()),
                ('object_id', models.CharField(max_length=255)),
                ('object_repr', models.CharField(max_length=255)),
                ('change_message', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField()),
                ('app_label', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField()),
                ('applied', models.DateTimeField()),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expire_date', models.DateTimeField()),
                ('session_key', models.CharField(max_length=255)),
                ('session_data', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.IntegerField()),
                ('idtipoempleado', models.IntegerField()),
                ('no_empleado', models.CharField(max_length=255)),
                ('apellido_paterno', models.CharField(max_length=255)),
                ('apellido_materno', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'empleados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmpleadosUnidad',
            fields=[
                ('id', models.IntegerField()),
                ('idunidades', models.IntegerField()),
                ('idempleados', models.IntegerField()),
            ],
            options={
                'db_table': 'empleados_unidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstatusMantenimiento',
            fields=[
                ('id', models.IntegerField()),
                ('clave', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'estatus_mantenimiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ExistenciasArticulos',
            fields=[
                ('id', models.IntegerField()),
                ('existencia', models.CharField(max_length=255)),
                ('idalmacen', models.IntegerField()),
                ('precio', models.CharField(max_length=255)),
                ('idarticulo', models.IntegerField()),
                ('clave', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'existencias_articulos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FamiliaArticulos',
            fields=[
                ('id', models.IntegerField()),
                ('clave', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'familia_articulos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Garantias',
            fields=[
                ('id', models.IntegerField()),
                ('idproveedor', models.IntegerField()),
                ('idmantenimiento', models.IntegerField()),
                ('idarticulo', models.IntegerField()),
                ('fechasolicitud', models.DateField()),
                ('fecharespuesta', models.DateField()),
            ],
            options={
                'db_table': 'garantias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Garatiaseguimiento',
            fields=[
                ('id', models.IntegerField()),
                ('fecha', models.DateField()),
                ('idgarantias', models.IntegerField()),
                ('comentarios', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'garatiaseguimiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mantenimientos',
            fields=[
                ('id', models.IntegerField()),
                ('fechainicio', models.DateField()),
                ('idtipomantenimiento', models.IntegerField()),
                ('idestatus', models.IntegerField()),
                ('Nombre', models.CharField(max_length=255)),
                ('fechafin', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'mantenimientos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MecanicosTaller',
            fields=[
                ('id', models.IntegerField()),
                ('idempleado', models.IntegerField()),
                ('idtaller', models.IntegerField()),
                ('responsabletaller', models.BooleanField()),
            ],
            options={
                'db_table': 'mecanicos_taller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PiezasActividades',
            fields=[
                ('id', models.IntegerField()),
                ('cantidad_solicitada', models.CharField(max_length=255)),
                ('cantidad_surtida', models.CharField(max_length=255)),
                ('Importesurtido', models.CharField(max_length=255)),
                ('idarticulo', models.IntegerField()),
                ('iddetalleactividad', models.IntegerField()),
            ],
            options={
                'db_table': 'piezas_actividades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.IntegerField()),
                ('clave', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('correo', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'proveedores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Requerimientosalmacen',
            fields=[
                ('id', models.IntegerField()),
                ('departamento', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'requerimientosalmacen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiciosTaller',
            fields=[
                ('id', models.IntegerField()),
                ('clave', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'servicios_taller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubfamiliaArticulos',
            fields=[
                ('id', models.IntegerField()),
                ('clave', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'subfamilia_articulos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('id', models.IntegerField()),
                ('clave', models.CharField(max_length=255)),
                ('Nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'taller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoEmpleados',
            fields=[
                ('id', models.IntegerField()),
                ('esoperador', models.BooleanField()),
                ('esmecanico', models.BooleanField()),
                ('clave', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tipo_empleados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipomantenimientos',
            fields=[
                ('id', models.IntegerField()),
                ('clave', models.CharField(max_length=255)),
                ('nombre', models.IntegerField()),
            ],
            options={
                'db_table': 'tipomantenimientos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoUnidades',
            fields=[
                ('id', models.IntegerField()),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tipo_unidades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Unidades',
            fields=[
                ('id', models.IntegerField()),
                ('id_tipounidades', models.IntegerField()),
                ('nombre', models.CharField(max_length=255)),
                ('no_economico', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'unidades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vaia',
            fields=[
                ('id', models.IntegerField()),
                ('idtaller', models.IntegerField()),
                ('clave', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'vaia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WebProject',
            fields=[
                ('id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'web_project',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WebTaller',
            fields=[
                ('id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'web_taller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WebTask',
            fields=[
                ('id', models.IntegerField()),
                ('project_id', models.IntegerField()),
                ('done', models.BooleanField()),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'web_task',
                'managed': False,
            },
        ),
    ]