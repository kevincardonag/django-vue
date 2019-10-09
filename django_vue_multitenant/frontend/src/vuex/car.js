
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
        
        car.total=producto.precio;
        
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
        state.carrito.productos.push(producto);
        state.carrito.total+=producto.precio;
    },

    
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}
  