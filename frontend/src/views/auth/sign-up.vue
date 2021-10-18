<template>
   <v-app id="inspire">
      <v-main>
         <v-container fluid>
            <v-row> 
               <v-layout align-center justify-center wrap>
                  <v-flex xs12 sm8 md4>
                      <v-img scr="../../assets/logo.jpg">
                      </v-img>
                     <!-- <h1>Session Key - {{ sessionKey }}</h1> -->
                     <v-card class="elevation-12">
                        <v-toolbar class="text-center" dark color="primary">
                        <v-toolbar-title >Register</v-toolbar-title>                      
                        </v-toolbar>
                        <v-card-text>
                           <v-form>
                              <v-text-field
                                 prepend-icon="mdi-account-circle"
                                 name="username"
                                 label="Username"
                                 type="text"
                                 v-model="username"
                              ></v-text-field>
                              <v-text-field
                                 id="password"
                                 prepend-icon="mdi-lock"
                                 name="password"
                                 label="Password"
                                 type="password"
                                 v-model="password"
                              ></v-text-field>
                              <v-text-field
                                 prepend-icon="mdi-lock"
                                 name="password2"
                                 label="Confirm Password"
                                 type="text"
                                 v-model="password2"
                              ></v-text-field>
                           </v-form>
                        </v-card-text>
                        <v-card-actions>
                           <v-spacer></v-spacer>
                           <!-- <v-btn color="primary" to="/">Forgot Password?</v-btn> -->
                           <v-btn color="primary" v-on:click="register()">Register</v-btn>
                        </v-card-actions>
                     </v-card>
                  </v-flex>
               </v-layout>
            </v-row>
         </v-container>
      </v-main>
   </v-app>
</template>