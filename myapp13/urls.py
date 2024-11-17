from django.urls import path
from . import views

urlpatterns = [
    path('requerimientosalmacen/', views.RequerimientosalmacenListView.as_view(), name='requerimientosalmacen_list'),
    path('requerimientosalmacen/<int:pk>/', views.RequerimientosalmacenDetailView.as_view(), name='requerimientosalmacen_detail'),
    path('requerimientosalmacen/create/', views.RequerimientosalmacenCreateView.as_view(), name='requerimientosalmacen_create'),
    path('requerimientosalmacen/<int:pk>/edit/', views.RequerimientosalmacenUpdateView.as_view(), name='requerimientosalmacen_edit'),
    path('requerimientosalmacen/<int:pk>/delete/', views.RequerimientosalmacenDeleteView.as_view(), name='requerimientosalmacen_delete'),
    path('detalle_mtto_externo/', views.DetalleMttoExternoListView.as_view(), name='detalle_mtto_externo_list'),
    path('detalle_mtto_externo/<int:pk>/', views.DetalleMttoExternoDetailView.as_view(), name='detalle_mtto_externo_detail'),
    path('detalle_mtto_externo/create/', views.DetalleMttoExternoCreateView.as_view(), name='detalle_mtto_externo_create'),
    path('detalle_mtto_externo/<int:pk>/edit/', views.DetalleMttoExternoUpdateView.as_view(), name='detalle_mtto_externo_edit'),
    path('detalle_mtto_externo/<int:pk>/delete/', views.DetalleMttoExternoDeleteView.as_view(), name='detalle_mtto_externo_delete'),
    path('familia_articulos/', views.FamiliaArticulosListView.as_view(), name='familia_articulos_list'),
    path('familia_articulos/<int:pk>/', views.FamiliaArticulosDetailView.as_view(), name='familia_articulos_detail'),
    path('familia_articulos/create/', views.FamiliaArticulosCreateView.as_view(), name='familia_articulos_create'),
    path('familia_articulos/<int:pk>/edit/', views.FamiliaArticulosUpdateView.as_view(), name='familia_articulos_edit'),
    path('familia_articulos/<int:pk>/delete/', views.FamiliaArticulosDeleteView.as_view(), name='familia_articulos_delete'),
    path('articulos/', views.ArticulosListView.as_view(), name='articulos_list'),
    path('articulos/<int:pk>/', views.ArticulosDetailView.as_view(), name='articulos_detail'),
    path('articulos/create/', views.ArticulosCreateView.as_view(), name='articulos_create'),
    path('articulos/<int:pk>/edit/', views.ArticulosUpdateView.as_view(), name='articulos_edit'),
    path('articulos/<int:pk>/delete/', views.ArticulosDeleteView.as_view(), name='articulos_delete'),
    path('subfamilia_articulos/', views.SubfamiliaArticulosListView.as_view(), name='subfamilia_articulos_list'),
    path('subfamilia_articulos/<int:pk>/', views.SubfamiliaArticulosDetailView.as_view(), name='subfamilia_articulos_detail'),
    path('subfamilia_articulos/create/', views.SubfamiliaArticulosCreateView.as_view(), name='subfamilia_articulos_create'),
    path('subfamilia_articulos/<int:pk>/edit/', views.SubfamiliaArticulosUpdateView.as_view(), name='subfamilia_articulos_edit'),
    path('subfamilia_articulos/<int:pk>/delete/', views.SubfamiliaArticulosDeleteView.as_view(), name='subfamilia_articulos_delete'),
    path('tipo_empleados/', views.TipoEmpleadosListView.as_view(), name='tipo_empleados_list'),
    path('tipo_empleados/<int:pk>/', views.TipoEmpleadosDetailView.as_view(), name='tipo_empleados_detail'),
    path('tipo_empleados/create/', views.TipoEmpleadosCreateView.as_view(), name='tipo_empleados_create'),
    path('tipo_empleados/<int:pk>/edit/', views.TipoEmpleadosUpdateView.as_view(), name='tipo_empleados_edit'),
    path('tipo_empleados/<int:pk>/delete/', views.TipoEmpleadosDeleteView.as_view(), name='tipo_empleados_delete'),
    path('empleados/', views.EmpleadosListView.as_view(), name='empleados_list'),
    path('empleados/<int:pk>/', views.EmpleadosDetailView.as_view(), name='empleados_detail'),
    path('empleados/create/', views.EmpleadosCreateView.as_view(), name='empleados_create'),
    path('empleados/<int:pk>/edit/', views.EmpleadosUpdateView.as_view(), name='empleados_edit'),
    path('empleados/<int:pk>/delete/', views.EmpleadosDeleteView.as_view(), name='empleados_delete'),
    path('tipo_unidades/', views.TipoUnidadesListView.as_view(), name='tipo_unidades_list'),
    path('tipo_unidades/<int:pk>/', views.TipoUnidadesDetailView.as_view(), name='tipo_unidades_detail'),
    path('tipo_unidades/create/', views.TipoUnidadesCreateView.as_view(), name='tipo_unidades_create'),
    path('tipo_unidades/<int:pk>/edit/', views.TipoUnidadesUpdateView.as_view(), name='tipo_unidades_edit'),
    path('tipo_unidades/<int:pk>/delete/', views.TipoUnidadesDeleteView.as_view(), name='tipo_unidades_delete'),
    path('unidades/', views.UnidadesListView.as_view(), name='unidades_list'),
    path('unidades/<int:pk>/', views.UnidadesDetailView.as_view(), name='unidades_detail'),
    path('unidades/create/', views.UnidadesCreateView.as_view(), name='unidades_create'),
    path('unidades/<int:pk>/edit/', views.UnidadesUpdateView.as_view(), name='unidades_edit'),
    path('unidades/<int:pk>/delete/', views.UnidadesDeleteView.as_view(), name='unidades_delete'),
    path('existencias_articulos/', views.ExistenciasArticulosListView.as_view(), name='existencias_articulos_list'),
    path('existencias_articulos/<int:pk>/', views.ExistenciasArticulosDetailView.as_view(), name='existencias_articulos_detail'),
    path('existencias_articulos/create/', views.ExistenciasArticulosCreateView.as_view(), name='existencias_articulos_create'),
    path('existencias_articulos/<int:pk>/edit/', views.ExistenciasArticulosUpdateView.as_view(), name='existencias_articulos_edit'),
    path('existencias_articulos/<int:pk>/delete/', views.ExistenciasArticulosDeleteView.as_view(), name='existencias_articulos_delete'),
    path('almacen/', views.AlmacenListView.as_view(), name='almacen_list'),
    path('almacen/<int:pk>/', views.AlmacenDetailView.as_view(), name='almacen_detail'),
    path('almacen/create/', views.AlmacenCreateView.as_view(), name='almacen_create'),
    path('almacen/<int:pk>/edit/', views.AlmacenUpdateView.as_view(), name='almacen_edit'),
    path('almacen/<int:pk>/delete/', views.AlmacenDeleteView.as_view(), name='almacen_delete'),
    path('taller/', views.TallerListView.as_view(), name='taller_list'),
    path('taller/<int:pk>/', views.TallerDetailView.as_view(), name='taller_detail'),
    path('taller/create/', views.TallerCreateView.as_view(), name='taller_create'),
    path('taller/<int:pk>/edit/', views.TallerUpdateView.as_view(), name='taller_edit'),
    path('taller/<int:pk>/delete/', views.TallerDeleteView.as_view(), name='taller_delete'),
    path('vaia/', views.VaiaListView.as_view(), name='vaia_list'),
    path('vaia/<int:pk>/', views.VaiaDetailView.as_view(), name='vaia_detail'),
    path('vaia/create/', views.VaiaCreateView.as_view(), name='vaia_create'),
    path('vaia/<int:pk>/edit/', views.VaiaUpdateView.as_view(), name='vaia_edit'),
    path('vaia/<int:pk>/delete/', views.VaiaDeleteView.as_view(), name='vaia_delete'),
    path('empleados_unidad/', views.EmpleadosUnidadListView.as_view(), name='empleados_unidad_list'),
    path('empleados_unidad/<int:pk>/', views.EmpleadosUnidadDetailView.as_view(), name='empleados_unidad_detail'),
    path('empleados_unidad/create/', views.EmpleadosUnidadCreateView.as_view(), name='empleados_unidad_create'),
    path('empleados_unidad/<int:pk>/edit/', views.EmpleadosUnidadUpdateView.as_view(), name='empleados_unidad_edit'),
    path('empleados_unidad/<int:pk>/delete/', views.EmpleadosUnidadDeleteView.as_view(), name='empleados_unidad_delete'),
    path('areastaller/', views.AreastallerListView.as_view(), name='areastaller_list'),
    path('areastaller/<int:pk>/', views.AreastallerDetailView.as_view(), name='areastaller_detail'),
    path('areastaller/create/', views.AreastallerCreateView.as_view(), name='areastaller_create'),
    path('areastaller/<int:pk>/edit/', views.AreastallerUpdateView.as_view(), name='areastaller_edit'),
    path('areastaller/<int:pk>/delete/', views.AreastallerDeleteView.as_view(), name='areastaller_delete'),
    path('tipomantenimientos/', views.TipomantenimientosListView.as_view(), name='tipomantenimientos_list'),
    path('tipomantenimientos/<int:pk>/', views.TipomantenimientosDetailView.as_view(), name='tipomantenimientos_detail'),
    path('tipomantenimientos/create/', views.TipomantenimientosCreateView.as_view(), name='tipomantenimientos_create'),
    path('tipomantenimientos/<int:pk>/edit/', views.TipomantenimientosUpdateView.as_view(), name='tipomantenimientos_edit'),
    path('tipomantenimientos/<int:pk>/delete/', views.TipomantenimientosDeleteView.as_view(), name='tipomantenimientos_delete'),
    path('mantenimientos/', views.MantenimientosListView.as_view(), name='mantenimientos_list'),
    path('mantenimientos/<int:pk>/', views.MantenimientosDetailView.as_view(), name='mantenimientos_detail'),
    path('mantenimientos/create/', views.MantenimientosCreateView.as_view(), name='mantenimientos_create'),
    path('mantenimientos/<int:pk>/edit/', views.MantenimientosUpdateView.as_view(), name='mantenimientos_edit'),
    path('mantenimientos/<int:pk>/delete/', views.MantenimientosDeleteView.as_view(), name='mantenimientos_delete'),
    path('estatus_mantenimiento/', views.EstatusMantenimientoListView.as_view(), name='estatus_mantenimiento_list'),
    path('estatus_mantenimiento/<int:pk>/', views.EstatusMantenimientoDetailView.as_view(), name='estatus_mantenimiento_detail'),
    path('estatus_mantenimiento/create/', views.EstatusMantenimientoCreateView.as_view(), name='estatus_mantenimiento_create'),
    path('estatus_mantenimiento/<int:pk>/edit/', views.EstatusMantenimientoUpdateView.as_view(), name='estatus_mantenimiento_edit'),
    path('estatus_mantenimiento/<int:pk>/delete/', views.EstatusMantenimientoDeleteView.as_view(), name='estatus_mantenimiento_delete'),
    path('detalle_mtto_actividades/', views.DetalleMttoActividadesListView.as_view(), name='detalle_mtto_actividades_list'),
    path('detalle_mtto_actividades/<int:pk>/', views.DetalleMttoActividadesDetailView.as_view(), name='detalle_mtto_actividades_detail'),
    path('detalle_mtto_actividades/create/', views.DetalleMttoActividadesCreateView.as_view(), name='detalle_mtto_actividades_create'),
    path('detalle_mtto_actividades/<int:pk>/edit/', views.DetalleMttoActividadesUpdateView.as_view(), name='detalle_mtto_actividades_edit'),
    path('detalle_mtto_actividades/<int:pk>/delete/', views.DetalleMttoActividadesDeleteView.as_view(), name='detalle_mtto_actividades_delete'),
    path('mecanicos_taller/', views.MecanicosTallerListView.as_view(), name='mecanicos_taller_list'),
    path('mecanicos_taller/<int:pk>/', views.MecanicosTallerDetailView.as_view(), name='mecanicos_taller_detail'),
    path('mecanicos_taller/create/', views.MecanicosTallerCreateView.as_view(), name='mecanicos_taller_create'),
    path('mecanicos_taller/<int:pk>/edit/', views.MecanicosTallerUpdateView.as_view(), name='mecanicos_taller_edit'),
    path('mecanicos_taller/<int:pk>/delete/', views.MecanicosTallerDeleteView.as_view(), name='mecanicos_taller_delete'),
    path('piezas_actividades/', views.PiezasActividadesListView.as_view(), name='piezas_actividades_list'),
    path('piezas_actividades/<int:pk>/', views.PiezasActividadesDetailView.as_view(), name='piezas_actividades_detail'),
    path('piezas_actividades/create/', views.PiezasActividadesCreateView.as_view(), name='piezas_actividades_create'),
    path('piezas_actividades/<int:pk>/edit/', views.PiezasActividadesUpdateView.as_view(), name='piezas_actividades_edit'),
    path('piezas_actividades/<int:pk>/delete/', views.PiezasActividadesDeleteView.as_view(), name='piezas_actividades_delete'),
    path('garantias/', views.GarantiasListView.as_view(), name='garantias_list'),
    path('garantias/<int:pk>/', views.GarantiasDetailView.as_view(), name='garantias_detail'),
    path('garantias/create/', views.GarantiasCreateView.as_view(), name='garantias_create'),
    path('garantias/<int:pk>/edit/', views.GarantiasUpdateView.as_view(), name='garantias_edit'),
    path('garantias/<int:pk>/delete/', views.GarantiasDeleteView.as_view(), name='garantias_delete'),
    path('proveedores/', views.ProveedoresListView.as_view(), name='proveedores_list'),
    path('proveedores/<int:pk>/', views.ProveedoresDetailView.as_view(), name='proveedores_detail'),
    path('proveedores/create/', views.ProveedoresCreateView.as_view(), name='proveedores_create'),
    path('proveedores/<int:pk>/edit/', views.ProveedoresUpdateView.as_view(), name='proveedores_edit'),
    path('proveedores/<int:pk>/delete/', views.ProveedoresDeleteView.as_view(), name='proveedores_delete'),
    path('garatiaseguimiento/', views.GaratiaseguimientoListView.as_view(), name='garatiaseguimiento_list'),
    path('garatiaseguimiento/<int:pk>/', views.GaratiaseguimientoDetailView.as_view(), name='garatiaseguimiento_detail'),
    path('garatiaseguimiento/create/', views.GaratiaseguimientoCreateView.as_view(), name='garatiaseguimiento_create'),
    path('garatiaseguimiento/<int:pk>/edit/', views.GaratiaseguimientoUpdateView.as_view(), name='garatiaseguimiento_edit'),
    path('garatiaseguimiento/<int:pk>/delete/', views.GaratiaseguimientoDeleteView.as_view(), name='garatiaseguimiento_delete'),
    path('articulos_servicios/', views.ArticulosServiciosListView.as_view(), name='articulos_servicios_list'),
    path('articulos_servicios/<int:pk>/', views.ArticulosServiciosDetailView.as_view(), name='articulos_servicios_detail'),
    path('articulos_servicios/create/', views.ArticulosServiciosCreateView.as_view(), name='articulos_servicios_create'),
    path('articulos_servicios/<int:pk>/edit/', views.ArticulosServiciosUpdateView.as_view(), name='articulos_servicios_edit'),
    path('articulos_servicios/<int:pk>/delete/', views.ArticulosServiciosDeleteView.as_view(), name='articulos_servicios_delete'),
    path('servicios_taller/', views.ServiciosTallerListView.as_view(), name='servicios_taller_list'),
    path('servicios_taller/<int:pk>/', views.ServiciosTallerDetailView.as_view(), name='servicios_taller_detail'),
    path('servicios_taller/create/', views.ServiciosTallerCreateView.as_view(), name='servicios_taller_create'),
    path('servicios_taller/<int:pk>/edit/', views.ServiciosTallerUpdateView.as_view(), name='servicios_taller_edit'),
    path('servicios_taller/<int:pk>/delete/', views.ServiciosTallerDeleteView.as_view(), name='servicios_taller_delete'),
    path('django_migrations/', views.DjangoMigrationsListView.as_view(), name='django_migrations_list'),
    path('django_migrations/<int:pk>/', views.DjangoMigrationsDetailView.as_view(), name='django_migrations_detail'),
    path('django_migrations/create/', views.DjangoMigrationsCreateView.as_view(), name='django_migrations_create'),
    path('django_migrations/<int:pk>/edit/', views.DjangoMigrationsUpdateView.as_view(), name='django_migrations_edit'),
    path('django_migrations/<int:pk>/delete/', views.DjangoMigrationsDeleteView.as_view(), name='django_migrations_delete'),
    path('django_content_type/', views.DjangoContentTypeListView.as_view(), name='django_content_type_list'),
    path('django_content_type/<int:pk>/', views.DjangoContentTypeDetailView.as_view(), name='django_content_type_detail'),
    path('django_content_type/create/', views.DjangoContentTypeCreateView.as_view(), name='django_content_type_create'),
    path('django_content_type/<int:pk>/edit/', views.DjangoContentTypeUpdateView.as_view(), name='django_content_type_edit'),
    path('django_content_type/<int:pk>/delete/', views.DjangoContentTypeDeleteView.as_view(), name='django_content_type_delete'),
    path('auth_permission/', views.AuthPermissionListView.as_view(), name='auth_permission_list'),
    path('auth_permission/<int:pk>/', views.AuthPermissionDetailView.as_view(), name='auth_permission_detail'),
    path('auth_permission/create/', views.AuthPermissionCreateView.as_view(), name='auth_permission_create'),
    path('auth_permission/<int:pk>/edit/', views.AuthPermissionUpdateView.as_view(), name='auth_permission_edit'),
    path('auth_permission/<int:pk>/delete/', views.AuthPermissionDeleteView.as_view(), name='auth_permission_delete'),
    path('auth_group/', views.AuthGroupListView.as_view(), name='auth_group_list'),
    path('auth_group/<int:pk>/', views.AuthGroupDetailView.as_view(), name='auth_group_detail'),
    path('auth_group/create/', views.AuthGroupCreateView.as_view(), name='auth_group_create'),
    path('auth_group/<int:pk>/edit/', views.AuthGroupUpdateView.as_view(), name='auth_group_edit'),
    path('auth_group/<int:pk>/delete/', views.AuthGroupDeleteView.as_view(), name='auth_group_delete'),
    path('auth_group_permissions/', views.AuthGroupPermissionsListView.as_view(), name='auth_group_permissions_list'),
    path('auth_group_permissions/<int:pk>/', views.AuthGroupPermissionsDetailView.as_view(), name='auth_group_permissions_detail'),
    path('auth_group_permissions/create/', views.AuthGroupPermissionsCreateView.as_view(), name='auth_group_permissions_create'),
    path('auth_group_permissions/<int:pk>/edit/', views.AuthGroupPermissionsUpdateView.as_view(), name='auth_group_permissions_edit'),
    path('auth_group_permissions/<int:pk>/delete/', views.AuthGroupPermissionsDeleteView.as_view(), name='auth_group_permissions_delete'),
    path('auth_user_groups/', views.AuthUserGroupsListView.as_view(), name='auth_user_groups_list'),
    path('auth_user_groups/<int:pk>/', views.AuthUserGroupsDetailView.as_view(), name='auth_user_groups_detail'),
    path('auth_user_groups/create/', views.AuthUserGroupsCreateView.as_view(), name='auth_user_groups_create'),
    path('auth_user_groups/<int:pk>/edit/', views.AuthUserGroupsUpdateView.as_view(), name='auth_user_groups_edit'),
    path('auth_user_groups/<int:pk>/delete/', views.AuthUserGroupsDeleteView.as_view(), name='auth_user_groups_delete'),
    path('auth_user/', views.AuthUserListView.as_view(), name='auth_user_list'),
    path('auth_user/<int:pk>/', views.AuthUserDetailView.as_view(), name='auth_user_detail'),
    path('auth_user/create/', views.AuthUserCreateView.as_view(), name='auth_user_create'),
    path('auth_user/<int:pk>/edit/', views.AuthUserUpdateView.as_view(), name='auth_user_edit'),
    path('auth_user/<int:pk>/delete/', views.AuthUserDeleteView.as_view(), name='auth_user_delete'),
    path('auth_user_user_permissions/', views.AuthUserUserPermissionsListView.as_view(), name='auth_user_user_permissions_list'),
    path('auth_user_user_permissions/<int:pk>/', views.AuthUserUserPermissionsDetailView.as_view(), name='auth_user_user_permissions_detail'),
    path('auth_user_user_permissions/create/', views.AuthUserUserPermissionsCreateView.as_view(), name='auth_user_user_permissions_create'),
    path('auth_user_user_permissions/<int:pk>/edit/', views.AuthUserUserPermissionsUpdateView.as_view(), name='auth_user_user_permissions_edit'),
    path('auth_user_user_permissions/<int:pk>/delete/', views.AuthUserUserPermissionsDeleteView.as_view(), name='auth_user_user_permissions_delete'),
    path('django_admin_log/', views.DjangoAdminLogListView.as_view(), name='django_admin_log_list'),
    path('django_admin_log/<int:pk>/', views.DjangoAdminLogDetailView.as_view(), name='django_admin_log_detail'),
    path('django_admin_log/create/', views.DjangoAdminLogCreateView.as_view(), name='django_admin_log_create'),
    path('django_admin_log/<int:pk>/edit/', views.DjangoAdminLogUpdateView.as_view(), name='django_admin_log_edit'),
    path('django_admin_log/<int:pk>/delete/', views.DjangoAdminLogDeleteView.as_view(), name='django_admin_log_delete'),
    path('django_session/', views.DjangoSessionListView.as_view(), name='django_session_list'),
    path('django_session/<int:pk>/', views.DjangoSessionDetailView.as_view(), name='django_session_detail'),
    path('django_session/create/', views.DjangoSessionCreateView.as_view(), name='django_session_create'),
    path('django_session/<int:pk>/edit/', views.DjangoSessionUpdateView.as_view(), name='django_session_edit'),
    path('django_session/<int:pk>/delete/', views.DjangoSessionDeleteView.as_view(), name='django_session_delete'),
    path('web_project/', views.WebProjectListView.as_view(), name='web_project_list'),
    path('web_project/<int:pk>/', views.WebProjectDetailView.as_view(), name='web_project_detail'),
    path('web_project/create/', views.WebProjectCreateView.as_view(), name='web_project_create'),
    path('web_project/<int:pk>/edit/', views.WebProjectUpdateView.as_view(), name='web_project_edit'),
    path('web_project/<int:pk>/delete/', views.WebProjectDeleteView.as_view(), name='web_project_delete'),
    path('web_task/', views.WebTaskListView.as_view(), name='web_task_list'),
    path('web_task/<int:pk>/', views.WebTaskDetailView.as_view(), name='web_task_detail'),
    path('web_task/create/', views.WebTaskCreateView.as_view(), name='web_task_create'),
    path('web_task/<int:pk>/edit/', views.WebTaskUpdateView.as_view(), name='web_task_edit'),
    path('web_task/<int:pk>/delete/', views.WebTaskDeleteView.as_view(), name='web_task_delete'),
    path('web_taller/', views.WebTallerListView.as_view(), name='web_taller_list'),
    path('web_taller/<int:pk>/', views.WebTallerDetailView.as_view(), name='web_taller_detail'),
    path('web_taller/create/', views.WebTallerCreateView.as_view(), name='web_taller_create'),
    path('web_taller/<int:pk>/edit/', views.WebTallerUpdateView.as_view(), name='web_taller_edit'),
    path('web_taller/<int:pk>/delete/', views.WebTallerDeleteView.as_view(), name='web_taller_delete'),
]
