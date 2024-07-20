<template>
<v-list lines="one">
  <v-list-item
    v-for="n in tasks"
    :key="n._id"
    :title="n.name"
    :subtitle="n.description"
  ></v-list-item>
</v-list>
</template>

<script setup lang="ts">
  import axios from 'axios';
  import {ref, onBeforeMount} from 'vue';

  const tasks = ref([])

  onBeforeMount( async () => {
    const data = await axios.get("http://0.0.0.0:8000/task/get_tasks");
    console.log(data.data)
    tasks.value = data.data
  }
  )
  
</script>
