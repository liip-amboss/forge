<template>
  <nav
    class="relative flex flex-wrap items-center justify-between py-1 bg-black"
  >
    <div
      class="container mx-auto flex flex-wrap items-center justify-between w-full"
    >
      <div
        class="w-full relative flex justify-between lg:w-auto lg:static lg:block lg:justify-start"
      >
        <Router-link
          class="text-sm font-bold leading-relaxed inline-block mr-4 py-2 whitespace-nowrap uppercase text-white"
          to="/"
        >
          <logo-path class="app-logo" />
        </Router-link>
        <button
          class="text-white cursor-pointer text-xl leading-none px-3 py-1 border border-solid border-transparent rounded bg-transparent block lg:hidden outline-none focus:outline-none"
          type="button"
          @click="toggleNavbar"
        >
          <svg
            class="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"
            ></path>
          </svg>
        </button>
      </div>
      <div
        :class="{ hidden: !showMenu, flex: showMenu }"
        class="lg:flex lg:flex-grow items-center"
      >
        <ul
          class="flex flex-col lg:flex-row list-none ml-auto items-start mt-8 lg:mt-0"
        >
          <li class="nav-item">
            <Router-link
              class="px-5 py-3 flex items-center text-sm uppercase font-bold leading-snug text-white no-underline"
              to="/dashboard"
            >
              <svgIcon
                class="inline-block w-10 h-10 mr-2 svg-icon--lg"
                name="home"
              />
              Home
            </Router-link>
          </li>
          <li class="nav-item">
            <Router-link
              class="no-underline px-5 py-3 flex items-center text-sm uppercase font-bold leading-snug text-white"
              :to="{ name: 'profile' }"
            >
              <svgIcon
                class="inline-block w-10 h-10 mr-2 svg-icon--lg"
                name="settings-user"
              />
              {{ name }}
            </Router-link>
          </li>
          <li class="nav-item">
            <button
              v-if="authStore.isLoggedIn"
              class="rounded-md px-1 py-1 flex items-center text-sm uppercase font-bold leading-snug bg-white rounded-lg ml-5 my-2 lg:mb-0"
              @click="logout"
            >
              <svgIcon
                class="inline-block w-10 h-10 mr-1 svg-icon--lg"
                name="logout-2"
              />
              {{ $t('general.logout') }}
            </button>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import SvgIcon from '@/components/SvgIcon.vue';
import logoPath from '@/assets/images/logo.svg';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/store/Auth';
import { computed, ref } from 'vue';

let showMenu = ref(false);
const authStore = useAuthStore();
const router = useRouter();

const name = computed(() => `${authStore.firstName} ${authStore.lastName}`);

function toggleNavbar() {
  showMenu.value = !showMenu.value;
}

const logout = () => {
  authStore.removeAuth();
  router.push({ name: 'login' });
};
</script>
