import Vue from "vue";
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
    // state used for statuses
    state: {
        loggedIn: false,
        token: localStorage.getItem('token') || '',
        username: localStorage.getItem('username') || ''
    },
    getters: {

    },
    actions: {
        // login start
        login(context, payload) {
            context.commit('login', payload)
        },
        // register start
        register(context, payload) {
            context.commit('register', payload)
        },
        // logout start
        logout(context) {
            context.commit('logout')
        },
    },
    mutations: {
        // login mutation
        login(state, payload) {
            // checkers to see if data is valid
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
            // POST request to /rest-author/login/
            axios.post("http://127.0.0.1:8000/rest-auth/login/", {
                username: payload.username,
                password: payload.password
            }, {
                headers: {'Content-Type': 'application/json',}
            }).then(function (response) {
                // if good response, user is logged in!
                if (response.status == 200) {
                    state.loggedIn = true;
                    state.token = response.data.key;
                    state.username = payload.username;
                    localStorage.setItem("token", response.data.key);
                    localStorage.setItem("loggedIn", true);
                    localStorage.setItem("username", payload.username);
                    Vue.notify({
                        position: "top center",
                        group: "login",
                        text: "Successfully logged into your account! 🙂",
                        type: "success",
                    })
                    // redirect user
                    window.setTimeout(function () {
                        window.location.href = "/dashboard/home";
                    }, 1000)
                }
                // uh oh, there's a problem
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
                // set data
                state.loggedIn = false;
                state.token = "NONE";
                state.username = "";
                localStorage.setItem("token", "NONE");
                localStorage.setItem("loggedIn", false);
                localStorage.setItem("username", "");
            })
            return(undefined);
        },
        // register user for account
        register(state, payload) {
            // data validation
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
            // POST request to /rest-auth/registration/
            axios.post("http://127.0.0.1:8000/rest-auth/registration/", {
                username: payload.username,
                email: payload.email,
                password1: payload.password1,
                password2: payload.password2
            }, {headers: {'Content-Type': 'application/json'}}).then(function (response) {
                // success response
                if (response.status == 201) {
                    state.loggedIn = true;
                    state.token = response.data.key;
                    state.username = payload.username;
                    localStorage.setItem("token", response.data.key);
                    localStorage.setItem("loggedIn", true);
                    localStorage.setItem("username", payload.username);
                    // create user object
                    axios.post("http://127.0.0.1:8000/createUser/", {
                        username: payload.username,
                        email: payload.email
                    }, {headers: {'Content-Type': 'application/json'}});
                    Vue.notify({
                        position: "top center",
                        group: "login",
                        text: "Successfully created your account! 🙂",
                        type: "success",
                    })
                    // redirect user
                    window.setTimeout(function () {
                        window.location.href = "/dashboard/home";
                    }, 1000)
                }
                // uh oh error!
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
                // set state & localstorage data
                state.loggedIn = false;
                state.token = "NONE";
                state.username = "";
                localStorage.setItem("token", "NONE");
                localStorage.setItem("loggedIn", false);
                localStorage.setItem("username", "");
            })
            return(undefined);
        },
        // log out user
        logout(state) {
            axios.post("http://127.0.0.1:8000/rest-auth/logout/").then(
                Vue.notify({
                    position: "top center",
                    group: "login",
                    text: `Successfully logged out` + " 👋",
                    type: "error"
                })
            )
            // set state & localstorage
            localStorage.setItem("loggedIn", false)
            localStorage.setItem("token", "NONE")
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
