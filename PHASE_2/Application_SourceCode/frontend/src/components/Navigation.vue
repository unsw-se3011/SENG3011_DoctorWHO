<template>
  <div>
    <nav class="navbar is-light">
      <div class="navbar-menu">
        <div class="navbar-start">
          <a class="navbar-item">
            <router-link to="/">Home</router-link>
          </a>
          <a class="navbar-item">
            <router-link to="/search">Search</router-link>
          </a>
          <a class="navbar-item">
            <router-link to="/graphs">Graphs</router-link>
          </a>
          <a class="navbar-item">
            <router-link to="/news">News</router-link>
          </a>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'Navigation'
}
</script>
