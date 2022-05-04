import datetime
import graphene
from graphene_django import DjangoObjectType
from .models import Employee, CustomUser
from .get_logger import get_logger
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations
from graphql_jwt.decorators import login_required
from graphql_jwt.shortcuts import get_token, create_refresh_token
from django.contrib.auth.hashers import make_password

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

class UserType(DjangoObjectType):
    """
    Django Object Type for Custom User
    """
    class Meta:
        model = CustomUser
        fields = ("email", "username", "display_name", "password",)
        description = 'Model having fields of User type'

class EmployeeQuery(UserQuery, MeQuery, graphene.ObjectType):
    all_employees = graphene.List(EmployeeType)

    # @login_required
    def resolve_all_employees(root, info):
        return Employee.objects.all()

class SingleEmployeeQuery(graphene.ObjectType):
    employees = graphene.List(EmployeeType, empID=graphene.Int())

    def resolve_employees(root, info, empID):
        return Employee.objects.filter(empID=empID)

class Query(EmployeeQuery, SingleEmployeeQuery, graphene.ObjectType):
    pass

class CreateEmployee(graphene.Mutation):

    logger = get_logger()

    class Arguments:
        empName = graphene.String(required=True)
        empDOJ = graphene.Date()
        empDescription = graphene.String()
        empCategory = graphene.String()
        empCity = graphene.String(required=True)
        empOfficeVenue = graphene.String(required=True)

    employee = graphene.Field(EmployeeType)

    @classmethod
    # @login_required
    def mutate(cls, root, info, empName = None, empDOJ = datetime.date.today(), empDescription = None, empCategory = None, empCity = None, empOfficeVenue = None):
        employee = Employee()

        try:
            cls.logger.info("started creating employee")
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

class UpdateEmployee(graphene.Mutation):

    logger = get_logger()

    class Arguments:
        empID = graphene.Int(required=True)
        empName = graphene.String()
        empDOJ = graphene.Date()
        empDescription = graphene.String()
        empCategory = graphene.String()
        empCity = graphene.String()
        empOfficeVenue = graphene.String()

    employee = graphene.Field(EmployeeType)

    @classmethod
    # @login_required
    def mutate(cls, root, info, empID, empName=None, empDOJ=None, empDescription=None, empCategory=None, empCity=None, empOfficeVenue=None):

        try:
            employee = Employee.objects.get(empID=empID)
        except:
            cls.logger.warn("employee does not exist")
            raise Exception("employee does not exist")
        
        try:
            if employee != None:
                cls.logger.info("started updating employee")
                if empName != None:
                    employee.empName = empName
                    cls.logger.info("updated empName successfully")
                if empDOJ != None:
                    employee.empDOJ = empDOJ
                    cls.logger.info("updated empDOJ successfully")
                if empDescription != None:
                    employee.empDescription = empDescription
                    cls.logger.info("updated empDescription successfully")
                if empCategory != None:
                    employee.empCategory = empCategory
                    cls.logger.info("updated empCategory successfully")
                if empCity != None:
                    employee.empCity = empCity
                    cls.logger.info("updated empCity successfully")
                if empOfficeVenue != None:
                    employee.empOfficeVenue = empOfficeVenue
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
    # @login_required
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

class Register(graphene.Mutation):
    """
        Mutation for registering user

        -- Params :   Graphene.mutation
    """
    user = graphene.Field(UserType)
    success = graphene.Boolean()
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        username = graphene.String(required=True)
        display_name = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, email, password, username, display_name):
        """
            Mutating for creating user

            Params: email, password, username, display_name
                    ** Username should be unique

            Return : newly registered user object
        """
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist as e:
            user = None

        if user:
            raise Exception('User Already Exists!')
        else:
            try:
                user_obj = CustomUser(email=email, password=make_password(password), username=username,
                                  display_name=display_name)
                user_obj.save()
                token = get_token(user_obj)
                refresh_token = create_refresh_token(user_obj)

                return Register(user=user_obj,
                                token=token,
                                refresh_token=refresh_token,
                                success=True)
            except Exception as e:
                cls.logger.error(str(e))
                raise Exception("Problem in User Creation.") 

class AuthMutation(graphene.ObjectType):
   register = Register.Field()
   verify_account = mutations.VerifyAccount.Field()
   token_auth = mutations.ObtainJSONWebToken.Field()
   update_account = mutations.UpdateAccount.Field()
   resend_activation_email = mutations.ResendActivationEmail.Field()
   send_password_reset_email = mutations.SendPasswordResetEmail.Field()
   password_reset = mutations.PasswordReset.Field()
   password_change = mutations.PasswordChange.Field()

class Mutation(AuthMutation, graphene.ObjectType):
    create_employee = CreateEmployee.Field()
    update_employee = UpdateEmployee.Field()
    delete_employee = DeleteEmployee.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)