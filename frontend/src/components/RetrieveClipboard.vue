<template>
<div class="component-container">
  <div class="text-field">
    <h1>RETRIEVE</h1>
    <p>Retrieves content to your system clipboard.</p>
  </div>

  <div class="input-field">
    <p v-bind:class="{'error-text': errorState, 'success-text': successState}">{{ shareMessage }}</p>
    <input v-bind:class="{'error-border': errorState, 'success-border': successState}" maxlength="5" onfocus="this.value=''" type="text" inputmode="numeric" autofocus v-model="shareCode" v-on:keyup.enter="getClipboard" />
  </div>

  <button v-bind:class="{'error-background': errorState, 'not-active': !buttonActive}" v-on:click="getClipboard"><img class="icon-small" src="../assets/icon-copy.svg" />{{ buttonMessage }}</button>
</div>
</template>

<script>
export default {
  name: "RetrieveClipboard",
  data() {
    return {
      shareCode: "",
      shareMessage: "Enter Share Code",
      errorState: false,
      successState: false,
      buttonMessage: "RETRIEVE"
    };
  },

  computed: {
    buttonActive: function() {
      if (this.shareCode.length >= 4 || this.successState == true) {
        return true
      } else {
        return false
      }
    }
  },

  methods: {

    getClipboard: function() {
      this.$http.get("http://127.0.0.1:5000/clipboard/" + this.shareCode)
        .then(response => {
          if (response.status == 200) {
            navigator.clipboard.writeText(decodeURIComponent(response.data.clipboard))
              .then(() => {
                this.buttonMessage = "SUCCESS";
                this.successState = true;
                this.shareMessage = "Success, clipboard copied!";
                this.shareCode = "";
                this.errorState = false;
              })
              .catch(() => {
                this.errorState = true;
                this.successState = false;
                this.buttonMessage = "RETRY";
                this.shareMessage = "Clipboard API Error!";
              });
          }
        })
        .catch(error => {
          this.successState = false;
          if (error.response.status == 400) {
            this.errorState = true;
            this.buttonMessage = "RETRY";
            this.shareMessage = "Invalid Share Code!";
          } else {
            this.errorState = true;
            this.shareMessage = "Connection Error!";
            console.log(error);
          };
        })

    }
  },
};
</script>

<style scoped>
.component-container {
  grid-row: 3 / 3;
  grid-column: 4 /4;

  padding: 1em 5em;
  border-radius: 0.7em;
  background-color: #f8f8f8;
  box-shadow: 3px 3px 3px 3px rgba(0, 0, 0, 0.045);

  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.input-field {
  width: 80%;
  margin: 0 auto;
}

.input-field p {
  color: #c5c5c5;
  font-size: 1.7rem;
  font-weight: 500;
  padding-bottom: 0.5em;
}

.input-field input {
  width: 100%;
  height: 1.5em;

  outline: none;
  border-radius: 0.15em;
  background-color: #eeeeee;
  border: 0.04em solid #c5c5c5;

  font-size: 5rem;
  color: #353535;
  font-family: "Russo One";
  font-weight: 500;
  text-align: center;
  letter-spacing: 0.25em;
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

  box-shadow: 3px 3px 3px 3px rgba(0, 0, 0, 0.045);
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

.success-text {
  color: #4093FF !important;
}

.success-border {
  border: 0.04em solid #4093FF !important;
  color: #4093FF !important;
}

.not-active {
  background-color: #C5C5C5 !important;
}

/* Used for POST errors. */
.error-text {
  color: #FF4040 !important;
}

.error-border {
  border: 0.04em solid #FF4040 !important;
  color: #FF4040 !important;
}

.error-background {
  background-color: #FF4040 !important;
}

@media (max-width: 1500px) {
  .component-container {
    grid-row: 5 / 5;
    grid-column: 2 / 5;
  }
}
</style>
