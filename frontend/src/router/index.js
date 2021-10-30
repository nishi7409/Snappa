import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from "../views/home.vue";
import SignUp from "../views/auth/sign-up.vue";
import Login from "../views/auth/login.vue";
import Dashboard_Home from "../views/dashboard/home.vue";
import League_Home from "../views/dashboard/league/home.vue";
import League_Create from "../views/dashboard/league/create.vue";
import League_Join from "../views/dashboard/league/join.vue";
import League_Preview from "../views/dashboard/league/onGoingLeague/preview.vue";
import League_Bracket from "../views/dashboard/league/onGoingLeague/bracket.vue";
import League_StatTracker from "../views/dashboard/league/onGoingLeague/statTracker.vue";
import Profile from "../views/dashboard/profile/profile.vue";
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
    path: "/dashboard/home",
    name: "Dashboard_Home",
    component: Dashboard_Home,
    meta: {
      requiresAuth: true,
      disableRouteIfLoggedIn: false,
    },
  },
  {
    path: "/dashboard/league/home",
    name: "Dashboard_League_Create_Join",
    component: League_Home,
    meta: {
      requiresAuth: true,
      disableRouteIfLoggedIn: false,
    },
  },
  {
    path: "/dashboard/league/create",
    name: "Dashboard_League_Create",
    component: League_Create,
    meta: {
      requiresAuth: true,
      disableRouteIfLoggedIn: false,
    },
  },
  {
    path: "/dashboard/league/join",
    name: "Dashboard_League_Join",
    component: League_Join,
    meta: {
      requiresAuth: true,
      disableRouteIfLoggedIn: false,
    },
  },
  {
    path: "/dashboard/league/:id/preview",
    name: "Dashboard_League_Preview",
    component: League_Preview,
    meta: {
      requiresAuth: true,
      disableRouteIfLoggedIn: false,
    },
  },
  {
    path: "/dashboard/league/:id/bracket",
    name: "Dashboard_League_Bracket",
    component: League_Bracket,
    meta: {
      requiresAuth: true,
      disableRouteIfLoggedIn: false,
    },
  },
  {
    path: "/dashboard/league/:id/bracket/:teamID/statTracker",
    name: "Dashboard_League_Bracket_StatTracker",
    component: League_StatTracker,
    meta: {
      requiresAuth: true,
      disableRouteIfLoggedIn: false,
    },
  },
  {
    path: "/dashboard/profile/:id",
    name: "Dashboard_Profile",
    component: Profile,
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
      window.location.href = "/dashboard/home";
    } else {
      next();
    }
  } else {
    next()
  }
})


export default router
