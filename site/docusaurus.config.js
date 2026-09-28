// @ts-check
import { themes as prismThemes } from "prism-react-renderer";

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "Rivals BP",
  tagline: "Créer des techniques Blue Lock",
  url: "https://realshavkat.github.io",
  baseUrl: "/rivals-bp-docs/",
  organizationName: "realshavkat",
  projectName: "rivals-bp-docs",
  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",
  i18n: { defaultLocale: "fr", locales: ["fr"] },
  stylesheets: [
    "https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;700&display=swap",
  ],
  headTags: [
    { tagName: "link", attributes: { rel: "preconnect", href: "https://fonts.googleapis.com" } },
    { tagName: "link", attributes: { rel: "preconnect", href: "https://fonts.gstatic.com", crossorigin: "anonymous" } },
  ],
  presets: [
    [
      "classic",
      {
        docs: {
          routeBasePath: "/",
          sidebarPath: "./sidebars.js",
        },
        blog: false,
        theme: { customCss: "./src/css/custom.css" },
      },
    ],
  ],
  plugins: [
    [
      require.resolve("@easyops-cn/docusaurus-search-local"),
      { hashed: true, language: ["fr"], indexDocs: true, docsRouteBasePath: "/" },
    ],
  ],
  themeConfig: {
    colorMode: { defaultMode: "dark", respectPrefersColorScheme: false },
    docs: {
      sidebar: {
        hideable: true,
        autoCollapseCategories: true,
      },
    },
    navbar: {
      title: "Rivals BP",
      items: [
        { to: "/guides/ouvrir", label: "Guides", position: "left" },
        { to: "/blocs", label: "Blocs", position: "left" },
        { to: "/langage/verbes", label: "Langage", position: "left" },
        { href: "https://github.com/realshavkat/rivals-bp-docs", label: "GitHub", position: "right" },
      ],
    },
    footer: {
      style: "dark",
      copyright: "Documentation Rivals BP. Une page par bloc, relue dans le module.",
    },
    prism: { theme: prismThemes.github, darkTheme: prismThemes.dracula },
  },
};

export default config;
