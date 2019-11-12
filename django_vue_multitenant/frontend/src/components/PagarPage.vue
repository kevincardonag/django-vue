<template>
    <v-app>
        <v-container
        class="pa-8"
        fluid
        >
            <p class="font-weight-medium font-italic display-3 text-center green--text  --text-darken-2">Generar Pedido</p>
            <v-row>
                <v-col
                cols="12"
                sm="12"
                md="6"
                lg="8"
                >

                    <v-card
                    >   
                        <v-card-title class="headline mb-1">Poductos</v-card-title>
                        <v-divider></v-divider>
                        <v-list >
                            <v-list-item 
                                v-for="(producto, index) in carrito.productos" 
                                :key="index"
                                three-line
                            >
                                <v-list-item-content>
                                    <v-list-item-title class="headline mb-4">
                                        {{producto.name}}  
                                        X {{producto.cantidad}}
                                        <span class= " hidden-sm-and-down green--text  --text-darken-2">$ {{producto.price.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')}}</span>
                                    </v-list-item-title>
                                    <v-list-item-subtitle class= "hidden-md-and-up green--text  --text-darken-2">$ {{producto.price.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')}}</v-list-item-subtitle>
                                    <v-list-item-subtitle>{{producto.description}}</v-list-item-subtitle>
                                </v-list-item-content>

                                <v-list-item-avatar
                                    tile
                                    size="80"
                                >
                                    <v-img :src="producto.image"></v-img>
                                </v-list-item-avatar>
                            </v-list-item>
                        </v-list>
                    </v-card>
                </v-col>

                <v-col
                    cols="12"
                    sm="12"
                    md="6"
                    lg="4"
                >

                    <v-card
                    >
                        <v-card-title class="headline mb-1">Total</v-card-title>
                        
                        <v-simple-table dense >
                            <tbody>
                                <tr>
                                    <td align="left">Productos ({{cantidad}}): </td>
                                    <td align="right">$ {{carrito.total.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')}}</td>
                                </tr>
                                <tr>
                                    <td align="left">Envio: </td>
                                    <td align="right">$ {{costoEnvio.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')}}</td>
                                </tr>
                            </tbody>
                            
                            <tfoot>
                                <tr>
                                    <td align="left">Total: </td>
                                    <td align="right">$ {{costoTotal.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')}}</td>
                                </tr>
                            </tfoot>
                        </v-simple-table>
                        <v-card-actions>
                            <v-btn block color="green" >
                                Generar pedido 
                                <v-icon>fa-money-bill-wave-alt</v-icon>
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-col>
            </v-row>
            
        </v-container>
    </v-app>
</template>
<script>
import axios from 'axios'
import {mapGetters,mapActions} from 'vuex';
export default {
    data () {
      return {
          costoEnvio:3000,
      }
    },
    mounted() {

        this.fetchCarrito();
                
    },
    computed:{

        ...mapGetters('car',{
            carrito:'allCarrito'
        }),
        
        cantidad:function(){

            let cantidad=0;
            for (const producto of this.carrito.productos) {
                cantidad+=producto.cantidad;
            }
            return cantidad;

        },

        costoTotal:function(){

            return this.carrito.total+this.costoEnvio;

        }

    },  

    methods:{


        ...mapActions('car',[
            'addCarrito','fetchCarrito'
        ]),

    }

}
</script>

<style scoped>

    
    table td{
        border:0 !important;
    }
    table tfoot td{
        border-top: 1px solid gray !important;
    }
</style>