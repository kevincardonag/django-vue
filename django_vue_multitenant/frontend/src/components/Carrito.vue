<template>
    <v-menu 
        ransition="slide-x-transition"
        offset-y
    >
        <template v-slot:activator="{ on }">
            <v-btn 
            text
            v-on="on"
            target="_blank"
            >
            <div
                style="margin-right:50px"
                text
                target="_blank"
            >
                <v-badge color="green">
                <template  v-slot:badge>{{cantidad}}</template>
                <v-icon>fa-cart-plus</v-icon>
                </v-badge>
            </div>      
            <span class="hidden-xs-only">${{carrito.total}}</span>
            </v-btn>
        </template>
        
        <v-card>
            <v-list>
                <v-list-item
                v-for="(producto, index) in carrito.productos" 
                :key="index"
                >
                
                    <v-list-item-content>
                        <v-list-item-title>{{ producto.title }}</v-list-item-title>
                    </v-list-item-content>

                    <v-list-item-icon>
                        <v-list-item-title>$ {{ producto.precio }}</v-list-item-title>
                    </v-list-item-icon>

                </v-list-item>
            </v-list>
  
            <v-divider></v-divider>
    
            <v-list>
                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-title>Total</v-list-item-title>
                    </v-list-item-content>

                    <v-list-item-icon>
                        <v-list-item-title>$ {{carrito.total}}</v-list-item-title>
                    </v-list-item-icon>
                </v-list-item>
            </v-list>
    
            <v-card-actions>
                
                <v-btn outlined small color="warning" @click="removeCar">Vaciar</v-btn>
                <v-btn outlined small color="primary"  @click="pagar">Pagar</v-btn>

            </v-card-actions>

        </v-card>
    </v-menu>
</template>
<script>

import {mapGetters,mapActions} from 'vuex'
export default {
    
    data: () => ({
        
        productos:[
            {title:'Pizza1',precio:3000},
            {title:'Pizza2',precio:3000},
            {title:'Pizza3',precio:3000}
        ],
        fav: true,
        menu: false,
        message: false,
        hints: true,
    }),

    mounted() {
        
    },

    computed:{

        ...mapGetters('car',{
            carrito:'allCarrito'
        }),
        
        cantidad:function(){

            return this.carrito.productos.length

        },

    },  
    

    methods:{

        ...mapActions('car',[
            'removeAllCarrito'
        ]),
        
        removeCar(){
            this.$swal.fire({
            title: 'Esta seguro ?',
            type: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Si',
            cancelButtonText: 'No'
            }).then((result) => {
            if (result.value) {
                
                this.removeAllCarrito();
                this.menu=false;
            }
            })

        },

        pagar(){
            // this.$store.car.commit('increment');
            // console.log(this.$store.car.state.count );
        }

    }

}
</script>