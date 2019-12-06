<template>
    <div>
    <v-app-bar app >
    
      <a :href="base_url">
        
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
            :href="categoria.href"
          >
            <v-list-item-title>{{ categoria.name }}</v-list-item-title>
            <v-icon color="green darken-2">fa-pizza-slice</v-icon>
          </v-list-item>
        </v-list>
      </v-menu>

      <v-spacer></v-spacer>

      <v-btn v-for="(categoria, index) in categorias" v-bind:key="index"
        text
        class="hidden-sm-and-down"
        :href="categoria.href"
      >

        <span class="mr-2">{{categoria.name}}</span>

        <v-icon color="green darken-2">fa-pizza-slice</v-icon>

      </v-btn>

      <v-spacer></v-spacer>
      
      <v-divider vertical></v-divider>
      <v-btn 
        v-if="!username" 
        text 
        :href="base_url+'/login/'"
      >

        <span class="mr-2">Ingresar</span>
        <v-icon color="green darken-2">fa-sign-in-alt</v-icon>

      </v-btn>
      <v-menu 
        ransition="slide-x-transition"
        v-else
        offset-y
      >
        <template v-slot:activator="{ on }">
          <v-btn
            text
            v-on="on"
          >
            <span class="mr-2">{{username}}</span>
          </v-btn>
        </template>
        
        <v-list>
          <v-list-item
            :href="base_url+'/users/edit'"
          >
            <v-list-item-title>Editar</v-list-item-title>
            <v-icon color="gray darken-2">fa-user-edit</v-icon>
          </v-list-item>

          <v-list-item
            :href="base_url+'/logout/'"
          >
            <v-list-item-title>Salir</v-list-item-title>
            <v-icon color="gray darken-2">fa-sign-out-alt</v-icon>
          </v-list-item>          
        </v-list>
      </v-menu>
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
        base_url:`${window.location.protocol}//${window.location.host}`,
        username:"",
        // logo:require('../../static/img/pizza.png'),
        logo:'',
        // categorias:['Pizza1','Pizza2','Pizza3']
        categorias:[
          {'name':'Productos','href':'/pizzas'}
        ]
    }),

    mounted(){
      this.logo=`${this.base_url}/static/client-page/img/pizza.png`;
      if (typeof usuario !== 'undefined') {
          this.username=usuario.username;
      }
    }

   
}
</script>