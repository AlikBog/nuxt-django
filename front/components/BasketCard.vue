<template>
    <v-card :elevation="10" class="pa-2">
        <v-img :src="URL_BACK+product.img" height="180px"></v-img>
        <v-card-title>{{ product.title }}</v-card-title>
        <v-card-subtitle>{{ product.made }} руб.</v-card-subtitle>
        <v-card-actions>
            <v-btn variant="flat" color="indigo" @click="basketStore.remove(product.id)">
                <v-icon>mdi mdi-delete</v-icon>
            </v-btn>
            <v-btn color="primary">
                <NuxtLink :to="`/products/${product.id}`">Подробнее...</NuxtLink>
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

</style>