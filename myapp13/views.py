from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *


class RequerimientosalmacenListView(ListView):
    model = Requerimientosalmacen
    template_name = 'myapp13/requerimientosalmacen_list.html'

class RequerimientosalmacenDetailView(DetailView):
    model = Requerimientosalmacen
    template_name = 'myapp13/requerimientosalmacen_detail.html'

class RequerimientosalmacenCreateView(CreateView):
    model = Requerimientosalmacen
    fields = '__all__'
    template_name = 'myapp13/requerimientosalmacen_form.html'
    success_url = reverse_lazy('requerimientosalmacen_list')

class RequerimientosalmacenUpdateView(UpdateView):
    model = Requerimientosalmacen
    fields = '__all__'
    template_name = 'myapp13/requerimientosalmacen_form.html'
    success_url = reverse_lazy('requerimientosalmacen_list')

class RequerimientosalmacenDeleteView(DeleteView):
    model = Requerimientosalmacen
    template_name = 'myapp13/requerimientosalmacen_confirm_delete.html'
    success_url = reverse_lazy('requerimientosalmacen_list')

class DetalleMttoExternoListView(ListView):
    model = DetalleMttoExterno
    template_name = 'myapp13/detalle_mtto_externo_list.html'

class DetalleMttoExternoDetailView(DetailView):
    model = DetalleMttoExterno
    template_name = 'myapp13/detalle_mtto_externo_detail.html'

class DetalleMttoExternoCreateView(CreateView):
    model = DetalleMttoExterno
    fields = '__all__'
    template_name = 'myapp13/detalle_mtto_externo_form.html'
    success_url = reverse_lazy('detalle_mtto_externo_list')

class DetalleMttoExternoUpdateView(UpdateView):
    model = DetalleMttoExterno
    fields = '__all__'
    template_name = 'myapp13/detalle_mtto_externo_form.html'
    success_url = reverse_lazy('detalle_mtto_externo_list')

class DetalleMttoExternoDeleteView(DeleteView):
    model = DetalleMttoExterno
    template_name = 'myapp13/detalle_mtto_externo_confirm_delete.html'
    success_url = reverse_lazy('detalle_mtto_externo_list')

class FamiliaArticulosListView(ListView):
    model = FamiliaArticulos
    template_name = 'myapp13/familia_articulos_list.html'

class FamiliaArticulosDetailView(DetailView):
    model = FamiliaArticulos
    template_name = 'myapp13/familia_articulos_detail.html'

class FamiliaArticulosCreateView(CreateView):
    model = FamiliaArticulos
    fields = '__all__'
    template_name = 'myapp13/familia_articulos_form.html'
    success_url = reverse_lazy('familia_articulos_list')

class FamiliaArticulosUpdateView(UpdateView):
    model = FamiliaArticulos
    fields = '__all__'
    template_name = 'myapp13/familia_articulos_form.html'
    success_url = reverse_lazy('familia_articulos_list')

class FamiliaArticulosDeleteView(DeleteView):
    model = FamiliaArticulos
    template_name = 'myapp13/familia_articulos_confirm_delete.html'
    success_url = reverse_lazy('familia_articulos_list')

class ArticulosListView(ListView):
    model = Articulos
    template_name = 'myapp13/articulos_list.html'

class ArticulosDetailView(DetailView):
    model = Articulos
    template_name = 'myapp13/articulos_detail.html'

class ArticulosCreateView(CreateView):
    model = Articulos
    fields = '__all__'
    template_name = 'myapp13/articulos_form.html'
    success_url = reverse_lazy('articulos_list')

class ArticulosUpdateView(UpdateView):
    model = Articulos
    fields = '__all__'
    template_name = 'myapp13/articulos_form.html'
    success_url = reverse_lazy('articulos_list')

class ArticulosDeleteView(DeleteView):
    model = Articulos
    template_name = 'myapp13/articulos_confirm_delete.html'
    success_url = reverse_lazy('articulos_list')

class SubfamiliaArticulosListView(ListView):
    model = SubfamiliaArticulos
    template_name = 'myapp13/subfamilia_articulos_list.html'

class SubfamiliaArticulosDetailView(DetailView):
    model = SubfamiliaArticulos
    template_name = 'myapp13/subfamilia_articulos_detail.html'

class SubfamiliaArticulosCreateView(CreateView):
    model = SubfamiliaArticulos
    fields = '__all__'
    template_name = 'myapp13/subfamilia_articulos_form.html'
    success_url = reverse_lazy('subfamilia_articulos_list')

