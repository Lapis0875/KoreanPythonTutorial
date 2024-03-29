const sidebar = require("./sidebar");

module.exports = {
  /**
   * Ref：https://v1.vuepress.vuejs.org/config/#title
   */
  title: 'Python Tutorial',
  /**
   * Ref：https://v1.vuepress.vuejs.org/config/#description
   */
  description: "Python Tutorial for All",
  dest: "build",
  base: "/PythonTutorial/",
  /**
   * Extra tags to be injected to the page HTML `<head>`
   *
   * ref：https://v1.vuepress.vuejs.org/config/#head
   */
  head: [["link", {rel: "icon", href: "./logo.png"}]], // TODO not found logo, 로고 추가 필요

  /**
   * Theme configuration, here is the default theme configuration for VuePress.
   *
   * ref：https://v1.vuepress.vuejs.org/theme/default-theme-config.html
   */
  themeConfig: {
    logo: "data:image/jpeg;base64,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",
    sidebar : sidebar,
    nav: [
      {
        text: 'Repository',
        link: 'https://github.com/KoreanTutorials/PythonTutorial'
      }
    ],
    smoothScrool: true,
    lastUpdated: 'Last Updated',
  },
};
