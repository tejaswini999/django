from datetime import date
import graphene
from graphene_django import DjangoObjectType
from .models import Employee
from .get_logger import get_logger
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations

class EmployeeType(DjangoObjectType):
    class Meta: 
        model = Employee
        fields = (
            'empID',
            'empName',
            'empDOJ',
            'empDescription',
            'empCategory',
            'empCity',
            'empOfficeVenue',
        )

class Query(graphene.ObjectType):
    employees = graphene.List(EmployeeType)

    def resolve_employees(root, info, **kwargs):
        return Employee.objects.all()

class CreateEmployee(graphene.Mutation):

    logger = get_logger()

    class Arguments:
        empID = graphene.Int(required=True)
        empName = graphene.String(required=True)
        empDOJ = graphene.Date()
        empDescription = graphene.String(required=True)
        empCategory = graphene.String()
        empCity = graphene.String(required=True)
        empOfficeVenue = graphene.String()

    employee = graphene.Field(EmployeeType)

    @classmethod
    def mutate(cls, root, info, empID = None, empName = None, empDOJ = date.today(), empDescription = None, empCategory = None, empCity = None, empOfficeVenue = None):
        employee = Employee()

        try:
            cls.logger.info("started creating employee")
            if empID != None:
                employee.empID = empID
            if empName != None:
                employee.empName = empName
            if empDOJ != None:
                employee.empDOJ = empDOJ
            if empDescription != None:
                employee.empDescription = empDescription
            if empCategory != None:
                employee.empCategory = empCategory
            if empCity != None:
                employee.empCity = empCity
            if empOfficeVenue != None:
                employee.empOfficeVenue = empOfficeVenue
                
            employee.save()
            cls.logger.info("created employee successfully")
            return CreateEmployee(employee=employee)

        except:
            cls.logger.error("problem in creating employee")
            raise Exception("problem in creating employee")

class EmployeeInput(graphene.InputObjectType):
    empName = graphene.String()
    empDOJ = graphene.Date()
    empDescription = graphene.String()
    empCategory = graphene.String()
    empCity = graphene.String()
    empOfficeVenue = graphene.String()

class UpdateEmployee(graphene.Mutation):

    logger = get_logger()

    class Arguments:
        empID = graphene.Int(required=True)
        input = EmployeeInput(required=True)

    employee = graphene.Field(EmployeeType)

    @classmethod
    def mutate(cls, root, info, empID, input):

        try:
            employee = Employee.objects.get(empID=empID)
        except:
            cls.logger.warn("employee does not exist")
            raise Exception("employee does not exist")
        
        try:
            if employee != None:
                cls.logger.info("started updating employee")
                if input.empName != None:
                    employee.empName = input.empName
                    cls.logger.info("updated empName successfully")
                if input.empDOJ != None:
                    employee.empDOJ = input.empDOJ
                    cls.logger.info("updated empDOJ successfully")
                if input.empDescription != None:
                    employee.empDescription = input.empDescription
                    cls.logger.info("updated empDescription successfully")
                if input.empCategory != None:
                    employee.empCategory = input.empCategory
                    cls.logger.info("updated empCategory successfully")
                if input.empCity != None:
                    employee.empCity = input.empCity
                    cls.logger.info("updated empCity successfully")
                if input.empOfficeVenue != None:
                    employee.empOfficeVenue = input.empOfficeVenue
                    cls.logger.info("updated empOfficeVenue successfully")

                employee.save()
                cls.logger.info("updated employee successfully")
                return UpdateEmployee(employee=employee)

        except:
            cls.logger.error("problem in updating employee")
            raise Exception("problem in updating employee")

class DeleteEmployee(graphene.Mutation):

    logger = get_logger()

    class Arguments:
        empID = graphene.Int(required=True)

    employee = graphene.Field(EmployeeType)

    @classmethod
    def mutate(cls, root, info, empID):

        try:
            employee = Employee.objects.get(empID=empID)
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

class AuthMutation(graphene.ObjectType):
   register = mutations.Register.Field()
   verify_account = mutations.VerifyAccount.Field()
   token_auth = mutations.ObtainJSONWebToken.Field()
   update_account = mutations.UpdateAccount.Field()
   resend_activation_email = mutations.ResendActivationEmail.Field()
   send_password_reset_email = mutations.SendPasswordResetEmail.Field()
   password_reset = mutations.PasswordReset.Field()
   password_change = mutations.PasswordChange.Field()

class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass

class Mutation(AuthMutation, graphene.ObjectType):
    create_employee = CreateEmployee.Field()
    update_employee = UpdateEmployee.Field()
    delete_employee = DeleteEmployee.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)