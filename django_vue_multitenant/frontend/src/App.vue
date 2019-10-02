<template>
  <v-app>
    <NavBar></NavBar>

    <v-content>
<!--      <HelloWorld/>-->
    </v-content>
  </v-app>
</template>

<script>
import NavBar from './components/NavBar';

export default {
  name: 'App',
  components: {
    NavBar,
  },
  data: () => ({
    categorias:['Pizza1','Pizza2','Pizza3']
  }),
};
</script>
