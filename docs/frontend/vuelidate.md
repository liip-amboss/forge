# Vuelidate

We use vuelidate which we set up in the main.js by importing it and then calling `vue.use(Vuelidate)` .
This allows us to use it anywhere in the app by using a validation object in the vue component,
this can look like this:
```HTML
 <p v-if="!$v.formResponses.name.required" class="mb-2 text-red-500">name is required</p>
  <forge-input
    v-model="formResponses.name"
    :value="input"
    placeholder="Max"
    label="First name"
    is-block
  />
```
```javascript
import { required, minLength } from 'vuelidate/lib/validators';
export default {
  components: {
   ...
  },
  data() {
    return {
      formResponses: {
        name: '',
        password: '',
      },
    };
  },
  validations: {
    formResponses: {
      name: {
        required,
        minLength: minLength(2),
      }
    },
  },
};
```
The important thing is that the validation of the inputs is in the `$v` object.
Please take note that you can use functions as a scheme and add more dynamic validations this way:
https://vuelidate.js.org/#sub-dynamic-validation-schema

