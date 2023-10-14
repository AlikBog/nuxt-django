<template>
    <v-container>
       <v-row>
           <v-col v-for="product in basketStore.getProducts" :key="product.id"  sm="6" md="4">
               <BasketCard :product="product" />
           </v-col>
       </v-row>
   </v-container>
</template>
 
<script setup>
const basketStore = useBasketStore()


</script>
 
<style scoped>
</style>