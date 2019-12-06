<template>
    <v-app>
        <v-container
        class="pa-8"
        fluid
        >
            <p class="font-weight-medium font-italic display-3 text-center green--text  --text-darken-2">Productos</p>

                <v-data-iterator
                    :items="products"
                    :single-expand="expand"
                    :items-per-page.sync="itemsPerPage"
                    :page="page"
                    :search="search"
                    :sort-by="sortBy.toLowerCase()"
                    :sort-desc="sortDesc"
                    hide-default-footer
                >   
                    <template v-slot:header>
                        <v-toolbar
                            dark
                            color="green"
                            class="mb-1"
                        >
                            <v-text-field
                            v-model="search"
                            clearable
                            flat
                            solo-inverted
                            hide-details
                            prepend-inner-icon="search"
                            label="Buscar"
                            ></v-text-field>
                            <template v-if="$vuetify.breakpoint.mdAndUp">
                                <v-spacer></v-spacer>
                                <v-select
                                    v-model="sortBy"
                                    flat
                                    solo-inverted
                                    hide-details
                                    :items="keys"
                                    prepend-inner-icon="search"
                                    label="Sort by"
                                ></v-select>
                                <v-spacer></v-spacer>
                                <v-btn-toggle
                                    v-model="sortDesc"
                                    mandatory
                                >
                                    <v-btn
                                    
                                    depressed
                                    color="green"
                                    :value="false"
                                    >
                                    <v-icon>fa-arrow-up</v-icon>
                                    </v-btn>
                                    <v-btn
                                    
                                    depressed
                                    color="green"
                                    :value="true"
                                    >
                                    <v-icon>fa-arrow-down</v-icon>
                                    </v-btn>
                                </v-btn-toggle>
                            </template>
                        </v-toolbar>
                    </template>

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
                                        <v-list-item-title>$ {{item.price.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')}}</v-list-item-title>
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

                    <template v-slot:footer>
                        <v-row class="mt-2" align="center" justify="center">
                            <span class="grey--text">Productos por pagina</span>
                            <v-menu offset-y>
                                <template v-slot:activator="{ on }">
                                    <v-btn
                                    dark
                                    text
                                    color="green"
                                    class="ml-2"
                                    v-on="on"
                                    >
                                    {{ itemsPerPage }}
                                    <v-icon>fa-chevron-down</v-icon>
                                    </v-btn>
                                </template>
                                <v-list>
                                    <v-list-item
                                    v-for="(number, index) in itemsPerPageArray"
                                    :key="index"
                                    @click="updateItemsPerPage(number)"
                                    >
                                    <v-list-item-title>{{ number }}</v-list-item-title>
                                    </v-list-item>
                                </v-list>
                            </v-menu>
                
                            <v-spacer></v-spacer>
                
                            <span
                                class="mr-4
                                grey--text"
                            >
                                Pagina {{ page }} de {{ numberOfPages }}
                            </span>
                            <v-btn
                                fab
                                small
                                dark
                                color="green"
                                class="mr-1"
                                @click="formerPage"
                            >
                                <v-icon>fa-chevron-left</v-icon>
                            </v-btn>
                            <v-btn
                                fab
                                small
                                dark
                                color="green"
                                class="ml-1"
                                @click="nextPage"
                            >
                                <v-icon>fa-chevron-right</v-icon>
                            </v-btn>
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
        // itemsPerPageOptions: [2, 4, 8, 12],
        itemsPerPageArray: [4, 8, 12],
        page: 1,
        itemsPerPage: 4,
        sortDesc: false,
        search: '',
        sortBy: 'name',
        keys: [
            'name',
            'price',
        ],
        products: [
            // { name: 'Hawaianaa', image: require('../../static/img/favoritas/pizza1.jpg'), price:27000, flex: 12 },
            // { name: 'Peperoni', image: require('../../static/img/favoritas/pizza2.jpg'), price:35000, flex: 6 },
            // { name: 'Chorizo', image: require('../../static/img/favoritas/pizza3.jpg'), price:40000, flex: 6 },
            // { name: 'Pollo', image: require('../../static/img/favoritas/pizza3.jpg'), price:40000, flex: 6 },
        ],
      }
    },
    mounted() {
        this.fetchCarrito();

        axios.get(`${window.location.protocol}//${window.location.host}/apiREST/products/`,)
        .then(response => {
            const products=response.data;
            products.forEach((element,index) => {
                if (!products[index]['flex']) {
                    
                    products[index]['flex']=6
                }
            });
            this.products=products;
            
        })
        .catch(response => {
            console.log(error);
        });
    },
    
    computed: {
        
        numberOfPages () {
            return Math.ceil(this.products.length / this.itemsPerPage)
        },
        filteredKeys () {
            return this.keys.filter(key => key !== `Name`)
        },
    },

    methods:{
        nextPage () {
            if (this.page + 1 <= this.numberOfPages) this.page += 1
        },
        formerPage () {
            if (this.page - 1 >= 1) this.page -= 1
        },
        updateItemsPerPage (number) {
            this.itemsPerPage = number
        },

        addItemCart(index){

            const item={
                id:this.products[index].id,
                name:this.products[index].name,
                description:this.products[index].description,
                image:this.products[index].image,
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