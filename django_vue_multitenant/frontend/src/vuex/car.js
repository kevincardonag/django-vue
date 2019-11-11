
const state={
    carrito:{
        productos:[],
        total:0,
    }
};

const getters={
    allCarrito: (state)=>state.carrito
};

const actions={
    fetchCarrito({commit}){

        if (localStorage.carrito) {

            const response=JSON.parse(localStorage.carrito);
            commit('setCarrito',response);

        }
    },

    addCarrito({commit},producto){

        let car=JSON.parse(localStorage.getItem('carrito'));
            
        if (!car) {

            car={
                productos:[],
                total:0,
            };

        }
        car.productos.push(producto);
        
        car.total+=producto.price;
        
        localStorage.carrito=JSON.stringify(car);
        
        commit('pushCarrito',producto);

    },

    removeAllCarrito({commit}){

        const carrito={

            productos:[],
            total:0,

        };

        localStorage.removeItem('carrito');
        commit('setCarrito',carrito);

    }
}; 

const mutations={

    setCarrito:(state, carrito) => (state.carrito = carrito ),

    pushCarrito:(state, producto) => {

        // state.carrito.productos.push(producto);
        let newproduct=true;
        for (let index = 0; index < state.carrito.productos.length; index++) {
            if (producto.id==state.carrito.productos[index].id) {
                state.carrito.productos[index].cantidad+=1;
                state.carrito.productos[index].price_total=state.carrito.productos[index].cantidad*state.carrito.productos[index].price;
                newproduct=false;
                break;
            }
        }
        if (newproduct) {
            state.carrito.productos.push(producto);
        }
        state.carrito.total+=producto.price;

    },

    
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}
  