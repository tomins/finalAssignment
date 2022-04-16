<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">Welcome to Final Assignment</p>
        <p class="subtitle"> An online clothes store with 2 categories, summer and winter</p>
      </div>
    </section>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered"> Avaliable Products</h2>
      </div>

      <ProductBox 
        v-for="product in products"
        v-bind:key="product.id"
        v-bind:product="product" />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import ProductBox from '@/components/ProductBox.vue'
export default {
  name: 'HomeView',
  data(){
    return {
      products: []
    }
  },
  components: {
    ProductBox
  },
  mounted(){
    this.getProducts()
  },
  methods:{
    async getProducts(){
      axios
        .get('/api/v1/products/')
        .then(response => {
          this.products = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

