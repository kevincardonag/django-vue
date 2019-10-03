<template>
    <v-app-bar app >
    <!-- <v-toolbar> -->
      <a href="">
        
        <v-avatar :tile="true" >
            <img :src="require('../../static/img/pizza.png')" alt="logo">
        </v-avatar>
      </a>
      <v-spacer></v-spacer>
      <v-btn v-for="(categoria, index) in categorias" v-bind:key="index"
        text
        target="_blank"
      >
        <span class="mr-2">{{categoria}}</span>
        <v-icon color="green darken-2">fa-pizza-slice</v-icon>
      </v-btn>
      <v-spacer></v-spacer>
      <v-divider vertical></v-divider>
      <div >
        <v-btn
          style="margin-right:100px"
          text
          target="_blank"
        >
          <v-badge color="green">
            <template  v-slot:badge>0</template>
            <v-icon>fa-cart-plus</v-icon>
          </v-badge>
        </v-btn>      
        <span class="hidden-sm-and-down">${{total}}</span>
      </div>
    <!-- </v-toolbar> -->
    </v-app-bar>
</template>
<script>
export default {
    data: () => ({
        total:0,
        categorias:['Pizza1','Pizza2','Pizza3']
    }),
}
</script>