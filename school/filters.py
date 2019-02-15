from .models import Students
import django_filters

class StudentsFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Students
        fields = ['id', 'first_name']