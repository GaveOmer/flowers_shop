<template>
  <h1 class="text-white border px-3.5 bg-black">{{ count }}</h1>
  <button class='border px-2 bg-fuchsia-500 text-white'  @click="inc"> +1</button>
  <button class="text-white border px-2 bg-red-500" @click="dec"> - 1</button>
</template>

<script>
  export default {
    data() {
      return {
        count: 0
      }
    },
    methods: {
      inc() { this.count++ },
      dec() { this.count-- }
    }  
  }
</script>