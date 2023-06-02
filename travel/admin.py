from django.contrib import admin
from django.core.exceptions import ValidationError


from django import forms
from django.db import models
from markdownx.widgets import MarkdownxWidget
from django_json_widget.widgets import JSONEditorWidget
from wangeditor.widgets import WangEditorWidget

from django_backend import settings
from .models import Travel, City, Person, Order
# Register your models here.


class WangEditorAdminForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = '__all__'
        widgets = {
            'description': WangEditorWidget
        }

    def clean_description(self):
        print("============ clean_description")
        description = self.cleaned_data.get('description')
        raw_images = []
        for tag in description.split():
            if tag.startswith('<img') and 'src=' in tag:
                raw_images.append(tag)
        for raw_image in raw_images:
            image_url = raw_image.split('src=')[1].split('"')[1]
            upload_max_size = getattr(settings, 'WANGEDITOR_CONFIGS', {}).get('default', {}).get('upload_max_size', 5*1024*1024)
            request = None # you may need to modify this to get the user's request object
            if request and int(request.META.get('CONTENT_LENGTH', 0)) > upload_max_size:
                raise ValidationError(f"上传的图片不能大于 {upload_max_size / (1024 * 1024)}MB！")
        return description


class TravelAdmin(admin.ModelAdmin):
    form = WangEditorAdminForm
    list_display = [field.name for field in Travel._meta.fields]

    # def formfield_for_dbfield(self, db_field, **kwargs):
    #     print("db_field:", db_field, kwargs.get('instance'))
    #     if db_field.name == 'options':
    #         kwargs['widget'] = JSONEditorWidget
    #     elif db_field.name == 'question':
    #         kwargs['widget'] = MarkdownxWidget
    #     # elif db_field.name == 'answer':
    #     #     # if kwargs.get('instance') and kwargs['instance'].type == 'multi_choice':
    #     #     kwargs['widget'] = JSONEditorWidget
    #     return super().formfield_for_dbfield(db_field, **kwargs)


admin.site.register(Travel, TravelAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = [field.name for field in City._meta.fields]

admin.site.register(City, CityAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Person._meta.fields]

admin.site.register(Person, PersonAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]

admin.site.register(Order, OrderAdmin)