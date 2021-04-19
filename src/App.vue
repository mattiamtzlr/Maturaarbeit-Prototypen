<template>
  <h1>Hello {{name}}</h1>
</template>

<script>

export default {
  name: 'App',
  components: {},
  setup() {
    return {
      name: "Mattia",
    }
  }
}
</script>

<style>
#app {
  font-family: monospace;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #386088;
  margin-top: 60px;
}
h1 {
  font-size: 3em;
}
</style>
