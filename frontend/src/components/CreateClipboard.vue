<template>
<div class="component-container">
  <div class="text-field">
    <h1>CREATE</h1>
    <p>Creates share from your clipboard content.</p>
  </div>

  <div class="output-field">
    <p>Your Share Code</p>
    <h1 class="output-code">67422</h1>
  </div>

  <button><img class="icon-small" src="../assets/icon-paste.svg" />CREATE</button>
</div>
</template>

<script>
export default {
  name: "CreateClipboard"
};
</script>

<style scoped>
.component-container {
  grid-row: 3 / 3;
  grid-column: 2 / 2;

  padding: 1em 5em;
  border-radius: 0.7em;
  background-color: #f8f8f8;
  box-shadow: 0 12.5px 10px rgba(0, 0, 0, 0.035), 0 100px 80px rgba(0, 0, 0, 0.07);

  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.output-field {
  height: 14rem;
  width: 80%;
  margin: 0 auto;
}

.output-field p {
  color: #c5c5c5;
  font-size: 1.7rem;
  text-align: center;
  font-weight: 500;
  padding-bottom: 0.5em;
}

.output-code {
  font-size: 8.5rem;
  letter-spacing: 0.25em;
  text-align: center;
}

h1 {
  font-size: 3.5rem;
}

p {
  margin-top: 0.7em;
  font-size: 2rem;
}

button {
  width: 38%;
  height: 4em;
  margin: 0 auto;
  display: block;

  font-size: 1.5rem;
  color: #ffffff;
  font-family: "Russo One";
  font-weight: 500;
  text-align: center;
  line-height: 4em;
  letter-spacing: 0.25em;

  background-color: #4093ff;
  border: none;
  outline: none;
  border-radius: 0.5em;

  box-shadow: 0 12.5px 10px rgba(0, 0, 0, 0.035), 0 100px 80px rgba(0, 0, 0, 0.07);
  transition: all 0.03s ease-in-out;
}

button:hover {
  background-color: #2E80EA;
}

button:active {
  background-color: #2E80EA;
  transform: scale(0.98);
}

.icon-small {
  width: 3em;
  padding-right: 1em;
  vertical-align: middle;
}

@media (max-width: 1500px) {
  .component-container {
    grid-row: 3 / 3;
    grid-column: 2 / 5;
  }
}
</style>
