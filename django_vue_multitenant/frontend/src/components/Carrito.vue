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
                <v-btn outlined small color="primary"  @click="menu = false">Pagar</v-btn>

            </v-card-actions>

        </v-card>
    </v-menu>
</template>
<script>

export default {
    
    data: () => ({
        
        carrito:{
            productos:[],
            total:null,
        },
        
        total:90000,
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

        if (localStorage.carrito) {

            this.carrito = JSON.parse(localStorage.carrito);
            
        }

    },

    computed:{

        cantidad:function(){

            return this.carrito.productos.length

        },

    },


    methods:{

        removeCar(){
            this.$swal.fire({
            title: 'Esta seguro ?',
            type: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Si',
            cancelButtonText: 'No'
            }).then((result) => {
            if (result.value) {
                localStorage.removeItem('carrito');
                this.menu=false;
            }
            })

        }

    }

}
</script>