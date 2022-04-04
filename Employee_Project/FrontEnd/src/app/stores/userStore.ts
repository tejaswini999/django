import { makeAutoObservable, runInAction } from "mobx";
import { toast } from "react-toastify";
import { history } from "../..";
import agent from "../api/agent";
import { current_user, login_User, refresh_Token, register_user } from "../common/query/query";
import { User, UserFormValues } from "../models/user";
import { store } from "./store";
import jwt_decode from "jwt-decode";

export default class UserStore {
    user: User | null = null;

    constructor() {
        makeAutoObservable(this)
    }

    get isLoggedIn() {
        return !!this.user;
    }

    login = async (creds: UserFormValues) => {
        const  login_Query={
            "query":login_User,
                  "variables":{
                     "password": creds.password,
                    "username": creds.username
                        }
               };
        try {
            const user = await agent.API.data(login_Query);
                if(!user.data.data.tokenAuth.success)
                    toast.error("Invalid Credentials !")
                else{
                    toast.success("Welcome !!")
                    store.commonStore.setToken(user.data.data.tokenAuth.token);
                    store.commonStore.setrefreshToken(user.data.data.tokenAuth.refreshToken);
                    runInAction(() => this.user = user.data.data.tokenAuth.user);
                    history.push('/employee');
                    store.modalStore.closeModal();
                    }
            } catch (error) {
            console.log(error)
        }
    }

    logout = () => {
        store.commonStore.setToken(null);
        window.localStorage.removeItem('jwt');
        window.localStorage.removeItem('jwt2');
        this.user = null;
        toast.success("Thank you for visiting !")
        history.push('/');
    }

    getUser = async () => {
        const  currentUser_Query={"query": current_user };
        try {
            const user = await agent.API.data(currentUser_Query);
           runInAction(() => this.user = user.data.data.me);
        } catch (error) {
             console.log(error);
        }
    }

    register = async (creds: UserFormValues) => {
        const  register_Query={
            "query":register_user,
                  "variables":{
                    "email": creds.email,
                     "password": creds.password,
                    "username": creds.username,
                    "displayName": creds.displayName
                        }
               };
        try {
            const user = await agent.API.data(register_Query);
            if(!user.data.data.register)                                   // error
            {                             
                if (user.data.errors[0].message=="User Already Exists!")
                       toast.error("User Already Exists!")
            }
            else{
                toast.success('User Registered Sucessfully !')
               store.commonStore.setToken(user.data.data.register.token);
                store.commonStore.setrefreshToken(user.data.data.register.refreshToken);
                runInAction(() => this.user = user.data.data.register.user);
                history.push('/employee');
                store.modalStore.closeModal();
            }
        } 
        catch (error:any) {
            console.log(error)
        }
    }
    updateToken = (token:any) =>
  {
    let decodedToken :any= jwt_decode(token);
    var exp_time=decodedToken.exp-decodedToken.origIat-5;      // 5 secs before expiration of token
    const  refreshToken_query={
        "query":refresh_Token,
              "variables":{
                  "refreshToken": store.commonStore.refreshToken
                }
        };
    setTimeout(async ()=>{
        const resp = await agent.API.data(refreshToken_query)
        store.commonStore.setToken(resp.data.data.refreshToken.token)
    },exp_time*1000)
  }
  
}
