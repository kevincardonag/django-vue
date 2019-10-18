<template>
  <v-app dark>
    <NavBar></NavBar>

    <v-content>
     <LandingPage/>
    </v-content>
    <Footer></Footer>
  </v-app>
</template>

<script>
import NavBar from './components/NavBar';
import LandingPage from './components/LandingPage';
import Footer from './components/Footer';

export default {
  name: 'App',
  components: {
    NavBar,
    LandingPage,
    Footer,
  },
  data: () => ({
  }),
};
</script>
