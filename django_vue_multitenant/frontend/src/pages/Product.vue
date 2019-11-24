<template>
  <v-app dark>
    <NavBar></NavBar>

    <v-content>
     <ProductPage/>
    </v-content>
    <Footer></Footer>
  </v-app>
</template>

<script>
import NavBar from '@/components/NavBar';
import ProductPage from '@/components/ProductPage';
import Footer from '@/components/Footer';

export default {
  name: 'App',
  components: {
    NavBar,
    ProductPage,
    Footer,
  },
  data: () => ({
  }),
};
</script>
