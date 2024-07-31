import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/Login.vue'
import Notes from '../components/Notes.vue'

const routes = [
  { path: '/', component: Login },
  { path: '/notes', component: Notes }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
