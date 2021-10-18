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
      requiresAuth: false,
      disableRouteIfLoggedIn: false,
    },
  },
  {
    path: "/auth/sign-up",
    name: "Sign Up",
    component: SignUp,
    meta: {
      requiresAuth: false,
      disableRouteIfLoggedIn: true,
    },
  },
  {
    path: "/auth/login",
    name: "Login",
    component: Login,
    meta: {
      requiresAuth: false,
      disableRouteIfLoggedIn: true,
    },
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
    meta: {
      requiresAuth: true,
      disableRouteIfLoggedIn: false,
    },
  },
  {
    path: "/dashboard/profile/:id",
    name: "Profile",
    component: Profile,
    meta: {
      requiresAuth: true,
      disableRouteIfLoggedIn: false,
    },
  },
  {
    path: "/admin",
    name: "Admin",
    component: Admin,
    meta: {
      requiresAuth: true,
      disableRouteIfLoggedIn: false,
    },
  },
  {
    path: "*",
    name: "404 Error",
    component: PageNotFound,
    meta: {
      requiresAuth: false,
      disableRouteIfLoggedIn: false,
    },
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// routing works (dependent on auth or not)
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (localStorage["token"] == "NONE" || localStorage["loggedIn"] == false) {
      window.location.href = "/auth/login";
    } else {
      next();
    }
  } else if (to.matched.some(record => record.meta.disableRouteIfLoggedIn)) {
    if (localStorage["token"] !== "NONE" || localStorage["loggedIn"] == true) {
      window.location.href = "/dashboard";
    } else {
      next();
    }
  } else {
    next()
  }
})


export default router
