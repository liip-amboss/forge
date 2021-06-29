# Localization

For the localization we are using the vue-i18n library. [vue-i18n](https://github.com/kazupon/vue-i18n)
There is also a documentation for this library. [documentation](https://kazupon.github.io/vue-i18n/)

## Installation

If you want to know how to install vue-i18n have a look at the [documentation](https://kazupon.github.io/vue-i18n/installation.html#compatibility-note)

## Update language

There is a service method to update the i18n language. The method is in the `services/language.service.js` file.
```javascript
import { setLanguage } from '@/services/language.service';

setLanguage('en')
```

## Features

Vue-i18n has some very useful features.

The first one is that you can have placeholders in your locales and replace them during the runtime. [formatting](https://kazupon.github.io/vue-i18n/guide/formatting.html)

The second one is pluralization. You can easily create plural and singular forms of messages. [pluralization](https://kazupon.github.io/vue-i18n/guide/pluralization.html#accessing-the-number-via-the-pre-defined-argument)

The third one is interpolation. With this you feature you can easily e.g. add links to your text. [interpolation](https://kazupon.github.io/vue-i18n/guide/interpolation.html#basic-usage)