class SubfamiliaArticulosUpdateView(UpdateView):
    model = SubfamiliaArticulos
    fields = '__all__'
    template_name = 'myapp13/subfamilia_articulos_form.html'
    success_url = reverse_lazy('subfamilia_articulos_list')

class SubfamiliaArticulosDeleteView(DeleteView):
    model = SubfamiliaArticulos
    template_name = 'myapp13/subfamilia_articulos_confirm_delete.html'
    success_url = reverse_lazy('subfamilia_articulos_list')

class TipoEmpleadosListView(ListView):
    model = TipoEmpleados
    template_name = 'myapp13/tipo_empleados_list.html'

class TipoEmpleadosDetailView(DetailView):
    model = TipoEmpleados
    template_name = 'myapp13/tipo_empleados_detail.html'

class TipoEmpleadosCreateView(CreateView):
    model = TipoEmpleados
    fields = '__all__'
    template_name = 'myapp13/tipo_empleados_form.html'
    success_url = reverse_lazy('tipo_empleados_list')

class TipoEmpleadosUpdateView(UpdateView):
    model = TipoEmpleados
    fields = '__all__'
    template_name = 'myapp13/tipo_empleados_form.html'
    success_url = reverse_lazy('tipo_empleados_list')

class TipoEmpleadosDeleteView(DeleteView):
    model = TipoEmpleados
    template_name = 'myapp13/tipo_empleados_confirm_delete.html'
    success_url = reverse_lazy('tipo_empleados_list')

class EmpleadosListView(ListView):
    model = Empleados
    template_name = 'myapp13/empleados_list.html'

class EmpleadosDetailView(DetailView):
    model = Empleados
    template_name = 'myapp13/empleados_detail.html'

class EmpleadosCreateView(CreateView):
    model = Empleados
    fields = '__all__'
    template_name = 'myapp13/empleados_form.html'
    success_url = reverse_lazy('empleados_list')

class EmpleadosUpdateView(UpdateView):
    model = Empleados
    fields = '__all__'
    template_name = 'myapp13/empleados_form.html'
    success_url = reverse_lazy('empleados_list')

class EmpleadosDeleteView(DeleteView):
    model = Empleados
    template_name = 'myapp13/empleados_confirm_delete.html'
    success_url = reverse_lazy('empleados_list')

class TipoUnidadesListView(ListView):
    model = TipoUnidades
    template_name = 'myapp13/tipo_unidades_list.html'

class TipoUnidadesDetailView(DetailView):
    model = TipoUnidades
    template_name = 'myapp13/tipo_unidades_detail.html'

class TipoUnidadesCreateView(CreateView):
    model = TipoUnidades
    fields = '__all__'
    template_name = 'myapp13/tipo_unidades_form.html'
    success_url = reverse_lazy('tipo_unidades_list')

class TipoUnidadesUpdateView(UpdateView):
    model = TipoUnidades
    fields = '__all__'
    template_name = 'myapp13/tipo_unidades_form.html'
    success_url = reverse_lazy('tipo_unidades_list')

class TipoUnidadesDeleteView(DeleteView):
    model = TipoUnidades
    template_name = 'myapp13/tipo_unidades_confirm_delete.html'
    success_url = reverse_lazy('tipo_unidades_list')

class UnidadesListView(ListView):
    model = Unidades
    template_name = 'myapp13/unidades_list.html'

class UnidadesDetailView(DetailView):
    model = Unidades
    template_name = 'myapp13/unidades_detail.html'

class UnidadesCreateView(CreateView):
    model = Unidades
    fields = '__all__'
    template_name = 'myapp13/unidades_form.html'
    success_url = reverse_lazy('unidades_list')

class UnidadesUpdateView(UpdateView):
    model = Unidades
    fields = '__all__'
    template_name = 'myapp13/unidades_form.html'
    success_url = reverse_lazy('unidades_list')

class UnidadesDeleteView(DeleteView):
    model = Unidades
    template_name = 'myapp13/unidades_confirm_delete.html'
    success_url = reverse_lazy('unidades_list')

class ExistenciasArticulosListView(ListView):
    model = ExistenciasArticulos
    template_name = 'myapp13/existencias_articulos_list.html'

class ExistenciasArticulosDetailView(DetailView):
    model = ExistenciasArticulos
    template_name = 'myapp13/existencias_articulos_detail.html'

class ExistenciasArticulosCreateView(CreateView):
    model = ExistenciasArticulos
    fields = '__all__'
    template_name = 'myapp13/existencias_articulos_form.html'
    success_url = reverse_lazy('existencias_articulos_list')

