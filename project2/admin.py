from django.contrib import admin
from .models import ProjectDetail, ProjectReview, ProjectShop, ProjectCertificate


# Register your models here.
class ProjectReviewInline(admin.TabularInline):
    model = ProjectReview
    extra = 2


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "cost", "start_date", "end_date")
    search_fields = ("title", "description")
    list_filter = ("type", "start_date")
    inlines = [ProjectReviewInline]


class ProjectShopAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    search_fields = ("name", "description", "address")
    # filter_horizontal = ("ProjectDetail",)


class ProjectCertificateAdmin(admin.ModelAdmin):
    list_display = ("project", "certificate_number", "issued_date", "valid_until")
    search_fields = ("certificate_number", "project__title")


admin.site.register(ProjectDetail, ProjectAdmin)
admin.site.register(ProjectShop, ProjectShopAdmin)
admin.site.register(ProjectCertificate, ProjectCertificateAdmin)
