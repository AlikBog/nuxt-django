<template>
    <v-container>
        <v-row>
            <v-col v-for="product in products" :key="product.id"  sm="6" md="4">
                <ProductCard :product="product" />
            </v-col>
        </v-row>
    </v-container>
  </template>
  
<script setup>
const { cat } = useRoute().params
const url = 'https://dummyjson.com/products/category/' + cat

const { data: products } = await useFetch(url,{
    transform:(_data) => _data.products,
})
definePageMeta({
    layout: 'default'
})
</script>
  
  <style scoped>
  
  </style>