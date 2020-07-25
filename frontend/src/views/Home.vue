<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <draw/>
  </div>
</template>

<script>
// @ is an alias to /src
import draw from '@/components/draw.vue'

export default {
  name: 'Home',
  components: {
    draw
  }
}
</script>
