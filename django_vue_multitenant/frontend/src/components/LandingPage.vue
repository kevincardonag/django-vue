<template>
    <v-app>
        <v-container
        class="pa-8"
        fluid
        >
            <v-row>
                <v-carousel>
                    <v-carousel-item
                        v-for="(item,i) in items"
                        :key="i"
                        :src="item.src"
                        reverse-transition="fade-transition"
                        transition="fade-transition"
                    ></v-carousel-item>
                </v-carousel>
            </v-row>
            <v-divider></v-divider>
            <p class="font-weight-medium font-italic display-3 text-center green--text  --text-darken-2">Favoritas</p>
            <v-row>
                <v-col
                v-for="(card, index) in cards"
                :key="card.title"
                :cols="card.flex"
                >
                    <v-card>
                        <v-img
                        :src="card.src"
                        class="white--text"
                        min-height="200"
                        max-height="300"
                        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                        >
                        <v-card-title
                            class="fill-height align-end"
                            v-text="card.title"
                        ></v-card-title>
                        </v-img>

                        <v-card-actions>
                        <v-list-item class="grow">
                            

                            <v-list-item-content>
                            <v-list-item-title>$ {{card.precio}}</v-list-item-title>
                            </v-list-item-content>

                            <v-btn icon @click="addItemCart(index)">
                                <v-icon>fa-cart-plus</v-icon>
                            </v-btn>
                        </v-list-item>
                        </v-card-actions>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </v-app>
</template>
<script>

import {mapActions} from 'vuex';
export default {
    data () {
      return {

        items: [
            {src: require('../../static/img/carousel/pizza1.jpg'),},
            {src: require('../../static/img/carousel/pizza2.jpg'),},
            {src: require('../../static/img/carousel/pizza3.jpg'),},
        ],
        cards: [
            { title: 'Hawaianaa', src: require('../../static/img/favoritas/pizza1.jpg'), precio:27000, flex: 12 },
            { title: 'Peperoni', src: require('../../static/img/favoritas/pizza2.jpg'), precio:35000, flex: 6 },
            { title: 'Chorizo', src: require('../../static/img/favoritas/pizza3.jpg'), precio:40000, flex: 6 },
        ],
      }
    },
    mounted() {

        this.fetchCarrito();
        
    },
    methods:{

        addItemCart(index){

            const item={
                title:this.cards[index].title,
                precio:this.cards[index].precio
            }

            this.addCarrito(item);
            
        },

        ...mapActions('car',[
            'addCarrito','fetchCarrito'
        ]),

    }

}
</script>