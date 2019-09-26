import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

new Vue({
  vuetify,
  delimiters: ['[[', ']]'],
  data: {
          message: 'Hello Vue!',
          foo: foo,
  },
  render: h => h(App)
}).$mount('#app')
