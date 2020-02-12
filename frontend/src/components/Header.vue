<template>
<div class="component-container">
  <h1 class="text-header"><span>REM.</span>BEDNARSKI<span>.</span>DEV</h1>
  <p class="text-subheader">Clipboard Sharing Service</p>
</div>
</template>

<script>
export default {
  name: "Header"
};
</script>

<style scoped>
.component-container {
  grid-column: 1 / 6;
  padding: 6em;
}

.text-header {
  font-size: 4rem;
  color: #f8f8f8;
}

.text-subheader {
  color: #f8f8f8;
  font-size: 2rem;
  margin-top: 1em;
}

span {
  color: #4093ff;
}
</style>
