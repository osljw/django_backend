from django.db import models


class Collection(models.Model):
    CATEGORY_CHOICES = [('A', '一级文物'), ('B', '二级文物'), ('C', '三级文物')]
    CONDITION_CHOICES = [('good', '完好'), ('damaged', '残损'), ('repairing', '修复中')]
    
    registration_number = models.CharField("总登记号", max_length=50, unique=True)
    original_number = models.CharField("原编号", max_length=50, blank=True)
    name = models.CharField("原名", max_length=200)
    era = models.CharField("年代", max_length=50)
    category = models.CharField("文物类别", max_length=100)
    material_type1 = models.CharField("质地类别1", max_length=50)
    material_type2 = models.CharField("质地类别2", max_length=50, blank=True)
    material = models.TextField("质地描述")
    quantity = models.IntegerField("数量")
    actual_quantity = models.IntegerField("实际数量")
    length = models.FloatField("通长(cm)", null=True, blank=True)
    width = models.FloatField("通宽(cm)", null=True, blank=True)
    height = models.FloatField("通高(cm)", null=True, blank=True)
    dimensions = models.TextField("具体尺寸", blank=True)
    weight_range = models.CharField("质量范围", max_length=50, blank=True)
    actual_weight = models.FloatField("具体质量(kg)", null=True, blank=True)
    grade = models.CharField("文物级别", max_length=1, choices=CATEGORY_CHOICES)
    provenance = models.TextField("来源")
    integrity = models.CharField("完残程度", max_length=20, choices=CONDITION_CHOICES)
    condition_detail = models.TextField("完残状况")
    storage_status = models.TextField("保存状态")
    acquisition_year = models.IntegerField("入藏年度")
    history = models.TextField("流传经历")
    
    class Meta:
        verbose_name = "藏品"
        # ordering = ['registration_number']