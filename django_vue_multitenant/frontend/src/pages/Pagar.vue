<template>
  <v-app dark>
    <NavBar></NavBar>

    <v-content>
     <PagarPage/>
    </v-content>
    <Footer></Footer>
  </v-app>
</template>

<script>
import NavBar from '@/components/NavBar';
import PagarPage from '@/components/PagarPage';
import Footer from '@/components/Footer';

export default {
  name: 'App',
  components: {
    NavBar,
    PagarPage,
    Footer,
  },
  data: () => ({
  }),
};
</script>
