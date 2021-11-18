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
import League_CreateTeams from "../views/dashboard/league/onGoingLeague/createTeams.vue";
import League_Bracket from "../views/dashboard/league/onGoingLeague/bracket.vue";
import League_Leaderboard from "../views/dashboard/league/onGoingLeague/leaderboard.vue";
import League_StatTracker from "../views/dashboard/league/onGoingLeague/statTracker.vue";
import Profile from "../views/dashboard/profile/profile.vue";
import PageNotFound from "../views/404.vue";

Vue.use(VueRouter)


const routes = [
  {
    // location
    path: "/",
    // what we want to call it
    name: "Home",
    // component that is utilized
    component: Home,
    meta: {
      // do you need to be logged in to the website
      requiresAuth: false,
      // prevent user from accessing webpage is logged in
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
      requiresAuth: false,
      disableRouteIfLoggedIn: false,
    },
  },
  {
    path: "/dashboard/league/create",
    name: "Dashboard_League_Create",
    component: League_Create,
    meta: {
      requiresAuth: false,
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
    path: "/dashboard/league/:leagueName/preview",
    name: "Dashboard_League_Preview",
    component: League_Preview,
    meta: {
      requiresAuth: true,
      disableRouteIfLoggedIn: false,
    },
  },
  {
    path: "/dashboard/league/:id/createTeams",
    name: "LeagueOwnerPreview",
    component: League_CreateTeams,
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
    path: "/dashboard/league/:id/leaderboard",
    name: "Dashboard_League_Leaderboard",
    component: League_Leaderboard,
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
      requiresAuth: false,
      disableRouteIfLoggedIn: false,
    },
  },
  {
    path: "/dashboard/profile/:username",
    name: "Dashboard_Profile",
    component: Profile,
    meta: {
      requiresAuth: false,
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

// prevents '#' from appearing in the url address ba
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// routing works (dependent on auth or not)
router.beforeEach((to, from, next) => {
  // user trying to access requires auth page
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // if user isn't logged in and user is trying to access an authorized only page, send to login
    if (localStorage["token"] == "NONE" || localStorage["loggedIn"] == false) {
      window.location.href = "/auth/login";
    } else {
      // user is logged in, send to page!
      next();
    }
  // user trying to access a page that requires a user to not be logged in
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
