<template>
  <div id="wrapper">
    <nav>
      <div>
        <router-link to="/"><strong>moviePJT</strong></router-link>
    <!-- 메뉴 -->
        <a href="">
          <span></span>
          <span></span>
          <span></span>
        </a>
      </div>
      <div>
        <div>
          <router-link to="/summer">Summer</router-link>
          <router-link to="/winter">Winter</router-link>
          <div>
            <div>
             <router-link to="/winter">Login</router-link>
              <router-link to="/winter">
              <span>
                cart</span></router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <section>
      <router-view/>
    </section>
    <footer>
      <p>Copyright (c) 2022</p>
    </footer>
  </div>
</template>

<script>
export default {
  data(){
    return{
     
    }
  }
}
</script>

<style>
</style>
