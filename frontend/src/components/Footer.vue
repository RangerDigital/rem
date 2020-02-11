<template>
<div class="component-container">
  <a href="https://github.com/RangerDigital/rem">GitHub</a>
  <a href="https://bednarski.dev">Copyright © Jakub Bednarski 2020</a>
</div>
</template>

<script>
export default {
  name: "Footer"
};
</script>

<style scoped>
.component-container {
  grid-row: 5 / 5;
  grid-column: 4 / 4;

  display: flex;
  align-items: center;
  justify-content: space-evenly;
}

a {
  color: #f8f8f8;
  font-size: 1.5rem;
  font-weight: 600;
  font-family: "Montserrat";
  letter-spacing: 0.07em;
  text-decoration-line: none;

  transition: all 0.05s ease-in-out;
}

a:hover {
  color: #4093ff;
  transform: scale(1.05);
}

@media (max-width: 1500px) {
  .component-container {
    grid-row: 7 / 7;
    grid-column: 2 / 5;
  }
}
</style>
