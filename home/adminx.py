import xadmin
from xadmin import views
from .models import Banner, NarBar

class BaseSetting(object):
    enable_thems = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSetting(object):
    site_title = "站点名称"
    site_footer = "站点脚注"

xadmin.site.register(views.CommAdminView, GlobalSetting)

class BannerAdmin:
    list_display = ["title", "orders", "is_show"]

xadmin.site.register(Banner, BannerAdmin)

class NarBarAdmin:
    list_display = ["title", "link_url", "orders", "is_show", "position"]
xadmin.site.register(NarBar, NarBarAdmin)