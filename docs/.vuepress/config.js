module.exports = {
  title: 'Forge',
  description: 'The documentation for Forge template',
  themeConfig: {
    smoothScroll: true,
    lastUpdated: 'Last Updated',
    nav: [{ text: 'GitHub', link: 'https://github.com/liip-amboss/forge' }],
    sidebar: [
      {
        title: 'Usage',
        collapsable: false,
        children: [
            '/usage/setup',
            '/usage/commands',
        ]
      },
      {
        title: 'Frontend',
        collapsable: false,
        children: [
          '/frontend/',
          '/frontend/accessibilty',
          '/frontend/ConnectingApis',
          '/frontend/linting',
          '/frontend/purge',
          '/frontend/SVG',
          '/frontend/testing',
          '/frontend/vuelidate',
          {
            title: 'Components',
            collapsable: false,
            children: [
              '/frontend/components/modal',
              '/frontend/components/simple-table',
              '/frontend/components/notification'
            ]
          }
        ]
      },
      {
        title: 'Backend',
        collapsable: false,
        children: [
            '/backend/',
            '/backend/ide',
            '/backend/apps'
        ]
      }
    ]
  }
};
