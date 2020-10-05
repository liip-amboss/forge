const path = require('path');

const colorGray100 = '#ccc5';
const colorBlack = '#000';
const borderStyle = '1px solid #e2e6ea';

const theme = {
  maxWidth: '1200px',
  color: {
    sidebarBackground: colorGray100,
    border: 'rgba(255, 255, 255, 0.1)',
    link: colorBlack,
    linkHover: '#353535',
    /**
     * prism colors configuration
     */
    codeComment: '#6d6d6d',
    codePunctuation: '#54a3f2',
    codeProperty: '#54a3f2',
    codeString: '#ffcc4d',
    codeInserted: '#EEEEEE',
    codeOperator: '#DDDDDD',
    codeKeyword: '#afe74c',
    codeFunction: '#54a3f2',
    codeVariable: '#AAAAAA',
    codeBase: '#FFFFFF',
    codeBackground: '#041d37',
  },
  sidebarWidth: 240,
  fontFamily: {
    base: ["'Fira Sans'", 'Helvetica', 'Arial', 'sans-serif'],
    monospace: ['Consolas', "'Liberation Mono'", 'Menlo', 'monospace'],
  },
  fontSize: {
    h2: '32px',
    h3: '26px',
    h4: '18px',
  },
};

const transpileDependencies = [
  'regexpu-core',
  'strip-ansi',
  'ansi-regex',
  'ansi-styles',
  'react-dev-utils',
  'chalk',
  'unicode-match-property-ecmascript',
  'unicode-match-property-value-ecmascript',
  'acorn-jsx',
  '@znck[\\\\/]prop-types',
  'camelcase',
  'tailwindcss',
  '@tailwindcss/custom-forms',
  'tailwindcss-transitions',
  'tailwindcss-typography',
];

module.exports = {
  title: 'Forge Style Guide',
  components: ['src/components/**/[A-Z]*.vue', 'src/styleguide/**/[A-Z]*.vue'],
  ignore: ['src/components/HelloWorld.vue'],
  pagePerSection: true,
  exampleMode: 'expand',
  usageMode: 'expand',
  copyCodeButton: true,
  compilerConfig: {
    target: { ie: 11 },
  },
  webpackConfig: Object.assign(
    {},
    {
      module: {
        rules: [
          {
            test: /\.css$/,
            exclude: /node_modules/,
            loader: 'postcss-loader',
          },
          {
            test: /\.js$/,
            exclude: modulePath =>
              (/node_modules/.test(modulePath) ||
                /packages[\\/]vue-styleguidist[\\/]lib/.test(modulePath)) &&
              !transpileDependencies.some(mod =>
                new RegExp(`node_modules[\\\\/]${mod}[\\\\/]`).test(modulePath)
              ),
            use: {
              loader: 'babel-loader',
              options: {
                sourceType: 'unambiguous',
                presets: [
                  [
                    '@babel/preset-env',
                    {
                      useBuiltIns: 'usage',
                      corejs: 3,
                      targets: {
                        ie: '11',
                      },
                    },
                  ],
                ],
                comments: false,
              },
            },
          },
        ],
      },
      devServer: {
        // We need this because otherwise Webpack prohibits the connection
        public: `${process.env.STYLEGUIDE_URL}`,
      },
    }
  ),

  // Print how to import component e.g.
  getComponentPathLine(componentPath) {
    const name = path.basename(componentPath, '.vue');
    const dir = path.dirname(componentPath);
    return `import ${name} from '${dir}/${name}' `;
  },
  sections: [
    {
      name: 'Components',
      components: 'src/components/**/[A-Z]*.vue',
    },
    {
      name: 'Styles',
      components: 'src/styleguide/styles/*.vue',
    },
    {
      name: 'Libraries',
      components: 'src/styleguide/libraries/*.vue',
    },
  ],
  require: [
    path.join(__dirname, 'src/assets/css/main.postcss'),
    path.join(__dirname, 'src/plugins/vTooltip.js'),
    path.join(__dirname, 'src/plugins/notifications.js'),
    path.join(__dirname, 'src/plugins/vuePortal.js'),
    path.join(__dirname, 'src/globals/svgIcon.js'),
    path.join(__dirname, 'node_modules/svgxuse'),
  ],
  theme,
  styles: {
    StyleGuide: {
      root: {
        'text-rendering': 'optimizeLegibility',
        '-moz-osx-font-smoothing': 'grayscale',
        '-webkit-font-smoothing': 'antialiased',
      },
      logo: {
        isolated: false,
        padding: 24,
        color: colorBlack,
        paddingBottom: 0,
      },
    },
    Version: {
      version: {
        isolated: false,
        color: theme.color.link,
        margin: [[8, 0, 0]],
        padding: [[4, 8, 5]],
        display: 'inline-block',
        fontWeight: 400,
        lineHeight: 1,
        border: [[1, 'solid', theme.color.link]],
        textTransform: 'uppercase',
        fontSize: '11px',
        letterSpacing: '1px',
        borderRadius: 3,
      },
    },
    Logo: {
      logo: {
        isolated: false,
        color: colorBlack,
        fontWeight: 400,
        fontSize: 16,
      },
    },
    Link: {
      link: {
        '&, &:link, &:visited': {
          isolated: false,
          fontWeight: 600,
        },
      },
    },
    ComponentsList: {
      list: {
        '& & a': {
          isolate: false,
          fontWeight: 'normal',
        },
        '& & a:hover': {
          isolate: false,
          color: theme.color.linkHover,
        },
      },
    },
    TableOfContents: {
      input: {
        isolated: false,
        padding: '8px 16px 9px',
        color: colorBlack,
        border: 'none',
        background: '#fffb',
      },
    },
    Playground: {
      preview: {
        isolated: false,
        padding: '40px',
        backgroundColor: '#f9fafb',
        border: borderStyle,
        boxShadow: 'inset 0 0 8px rgba(0, 17, 35, 0.05)',
        margin: '16px 0 0',
        borderRadius: '0',
        borderTopLeftRadius: 3,
        borderTopRightRadius: 3,
      },
    },
    SectionHeading: {
      sectionName: {
        lineHeight: '1.2',
        fontSize: '26px',
        '&:hover': {
          textDecoration: 'none',
          fontSize: '26px',
          lineHeight: '1.2',
        },
      },
      wrapper: {
        '& > h1': {
          width: 'calc(100% + 64px)',
          flexGrow: 2,
          padding: '48px 30px',
          fontFamily: ["'Fira Sans'", 'Helvetica', 'Arial', 'sans-serif'],
          margin: '-16px -30px 24px',
          background: 'transparent',
        },
      },
      toolbar: {
        display: 'none',
      },
    },
    Editor: {
      root: {
        borderTopLeftRadius: 0,
        borderTopRightRadius: 0,
      },
    },
    Table: {
      cellHeading: {
        color: '#1a3c5f',
        padding: '16px 48px 16px 16px',
      },
      tableHead: {
        borderBottom: borderStyle,
      },
      cell: {
        padding: '16px 48px 16px 16px',
      },
      table: {
        '& tr:hover': {
          backgroundColor: 'rgba(233, 243, 253, 0.3)',
        },
      },
    },
  },
};
