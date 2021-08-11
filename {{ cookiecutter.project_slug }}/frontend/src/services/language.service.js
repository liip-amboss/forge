import i18n from '@/i18n';

/**
 * Sets the i18n language to the given language
 * @param {string} language The new language
 */
const setLanguage = language => {
  i18n.locale = language;
};

export { setLanguage };