class ExistenciasArticulosUpdateView(UpdateView):
    model = ExistenciasArticulos
    fields = '__all__'
    template_name = 'myapp13/existencias_articulos_form.html'
    success_url = reverse_lazy('existencias_articulos_list')

class ExistenciasArticulosDeleteView(DeleteView):
    model = ExistenciasArticulos
    template_name = 'myapp13/existencias_articulos_confirm_delete.html'
    success_url = reverse_lazy('existencias_articulos_list')

class AlmacenListView(ListView):
    model = Almacen
    template_name = 'myapp13/almacen_list.html'

class AlmacenDetailView(DetailView):
    model = Almacen
    template_name = 'myapp13/almacen_detail.html'

class AlmacenCreateView(CreateView):
    model = Almacen
    fields = '__all__'
    template_name = 'myapp13/almacen_form.html'
    success_url = reverse_lazy('almacen_list')

class AlmacenUpdateView(UpdateView):
    model = Almacen
    fields = '__all__'
    template_name = 'myapp13/almacen_form.html'
    success_url = reverse_lazy('almacen_list')

class AlmacenDeleteView(DeleteView):
    model = Almacen
    template_name = 'myapp13/almacen_confirm_delete.html'
    success_url = reverse_lazy('almacen_list')

class TallerListView(ListView):
    model = Taller
    template_name = 'myapp13/taller_list.html'

class TallerDetailView(DetailView):
    model = Taller
    template_name = 'myapp13/taller_detail.html'

class TallerCreateView(CreateView):
    model = Taller
    fields = '__all__'
    template_name = 'myapp13/taller_form.html'
    success_url = reverse_lazy('taller_list')

class TallerUpdateView(UpdateView):
    model = Taller
    fields = '__all__'
    template_name = 'myapp13/taller_form.html'
    success_url = reverse_lazy('taller_list')

class TallerDeleteView(DeleteView):
    model = Taller
    template_name = 'myapp13/taller_confirm_delete.html'
    success_url = reverse_lazy('taller_list')

class VaiaListView(ListView):
    model = Vaia
    template_name = 'myapp13/vaia_list.html'

class VaiaDetailView(DetailView):
    model = Vaia
    template_name = 'myapp13/vaia_detail.html'

class VaiaCreateView(CreateView):
    model = Vaia
    fields = '__all__'
    template_name = 'myapp13/vaia_form.html'
    success_url = reverse_lazy('vaia_list')

class VaiaUpdateView(UpdateView):
    model = Vaia
    fields = '__all__'
    template_name = 'myapp13/vaia_form.html'
    success_url = reverse_lazy('vaia_list')

class VaiaDeleteView(DeleteView):
    model = Vaia
    template_name = 'myapp13/vaia_confirm_delete.html'
    success_url = reverse_lazy('vaia_list')

class EmpleadosUnidadListView(ListView):
    model = EmpleadosUnidad
    template_name = 'myapp13/empleados_unidad_list.html'

class EmpleadosUnidadDetailView(DetailView):
    model = EmpleadosUnidad
    template_name = 'myapp13/empleados_unidad_detail.html'

class EmpleadosUnidadCreateView(CreateView):
    model = EmpleadosUnidad
    fields = '__all__'
    template_name = 'myapp13/empleados_unidad_form.html'
    success_url = reverse_lazy('empleados_unidad_list')

class EmpleadosUnidadUpdateView(UpdateView):
    model = EmpleadosUnidad
    fields = '__all__'
    template_name = 'myapp13/empleados_unidad_form.html'
    success_url = reverse_lazy('empleados_unidad_list')

class EmpleadosUnidadDeleteView(DeleteView):
    model = EmpleadosUnidad
    template_name = 'myapp13/empleados_unidad_confirm_delete.html'
    success_url = reverse_lazy('empleados_unidad_list')

class AreastallerListView(ListView):
    model = Areastaller
    template_name = 'myapp13/areastaller_list.html'

class AreastallerDetailView(DetailView):
    model = Areastaller
    template_name = 'myapp13/areastaller_detail.html'

class AreastallerCreateView(CreateView):
    model = Areastaller
    fields = '__all__'
    template_name = 'myapp13/areastaller_form.html'
    success_url = reverse_lazy('areastaller_list')

class AreastallerUpdateView(UpdateView):
    model = Areastaller
    fields = '__all__'
    template_name = 'myapp13/areastaller_form.html'
    success_url = reverse_lazy('areastaller_list')

