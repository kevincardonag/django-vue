import Vue from 'vue'
import App from './pages/Pagar.vue'
import {store,vuetify} from'./plugins/settings';

Vue.config.productionTip = false


new Vue({
  vuetify,
  store,
  delimiters: ['[[', ']]'],
  data: {
      message: 'Hello Vue!',
  },
  render: h => h(App)
}).$mount('#app')
