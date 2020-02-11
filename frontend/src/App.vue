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
  background-color: #2b2b2b;
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

/* Vertical Grid Layout */
@media (max-width: 1500px) {
  .grid-container {
    grid-template-columns: 5vw 35vw 20vw 35vw 5vw;
    grid-template-rows: 15vh 5vh 30vh 5vh 30vh 5vh 10vh;
  }
}

/* Smartphones - Vertical and Keyboard */
@media (max-height: 550px) and (orientation: portrait) {
  html {
    font-size: 3px !important;
  }
}

/* Smartphones - Vertical */
@media (max-width: 500px) and (orientation: portrait) {
  html {
    font-size: 5px;
  }
}

/* Smartphones - Horizontal */
@media (max-width: 750px) and (orientation: landscape) {
  html {
    font-size: 3px;
  }
}

/* Tablets - Vertical */
@media (min-width: 750px) and (max-width: 1100px) and (orientation: portrait) {
  html {
    font-size: 6px;
  }

  .grid-container {
    grid-template-columns: 15vw 25vw 20vw 25vw 15vw;
  }
}

/* Tablets - Horizontal */
@media (min-width: 750px) and (max-width: 1100px) and (orientation: landscape) {
  html {
    font-size: 6px;
  }

  .grid-container {
    grid-template-columns: 15vw 25vw 20vw 25vw 15vw;
  }
}

/* Laptops - Vertical */
@media (min-width: 1100px) and (max-width: 1500px) and (orientation: portrait) {
  html {
    font-size: 7px;
  }

  .grid-container {
    grid-template-columns: 15vw 25vw 20vw 25vw 15vw;
  }
}

/* Laptops - Horizontal */
@media (min-width: 1100px) and (max-width: 1500px) and (orientation: landscape) {
  html {
    font-size: 7px;
  }

  .grid-container {
    grid-template-columns: 20vw 20vw 20vw 20vw 20vw;
  }
}

/* Desktop - Horizontal */
@media (min-width: 1500px) and (max-width: 2000px) and (orientation: landscape) {
  html {
    font-size: 8px;
  }
}
</style>
