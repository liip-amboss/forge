<template>
  <form class="shadow overflow-hidden sm:rounded-md">
    <div class="px-4 py-5 bg-white sm:p-6 h-full">
      <div class="grid grid-cols-6 gap-6">
        <div class="col-span-6 sm:col-span-3">
          <LabelField
            :label="$t('profile.firstName')"
            is-block
            class="block text-sm font-medium text-gray-700"
          >
            <input
              v-model.trim="v$.firstName.$model"
              class="mt-1 py-1 px-3 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm text-sm border-2 border-gray-300 rounded-md"
              @blur="v$.firstName.$touch"
            />
          </LabelField>
        </div>

        <div class="col-span-6 sm:col-span-3">
          <LabelField
            :label="$t('profile.lastName')"
            is-block
            class="block text-sm font-medium text-gray-700"
          >
            <input
              v-model.trim="v$.lastName.$model"
              class="mt-1 py-1 px-3 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm text-sm border-2 border-gray-300 rounded-md"
              @blur="v$.lastName.$touch"
            />
          </LabelField>
        </div>

        <div class="col-span-6 sm:col-span-3">
          <label
            for="phone-number"
            class="block text-sm font-medium text-gray-700"
            >{{ $t('profile.phoneNumber') }}</label
          >
          <vue-tel-input
            :value="v$.phoneNumber.$model"
            mode="international"
            class="telephone-input"
            @input="onInput"
            @blur="v$.phoneNumber.$touch"
          ></vue-tel-input>
          {{ errorMessage }}
        </div>
      </div>
      <div
        v-show="editButtonShow"
        class="py-3 bg-gray-50 text-right mt-2 sm:px-2"
      >
        <button
          class="inline-flex justify-center mr-4 py-1 px-2 border border-transparent shadow-sm text-sm font-medium rounded-lg text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          @click.prevent="doEdit"
        >
          {{ t('profile.editForm.submitButton') }}
        </button>
        <button
          class="inline-flex justify-center py-1 px-2 border border-transparent shadow-sm text-sm font-medium rounded-lg text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          @click.prevent="doDiscard"
        >
          {{ t('profile.editForm.discardButton') }}
        </button>
      </div>
    </div>
  </form>
</template>

<script setup>
import { ref, computed, watch } from 'vue';

import { update } from '@/services/auth.js';
import { useAuthStore } from '@/store/Auth';
import { useI18n } from 'vue-i18n';
import { VueTelInput } from 'vue3-tel-input';
import 'vue3-tel-input/dist/vue3-tel-input.css';
import LabelField from '@/components/LabelField.vue';
import useVuelidate from '@vuelidate/core';

const { t } = useI18n();
const authStore = useAuthStore();

const state = ref({
  id: authStore.id,
  firstName: authStore.firstName,
  lastName: authStore.lastName,
  phoneNumber: authStore.phoneNumber,
});

const store = ref({
  id: authStore.id,
  firstName: authStore.firstName,
  lastName: authStore.lastName,
  phoneNumber: authStore.phoneNumber,
});

const editButtonShow = ref(false);

watch(
  () => state.value,
  (currentValue) => {
    if (
      currentValue.firstName != store.value.firstName ||
      currentValue.lastName != store.value.lastName ||
      currentValue.phoneNumber != store.value.phoneNumber
    ) {
      editButtonShow.value = true;
      console.log(editButtonShow.value);
      console.log(currentValue);
      console.log(store.value.firstName);
      console.log(authStore.firstName);
    }
    // if (
    //   state.value.firstName == '' ||
    //   state.value.lastName == '' ||
    //   state.value.phoneNumber == ''
    // ) {
    //   editButtonShow.value = false;
    // }
    else {
      editButtonShow.value = false;
      console.log(currentValue);
      console.log(editButtonShow.value);
    }
    console.log('===========================');
    console.log(store.value.firstName);
    console.log(state.value.firstName);
    console.log(authStore.firstName);
  },
  { deep: true }
);
const errorMessage = ref('');

const rules = computed(() => ({
  firstName: {},
  lastName: {},
  phoneNumber: {},
}));

const onInput = (_, phoneObject) => {
  if (phoneObject?.number) {
    state.value.phoneNumber = phoneObject.number;
  }
};
const v$ = useVuelidate(rules, state);

const doEdit = async () => {
  try {
    const response = await update(
      state.value.id,
      state.value.firstName,
      state.value.lastName,
      state.value.phoneNumber
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
    editButtonShow.value = false;
  } catch (e) {
    errorMessage.value = t('profile.editForm.error');
    editButtonShow.value = true;
  }
};

const doDiscard = () => {
  const con = confirm(t('profile.editForm.discardMessage'));
  if (con) {
    state.value = store.value;
    console.log(editButtonShow.value);
  } else {
    return;
  }
};
</script>

<style lang="postcss">
.telephone-input.vue-tel-input:focus-within {
  box-shadow: none;
}
.telephone-input.vue-tel-input {
  width: 100%;
  border: solid #e2e8f0;
  border-width: 1px;
  font-size: 0.875rem;
  color: rgb(74 85 104);
  display: flex;
  justify-content: space-between;
}
.telephone-input.vue-tel-input input::placeholder {
  overflow: hidden;
  color: transparent;
  display: none;
}
.telephone-input input {
  padding: 5px 0;
}
.telephone-input input:focus-within {
  border: 2px solid rgba(39, 93, 197);
}

.telephone-input div.open .vti__dropdown-list.below {
  top: 0;
}
.telephone-input div.open ul {
  margin-top: 10px;
  position: relative;
  height: 100px;
  width: 100%;
  padding-right: 0.75rem;
}
</style>