class AreastallerDeleteView(DeleteView):
    model = Areastaller
    template_name = 'myapp13/areastaller_confirm_delete.html'
    success_url = reverse_lazy('areastaller_list')

class TipomantenimientosListView(ListView):
    model = Tipomantenimientos
    template_name = 'myapp13/tipomantenimientos_list.html'

class TipomantenimientosDetailView(DetailView):
    model = Tipomantenimientos
    template_name = 'myapp13/tipomantenimientos_detail.html'

class TipomantenimientosCreateView(CreateView):
    model = Tipomantenimientos
    fields = '__all__'
    template_name = 'myapp13/tipomantenimientos_form.html'
    success_url = reverse_lazy('tipomantenimientos_list')

class TipomantenimientosUpdateView(UpdateView):
    model = Tipomantenimientos
    fields = '__all__'
    template_name = 'myapp13/tipomantenimientos_form.html'
    success_url = reverse_lazy('tipomantenimientos_list')

class TipomantenimientosDeleteView(DeleteView):
    model = Tipomantenimientos
    template_name = 'myapp13/tipomantenimientos_confirm_delete.html'
    success_url = reverse_lazy('tipomantenimientos_list')

class MantenimientosListView(ListView):
    model = Mantenimientos
    template_name = 'myapp13/mantenimientos_list.html'

class MantenimientosDetailView(DetailView):
    model = Mantenimientos
    template_name = 'myapp13/mantenimientos_detail.html'

class MantenimientosCreateView(CreateView):
    model = Mantenimientos
    fields = '__all__'
    template_name = 'myapp13/mantenimientos_form.html'
    success_url = reverse_lazy('mantenimientos_list')

class MantenimientosUpdateView(UpdateView):
    model = Mantenimientos
    fields = '__all__'
    template_name = 'myapp13/mantenimientos_form.html'
    success_url = reverse_lazy('mantenimientos_list')

class MantenimientosDeleteView(DeleteView):
    model = Mantenimientos
    template_name = 'myapp13/mantenimientos_confirm_delete.html'
    success_url = reverse_lazy('mantenimientos_list')

class EstatusMantenimientoListView(ListView):
    model = EstatusMantenimiento
    template_name = 'myapp13/estatus_mantenimiento_list.html'

class EstatusMantenimientoDetailView(DetailView):
    model = EstatusMantenimiento
    template_name = 'myapp13/estatus_mantenimiento_detail.html'

class EstatusMantenimientoCreateView(CreateView):
    model = EstatusMantenimiento
    fields = '__all__'
    template_name = 'myapp13/estatus_mantenimiento_form.html'
    success_url = reverse_lazy('estatus_mantenimiento_list')

class EstatusMantenimientoUpdateView(UpdateView):
    model = EstatusMantenimiento
    fields = '__all__'
    template_name = 'myapp13/estatus_mantenimiento_form.html'
    success_url = reverse_lazy('estatus_mantenimiento_list')

class EstatusMantenimientoDeleteView(DeleteView):
    model = EstatusMantenimiento
    template_name = 'myapp13/estatus_mantenimiento_confirm_delete.html'
    success_url = reverse_lazy('estatus_mantenimiento_list')

class DetalleMttoActividadesListView(ListView):
    model = DetalleMttoActividades
    template_name = 'myapp13/detalle_mtto_actividades_list.html'

class DetalleMttoActividadesDetailView(DetailView):
    model = DetalleMttoActividades
    template_name = 'myapp13/detalle_mtto_actividades_detail.html'

class DetalleMttoActividadesCreateView(CreateView):
    model = DetalleMttoActividades
    fields = '__all__'
    template_name = 'myapp13/detalle_mtto_actividades_form.html'
    success_url = reverse_lazy('detalle_mtto_actividades_list')

class DetalleMttoActividadesUpdateView(UpdateView):
    model = DetalleMttoActividades
    fields = '__all__'
    template_name = 'myapp13/detalle_mtto_actividades_form.html'
    success_url = reverse_lazy('detalle_mtto_actividades_list')

class DetalleMttoActividadesDeleteView(DeleteView):
    model = DetalleMttoActividades
    template_name = 'myapp13/detalle_mtto_actividades_confirm_delete.html'
    success_url = reverse_lazy('detalle_mtto_actividades_list')

class MecanicosTallerListView(ListView):
    model = MecanicosTaller
    template_name = 'myapp13/mecanicos_taller_list.html'

class MecanicosTallerDetailView(DetailView):
    model = MecanicosTaller
    template_name = 'myapp13/mecanicos_taller_detail.html'

