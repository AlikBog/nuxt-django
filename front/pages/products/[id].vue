<template>

    <v-container>
        <h1>{{ product.title }}</h1>
        <v-img :src="URL_BACK+product.img" height="264px"></v-img>
        <p>{{ product.text }}</p>
        <p>{{ product.made }}</p>
    </v-container>
 
</template>
  
<script setup>
const { id } = useRoute().params
const url = `http://127.0.0.1:8000/api/v1/${id}/`

const URL_BACK = 'http://127.0.0.1:8000'


const { data:product } = await useFetch(url)
  
definePageMeta({
        layout: 'default'
    })
</script>
  
<style scoped>
  
</style>