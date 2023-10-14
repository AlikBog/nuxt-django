// https://nuxt.com/docs/api/configuration/nuxt-config
import vuetify from "vite-plugin-vuetify"

export default defineNuxtConfig({
  modules:[
    '@pinia/nuxt',
    async (options, nuxt) => {
      nuxt.hooks.hook('vite:extendConfig', (config) => config.plugins.push(vuetify()))
    }
  ],
  build:{transpile:['vuetify']},
  vite: {ssr: {noExternal: ['vuetify']}},
  imports:{
    dirs:['./stores'] 
  },
  pinia: {
    autoImports: ['defineStore', 'mapeStores', 'acceptHMRUpdate'],
  }
})