class MecanicosTallerCreateView(CreateView):
    model = MecanicosTaller
    fields = '__all__'
    template_name = 'myapp13/mecanicos_taller_form.html'
    success_url = reverse_lazy('mecanicos_taller_list')

class MecanicosTallerUpdateView(UpdateView):
    model = MecanicosTaller
    fields = '__all__'
    template_name = 'myapp13/mecanicos_taller_form.html'
    success_url = reverse_lazy('mecanicos_taller_list')

class MecanicosTallerDeleteView(DeleteView):
    model = MecanicosTaller
    template_name = 'myapp13/mecanicos_taller_confirm_delete.html'
    success_url = reverse_lazy('mecanicos_taller_list')

class PiezasActividadesListView(ListView):
    model = PiezasActividades
    template_name = 'myapp13/piezas_actividades_list.html'

class PiezasActividadesDetailView(DetailView):
    model = PiezasActividades
    template_name = 'myapp13/piezas_actividades_detail.html'

class PiezasActividadesCreateView(CreateView):
    model = PiezasActividades
    fields = '__all__'
    template_name = 'myapp13/piezas_actividades_form.html'
    success_url = reverse_lazy('piezas_actividades_list')

class PiezasActividadesUpdateView(UpdateView):
    model = PiezasActividades
    fields = '__all__'
    template_name = 'myapp13/piezas_actividades_form.html'
    success_url = reverse_lazy('piezas_actividades_list')

class PiezasActividadesDeleteView(DeleteView):
    model = PiezasActividades
    template_name = 'myapp13/piezas_actividades_confirm_delete.html'
    success_url = reverse_lazy('piezas_actividades_list')

class GarantiasListView(ListView):
    model = Garantias
    template_name = 'myapp13/garantias_list.html'

class GarantiasDetailView(DetailView):
    model = Garantias
    template_name = 'myapp13/garantias_detail.html'

class GarantiasCreateView(CreateView):
    model = Garantias
    fields = '__all__'
    template_name = 'myapp13/garantias_form.html'
    success_url = reverse_lazy('garantias_list')

class GarantiasUpdateView(UpdateView):
    model = Garantias
    fields = '__all__'
    template_name = 'myapp13/garantias_form.html'
    success_url = reverse_lazy('garantias_list')

class GarantiasDeleteView(DeleteView):
    model = Garantias
    template_name = 'myapp13/garantias_confirm_delete.html'
    success_url = reverse_lazy('garantias_list')

class ProveedoresListView(ListView):
    model = Proveedores
    template_name = 'myapp13/proveedores_list.html'

class ProveedoresDetailView(DetailView):
    model = Proveedores
    template_name = 'myapp13/proveedores_detail.html'

class ProveedoresCreateView(CreateView):
    model = Proveedores
    fields = '__all__'
    template_name = 'myapp13/proveedores_form.html'
    success_url = reverse_lazy('proveedores_list')

class ProveedoresUpdateView(UpdateView):
    model = Proveedores
    fields = '__all__'
    template_name = 'myapp13/proveedores_form.html'
    success_url = reverse_lazy('proveedores_list')

class ProveedoresDeleteView(DeleteView):
    model = Proveedores
    template_name = 'myapp13/proveedores_confirm_delete.html'
    success_url = reverse_lazy('proveedores_list')

class GaratiaseguimientoListView(ListView):
    model = Garatiaseguimiento
    template_name = 'myapp13/garatiaseguimiento_list.html'

class GaratiaseguimientoDetailView(DetailView):
    model = Garatiaseguimiento
    template_name = 'myapp13/garatiaseguimiento_detail.html'

class GaratiaseguimientoCreateView(CreateView):
    model = Garatiaseguimiento
    fields = '__all__'
    template_name = 'myapp13/garatiaseguimiento_form.html'
    success_url = reverse_lazy('garatiaseguimiento_list')

class GaratiaseguimientoUpdateView(UpdateView):
    model = Garatiaseguimiento
    fields = '__all__'
    template_name = 'myapp13/garatiaseguimiento_form.html'
    success_url = reverse_lazy('garatiaseguimiento_list')

class GaratiaseguimientoDeleteView(DeleteView):
    model = Garatiaseguimiento
    template_name = 'myapp13/garatiaseguimiento_confirm_delete.html'
    success_url = reverse_lazy('garatiaseguimiento_list')

class ArticulosServiciosListView(ListView):
    model = ArticulosServicios
    template_name = 'myapp13/articulos_servicios_list.html'

