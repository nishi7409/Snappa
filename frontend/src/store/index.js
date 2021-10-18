import Vue from "vue";
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        loggedIn: false,
        token: "NONE",
    },
    getters: {

    },
    actions: {
        login(context) {
            context.commit('login')
        },
        register(context) {
            context.commit('register')
        },
        logout(context) {
            context.commit('logout')
        },
    },
    mutations: {
        login(state) {
            axios.post("http://127.0.0.1:8000/rest-auth/login/", {
                username: 'admin',
                password: 'password'
            }, {
                headers: {
                    'Content-Type': 'application/json',
                }
            }).then(function (response) {
                if (response.status == 200) {
                    state.loggedIn = true;
                    state.token = response.data.key;
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
                if (error.response) {
                    Vue.notify({
                        position: "top center",
                        group: "login",
                        text: "Enter error information here 😔",
                        type: "error",
                    });
                } else if (error.request) {
                    Vue.notify({
                        position: "top center",
                        group: "login",
                        text: "Enter error information here 😔",
                        type: "error",
                    });
                } else {
                    Vue.notify({
                        position: "top center",
                        group: "login",
                        text: "Enter error information here 😔",
                        type: "error",
                    });
                }
                state.loggedIn = false;
                state.token = "NONE";
            })
            console.log(!state.loggedIn);
            return (state.loggedIn = !state.loggedIn);
        },
        register() {
            return null;
        },
        logout() {
            // axios.post("http://127.0.0.1:8000/rest-auth/logout/", {

            // })
            return null;
        }
    },
});
