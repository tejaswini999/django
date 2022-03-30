from datetime import date
import graphene
from graphene_django import DjangoObjectType
from .models import Employee
from .get_logger import get_logger

class EmployeeType(DjangoObjectType):
    class Meta: 
        model = Employee
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'job_role',
            'is_staff',
            'date_joined',
        )

class Query(graphene.ObjectType):
    employees = graphene.List(EmployeeType)

    def resolve_employees(root, info, **kwargs):
        return Employee.objects.all()

class CreateEmployee(graphene.Mutation):

    logger = get_logger()

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        job_role = graphene.String()
        is_staff = graphene.Boolean()
        date_joined = graphene.Date()

    employee = graphene.Field(EmployeeType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, email, job_role = None, is_staff = False, date_joined = date.today()):
        employee = Employee()

        try:
            cls.logger.info("started creating employee")
            if first_name != None:
                employee.first_name = first_name
            if last_name != None:
                employee.last_name = last_name
            if email != None:
                employee.email = email
            if job_role != None:
                employee.job_role = job_role
            if is_staff != None:
                employee.is_staff = is_staff
            if date_joined != None:
                employee.date_joined = date_joined
                
            employee.save()
            cls.logger.info("created employee successfully")
            return CreateEmployee(employee=employee)

        except:
            cls.logger.error("problem in creating employee")
            raise Exception("problem in creating employee")

class EmployeeInput(graphene.InputObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()
    job_role = graphene.String()
    is_staff = graphene.Boolean()
    date_joined = graphene.Date()

class UpdateEmployee(graphene.Mutation):

    logger = get_logger()

    class Arguments:
        id = graphene.ID(required=True)
        input = EmployeeInput(required=True)

    employee = graphene.Field(EmployeeType)

    @classmethod
    def mutate(cls, root, info, id, input):

        try:
            employee = Employee.objects.get(id=id)
        except:
            cls.logger.warn("employee does not exist")
            raise Exception("employee does not exist")
        
        try:
            if employee != None:
                cls.logger.info("started updating employee")
                if input.first_name != None:
                    employee.first_name = input.first_name
                if input.last_name != None:
                    employee.last_name = input.last_name
                if input.email != None:
                    employee.email = input.email
                if input.job_role != None:
                    employee.job_role = input.job_role
                if input.is_staff != None:
                    employee.is_staff = input.is_staff
                if input.date_joined != None:
                    employee.date_joined = input.date_joined

                employee.save()
                cls.logger.info("updated employee successfully")
                return UpdateEmployee(employee=employee)

        except:
            cls.logger.error("problem in updating employee")
            raise Exception("problem in updating employee")

class DeleteEmployee(graphene.Mutation):

    logger = get_logger()

    class Arguments:
        id = graphene.ID(required=True)

    employee = graphene.Field(EmployeeType)

    @classmethod
    def mutate(cls, root, info, id):

        try:
            employee = Employee.objects.get(id=id)
        except:
            cls.logger.warn("employee does not exist")
            raise Exception("employee does not exist")

        try:
            cls.logger.info("started deleting employee")
            employee.delete()
            cls.logger.info("deleted employee successfully")
            return
        except:
            cls.logger.info("problem in deleting employee")
            raise Exception("problem in deleting employee")    

class Mutation(graphene.ObjectType):
    create_employee = CreateEmployee.Field()
    update_employee = UpdateEmployee.Field()
    delete_employee = DeleteEmployee.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)