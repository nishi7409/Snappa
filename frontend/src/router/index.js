import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from "../views/home.vue";
import SignUp from "../views/auth/sign-up.vue";
import Login from "../views/auth/login.vue";
import Dashboard from "../views/dashboard/home.vue";
import Profile from "../views/dashboard/profile.vue";
import Admin from "../views/admin/home.vue";
import PageNotFound from "../views/404.vue";

Vue.use(VueRouter)


const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
    meta: {
      requiresAuth: false
    }
  },
  {
    path: "/auth/sign-up",
    name: "Sign Up",
    component: SignUp,
    meta: {
      requiresAuth: false
    }
  },
  {
    path: "/auth/login",
    name: "Login",
    component: Login,
    meta: {
      requiresAuth: false
    }
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/dashboard/profile/:id",
    name: "Profile",
    component: Profile,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "/admin",
    name: "Admin",
    component: Admin,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: "*",
    name: "404 Error",
    component: PageNotFound,
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


export default router
