<template>
  <div class="shadow overflow-hidden sm:rounded-md">
    <div class="px-4 py-5 bg-white sm:p-6">
      <div class="flex justify-center items-center">
        <div
          class="flex justify-center items-center border-2 p-20 border-gray-300 border-dashed rounded-md h-64 w-auto"
        >
          <div class="text-center">
            <img
              v-if="imgSrc"
              :src="imgSrc"
              alt="User avatar"
              class="object-cover inline-block w-48 h-48 rounded-lg"
            />
            <svg
              v-else
              class="mx-auto h-12 w-12 text-gray-400"
              stroke="currentColor"
              fill="none"
              viewBox="0 0 48 48"
              aria-hidden="true"
            >
              <path
                d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>

            <p v-if="selectedPicture">
              {{ selectedPicture.name }}
            </p>
            <div v-else class="text-sm text-gray-600">
              <label
                for="picture"
                class="relative bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500 flex justify-center items-center"
              >
                <input
                  id="picture"
                  :accept="acceptedFileType"
                  name="picture"
                  type="file"
                  class="dropbox md:h-[256px] md:w-[317px] h-[253px] w-[253px] absolute opacity-0 md:mb-2 cursor-pointer"
                  @change="(e) => fileChange(e)"
                />
                <span>{{ t('profile.avatar.upload') }}</span>
              </label>
              <p class="pl-1">{{ t('profile.avatar.dragDrop') }}</p>
              <p class="text-xs text-gray-500">PNG, JPG, GIF</p>
            </div>
          </div>
        </div>
        <div v-if="imgSrc" class="flex flex-col justify-end items-center mt-3">
          <button
            class="inline-flex justify-center ml-4 py-1 px-2 border border-transparent shadow-sm text-sm font-medium rounded-lg text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            @click.prevent="doEdit"
            type="button"
          >
            {{ t('profile.editForm.submitButton') }}
          </button>
          <button
            class="inline-flex justify-center ml-4 mt-2 py-1 px-2 border border-transparent shadow-sm text-sm font-medium rounded-lg text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            @click.prevent="doDiscard"
            type="button"
          >
            {{ t('profile.editForm.discardButton') }}
          </button>
        </div>
      </div>
      <div
        class="base-image-input"
        :style="{ 'background-image': `url(${imgSrc})` }"
      ></div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { updatePictuer } from '@/services/auth.js';
import { useAuthStore } from '@/store/Auth';
import { useI18n } from 'vue-i18n';
const authStore = useAuthStore();
const { t } = useI18n();

const props = defineProps({
  mode: {
    type: String,
    default: 'jpeg',
  },
  acceptedFileType: {
    type: String,
    default: 'image/jpeg',
  },
});

const acceptedFileTypeMatches = (fileType) => {
  return props.acceptedFileType.split(',').includes(fileType);
};

const MAX_SIZE = import.meta.VUE_APP_MAX_IMAGE_UPLOAD * 2048 * 2048;
const IMAGE_MODE = 'image';

const selectedPicture = ref(null);
const imgSrc = ref(null);
const fileChange = (e) => {
  if (!e.target.files?.[0]) {
    return;
  }

  const file = e.target.files[0];
  if (!acceptedFileTypeMatches(file.type)) {
    // this.error = this.$t('upload.typeError_' + this.mode);
    // startErrorScheduler();
    e.target.value = '';
    return;
  } else if (props.mode === IMAGE_MODE && file.size > MAX_SIZE) {
    // error = this.$t('upload.sizeError_' + this.mode);
    // startErrorScheduler();
    e.target.value = '';
    return;
  }
  const reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onload = () => (imgSrc.value = reader.result);
  selectedPicture.value = file;
};
const errorMessage = ref('');
const id = ref(authStore.id);
const doEdit = async () => {
  try {
    const response = await updatePictuer(id.value, selectedPicture.value);
    if (response.status === 204) {
      ('success');
      return;
    }
    authStore.setPictureUrl(response.profilePic);
    errorMessage.value = '';
  } catch (e) {
    errorMessage.value = t('profile.editForm.error');
  }
  selectedPicture.value = '';
  imgSrc.value = '';
};

const doDiscard = () => {
  const con = confirm(t('profile.editForm.discardMessage'));
  if (con) {
    imgSrc.value = null;
    selectedPicture.value = null;
  }
};
</script>

<style></style>
