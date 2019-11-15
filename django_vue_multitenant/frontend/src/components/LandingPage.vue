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
                v-for="(fav, index) in favorites"
                :key="fav.title"
                :cols="fav.flex"
                >
                    <v-card>
                        <v-img
                        :src="fav.image"
                        class="white--text"
                        min-height="200"
                        max-height="300"
                        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                        >
                        <v-card-title
                            class="fill-height align-end"
                            v-text="fav.name"
                        ></v-card-title>
                        </v-img>

                        <v-card-actions>
                        <v-list-item class="grow">
                            

                            <v-list-item-content>
                            <v-list-item-title>$ {{fav.price.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')}}</v-list-item-title>
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
import axios from 'axios'
import {mapActions} from 'vuex';
export default {
    data () {
      return {

        items: [
            {src: require('../../static/img/carousel/pizza1.jpg'),},
            {src: require('../../static/img/carousel/pizza2.jpg'),},
            {src: require('../../static/img/carousel/pizza3.jpg'),},
        ],
        favorites: [
            { name: 'Hawaianaa', image: require('../../static/img/favoritas/pizza1.jpg'), price:27000, flex: 12 },
            { name: 'Peperoni', image: require('../../static/img/favoritas/pizza2.jpg'), price:35000, flex: 6 },
            { name: 'Chorizo', image: require('../../static/img/favoritas/pizza3.jpg'), price:40000, flex: 6 },
            { name: 'Pollo', image: require('../../static/img/favoritas/pizza3.jpg'), price:40000, flex: 6 },
        ],
      }
    },
    mounted() {
        this.fetchCarrito();

        axios.get(`${window.location.protocol}//${window.location.host}/apiREST/products/`,
                {
                    params: {
                        favorites:true,
                    }
                }
        )
        .then(response => {
            const favorites=response.data;
            favorites.forEach((element,index) => {
                if (!favorites[index]['flex']) {
                    
                    favorites[index]['flex']=12
                }
            });
            this.favorites=favorites;
            console.log(favorites)
        })
        .catch(response => {
            console.log(error);
        });
    },
    methods:{

        addItemCart(index){

            const item={
                id:this.favorites[index].id,
                name:this.favorites[index].name,
                price:this.favorites[index].price,
                price_total:this.favorites[index].price,
                cantidad:1
            }
            

            this.addCarrito(item);
            
        },

        ...mapActions('car',[
            'addCarrito','fetchCarrito'
        ]),

    }

}
</script>