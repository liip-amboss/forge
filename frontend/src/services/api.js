import axios from 'axios';
const mtgApi = axios.create({
  baseURL: `https://api.scryfall.com`,
});

export { mtgApi };
