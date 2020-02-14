import Vue from "vue";
import App from "./App.vue";
import Axios from "axios";

import * as Sentry from '@sentry/browser';
import * as Integrations from '@sentry/integrations';

Sentry.init({
  dsn: 'https://a9278d6a545c473b98af38c9da4cca33@sentry.io/2501473',
  integrations: [new Integrations.Vue({Vue, attachProps: true})],
});

Vue.prototype.$http = Axios;
Vue.config.productionTip = false;


new Vue({
  render: h => h(App)
}).$mount("#app");