class ArticulosServiciosDetailView(DetailView):
    model = ArticulosServicios
    template_name = 'myapp13/articulos_servicios_detail.html'

class ArticulosServiciosCreateView(CreateView):
    model = ArticulosServicios
    fields = '__all__'
    template_name = 'myapp13/articulos_servicios_form.html'
    success_url = reverse_lazy('articulos_servicios_list')

class ArticulosServiciosUpdateView(UpdateView):
    model = ArticulosServicios
    fields = '__all__'
    template_name = 'myapp13/articulos_servicios_form.html'
    success_url = reverse_lazy('articulos_servicios_list')

class ArticulosServiciosDeleteView(DeleteView):
    model = ArticulosServicios
    template_name = 'myapp13/articulos_servicios_confirm_delete.html'
    success_url = reverse_lazy('articulos_servicios_list')

class ServiciosTallerListView(ListView):
    model = ServiciosTaller
    template_name = 'myapp13/servicios_taller_list.html'

class ServiciosTallerDetailView(DetailView):
    model = ServiciosTaller
    template_name = 'myapp13/servicios_taller_detail.html'

class ServiciosTallerCreateView(CreateView):
    model = ServiciosTaller
    fields = '__all__'
    template_name = 'myapp13/servicios_taller_form.html'
    success_url = reverse_lazy('servicios_taller_list')

class ServiciosTallerUpdateView(UpdateView):
    model = ServiciosTaller
    fields = '__all__'
    template_name = 'myapp13/servicios_taller_form.html'
    success_url = reverse_lazy('servicios_taller_list')

class ServiciosTallerDeleteView(DeleteView):
    model = ServiciosTaller
    template_name = 'myapp13/servicios_taller_confirm_delete.html'
    success_url = reverse_lazy('servicios_taller_list')

class DjangoMigrationsListView(ListView):
    model = DjangoMigrations
    template_name = 'myapp13/django_migrations_list.html'

class DjangoMigrationsDetailView(DetailView):
    model = DjangoMigrations
    template_name = 'myapp13/django_migrations_detail.html'

class DjangoMigrationsCreateView(CreateView):
    model = DjangoMigrations
    fields = '__all__'
    template_name = 'myapp13/django_migrations_form.html'
    success_url = reverse_lazy('django_migrations_list')

class DjangoMigrationsUpdateView(UpdateView):
    model = DjangoMigrations
    fields = '__all__'
    template_name = 'myapp13/django_migrations_form.html'
    success_url = reverse_lazy('django_migrations_list')

class DjangoMigrationsDeleteView(DeleteView):
    model = DjangoMigrations
    template_name = 'myapp13/django_migrations_confirm_delete.html'
    success_url = reverse_lazy('django_migrations_list')

class DjangoContentTypeListView(ListView):
    model = DjangoContentType
    template_name = 'myapp13/django_content_type_list.html'

class DjangoContentTypeDetailView(DetailView):
    model = DjangoContentType
    template_name = 'myapp13/django_content_type_detail.html'

class DjangoContentTypeCreateView(CreateView):
    model = DjangoContentType
    fields = '__all__'
    template_name = 'myapp13/django_content_type_form.html'
    success_url = reverse_lazy('django_content_type_list')

class DjangoContentTypeUpdateView(UpdateView):
    model = DjangoContentType
    fields = '__all__'
    template_name = 'myapp13/django_content_type_form.html'
    success_url = reverse_lazy('django_content_type_list')

class DjangoContentTypeDeleteView(DeleteView):
    model = DjangoContentType
    template_name = 'myapp13/django_content_type_confirm_delete.html'
    success_url = reverse_lazy('django_content_type_list')

class AuthPermissionListView(ListView):
    model = AuthPermission
    template_name = 'myapp13/auth_permission_list.html'

class AuthPermissionDetailView(DetailView):
    model = AuthPermission
    template_name = 'myapp13/auth_permission_detail.html'

class AuthPermissionCreateView(CreateView):
    model = AuthPermission
    fields = '__all__'
    template_name = 'myapp13/auth_permission_form.html'
    success_url = reverse_lazy('auth_permission_list')

class AuthPermissionUpdateView(UpdateView):
    model = AuthPermission
    fields = '__all__'
    template_name = 'myapp13/auth_permission_form.html'
    success_url = reverse_lazy('auth_permission_list')

class AuthPermissionDeleteView(DeleteView):
    model = AuthPermission
    template_name = 'myapp13/auth_permission_confirm_delete.html'
    success_url = reverse_lazy('auth_permission_list')

