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

      <div
        class="column is-3" 
        v-for="product in products"
        v-bind:key="product.id">
        <div class="box">
          <figure class="image mb-4">
            <img :src="product.get_thumbnail">
          </figure>

          <h3 class="is-size-4">{{ product.name }}</h3>
          <h4 class="is-size-5">{{ product.manufacturer }}</h4>
          <p class = "is-size-6 has-text-grey">€{{ product.price }}</p>

          <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">Details</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
export default {
  name: 'HomeView',
  data(){
    return {
      products: []
    }
  },
  components: {
    
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

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>