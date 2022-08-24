const customDocsBlockPlugin = () => {
  return {
    name: 'custom-docs-block',
    transform(code, id) {
      // return empty function the compile <docs> blocks in vue files
      if (/vue&type=docs/.test(id)) {
        return {
          code: 'export default () => {}',
          map: null,
        };
      }
    },
  }
}

export default customDocsBlockPlugin