<template>
<div id="app">
  <div class="grid-container">
    <Header />
    <RetrieveClipboard />
    <CreateClipboard />
    <Footer />
  </div>
</div>
</template>

<script>
import Header from "./components/Header.vue";
import RetrieveClipboard from "./components/RetrieveClipboard.vue";
import CreateClipboard from "./components/CreateClipboard.vue";
import Footer from "./components/Footer.vue";

export default {
  name: "App",
  components: {
    Header,
    RetrieveClipboard,
    CreateClipboard,
    Footer
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Montserrat|Russo+One&display=swap");

/* CSS Reset */
html {
  background-color: #1a1a1a;

  background-image: url(assets/bg-one.svg), url(assets/bg-two.svg);
  background-repeat: no-repeat, no-repeat;
  background-size: cover, cover;
  background-position: bottom;

  box-sizing: border-box;
  font-size: 10px;
  height: 100vh;
  width: 100vw;
}

*,
*:before,
*:after {
  box-sizing: inherit;
}

body,
h1,
h2,
h3,
p {
  margin: 0;
  padding: 0;
  font-weight: normal;
}

/* Global */
.grid-container {
  display: grid;
  grid-template-columns: 15vw 30vw 10vw 30vw 15vw;
  grid-template-rows: 20vh 10vh 33vh 27vh 10vh;
}

h1 {
  font-family: "Russo One";
  color: #353535;
  font-weight: 500;
  text-align: left;
  letter-spacing: 0.15em;
}

p {
  font-family: "Montserrat";
  color: #353535;
  font-weight: 600;
  letter-spacing: 0.15em;
}

/* Vertical Grid Layout for Mobile */
@media (max-width: 1500px) {
  html {
    background-image: none, none;
  }

  .grid-container {
    grid-template-columns: 5vw 35vw 20vw 35vw 5vw;
    grid-template-rows: 15vh 5vh 30vh 5vh 30vh 5vh 10vh;
  }
}

/* Grid adjustments for Small Height */
@media (max-height: 500px) {
  .grid-container {
    grid-template-rows: 30vh 10vh 80vh 10vh 80vh 10vh 25vh;
  }
}

@media (min-height: 500px) and (max-height: 600px) {
  .grid-container {
    grid-template-rows: 20vh 5vh 50vh 5vh 50vh 5vh 20vh;
  }
}

/* Small height laptops */
@media (min-width: 1100px) and (max-width: 1500px) and (min-height: 600px) and (max-height: 1000px) {
  .grid-container {
    grid-template-rows: 20vh 5vh 50vh 5vh 50vh 5vh 20vh;
  }
}

/* Font size adjustments */
/* Smartphones */
@media (max-width: 500px) {
  html {
    font-size: 5px;
  }
}

/* Tablets */
@media (min-width: 500px) and (max-width: 1100px) {
  html {
    font-size: 7px;
  }

  .grid-container {
    grid-template-columns: 15vw 25vw 20vw 25vw 15vw;
  }
}

/* Laptops */
@media (min-width: 1100px) and (max-width: 1500px) {
  html {
    font-size: 8px;
  }

  .grid-container {
    grid-template-columns: 15vw 25vw 20vw 25vw 15vw;
  }
}

/* Desktop */
@media (min-width: 1500px) and (max-width: 2000px) {
  html {
    font-size: 8px;
  }
}
</style>
