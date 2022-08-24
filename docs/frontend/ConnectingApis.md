# Connecting APIs

## Installing Axios
Forge uses [axios](https://github.com/axios/axios/) to manage HTTP Requests, you can install it by running:
`npm install axios`

## Setting up your Service
After installing Axios we recommend to create 'API Bases'. Create a folder named "services" (or whatever you think makes most sense for a service which returns a configured Axios instance). In this folder create a file named `api.js`, copy and paste this code for the base setup:
```javascript
import axios from 'axios';
const APINAME = axios.create({
  baseURL: `https://www.myapi.ch`,
});

export { APINAME };
```

## Setting up your Service with .env variables
Note that we can also use `.env` variables like this:
```javascript
import axios from 'axios';
const APINAME = axios.create({
  baseURL: `${process.env.VUE_APP_API_URL}`
});

export { APINAME };
```
## Adding interceptors to your service
There are cases where calling some endpoints should have some logic happening beforehand, for example when you want to add the credentials of your user to any call on the base-service `secretCIAStuff` your `api.js` can look like this:
```javascript
import axios from "axios";
import store from "@/store/";

const loginCredentialsInterceptor = config => {
  if (store.getters["Auth/isLoggedIn"]) {
    const token = store.state.Auth.token;
    config.headers.common["Authorization"] = `Bearer ${token}`;
  }
  return config;
};

const secretCIAStuff = axios.create({
  baseURL: `${process.env.VUE_APP_API_SECRET_URL}`
});

secretCIAStuff.interceptors.request.use(loginCredentialsInterceptor);

export {secretCIAStuff};
```
This will check the store for login credentials and add them to the call if they exist

## Connecting your base service
Using this base-service now allows you to easier handle your requests, so your service `getSecretCIAData` would now look like this:
```javascript
import { secretCIAStuff } from '@/services/api';
const getSecretCIAData = async function() {
  // you can add more settings here
  let config = { crossdomain: true };
  const response = await secretCIAStuff.get('secretdata/aliens', config);
  return response;
};
export { getSecretCIAData };
```
## Adding Models
The service now works but working with APIs can often be a bit fickle.
Let's say, for example, we expect our data from `getSecretCIAData` to look like this:
```JSON
{
  type:1,
  alienName:"Manfred",
  numberOfEyes:12,
  planet: {
    planetName:"orgfort",
    population:120000000,
    solarSystem:"Xyklorp"
  }
}
```
Now, as long as the data always looks like this everything is fine, our tests (if we have them), will pass, our application will be usable and our team will be happy and productive. But what if the name is not existant? Do we get an empty string? do we get `null`? do we get `undefined`?
Having models to map the data helps us here, a model can look like this:
```javascript
export function Alien(data) {
  if(!data) return null
  let model = {};
  model.alienType = data.type || -1;
  model.eyeAmount = data.numberOfEyes || null;
  model.name = data.alienName || "No Name defined";
  if(data.planet && data.planet.planetName) {
    model.planet = data.planet
  }else {
    model.planet = null
  }
  return model;
}
```
In this case we can always go sure that we have a name to display, even if it is "No Name defined". We also know for sure that if our planet has no name we will have the planet set to `null` which we can use for easier checks in the template like this:
```vue
<h2 v-if='alien && alien.planet'>{{alien.planet.planetName}}</h2>
```
Adding this model to your service will look like this:
```javascript
import { secretCIAStuff } from '@/services/api';
import { Alien } from '@/models/alien.model';
const getSecretCIAData = async function() {
  // you can add more settings here
  let config = { crossdomain: true };
  const response = await secretCIAStuff.get('secretdata/aliens', config);
  return new Alien(response);
};
export { getSecretCIAData };
```
As you see we named the file `Alien.model.js` and added it in a folder called `models` we do this because often a model can have the same name as a service or a base service or sometimes even a component, by adding ".model" at the end of the filename it makes it easier to navigate your code in the search. Since models are typically something that we change from time to time (as data tends to get added or changed in projects) navigating through models with search is crucial!


