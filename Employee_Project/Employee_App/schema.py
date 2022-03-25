import graphene
from graphene_django import DjangoObjectType
from .models import Employee

class EmployeeType(DjangoObjectType):
    class Meta: 
        model = Employee
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'date_joined',
        )

class Query(graphene.ObjectType):
    employees = graphene.List(EmployeeType)

    def resolve_employees(root, info, **kwargs):
        return Employee.objects.all()

schema = graphene.Schema(query=Query)