import Vue from 'vue';
import VueI18n from 'vue-i18n';

Vue.use(VueI18n);

function loadLocaleMessages() {
  const locales = require.context(
    './locales',
    true,
    // All files with letters or numbers or underscore (the file needs to end with .json)
    /[A-Za-z0-9-_,\s]+\.json$/i
  );
  const messages = {};
  // Loop through all the keys (file names)
  locales.keys().forEach(key => {
    // matched is used to get the language name from the filename (LANGUAGE.json)
    const matched = key.match(/([A-Za-z0-9-_]+)\./i);
    if (matched && matched.length > 1) {
      const locale = matched[1];
      messages[locale] = locales(key);
    }
  });
  return messages;
}

export default new VueI18n({
  locale: process.env.VUE_APP_I18N_LOCALE || 'en',
  fallbackLocale: process.env.VUE_APP_I18N_FALLBACK_LOCALE || 'en',
  messages: loadLocaleMessages(),
});
