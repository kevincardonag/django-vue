import Vue from 'vue'
import App from './App.vue'
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
