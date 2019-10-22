const _ = require('lodash')

module.exports = function({
  grids = _.range(1, 12),
  variants = ['responsive'],
}) {
  return function({ e, addUtilities, theme }) {
    const gridGaps = theme('gridGap', {})

    addUtilities(
      [
        { '.css-grid': { display: 'grid' } },
        { '.css-grid-dense': { gridAutoFlow: 'dense' } },
        ..._.map(gridGaps, (size, name) => ({
          [`.${e(`grid-gap-${name}`)}`]: { gridGap: size },
        })),
        ...grids.map(columns => ({
          [`.grid-columns-${columns}`]: {
            gridTemplateColumns: `repeat(${columns}, 1fr)`,
          },
        })),
        ..._.range(1, _.max(grids) + 1).map(span => ({
          [`.col-span-${span}`]: {
            gridColumnStart: `span ${span}`,
          },
        })),
        ..._.range(1, _.max(grids) + 2).map(line => ({
          [`.col-start-${line}`]: {
            gridColumnStart: `${line}`,
          },
          [`.col-end-${line}`]: {
            gridColumnEnd: `${line}`,
          },
        })),
      ],
      variants
    )
  }
}
