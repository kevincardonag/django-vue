import '@fortawesome/fontawesome-free/css/all.css'
import Vue from 'vue'
import VueSweetalert2 from 'vue-sweetalert2';
import Vuex from 'vuex'
import car from '@/vuex/car'
import Vuetify from 'vuetify/lib';
 
 
// Vue.use(VueSweetalert2);

Vue.use(Vuetify);

Vue.use(VueSweetalert2);
Vue.use(Vuex)


export const store= new Vuex.Store({
    modules: {
        car,
    },
    // state: {
    //     count: 0
    // },
    // mutations: {
    //     increment (state) {
    //         state.count++
    //     }
    // }
});

export const vuetify= new Vuetify({
    icons: {
      iconfont: 'fa',
    },
});