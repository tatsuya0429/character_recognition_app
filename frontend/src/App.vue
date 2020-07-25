<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <h1>Character Recognition Demo</h1>
      </div>
    </v-app-bar>

    <v-content>
      <draw/>
    </v-content>
  </v-app>
</template>

<script>
import draw from './components/draw';

export default {
  name: 'App',

  components: {
    draw,
  },

  data: () => ({
    //
  }),
};
</script>
