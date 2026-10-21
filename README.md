# Latent Paths GitHub profile

Maintains the [Latent Paths organization profile](profile/README.md) and shared brand assets used by the organization’s repositories.

[Website](https://www.latentpaths.com/) · [GitHub organization](https://github.com/latentpaths) · [Contact](mailto:ayush@latentpaths.com)

## Assets

`assets/` contains the supplied symbol and wordmark as editable SVG sources and PNG exports. Keep each SVG and its export together. Link to these files from other repositories rather than maintaining competing logo copies.

Use `assets/latent-paths-symbol-cream.png` for the organization avatar and
`assets/latent-paths-wordmark-cream.png` for README headers. Their permanent
cream (`#F1EBDD`) backing and padding keep the original dark logo readable on
both light and dark surfaces, without theme switching or an added border.

Edit the original `latent-paths-symbol.svg` and `latent-paths-wordmark.svg`
sources, then run `python3 scripts/export-logos.py` (requires librsvg's
`rsvg-convert`) to rebuild the cream-backed SVG and PNG exports. Do not edit
the generated variants separately.
