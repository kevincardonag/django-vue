<template>
    <v-app>
        <v-container
        class="pa-8"
        fluid
        >
            <p class="font-weight-medium font-italic display-3 text-center green--text  --text-darken-2">Generar Pedido</p>
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
                                        ></v-text-field>
                                        <v-select
                                            v-else-if="input.type =='select'"
                                            v-model="input.value"
                                            :items="input.select"
                                            :rules="input.rules"
                                            :label="input.label"
                                        ></v-select>
                                    </v-col>

                                </v-row>
                                <!-- <v-row>
                                    <v-col
                                        cols="12"
                                    >

                                        <v-text-field
                                            v-model="form.name"
                                            :rules="nameRules"
                                            label="Nombre Comprador"
                                        ></v-text-field>

                                    </v-col>

                                    <v-col
                                        cols="12"
                                    >

                                        <v-text-field
                                            v-model="form.direccion"
                                            :rules="direccionRules"
                                            label="Dirección"
                                        ></v-text-field>

                                    </v-col>

                                    <v-col
                                        cols="12"
                                    >

                                        <v-text-field
                                            v-model="form.email"
                                            :rules="emailRules"
                                            label="E-mail"
                                        ></v-text-field>

                                    </v-col>
                                    
                                    <v-col
                                        cols="12"
                                        sm="4"
                                    >

                                        <v-select
                                            v-model="form.metodo"
                                            :items="metodosPago"
                                            :rules="[v => !!v || 'Seleccione un metodo de pago']"
                                            label="Metodo de pago"
                                        ></v-select>
                                        
                                    </v-col>
                                        <v-col
                                            cols="12"
                                            sm="8"
                                            v-if="form.metodo==metodosPago[1]"
                                        >

                                            <v-text-field
                                                v-model="form.card"
                                                :rules="cardRules"
                                                label="Numero"
                                            ></v-text-field>

                                        </v-col>

                                        <v-col
                                            cols="12"
                                            sm="6"
                                            v-if="form.metodo==metodosPago[1]"
                                        >

                                            <v-text-field
                                                v-model="form.datecard"
                                                :rules="datecardRules"
                                                label="MM/YY"
                                            ></v-text-field>

                                        </v-col>

                                        <v-col
                                            cols="12"
                                            sm="6"
                                            v-if="form.metodo==metodosPago[1]"
                                        >

                                            <v-text-field
                                                v-model="form.cvccard"
                                                :rules="cvccardRules"
                                                label="CVC"
                                            ></v-text-field>

                                        </v-col>

                                    <v-btn
                                    :disabled="!valid"
                                    color="success"
                                    class="mr-4"
                                    @click="validate"
                                    >
                                    Validate
                                    </v-btn>

                                    <v-btn
                                    color="error"
                                    class="mr-4"
                                    @click="reset"
                                    >
                                    Reset Form
                                    </v-btn>

                                    <v-btn
                                    color="warning"
                                    @click="resetValidation"
                                    >
                                    Reset Validation
                                    </v-btn>
                                </v-row> -->
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
          
          valid: true,
          
          nameRules: [
            v => !!v || 'Nombre es requerido',
          ],
          
          emailRules: [
            v => !!v || 'E-mail es requerido',
            v => /.+@.+\..+/.test(v) || 'E-mail invalido',
          ],

          
          direccionRules: [
            v => !!v || 'Dirección es requerida',
          ],

          
          cardRules: [
            v => !!v || 'Tarjeta es requerida',
            v => /^(\d{4}[\s|\-]?){3}(\d{2,}\s{0,})$/.test(v) || 'Tarjeta no valida',
          ],
          
          datecardRules: [
            v => !!v || 'Fecha de vencimiento es requerida',
            v => /^([0][0-9]|[1][0-2])\/\d{2}$/.test(v) || 'Fecha no valida',
          ],
          
          cvccardRules: [
            v => !!v || 'CVC es requerida',
            v => /^\d{3}$/.test(v) || 'Fecha no valida',
          ],
          
          metodosPago: [
          'Contra Entrega',
          'Tarjeta de credito',
          ],
          
          form:{

                name: '',
                email: '',
                direccion: '',
                card: '',
                datecard: '',
                cvccard: '',
                metodo: null,

          },
          inputs:[

                {
                    name:'name',
                    vale:'', 
                    rules:[v => !!v || 'Nombre es requerido'], 
                    type:'text', 
                    label:"Nombre Comprador",
                    render:true,
                    cols:{cols:"12",sm:"12"},
                },
                {
                    name:'direccion',
                    vale:'', 
                    rules:
                        [
                            v => !!v || 'E-mail es requerido',
                            v => /.+@.+\..+/.test(v) || 'E-mail invalido',
                        ],  
                    type:'text', 
                    label:"Dirección",
                    render:true,
                    cols:{cols:"12",sm:"12"},
                },
                {
                    name:'email',
                    vale:'', 
                    rules:[v => !!v || 'Dirección es requerida',],
                    type:'text', 
                    label:"E-mail",
                    render:true,
                    cols:{cols:"12",sm:"12"},
                },
                {
                    name:'metodo',
                    vale:null, 
                    rules:[v => !!v || 'Metodo de pago es requerido',], 
                    type:'select', 
                    label:"Metodo de pago",
                    select:[
                        'Contra Entrega',
                        'Tarjeta de credito',
                    ],
                    render:true,
                    cols:{cols:"12",sm:"4"},
                },
                {
                    name:'card',
                    vale:'', 
                    rules:
                        [
                            v => !!v || 'Tarjeta es requerida',
                            v => /^(\d{4}[\s|\-]?){3}(\d{2,}\s{0,})$/.test(v) || 'Tarjeta no valida',
                        ], 
                    type:'text',
                    label:"Metodo de pago",
                    render:true,
                    cols:{cols:"12",sm:"8"},
                },
                {
                    name:'datecard',
                    vale:'', 
                    rules:
                        [
                            v => !!v || 'Fecha de vencimiento es requerida',
                            v => /^([0][0-9]|[1][0-2])\/\d{2}$/.test(v) || 'Fecha no valida',
                        ], 
                    type:'text', 
                    label:"Numero",
                    render:true,
                    cols:{cols:"12",sm:"6"},
                },
                {
                    name:'cvccard',
                    vale:'', 
                    rules:
                        [
                            v => !!v || 'CVC es requerida',
                            v => /^\d{3}$/.test(v) || 'Fecha no valida',
                        ], 
                    type:'text', 
                    label:"MM/YY",
                    render:true,
                    cols:{cols:"12",sm:"6"},
                },

          ]
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
        

        validate () {
            if (this.$refs.form.validate()) {
                this.snackbar = true
            }
        },
        reset () {
            this.$refs.form.reset()
        },
        resetValidation () {
            this.$refs.form.resetValidation()
        },

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