<template>
  <div class="">
    <div class="mx-auto md:mt-2">
      <div class="md:flex">
        <!-- Left Side -->
        <div class="w-full md:w-4/12 lg:w-3/12">
          <!-- Profile Card -->
          <div class="bg-white shadow overflow-hidden sm:rounded-md">
            <div class="image overflow-hidden text-center">
              <img
                :src="getURL()"
                alt="User avatar"
                class="object-cover inline-block w-48 h-48 rounded-lg mx-auto my-6"
                @error="imageError = true"
              />
            </div>
            <h1 class="text-gray-900 font-bold text-xl leading-8 m-2">
              {{ authStore.firstName }} {{ authStore.lastName }}
            </h1>
            <h3 class="text-gray-600 font-lg text-semibold leading-6 m-2">
              Owner at Her Company Inc.
            </h3>
            <p class="text-sm text-gray-500 hover:text-gray-600 leading-6 m-2">
              Lorem ipsum dolor sit amet consectetur adipisicing elit.
              Reprehenderit, eligendi dolorum sequi illum qui unde aspernatur
              non deserunt
            </p>
            <ul
              class="bg-gray-100 text-gray-600 hover:text-gray-700 hover:shadow px-3 mt-3 divide-y rounded shadow-sm"
            >
              <!-- <li class="flex items-center py-3">
                <span> {{ $t('twoFactorAuthentication') }}</span>
                <span class="ml-auto"
                  ><span
                    class="bg-green-500 py-1 px-2 rounded text-white text-sm"
                    >Active</span
                  ></span
                >
              </li> -->
              <li class="flex items-center py-3">
                <span>Member since</span>
                <span class="ml-auto">Nov 07, 2016</span>
              </li>
            </ul>
          </div>
          <!-- End of profile card -->
          <div class="my-4"></div>
        </div>
        <!-- Right Side -->
        <div class="w-full md:w-9/12 md:mx-2 mb-16">
          <!-- Profile tab -->

          <div class="bg-white shadow overflow-hidden sm:rounded-md py-5 px-2">
            <div
              class="flex items-center space-x-2 font-semibold text-gray-900 leading-8"
            >
              <span clas="text-green-500">
                <svg
                  class="h-5"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                  />
                </svg>
              </span>
              <span class="tracking-wide"> {{ $t('profile.titleData') }}</span>
            </div>
            <div v-show="!editShow" class="text-gray-700 mt-4">
              <div class="grid md:grid-cols-2 text-sm">
                <div class="grid grid-cols-2">
                  <p class="px-4 py-2 font-semibold">
                    {{ $t('profile.firstName') }}:
                  </p>
                  <p class="px-4 py-2">{{ authStore.firstName }}</p>
                </div>
                <div class="grid grid-cols-2">
                  <p class="px-4 py-2 font-semibold">
                    {{ $t('profile.lastName') }}:
                  </p>
                  <p class="px-4 py-2">{{ authStore.lastName }}</p>
                </div>
                <div class="grid grid-cols-2">
                  <p class="px-4 py-2 font-semibold">Email:</p>
                  <p class="px-4 py-2">{{ authStore.email }}</p>
                </div>
                <div class="grid grid-cols-2">
                  <p class="px-4 py-2 font-semibold">
                    {{ $t('profile.phoneNumber') }}:
                  </p>
                  <p class="px-4 py-2">{{ authStore.phoneNumber }}</p>
                </div>
              </div>
            </div>
            <UserProfileEdit v-show="editShow" />
            <div class="flex justify-center">
              <button
                class="lg:w-1/5 w-2/3 text-blue-800 text-sm border border-blue-300 font-semibold rounded-lg hover:bg-gray-100 focus:outline-none focus:shadow-outline focus:bg-gray-100 hover:shadow-xs p-1 my-4"
                @click.prevent="doShow"
              >
                Edit Information
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref } from 'vue';
import defaultImage from '@/assets/images/defaultAvatar.jpeg';
import { useAuthStore } from '@/store/Auth';
import UserProfileEdit from '../components/UserProfileEdit.vue';
// import { useI18n } from 'vue-i18n';

// const { t } = useI18n();
const authStore = useAuthStore();

const editShow = ref(false);

const doShow = () => {
  editShow.value = !editShow.value;
};
const imageError = ref(false);
const getURL = () => {
  return imageError.value ? defaultImage : authStore.profilePic;
};
</script>

<style></style>
