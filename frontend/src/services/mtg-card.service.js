import { mtgApi } from './api';
import { MtgCard } from '../models/mtg-card.model';

const getMagicCard = async function() {
  // you can add things like bearertokens or payloads here
  let config = { crossdomain: true };
  const response = await mtgApi.get('cards/random', config);
  const result = MtgCard(response.data);
  return result;
};

export { getMagicCard };
