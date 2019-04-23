<template>
  <div>
    <h1>Home page</h1>
    <p v-if="username">{{ username }}</p>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data: () => {
    return { username: ''}
  }
}
</script>
