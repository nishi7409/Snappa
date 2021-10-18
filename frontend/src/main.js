import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import store from './store/index.js'
import Notifications from 'vue-notification'

Vue.config.productionTip = false
Vue.use(Notifications);

// localStorage.setItem("loggedIn", false);
// localStorage.setItem("token", "NONE");

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App),
}).$mount('#app')
