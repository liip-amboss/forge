export function MtgCard(card) {
  let model = {};
  model.name = card.name || null;
  model.image = card.image_uris.normal || null;
  model.rareLevel = card.rarity || null;
  model.painter = card.artist || null;
  return model;
}
