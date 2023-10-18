<template>
    <v-app>

        <header>
            <v-app-bar
            app
            color="black" margin-top="10px"
            >
            <v-app-bar-title>
                    <h3 class="itets">iTEST</h3>
                    <v-btn flat to="/" style="font-size: 15px;">Домой</v-btn>
                    <v-btn flat to="/about" style="font-size: 15px;">О нас</v-btn>

                
                <v-btn to="/basket" class="text-none" stacked>
                    <v-badge  :content="basketStore.productsTotal" color="error">
                        <v-icon>mdi-cart-outline</v-icon>
                    </v-badge>
                </v-btn>

            </v-app-bar-title>
            </v-app-bar>
        </header>

        <v-main class="cont" style="background-color: white;">
            <slot/>
        </v-main>

        <v-footer class="b" :elevation="20" rounded>
            <v-row justify="center" no-gutters>
                <v-btn
                    v-for="link in links"
                    :key="link.name"
                    variant="text"
                    class="mx-2 rotate-btn"
                    rounded="xl"
                    :to=link.href>
                    {{ link.name }}
                </v-btn>
            </v-row>
        </v-footer>

    </v-app>
</template>

<script setup>
const basketStore = useBasketStore()

const links = [
    { name: 'Главная', href: '/' },

    { name: 'О нас', href: '/about' }

]
</script>

<style  scoped>
.v-container{
    display: inline-flex;
}
/* .text-decoration-none {
  color: grey;
} */


/* .router-link-exact-active {
  color: #12b488;
} */



header {
    background-color: black;
}



/* .router-link-exact-active {
  color: #12b488;
} */






footer{
   max-height: 100px;
   color: white;
   background-color: white;
}


header {
    height: 86px;
}

.itets {
    margin-top: 40px;




}

.mx-2 {
    background-color: white;
    color: black;
    font-size: 15px;
    font-family: Arial, Helvetica, sans-serif;

}


.rotate-btn:active {
    transition: transform 0.6ms;
    transform: rotate(360deg);
    color: blueviolet;
}


</style>
