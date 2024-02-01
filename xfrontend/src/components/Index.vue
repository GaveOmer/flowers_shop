<script setup></script>

<template>
	<div>
    <h1>Загруженные данные</h1>
    <div v-if="loading">Загрузка...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else>
      <ul class="">
        <li v-for="item in data" :key="item.slug">
          {{ item.name }}
          <img :src="imageUrl" alt="Описание изображения">
        </li>
      </ul>
      <pre>{{ data }}</pre>
    </div>
  </div>
</template>

<style scoped></style>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      data: null,
      loading: true,
      error: null,
    };
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/api/products/')
      .then(response => {
        this.data = response.data;
      })
      .catch(error => {
        console.error("Ошибка при получении данных: ", error);
        this.error = 'Произошла ошибка при загрузке данных';
      })
      .finally(() => {
        this.loading = false;
      });
  }
};
</script>