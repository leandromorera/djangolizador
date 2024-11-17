from django.db import models

class Requerimientosalmacen(models.Model):
    departamento = models.CharField(max_length=255)

    class Meta:
        db_table = 'requerimientosalmacen'
        managed = False

class DetalleMttoExterno(models.Model):
    iddetalle_mtto = models.IntegerField()
    idroveedor = models.IntegerField()

    class Meta:
        db_table = 'detalle_mtto_externo'
        managed = False

class FamiliaArticulos(models.Model):
    clave = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'familia_articulos'
        managed = False

class Articulos(models.Model):
    idFamilia = models.IntegerField()
    idSubfamilia = models.IntegerField()
    nombre = models.CharField(max_length=255)
    nombre_generico = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)

    class Meta:
        db_table = 'articulos'
        managed = False

class SubfamiliaArticulos(models.Model):
    clave = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'subfamilia_articulos'
        managed = False

class TipoEmpleados(models.Model):
    esoperador = models.BooleanField()
    esmecanico = models.BooleanField()
    clave = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'tipo_empleados'
        managed = False

class Empleados(models.Model):
    idtipoempleado = models.IntegerField()
    no_empleado = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'empleados'
        managed = False

class TipoUnidades(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'tipo_unidades'
        managed = False

class Unidades(models.Model):
    id_tipounidades = models.IntegerField()
    nombre = models.CharField(max_length=255)
    no_economico = models.CharField(max_length=255)

    class Meta:
        db_table = 'unidades'
        managed = False

class ExistenciasArticulos(models.Model):
    existencia = models.CharField(max_length=255)
    idalmacen = models.IntegerField()
    precio = models.CharField(max_length=255)
    idarticulo = models.IntegerField()
    clave = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'existencias_articulos'
        managed = False

class Almacen(models.Model):
    clave = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'almacen'
        managed = False

class Taller(models.Model):
    clave = models.CharField(max_length=255)
    Nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'taller'
        managed = False

class Vaia(models.Model):
    idtaller = models.IntegerField()
    clave = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'vaia'
        managed = False

class EmpleadosUnidad(models.Model):
    idunidades = models.IntegerField()
    idempleados = models.IntegerField()

    class Meta:
        db_table = 'empleados_unidad'
        managed = False

class Areastaller(models.Model):
    idtaller = models.IntegerField()
    clave = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'areastaller'
        managed = False

class Tipomantenimientos(models.Model):
    clave = models.CharField(max_length=255)
    nombre = models.IntegerField()

    class Meta:
        db_table = 'tipomantenimientos'
        managed = False

class Mantenimientos(models.Model):
    fechainicio = models.DateField()
    idtipomantenimiento = models.IntegerField()
    idestatus = models.IntegerField()
    Nombre = models.CharField(max_length=255)
    fechafin = models.CharField(max_length=255)

    class Meta:
        db_table = 'mantenimientos'
        managed = False

class EstatusMantenimiento(models.Model):
    clave = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'estatus_mantenimiento'
        managed = False

class DetalleMttoActividades(models.Model):
    idmentenimientoo = models.IntegerField()
    servicioexterno = models.BooleanField()
    tiempoestimado = models.CharField(max_length=255)
    idservicios = models.IntegerField()
    tiemporeal = models.CharField(max_length=255)
    clave = models.CharField(max_length=255)

    class Meta:
        db_table = 'detalle_mtto_actividades'
        managed = False

class MecanicosTaller(models.Model):
    idempleado = models.IntegerField()
    idtaller = models.IntegerField()
    responsabletaller = models.BooleanField()

    class Meta:
        db_table = 'mecanicos_taller'
        managed = False

class PiezasActividades(models.Model):
    cantidad_solicitada = models.CharField(max_length=255)
    cantidad_surtida = models.CharField(max_length=255)
    Importesurtido = models.CharField(max_length=255)
    idarticulo = models.IntegerField()
    iddetalleactividad = models.IntegerField()

    class Meta:
        db_table = 'piezas_actividades'
        managed = False

class Garantias(models.Model):
    idproveedor = models.IntegerField()
    idmantenimiento = models.IntegerField()
    idarticulo = models.IntegerField()
    fechasolicitud = models.DateField()
    fecharespuesta = models.DateField()

    class Meta:
        db_table = 'garantias'
        managed = False

class Proveedores(models.Model):
    clave = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)

    class Meta:
        db_table = 'proveedores'
        managed = False

class Garatiaseguimiento(models.Model):
    fecha = models.DateField()
    idgarantias = models.IntegerField()
    comentarios = models.CharField(max_length=255)

    class Meta:
        db_table = 'garatiaseguimiento'
        managed = False

class ArticulosServicios(models.Model):
    cantidad = models.CharField(max_length=255)
    idservicios = models.IntegerField()
    idarticulos = models.IntegerField()

    class Meta:
        db_table = 'articulos_servicios'
        managed = False

class ServiciosTaller(models.Model):
    clave = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'servicios_taller'
        managed = False

class DjangoMigrations(models.Model):
    applied = models.DateTimeField()
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'django_migrations'
        managed = False

class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=255)
    model = models.CharField(max_length=255)

    class Meta:
        db_table = 'django_content_type'
        managed = False

class AuthPermission(models.Model):
    content_type_id = models.IntegerField()
    name = models.CharField(max_length=255)
    codename = models.CharField(max_length=255)

    class Meta:
        db_table = 'auth_permission'
        managed = False

class AuthGroup(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'auth_group'
        managed = False

class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        db_table = 'auth_group_permissions'
        managed = False

class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        db_table = 'auth_user_groups'
        managed = False

class AuthUser(models.Model):
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    password = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'auth_user'
        managed = False

class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        db_table = 'auth_user_user_permissions'
        managed = False

class DjangoAdminLog(models.Model):
    user_id = models.IntegerField()
    action_time = models.DateTimeField()
    action_flag = models.IntegerField()
    content_type_id = models.IntegerField()
    object_id = models.CharField(max_length=255)
    object_repr = models.CharField(max_length=255)
    change_message = models.CharField(max_length=255)

    class Meta:
        db_table = 'django_admin_log'
        managed = False

class DjangoSession(models.Model):
    expire_date = models.DateTimeField()
    session_key = models.CharField(max_length=255)
    session_data = models.CharField(max_length=255)

    class Meta:
        db_table = 'django_session'
        managed = False

class WebProject(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'web_project'
        managed = False

class WebTask(models.Model):
    project_id = models.IntegerField()
    done = models.BooleanField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'web_task'
        managed = False

class WebTaller(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'web_taller'
        managed = False

