<template>
  <div>
    <div class="md:grid md:grid-cols-2 md:gap-6">
      <div class="md:col-span-1 m-5">
        <div class="px-4 sm:px-0">
          <h3 class="text-lg font-medium leading-6 text-gray-900">
            {{ $t('profile.title') }}
          </h3>

          <p class="mt-1 text-sm text-gray-600">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Natus
            deserunt rerum tenetur sit voluptatibus nihil quos consequuntur,
            alias ipsa vitae quas laudantium vero eius voluptates earum
            assumenda temporibus sed accusantium libero provident vel optio
            explicabo sint? Animi minus expedita iure omnis sapiente? Aliquam
            cumque ratione ea quo incidunt deleniti temporibus assumenda
            blanditiis, delectus nostrum in voluptates vel numquam quibusdam
            fugit rerum, architecto cum doloribus quod quia harum ullam,
            distinctio itaque mollitia! Accusantium magnam porro assumenda.
            Commodi asperiores, mollitia tenetur velit non rerum, veritatis
            omnis quibusdam dolorum iusto modi. Labore, repudiandae.
          </p>
        </div>
      </div>
      <div class="mt-5 md:mt-0 md:col-span-1">
        <form>
          <div class="shadow sm:rounded-md sm:overflow-hidden">
            <div class="px-4 py-5 bg-white space-y-6 sm:p-6">
              <UserAvatarForm />
              <user-info-form
                v-model:firstName="firstName"
                v-model:lastName="lastName"
                v-model:phoneNumber="phoneNumber"
              />
              <TowFactorAuthentication />
              <div class="px-4 py-3 bg-gray-50 text-right sm:px-2">
                <button
                  class="inline-flex justify-center mr-4 py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-lg text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                  @click.prevent="doEdit"
                >
                  Save
                </button>
                <button
                  class="inline-flex justify-center mr-4 py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-lg text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                  @click.prevent="doDiscard"
                >
                  Cancle
                </button>
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { update } from '@/services/auth.js';
import UserInfoForm from './UserInfoForm.vue';
import UserAvatarForm from './UserAvatarForm.vue';
import TowFactorAuthentication from './TowFactorAuthentication.vue';
import { useAuthStore } from '@/store/Auth';
import { useI18n } from 'vue-i18n';

const { t } = useI18n();
const authStore = useAuthStore();

const id = ref(authStore.id);
const firstName = ref(authStore.firstName);
const lastName = ref(authStore.lastName);
const phoneNumber = ref(authStore.phoneNumber);

const errorMessage = ref('');

const doEdit = async () => {
  try {
    const response = await update(
      id.value,
      firstName.value,
      lastName.value,
      phoneNumber.value
    );
    if (response.status === 204) {
      ('success');
      return;
    }
    authStore.setPhoneNumber(response.phoneNumber);
    authStore.setUserName({
      firstName: response.firstName,
      lastName: response.lastName,
    });
    errorMessage.value = '';
  } catch (e) {
    errorMessage.value = t('profile.editForm.error');
  }
};

const doDiscard = () => {
  const con = confirm(t('profile.editForm.discardMessage'));
  if (!con) {
    return;
  }
};
</script>

<style></style>
