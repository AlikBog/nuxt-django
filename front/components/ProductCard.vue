<template>
    <v-card :elevation="10" width="350px"  class="pa-2">
        <v-img :src="URL_BACK+product.img" height="180px" class="imggr"></v-img>
        <v-card-title class="titlec">{{ product.title }}</v-card-title>
        <v-card-subtitle class="mader">{{ product.made }} руб.</v-card-subtitle>
        <v-card-title class="card">{{ product.cat.name }}</v-card-title>
       <v-card-actions>
        <v-btn style="background-color: black; color: white;"   variant="flat" @click="basketStore.add(this.product)">
                Купить
            </v-btn>
              
            <v-btn style="background-color: black; color: white;">
                <NuxtLink :to="`/products/${ product.id }`" style="text-decoration: none; color: inherit;">Подробнее...</NuxtLink>
        </v-btn>
           

        </v-card-actions> 
    </v-card>
</template>

<script setup>
const basketStore = useBasketStore();
const URL_BACK = 'http://127.0.0.1:8000'
const { product } = defineProps(['product'])
</script>

<style scoped>
.titlec {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 20px;


}






/* .imggr:hover {
    transition: transform 2.5s;
    transform: rotate(360deg);
} */


.mader {
    font-family: Arial, Helvetica, sans-serif;
    font-size: 20px;
    color: black;
}

</style>

