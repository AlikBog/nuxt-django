<template>
    <v-container>

        <div class="homec">
            <h1>Домашняя страница</h1>
        </div>
        <v-row>
            <v-col cols="2">
                <v-btn v-for="cat in categories" class="catgory" block variant="flat" style="margin: 5px;" color="indigo"
                    @click="funcBtn(cat)">
                    {{ cat.name }}
                </v-btn>
            </v-col>
            <v-col>
                <v-row>
                    <v-col v-for="product in products" :key="product.id" sm="4" md="3" class="card_line">
                        <ProductCard :product="product" />
                    </v-col>
                </v-row>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
const basketStore = useBasketStore()
// const {data: products} = await useFetch('http://127.0.0.1:8000/api/v1')
const { data: categories } = await useFetch('http://127.0.0.1:8000/api/v1/category/')

const cat = ref(1)

const funcBtn = (x) => {
    cat.value = x.id
}
const url = computed(() =>
    `http://127.0.0.1:8000/api/v1/category/${cat.value}/`
)

const { data: products } = await useFetch(url)

</script>

<style scoped>

.flane {

    text-align: left;
}

.homec {
    margin-left: 7px;
    margin-top: -63px;
}



.homec {
    margin-left: 15px;
    margin-top: -63px;
}

</style>

