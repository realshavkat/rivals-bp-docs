import siteConfig from "@generated/docusaurus.config";

export default function prismIncludeLanguages(PrismObject) {
  const {
    themeConfig: { prism },
  } = siteConfig;
  const { additionalLanguages } = prism;
  const PrismBefore = globalThis.Prism;
  globalThis.Prism = PrismObject;
  (additionalLanguages || []).forEach((lang) => {
    if (lang === "php") {
      require("prismjs/components/prism-markup-templating.js");
    }
    require(`prismjs/components/prism-${lang}`);
  });
  delete globalThis.Prism;
  if (typeof PrismBefore !== "undefined") {
    globalThis.Prism = PrismBefore;
  }

  PrismObject.languages.rbp = {
    comment: {
      pattern: /--.*/,
      greedy: true,
    },
    string: {
      pattern: /"(?:\\.|[^"\\])*"/,
      greedy: true,
    },
    constant: /@[A-Za-z_]\w*/,
    keyword:
      /\b(?:skill|flow|macro|test|on|as|if|else|repeat|every|loop|from|to|goto|data|params|vars|detached|after|requires|true|false|and|or|not)\b/,
    function: /\b[A-Za-z_][\w.]*(?=\s*\()/,
    number: /\b\d+(?:\.\d+)?\b/,
    operator: /=>|[=+\-*/<>]+/,
    punctuation: /[{}()[\],:.]/,
  };
  PrismObject.languages.text = PrismObject.languages.rbp;
}
