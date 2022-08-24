import { computed } from 'vue'

export const useModelWrapper = (props, emit) => {
  return computed({
    get: () => props.modelValue,
    set: (value) => emit('update:modelValue', value)
  })
}