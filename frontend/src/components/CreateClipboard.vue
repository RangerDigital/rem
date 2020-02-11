<template>
<div class="component-container">
  <div class="text-field">
    <h1>CREATE</h1>
    <p>Creates share from your clipboard content.</p>
  </div>

  <div class="output-field">
    <p v-bind:class="{'error-text': errorState}">{{ shareMessage }}</p>
    <h1 class="output-code" v-bind:style="{ opacity: shareOpacity + '%' }" v-bind:class="{'error-text': errorState}">{{ shareCode }}</h1>
  </div>

  <button v-bind:class="{'error-background': errorState}" v-on:click="postClipboard"><img class="icon-small" src="../assets/icon-paste.svg" />{{ buttonMessage }}</button>
</div>
</template>

<script>
export default {
  name: "CreateClipboard",
  data() {
    return {
      shareMessage: "Your Share Code",
      shareCode: "_____",
      shareOpacity: 100,
      errorState: false,
      buttonMessage: "CREATE"
    };
  },
  methods: {
    // Send POST to the backend, On error displays a message.
    postClipboard: function() {
      navigator.clipboard.readText()
        .then(text => {
          this.$http.post("http://127.0.0.1:5000/clipboard", {
              clipboard: encodeURIComponent(text)
            })
            .catch(error => {
              this.errorState = true;
              this.shareMessage = "Connection Error!";
              console.log(error);
            })
            .then(response => {
              if (response.status == 200) {
                this.shareCode = response.data.code;
                this.shareMessage = "Your Share Code";
                this.shareOpacity = 100;
                this.errorState = false;
                this.buttonMessage = "RECREATE";
              } else {
                this.shareCode = "_____";
                this.shareMessage = "Empty Clipboard Error!";
                this.errorState = true;
              }
            });
        })
        .catch(error => {
          this.errorState = true;
          this.shareMessage = "Permission Error!";
          console.log(error);
        })
    },

    // Count opacity down every second, reset component after code expires
    opacityAnimation: function() {
      setTimeout(() => {
        if (this.shareOpacity > 0 && this.buttonMessage == "RECREATE") {
          this.shareOpacity -= 1.66;
        } else {
          this.shareCode = "_____";
          this.shareOpacity = 100;
          this.buttonMessage = "CREATE";
        }
        this.opacityAnimation();
      }, 1000);
    },
  },
  created() {
    this.opacityAnimation();
  }
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
  transition: opacity 1s ease-in-out;
  font-size: 8.5rem;
  letter-spacing: 0.25em;
  opacity: 100%;
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

/* Used for POST errors. */
.error-text {
  color: #FF4040 !important;
}

.error-background {
  background-color: #FF4040 !important;
}

@media (max-width: 1500px) {
  .component-container {
    grid-row: 3 / 3;
    grid-column: 2 / 5;
  }
}
</style>
