import { makeAutoObservable, reaction } from "mobx";
import { ServerError } from "../models/serverError";

export default class CommonStore {
    error: ServerError | null = null;
    token: string | null = window.localStorage.getItem('jwt');
    appLoaded = false;
    refreshToken:string|null=window.localStorage.getItem('jwt2');

    constructor() {
        makeAutoObservable(this);

        reaction(
            () => this.token,
            token => {
                if (token) {
                    window.localStorage.setItem('jwt', token)
                } else {
                    window.localStorage.removeItem('jwt')
                }
            }
        )
        reaction(
            () => this.refreshToken,
            refreshToken => {
                if (refreshToken) {
                    window.localStorage.setItem('jwt2', refreshToken)
                } else {
                    window.localStorage.removeItem('jwt2')
                }
            }
        )
    }
    
    setServerError = (error: ServerError) => {
        this.error = error;
    }

    setToken = (token: string | null) => {
        this.token = token;
    }
    setrefreshToken = (refreshtoken: string | null) => {
        this.refreshToken = refreshtoken;
    }

    setAppLoaded = () => {
        this.appLoaded = true;
    }
}