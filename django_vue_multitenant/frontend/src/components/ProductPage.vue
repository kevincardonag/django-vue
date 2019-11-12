<template>
    <v-app>
        <v-container
        class="pa-8"
        fluid
        >
            <p class="font-weight-medium font-italic display-3 text-center green--text  --text-darken-2">Productos</p>

                <v-data-iterator
                    :items="products"
                    :items-per-page.sync="productsPerPage"
                    :footer-props="{ productsPerPageOptions }"
                    :single-expand="expand"
                >
                    <template v-slot:default="props">
                    <v-row>
                        <v-col
                        v-for="(item,index) in props.items"
                        :key="item.name"
                        cols="12"
                        sm="6"
                        md="4"
                        lg="3"
                        >
                        <v-card>
                            <!-- <v-card-title><h4>{{ item.name }}</h4></v-card-title> -->
                            <v-img
                            :src="item.image"
                            class="white--text"
                            height="200"
                            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                            >

                                <v-card-title
                                    class="fill-height align-end"
                                    v-text="item.name"
                                ></v-card-title>

                            </v-img>

                            <v-divider></v-divider>

                            <v-list dense>

                                <v-list-item class="grow">
                                
                                    <v-list-item-content>
                                        <v-list-item-title class="my-4 subtitle-1 black--text">Descripción</v-list-item-title>
                                        <div >{{item.description}}</div>
                                    </v-list-item-content>

                                </v-list-item>

                                <v-list-item class="grow">
                                
                                    <v-list-item-content>
                                        <v-list-item-title class="subtitle-1 black--text">Ingredientes</v-list-item-title>
                                    </v-list-item-content>

                                    <v-spacer></v-spacer>

                                    <v-btn
                                        icon
                                        @click="show(props,item)"
                                    >
                                        <v-icon>{{ props.isExpanded(item) ? 'fa-chevron-up' : 'fa-chevron-down' }}</v-icon>
                                    </v-btn>

                                </v-list-item>
                            </v-list>

                            <v-expand-transition>
                                <div v-if="props.isExpanded(item)" >
                                    <v-divider></v-divider>

                                    <v-list dense>
                                        <v-list-item
                                        v-for="(ingredient, index) in item.ingredient"
                                        :key="index"
                                        >
                                            <v-list-item-content class="align-end">{{ ingredient }}</v-list-item-content>
                                        </v-list-item>
                                    </v-list>
                                </div>
                            </v-expand-transition>
                            
                            <v-divider></v-divider>
                            <v-card-actions>
                                <v-list-item class="grow">
                                    

                                    <v-list-item-content>
                                    <v-list-item-title>$ {{item.price}}</v-list-item-title>
                                    </v-list-item-content>

                                    <v-btn icon @click="addItemCart(index)">
                                        <v-icon>fa-cart-plus</v-icon>
                                    </v-btn>
                                </v-list-item>
                            </v-card-actions>

                        </v-card>
                        </v-col>
                    </v-row>
                    </template>
                </v-data-iterator>
            
        </v-container>
    </v-app>
</template>
<script>
import axios from 'axios'
import {mapActions} from 'vuex';
export default {
    data () {
      return {
        expand: false,
        productsPerPageOptions: [10, 15, 20],
        productsPerPage: 20,
        products: [
            { name: 'Hawaianaa', image: require('../../static/img/favoritas/pizza1.jpg'), price:27000, flex: 12 },
            { name: 'Peperoni', image: require('../../static/img/favoritas/pizza2.jpg'), price:35000, flex: 6 },
            { name: 'Chorizo', image: require('../../static/img/favoritas/pizza3.jpg'), price:40000, flex: 6 },
            { name: 'Pollo', image: require('../../static/img/favoritas/pizza3.jpg'), price:40000, flex: 6 },
        ],
      }
    },
    mounted() {
        this.fetchCarrito();

        axios.get('http://pizzachimba.localhost:8000/apiREST/products/',)
        .then(response => {
            const products=response.data;
            products.forEach((element,index) => {
                if (!products[index]['flex']) {
                    
                    products[index]['flex']=6
                }
            });
            this.products=products;
            console.log(products)
        })
        .catch(response => {
            console.log(error);
        });
    },
    methods:{

        addItemCart(index){

            const item={
                id:this.products[index].id,
                name:this.products[index].name,
                price:this.products[index].price,
                price_total:this.products[index].price,
                cantidad:1
            }
            

            this.addCarrito(item);
            
        },
        show(props,item){
            const value=props.isExpanded(item);
            props.expand(item,!value);
        },

        ...mapActions('car',[
            'addCarrito','fetchCarrito'
        ]),

    }

}
</script>