<template>
  <div class="shadow overflow-hidden sm:rounded-md">
    <div class="px-4 py-5 bg-white sm:p-6">
      <div class="grid grid-cols-6 gap-6">
        <div class="col-span-6 sm:col-span-3">
          <label
            for="first-name"
            class="block text-sm font-medium text-gray-700"
            >{{ $t('profile.editForm.firstName') }}</label
          >
          <input
            id="first-name"
            type="text"
            :value="firstName"
            @input="$emit('update:firstName', $event.target.value)"
            name="first-name"
            autocomplete="given-name"
            class="mt-1 py-1 px-3 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-2 border-gray-300 rounded-md"
          />
        </div>

        <div class="col-span-6 sm:col-span-3">
          <label
            for="last-name"
            class="block text-sm font-medium text-gray-700"
            >{{ $t('profile.editForm.lastName') }}</label
          >
          <input
            id="last-name"
            type="text"
            :value="lastName"
            @input="$emit('update:lastName', $event.target.value)"
            name="last-name"
            autocomplete="family-name"
            class="mt-1 py-1 px-3 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-2 border-gray-300 rounded-md"
          />
        </div>

        <div class="col-span-6 sm:col-span-3">
          <label for="country" class="block text-sm font-medium text-gray-700"
            >Country</label
          >
          <select
            id="country"
            name="country"
            autocomplete="country-name"
            class="mt-1 block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
          >
            <option>Switzerland</option>
            <option>Germany</option>
            <option>United States</option>
            <option>Canada</option>
          </select>
        </div>

        <div class="col-span-6 sm:col-span-3">
          <label
            for="phone-number"
            class="block text-sm font-medium text-gray-700"
            >{{ $t('profile.editForm.phoneNumber') }}</label
          >
          <input
            id="phone-number"
            type="text"
            :value="phoneNumber"
            @input="$emit('update:phoneNumber', $event.target.value)"
            name="phone-number"
            class="mt-1 py-1 px-3 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-2 border-gray-300 rounded-md"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  firstName: {
    type: String,
    required: true,
  },
  lastName: {
    type: String,
    required: true,
  },
  phoneNumber: {
    type: String,
    required: true,
  },
});

defineEmits(['update:firstName', 'update:lastName', 'update:phoneNumber']);
</script>

<style></style>
