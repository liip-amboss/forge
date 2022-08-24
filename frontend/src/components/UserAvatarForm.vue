<template>
  <div class="shadow overflow-hidden sm:rounded-md">
    <div class="px-4 py-5 bg-white sm:p-6">
      <div>
        <label class="block text-sm font-medium text-gray-700"> Photo </label>
        <div class="mt-1 flex items-center">
          <span
            class="inline-block h-32 w-32 rounded-full overflow-hidden bg-gray-100"
          >
            <img
              :src="getURL()"
              alt="User avatar"
              class="object-cover inline-block w-32 h-32 rounded-full"
              @error="imageError = true"
            />
          </span>
          <button
            class="ml-5 bg-indigo-200 py-1 px-2 border border-gray-300 rounded-lg shadow-sm text-sm leading-4 font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            @click.prevent="doEdit"
            type="button"
          >
            Change
          </button>
        </div>
      </div>
      <div>
        <div
          class="mt-4 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-md"
        >
          <div class="space-y-1 text-center">
            <img
              v-if="imgSrc"
              :src="imgSrc"
              alt="User avatar"
              class="object-cover inline-block w-20 h-20 rounded-lg"
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
            <div v-else class="flex text-sm text-gray-600">
              <label
                for="picture"
                class="relative cursor-pointer bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500"
              >
                <span>{{ t('profile.avatar.upload') }}</span>
                <input
                  id="picture"
                  :accept="acceptedFileType"
                  name="picture"
                  type="file"
                  class="sr-only"
                  @change="(e) => fileChange(e)"
                />
              </label>
              <p class="pl-1">{{ t('profile.avatar.dragDrop') }}</p>
            </div>
            <p class="text-xs text-gray-500">PNG, JPG, GIF</p>
          </div>
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
import defaultImage from '@/assets/images/defaultAvatar.jpeg';
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

const imageError = ref(false);
const getURL = () => {
  return imageError.value ? defaultImage : authStore.profilePic;
};

const acceptedFileTypeMatches = (fileType) => {
  return props.acceptedFileType.split(',').includes(fileType);
};

const MAX_SIZE = import.meta.VUE_APP_MAX_IMAGE_UPLOAD * 1024 * 1024;
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
</script>

<style></style>