class AuthGroupListView(ListView):
    model = AuthGroup
    template_name = 'myapp13/auth_group_list.html'

class AuthGroupDetailView(DetailView):
    model = AuthGroup
    template_name = 'myapp13/auth_group_detail.html'

class AuthGroupCreateView(CreateView):
    model = AuthGroup
    fields = '__all__'
    template_name = 'myapp13/auth_group_form.html'
    success_url = reverse_lazy('auth_group_list')

class AuthGroupUpdateView(UpdateView):
    model = AuthGroup
    fields = '__all__'
    template_name = 'myapp13/auth_group_form.html'
    success_url = reverse_lazy('auth_group_list')

class AuthGroupDeleteView(DeleteView):
    model = AuthGroup
    template_name = 'myapp13/auth_group_confirm_delete.html'
    success_url = reverse_lazy('auth_group_list')

class AuthGroupPermissionsListView(ListView):
    model = AuthGroupPermissions
    template_name = 'myapp13/auth_group_permissions_list.html'

class AuthGroupPermissionsDetailView(DetailView):
    model = AuthGroupPermissions
    template_name = 'myapp13/auth_group_permissions_detail.html'

class AuthGroupPermissionsCreateView(CreateView):
    model = AuthGroupPermissions
    fields = '__all__'
    template_name = 'myapp13/auth_group_permissions_form.html'
    success_url = reverse_lazy('auth_group_permissions_list')

class AuthGroupPermissionsUpdateView(UpdateView):
    model = AuthGroupPermissions
    fields = '__all__'
    template_name = 'myapp13/auth_group_permissions_form.html'
    success_url = reverse_lazy('auth_group_permissions_list')

class AuthGroupPermissionsDeleteView(DeleteView):
    model = AuthGroupPermissions
    template_name = 'myapp13/auth_group_permissions_confirm_delete.html'
    success_url = reverse_lazy('auth_group_permissions_list')

class AuthUserGroupsListView(ListView):
    model = AuthUserGroups
    template_name = 'myapp13/auth_user_groups_list.html'

class AuthUserGroupsDetailView(DetailView):
    model = AuthUserGroups
    template_name = 'myapp13/auth_user_groups_detail.html'

class AuthUserGroupsCreateView(CreateView):
    model = AuthUserGroups
    fields = '__all__'
    template_name = 'myapp13/auth_user_groups_form.html'
    success_url = reverse_lazy('auth_user_groups_list')

class AuthUserGroupsUpdateView(UpdateView):
    model = AuthUserGroups
    fields = '__all__'
    template_name = 'myapp13/auth_user_groups_form.html'
    success_url = reverse_lazy('auth_user_groups_list')

class AuthUserGroupsDeleteView(DeleteView):
    model = AuthUserGroups
    template_name = 'myapp13/auth_user_groups_confirm_delete.html'
    success_url = reverse_lazy('auth_user_groups_list')

class AuthUserListView(ListView):
    model = AuthUser
    template_name = 'myapp13/auth_user_list.html'

class AuthUserDetailView(DetailView):
    model = AuthUser
    template_name = 'myapp13/auth_user_detail.html'

class AuthUserCreateView(CreateView):
    model = AuthUser
    fields = '__all__'
    template_name = 'myapp13/auth_user_form.html'
    success_url = reverse_lazy('auth_user_list')

class AuthUserUpdateView(UpdateView):
    model = AuthUser
    fields = '__all__'
    template_name = 'myapp13/auth_user_form.html'
    success_url = reverse_lazy('auth_user_list')

class AuthUserDeleteView(DeleteView):
    model = AuthUser
    template_name = 'myapp13/auth_user_confirm_delete.html'
    success_url = reverse_lazy('auth_user_list')

class AuthUserUserPermissionsListView(ListView):
    model = AuthUserUserPermissions
    template_name = 'myapp13/auth_user_user_permissions_list.html'

class AuthUserUserPermissionsDetailView(DetailView):
    model = AuthUserUserPermissions
    template_name = 'myapp13/auth_user_user_permissions_detail.html'

class AuthUserUserPermissionsCreateView(CreateView):
    model = AuthUserUserPermissions
    fields = '__all__'
    template_name = 'myapp13/auth_user_user_permissions_form.html'
    success_url = reverse_lazy('auth_user_user_permissions_list')

class AuthUserUserPermissionsUpdateView(UpdateView):
    model = AuthUserUserPermissions
    fields = '__all__'
    template_name = 'myapp13/auth_user_user_permissions_form.html'
    success_url = reverse_lazy('auth_user_user_permissions_list')

