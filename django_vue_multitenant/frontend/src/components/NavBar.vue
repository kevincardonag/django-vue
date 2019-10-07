<template>
    <div>
    <v-app-bar app >
    
      <a href="/client">
        
        <v-avatar :tile="true" >
            <img :src="logo" alt="logo">
        </v-avatar>
      </a>

      <v-menu 
        ransition="slide-x-transition"
        offset-y
      >
        <template v-slot:activator="{ on }">
          <v-btn
            text
            target="_blank"
            v-on="on"
            class="hidden-md-and-up"
          >
            <v-icon color="green darken-2">fa-bars</v-icon>
          </v-btn>
        </template>
        
        <v-list>
          <v-list-item
            v-for="(categoria, index) in categorias" 
            :key="index"
          >
            <v-list-item-title>{{ categoria }}</v-list-item-title>
            <v-icon color="green darken-2">fa-pizza-slice</v-icon>
          </v-list-item>
        </v-list>
      </v-menu>

      <v-spacer></v-spacer>

      <v-btn v-for="(categoria, index) in categorias" v-bind:key="index"
        text
        class="hidden-sm-and-down"
        target="_blank"
      >

        <span class="mr-2">{{categoria}}</span>

        <v-icon color="green darken-2">fa-pizza-slice</v-icon>

      </v-btn>

      <v-spacer></v-spacer>

      <v-divider vertical></v-divider>

      <Carrito/>
    </v-app-bar>
    
  </div>
</template>
<script>
import Carrito from './Carrito';
export default {
    components: {
      Carrito,
    },
    data: () => ({
        logo:require('../../static/img/pizza.png'),
        categorias:['Pizza1','Pizza2','Pizza3']
    }),

    
}
</script>