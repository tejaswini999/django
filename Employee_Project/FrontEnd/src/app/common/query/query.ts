export const get_all_Employees = `query{
    allEmployees{
        empID
        empName
        empOfficeVenue
        empDOJ
        empCity 
        empDescription 
        empCategory 
        }
    }`
    
export const get_employee =  `query($empID:Int){
    employees(empID:$empID){
    empID
    empName
    empCity
    empOfficeVenue
    empDOJ
    empDescription
    empCategory
    }
    }`

export const create_employee=` mutation firstmutation($empName:String!, $empCity:String!,  $empOfficeVenue:String!,
    $empDOJ:Date, $empDescription:String!,$empCategory:String!)
    {
     createEmployee(empName: $empName,empCity: $empCity, empOfficeVenue: $empOfficeVenue,
  empDOJ:$empDOJ, empDescription:$empDescription, 
  empCategory:$empCategory)
   {
  employee {
    empName: empName
    empCity: empCity
    empOfficeVenue: empOfficeVenue
    empDOJ: empDOJ
    empDescription:empDescription
    empCategory:empCategory
    empID
  }
}
}`
export const update_employee=`mutation firstupdatemutation($empID:Int!,$empName:String!,$empCity:String!,
    $empOfficeVenue:String!,$empDOJ:Date, $empDescription:String!,$empCategory:String!){
    updateEmployee(empID:$empID, empName: $empName,empCity: $empCity, empOfficeVenue: $empOfficeVenue,
        empDOJ:$empDOJ, empDescription:$empDescription, 
        empCategory:$empCategory){
            employee {
                empName: empName
                empID: empID
                empCity: empCity
                empOfficeVenue: empOfficeVenue
                empDOJ: empDOJ
                empDescription:empDescription
                empCategory:empCategory
              }
    }
  }`

export const delete_employee= `mutation firstdeletemutation($empID:Int!)
  {
      deleteEmployee(empID:$empID){
        employee{
          empID
          }
      }
    }`

export const login_User =  `
    mutation($username:String, $password:String!){
        tokenAuth(username:$username, password:$password){
          success,
          token,
          errors,
          refreshToken,
          user{
            username, email , displayName
          }
        }
      }`

export const current_user=`
      query{
          me{
            username,
            email,
            displayName
          }
        }`

export const register_user= `
        mutation($email:String!,$username:String!, $password:String!,$displayName:String!)
        {
        register(email:$email,username:$username,password: $password,displayName:$displayName)
            {
                success,token, refreshToken, user{username,displayName,email}
            }
        }`

export const refresh_Token= `mutation($refreshToken:String!){
          refreshToken(refreshToken: $refreshToken){
            token,
            success,
            errors
        
          }
        }`