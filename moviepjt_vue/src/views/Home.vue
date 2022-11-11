<template>
  <div class="home">
   HOME
   <div v-for="product in latestProducts"
   v-bind:key="product.id">
    <div>
      <img v-bind:src="product.get_thumbnail">
      <h3>{{product.name}}</h3>
      <p>{{product.price}}</p>

      view details

    </div>
   </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {
  }
}
</script>
