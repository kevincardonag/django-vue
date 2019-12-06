<template>
    <v-app>
        <v-container
        class="pa-8"
        fluid
        >
            <p class="font-weight-medium font-italic display-3 text-center green--text  --text-darken-2">Generar Pedido</p>
            <v-alert
              v-model="errorproducts"
              dense
              outlined 
              type="error"
            >
                No hay productos en el carrito
            </v-alert>
            <v-row>
                <v-col
                    sm="12"
                    md="8"
                >
                    <v-card>
                        <v-container>

                            <v-form
                                ref="form"
                                v-model="valid"
                                lazy-validation
                            >   
                                <v-row>
                                    <v-col 
                                        v-for="(input, index) in inputs"
                                        :key="index"
                                        :cols="input.cols.cols"
                                        :sm="input.cols.sm"
                                    >   
                                        
                                        <v-text-field
                                            v-if="input.type == 'text' && input.render"
                                            v-model="input.value"
                                            :rules="input.rules"
                                            :label="input.label"
                                            :disabled="input.disabled"
                                        ></v-text-field>
                                        <v-select
                                            v-else-if="input.type =='select'"
                                            v-model="input.value"
                                            :items="input.select"
                                            :rules="input.rules"
                                            :label="input.label"
                                            :disabled="input.disabled"
                                        ></v-select>
                                    </v-col>

                                </v-row>
                                
                            </v-form>

                        </v-container>
                    </v-card>
                    <v-card>   
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
                    sm="12"
                    md="4"
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
                            <v-btn block color="green" @click="pay">
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
          
          valid: true,

          inputs:{

            client_name:{
                value:'', 
                rules:[v => !!v || 'Nombre es requerido'], 
                type:'text', 
                label:"Nombre Comprador",
                render:true,
                required:true,
                cols:{cols:"12",sm:"12"},
                disabled:false,
            },
            direction:{
                value:'', 
                rules:[v => !!v || 'Dirección es requerida',],
                type:'text', 
                label:"Dirección",
                render:true,
                required:true,
                cols:{cols:"12",sm:"12"},
                disabled:false,
            },
            payment_method:{
                value:null, 
                rules:[v => !!v || 'Metodo de pago es requerido',], 
                type:'select', 
                label:"Metodo de pago",
                select:[
                    {value:'contra_entrega',text:'Contra Entrega'},
                    {value:'credit_cart',text:'Tarjeta de credito'},
                ],
                render:true,
                required:true,
                cols:{cols:"12",sm:"4"},
                disabled:false,
            },
            card:{
                value:'', 
                rules:
                    [
                        v => !!v || 'Tarjeta es requerida',
                        v => /^(\d{4}[\s|\-]?){3}(\d{2,}\s{0,})$/.test(v) || 'Tarjeta no valida',
                    ], 
                type:'text',
                label:"Numero",
                render:false,
                required:false,
                cols:{cols:"12",sm:"8"},
                disabled:false,
            },
            datecard:{
                value:'', 
                rules:
                    [
                        v => !!v || 'Fecha de vencimiento es requerida',
                        v => /^([0][0-9]|[1][0-2])\/\d{2}$/.test(v) || 'Fecha no valida',
                    ], 
                type:'text', 
                label:"MM/YY",
                render:false,
                required:false,
                cols:{cols:"12",sm:"6"},
                disabled:false,
            },
            cvscard:{
                value:'', 
                rules:
                    [
                        v => !!v || 'CVS es requerida',
                        v => /^\d{3}$/.test(v) || 'CVS invalido',
                    ], 
                type:'text', 
                label:"CVS  ",
                render:false,
                required:false,
                cols:{cols:"12",sm:"6"},
                disabled:false,
            },
          },
        
      }
    },
    mounted() {

        this.fetchCarrito();
        if (typeof usuario !== 'undefined') {
            
            if (usuario.name) {
                
                this.inputs.client_name.value=usuario.name;
                this.inputs.client_name.disabled=true;
                
            }

            if (usuario.direction!='None') {
                
                this.inputs.direction.value=usuario.direction;
                
            }

        }
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

        errorproducts:function(){
            return this.carrito.productos.length==0;
        },

        costoTotal:function(){

            return this.carrito.total+this.costoEnvio;

        },

        form:function(){
            
            
            const form={
                products:[],
            };
            for (const key in this.inputs) {
                if (this.inputs[key].required) {
                    
                    form[key]=this.inputs[key].value;

                }
            }

            form.products=this.carrito.productos.map(element => {
                return {
                    product:element.id,
                    quantity:element.cantidad,
                }
            });
            return form;
        },


    },

    watch:{

        inputs:{

            handler: function(val) {
                let render=false;
                if( this.inputs.payment_method.value=='credit_cart'){

                    render=true;

                }

                for (const key in this.inputs) {

                    if (key.includes('card')) {
                        
                        this.inputs[key].render=render;

                    }

                }
            },
            deep: true
        }

    },

    methods:{


        ...mapActions('car',[
            'addCarrito','fetchCarrito','removeAllCarrito'
        ]),
        
        pay(){
            
            if (this.$refs.form.validate()) {
                
                if (!this.errorproducts) {
                    let csrftoken = this.getCookie('csrftoken');
                    
                    
                    axios.post(`${window.location.protocol}//${window.location.host}/apiREST/order/`,
                    this.form,
                    {headers: {"X-CSRFToken": csrftoken}},)
                    .then(response => {
                        this.$swal.fire({
                            title: 'Orden creada exitosamente',
                            type: 'success',
                            confirmButtonText: 'Si',
                        }).then((result) => {
                            if (result.value) {
    
                                this.removeAllCarrito();
                                // location.reload();
                                window.location.replace(`${window.location.protocol}//${window.location.host}`);
                                
                            }
                        })
                    })
                    .catch(error => {
                        console.log(error);
                    });

                }
            }
            
        },

        getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

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