class AuthUserUserPermissionsDeleteView(DeleteView):
    model = AuthUserUserPermissions
    template_name = 'myapp13/auth_user_user_permissions_confirm_delete.html'
    success_url = reverse_lazy('auth_user_user_permissions_list')

class DjangoAdminLogListView(ListView):
    model = DjangoAdminLog
    template_name = 'myapp13/django_admin_log_list.html'

class DjangoAdminLogDetailView(DetailView):
    model = DjangoAdminLog
    template_name = 'myapp13/django_admin_log_detail.html'

class DjangoAdminLogCreateView(CreateView):
    model = DjangoAdminLog
    fields = '__all__'
    template_name = 'myapp13/django_admin_log_form.html'
    success_url = reverse_lazy('django_admin_log_list')

class DjangoAdminLogUpdateView(UpdateView):
    model = DjangoAdminLog
    fields = '__all__'
    template_name = 'myapp13/django_admin_log_form.html'
    success_url = reverse_lazy('django_admin_log_list')

class DjangoAdminLogDeleteView(DeleteView):
    model = DjangoAdminLog
    template_name = 'myapp13/django_admin_log_confirm_delete.html'
    success_url = reverse_lazy('django_admin_log_list')

class DjangoSessionListView(ListView):
    model = DjangoSession
    template_name = 'myapp13/django_session_list.html'

class DjangoSessionDetailView(DetailView):
    model = DjangoSession
    template_name = 'myapp13/django_session_detail.html'

class DjangoSessionCreateView(CreateView):
    model = DjangoSession
    fields = '__all__'
    template_name = 'myapp13/django_session_form.html'
    success_url = reverse_lazy('django_session_list')

class DjangoSessionUpdateView(UpdateView):
    model = DjangoSession
    fields = '__all__'
    template_name = 'myapp13/django_session_form.html'
    success_url = reverse_lazy('django_session_list')

class DjangoSessionDeleteView(DeleteView):
    model = DjangoSession
    template_name = 'myapp13/django_session_confirm_delete.html'
    success_url = reverse_lazy('django_session_list')

class WebProjectListView(ListView):
    model = WebProject
    template_name = 'myapp13/web_project_list.html'

class WebProjectDetailView(DetailView):
    model = WebProject
    template_name = 'myapp13/web_project_detail.html'

class WebProjectCreateView(CreateView):
    model = WebProject
    fields = '__all__'
    template_name = 'myapp13/web_project_form.html'
    success_url = reverse_lazy('web_project_list')

class WebProjectUpdateView(UpdateView):
    model = WebProject
    fields = '__all__'
    template_name = 'myapp13/web_project_form.html'
    success_url = reverse_lazy('web_project_list')

class WebProjectDeleteView(DeleteView):
    model = WebProject
    template_name = 'myapp13/web_project_confirm_delete.html'
    success_url = reverse_lazy('web_project_list')

class WebTaskListView(ListView):
    model = WebTask
    template_name = 'myapp13/web_task_list.html'

class WebTaskDetailView(DetailView):
    model = WebTask
    template_name = 'myapp13/web_task_detail.html'

class WebTaskCreateView(CreateView):
    model = WebTask
    fields = '__all__'
    template_name = 'myapp13/web_task_form.html'
    success_url = reverse_lazy('web_task_list')

class WebTaskUpdateView(UpdateView):
    model = WebTask
    fields = '__all__'
    template_name = 'myapp13/web_task_form.html'
    success_url = reverse_lazy('web_task_list')

class WebTaskDeleteView(DeleteView):
    model = WebTask
    template_name = 'myapp13/web_task_confirm_delete.html'
    success_url = reverse_lazy('web_task_list')

class WebTallerListView(ListView):
    model = WebTaller
    template_name = 'myapp13/web_taller_list.html'

class WebTallerDetailView(DetailView):
    model = WebTaller
    template_name = 'myapp13/web_taller_detail.html'

class WebTallerCreateView(CreateView):
    model = WebTaller
    fields = '__all__'
    template_name = 'myapp13/web_taller_form.html'
    success_url = reverse_lazy('web_taller_list')

class WebTallerUpdateView(UpdateView):
    model = WebTaller
    fields = '__all__'
    template_name = 'myapp13/web_taller_form.html'
    success_url = reverse_lazy('web_taller_list')

class WebTallerDeleteView(DeleteView):
    model = WebTaller
    template_name = 'myapp13/web_taller_confirm_delete.html'
    success_url = reverse_lazy('web_taller_list')
