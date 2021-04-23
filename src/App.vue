<template>
  <h1 v-if="loggedIn">Hello {{name}}</h1>
  <input 
    type="text" 
    v-else 
    placeholder="What's your name?"
    v-model="nameInput"
    @keyup.enter="saveName"
  >
</template>

<script>
import {ref, computed} from "vue";

export default {
  name: 'App',
  components: {},
  setup() {
    let hugeNumber = computed(function () {
      return (2234972389427349623856293462834792n * 8104737263472634962734792834n).toString();
    })

    let name = ref(localStorage.getItem("username"));
    // let loggedIn = true;
    let loggedIn = computed(function () {
      return name.value != null;
    })

    let nameInput = ref("");
    
    function saveName() {
      name.value = nameInput.value;
      localStorage.setItem("username", name.value);
    }

    return {
      name: name,
      loggedIn,
      nameInput,
      saveName,
      hugeNumber,
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
::placeholder {
  font-family: monospace;
}
input {
  font-family: monospace;
  font-size: 2em;
  padding: 10px;
}
</style>
