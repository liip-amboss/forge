import { createI18n } from 'vue-i18n';

function loadLocaleMessages() {
  // load every locale file found in @/src/locales
  const locales = import.meta.globEager('./locales/*.json');
  const messages = {};
  // Loop through all the keys (file names)
  Object.keys(locales).forEach((key) => {
    // matched is used to get the language name from the filename (LANGUAGE.json)
    const matched = key.match(/([A-Za-z0-9-_]+)\./i);
    if (matched && matched.length > 1) {
      const locale = matched[1];
      messages[locale] = locales[key];
    }
  });
  return messages;
}

export default createI18n({
  locale: import.meta.env.VITE_I18N_LOCALE || 'en',
  fallbackLocale: import.meta.env.VITE_I18N_FALLBACK_LOCALE || 'en',
  globalInjection: true,
  messages: loadLocaleMessages()
});
