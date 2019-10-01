<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Vuetify</span>
        <span class="font-weight-light">MATERIAL DESIGN</span>
      </v-toolbar-title>

      <v-btn v-for="(categoria, index) in categorias" v-bind:key="index"
        text
        target="_blank"
      >
        <span class="mr-2">{{categoria}}</span>
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn
        text
        target="_blank"
      >
        <span class="mr-2">Latest Release</span>
      </v-btn>
    </v-app-bar>

    <v-content>
<!--      <HelloWorld/>-->
    </v-content>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld';

export default {
  name: 'App',
/*  components: {
    HelloWorld,
  },*/
  data: () => ({
    categorias:['Pizza1','Pizza2','Pizza3']
  }),
};
</script>
