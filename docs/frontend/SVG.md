# SVG
Forge comes with a SVG sprite map generator and `<svg-icon />` component which requires only the name of the icon.
To add a new icon a new svg icon file needs be located in the `frontend/src/assets/icons/` directory. The name given to the file will be associated with the component. Eg. a 'menu.svg' can be used as `<svg-icon name="menu" />`

## SVG Plugins
- [vue-cli-plugin-svg-sprite](https://github.com/swisnl/vue-cli-plugin-svg-sprite)
- [svgo](https://github.com/svg/svgo)
- [svgo-loader](https://github.com/rpominov/svgo-loader)

## Installation

To install these packages to a new project, simple invoke
`vue add svg-sprite`

It will install all the necessary tools automatically. See [github](https://github.com/JetBrains/svg-sprite-loader#runtime-configuration) for instructions how to use it.
