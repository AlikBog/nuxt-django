<template>
    <v-container class="id">
        <h1>{{ product.title }}</h1>
        <v-img :src="URL_BACK + product.img" height="264px"></v-img>
        <p id="m_top">{{ product.text }}</p>
        
        <p> Цена: {{ product.made }} р.</p>
    </v-container>
    <div class="count">

    </div>
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
    .id {
        width: 70%;
        float: left;
        text-align: justify;
        /* margin-right: 20px; */
    }

    #m_top{
        margin-top: 25px;
    }

    .count {
        display: inline-block;
        /* float: right; */
        
        width: 550px;
        height: 500px;
        box-shadow: 10px 10px black;
        background-image: url('https://img.freepik.com/premium-vector/roll-up-business-banner-design-vertical-template_407821-9.jpg');
        border-radius: 5px;

    }

</style>
