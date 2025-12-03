# CaveCode Badges

These badges can be embedded in README files or docs to indicate
that a project uses or supports CaveCode.

Examples:

```markdown
![CaveCode Compliant](badges/cavecode-compliant.svg)

Badges are simple SVGs and can be recolored as needed, as long as the text “CaveCode” remains visible.

### `badges/cavecode-compliant.svg`

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="150" height="24" role="img" aria-label="CaveCode: compliant">
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#222222"/>
    <stop offset="100%" stop-color="#444444"/>
  </linearGradient>
  <rect rx="4" width="150" height="24" fill="url(#bg)"/>
  <text x="10" y="16" fill="#ffffff" font-family="monospace" font-size="11">
    🪨 CaveCode: compliant
  </text>
</svg>
