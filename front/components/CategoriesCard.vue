<template>
     <v-card :elevation="10" class="pa-2">
        <v-card-title>{{ cat }}</v-card-title>
        <v-card-actions>
            <v-btn variant="flat" color="indigo" :to="`/products/categories/${ cat }`">
                Открыть
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script setup>
    const { cat } = defineProps(['cat'])
</script>

<style scoped>

</style>