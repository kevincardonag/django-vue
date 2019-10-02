<template>
    <v-app-bar app >
        <!-- <v-btn text
        target="_blank">

        </v-btn> -->
        <a href="">

        <v-avatar :tile="true" style="">
            <img :src="require('../../static/img/pizza.png')" alt="logo">
        </v-avatar>
        </a>
        <v-spacer></v-spacer>
      <v-btn v-for="(categoria, index) in categorias" v-bind:key="index"
        text
        target="_blank"
      >
        <span class="mr-2">{{categoria}}</span>
        <v-icon color="green darken-2">local_pizza</v-icon>
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn
        text
        target="_blank"
      >
        <span class="mr-2">Contatenos</span>
        <v-icon>contact_phone</v-icon>
      </v-btn>
    </v-app-bar>
</template>
<script>
export default {
    data: () => ({
        categorias:['Pizza1','Pizza2','Pizza3']
    }),
}
</script>