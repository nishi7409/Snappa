<template>
   <v-app id="inspire">
      <v-content>
         <v-container fluid>
            <v-row>
               <v-layout align-center justify-center wrap>
                  <!-- <v-img  
                  :scr="require('./snappaLogo.jpg')"
                  >
                  </v-img> -->
               </v-layout>
            </v-row>
            <v-row> 
            <v-layout align-center justify-center wrap>
               
               <v-flex xs12 sm8 md4>
                  <v-card class="elevation-12">
                     <v-toolbar class="text-center" dark color="primary">
                        <v-toolbar-title >Login</v-toolbar-title>                      
                     </v-toolbar>
                     <v-card-text>
                        <v-form>
                           <v-text-field
                              prepend-icon="mdi-account-circle"
                              name="username"
                              label="Username"
                              type="text"
                           ></v-text-field>
                           <v-text-field
                              id="password"
                              prepend-icon="mdi-lock"
                              name="password"
                              label="Password"
                              type="password"
                           ></v-text-field>
                        </v-form>
                     </v-card-text>
                     <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" to="/">Forgot Password?</v-btn>
                        <v-btn color="primary">Login</v-btn>
                     </v-card-actions>
                  </v-card>
               </v-flex>
            </v-layout>
            </v-row>
         </v-container>
      </v-content>
   </v-app>
</template>

<script>
export default {
   name: 'Login',
   props: {
      source: String,
   },
};
</script>

<style></style>
