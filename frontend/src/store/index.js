import Vue from "vue";
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        loggedIn: false,
        token: localStorage.getItem('token') || '',
        username: localStorage.getItem('username') || ''
    },
    getters: {

    },
    actions: {
        login(context, payload) {
            context.commit('login', payload)
        },
        register(context, payload) {
            context.commit('register', payload)
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
                headers: {'Content-Type': 'application/json',}
            }).then(function (response) {
                if (response.status == 200) {
                    state.loggedIn = true;
                    state.token = response.data.key;
                    state.username = payload.username;
                    localStorage.setItem("token", response.data.key);
                    localStorage.setItem("loggedIn", true);
                    localStorage.setItem("username", payload.username)
                    Vue.notify({
                        position: "top center",
                        group: "login",
                        text: "Successfully logged into your account! 🙂",
                        type: "success",
                    })
                    window.setTimeout(function () {
                        window.location.href = "/dashboard/home";
                    }, 1000)
                }
            }).catch(function (error) {
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
                state.username = "";
                localStorage.setItem("token", "NONE");
                localStorage.setItem("loggedIn", false);
                localStorage.setItem("username", "");
            })
            return(undefined);
        },
        register(state, payload) {
            if (String(payload.username).length == 0) {
                Vue.notify({
                    position: "top center",
                    group: "login",
                    text: "The username can't be blank 😔",
                    type: "error",
                })
                return(undefined);
            } else if (String(payload.password1).length == 0) {
                Vue.notify({
                    position: "top center",
                    group: "login",
                    text: "The password can't be blank 😔",
                    type: "error",
                })
                return(undefined);
            } else if (String(payload.password2).length == 0) {
                Vue.notify({
                    position: "top center",
                    group: "login",
                    text: "The password can't be blank 😔",
                    type: "error",
                })
                return(undefined);
            } else if (String(payload.email).length == 0) {
                Vue.notify({
                    position: "top center",
                    group: "login",
                    text: "The password can't be blank 😔",
                    type: "error",
                })
                return(undefined);
            }
            axios.post("http://127.0.0.1:8000/rest-auth/registration/", {
                username: payload.username,
                email: payload.email,
                password1: payload.password1,
                password2: payload.password2
            }, {headers: {'Content-Type': 'application/json'}}).then(function (response) {
                if (response.status == 201) {
                    state.loggedIn = true;
                    state.token = response.data.key;
                    state.username = payload.username
                    localStorage.setItem("token", response.data.key);
                    localStorage.setItem("loggedIn", true);
                    localStorage.setItem("username", payload.username);
                    axios.post("http://127.0.0.1:8000/createUserObject/", {
                        username: payload.username,
                        email: payload.email
                    }, {headers: {'Content-Type': 'application/json'}});
                    Vue.notify({
                        position: "top center",
                        group: "login",
                        text: "Successfully created your account! 🙂",
                        type: "success",
                    })
                    window.setTimeout(function () {
                        window.location.href = "/dashboard/home";
                    }, 1000)
                }
            }).catch(function (error) {
                if (error.response) {
                    for (const key in error.response.data) {
                        Vue.notify({    
                            position: "top center",
                            group: "login",
                            text: `${key} - ${error.response.data[key]}` + " 😔",
                            type: "error",
                        });
                    }
                } else {
                    for (const key in error.response.data) {
                        Vue.notify({    
                            position: "top center",
                            group: "login",
                            text: `${key} - ${error.response.data[key]}` + " 😔",
                            type: "error",
                        });
                    }
                }
                state.loggedIn = false;
                state.token = "NONE";
                state.username = "username";
                localStorage.setItem("token", "NONE");
                localStorage.setItem("loggedIn", false);
                localStorage.setItem("username", "");
            })
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
            localStorage.setItem("token", "NONE");
            localStorage.setItem("username", "");
            state.loggedIn = false;
            state.token = "NONE";
            state.username = "";
            window.setTimeout(function() {
                window.location.href = "/";
            }, 1000);
            return(undefined);
        }
    },
});
