import Vue from "vue";
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        loggedIn: false,
        token: localStorage.getItem('token') || ''
    },
    getters: {

    },
    actions: {
        login(context, payload) {
            context.commit('login', payload)
        },
        register(context) {
            context.commit('register')
        },
        logout(context) {
            context.commit('logout')
        },
    },
    mutations: {
        login(state, payload) {
            if (String(payload.username).length == 0) {
                Vue.notify({
                    position: "top center",
                    group: "login",
                    text: "The username can't be blank 😔",
                    type: "error",
                })
                return(undefined);
            } else if (String(payload.password).length == 0) {
                Vue.notify({
                    position: "top center",
                    group: "login",
                    text: "The password can't be blank 😔",
                    type: "error",
                })
                return(undefined);
            }
            axios.post("http://127.0.0.1:8000/rest-auth/login/", {
                username: payload.username,
                password: payload.password
            }, {
                headers: {
                    'Content-Type': 'application/json',
                }
            }).then(function (response) {
                if (response.status == 200) {
                    state.loggedIn = true;
                    state.token = response.data.key;
                    localStorage.setItem("token", response.data.key);
                    localStorage.setItem("loggedIn", true);
                    Vue.notify({
                        position: "top center",
                        group: "login",
                        text: "Successfully logged into your account! 🙂",
                        type: "success",
                    })
                    window.setTimeout(function () {
                        window.location.href = "/dashboard";
                    }, 1000)
                }
            }).catch(function (error) {
                console.log(error.response)
                if (error.response) {
                    Vue.notify({    
                        position: "top center",
                        group: "login",
                        text: `${error.response.data.non_field_errors[0]}` + " 😔",
                        type: "error",
                    });
                } else {
                    Vue.notify({
                        position: "top center",
                        group: "login",
                        text: `${error.response.data.password[0]}` + " 😔",
                        type: "error",
                    });
                }
                state.loggedIn = false;
                state.token = "NONE";
                localStorage.setItem("token", "NONE");
                localStorage.setItem("loggedIn", false);
            })
            console.log(!state.loggedIn);
            return(undefined);
        },
        register() {
            return(undefined);
        },
        logout(state) {
            axios.post("http://127.0.0.1:8000/rest-auth/logout/").then(
                Vue.notify({
                    position: "top center",
                    group: "login",
                    text: `Successfully logged out` + " 👋",
                    type: "error"
                })
            )
            localStorage.setItem("loggedIn", false)
            localStorage.setItem("token", "NONE")
            state.loggedIn = false;
            state.token = "NONE";
            window.setTimeout(function() {
                window.location.href = "/";
            }, 1000);
            return(undefined);
        }
    },
});
