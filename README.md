# Kimball · Apps

Static official product, support and privacy pages for independent apps by Kimball. No JavaScript runtime, tracking scripts or build dependencies.

## KimDrop

| Page | 简体中文 | English |
| --- | --- | --- |
| Product | https://kimball-han.github.io/kimdrop/ | https://kimball-han.github.io/kimdrop/en/ |
| Support | https://kimball-han.github.io/kimdrop/support/ | https://kimball-han.github.io/kimdrop/en/support/ |
| Privacy | https://kimball-han.github.io/kimdrop/privacy/ | https://kimball-han.github.io/kimdrop/en/privacy/ |

Contact: bovvge@gmail.com. Copyright: 2026 Kimball. The public pages say “Coming soon” until a real App Store ID is available. Replace that text with the actual download link only after release. Product screenshots are real simulator captures from the App; filenames distinguish Chinese and English.

## Kim Games

Product and support content reflects version 1.2.0: 17 games, including Chess, with shared board-game feedback and Go capture animation.

- Product: https://kimball-han.github.io/kimgames/
- Support: https://kimball-han.github.io/kimgames/support/
- Privacy: https://kimball-han.github.io/kimgames/privacy/

## Preview and validate

```sh
python3 scripts/check-site.py
python3 -m http.server 8198 --bind 127.0.0.1
```

Open `http://127.0.0.1:8198/kimdrop/`. Use an HTTP server because links are rooted at the site domain.

## Publish

In GitHub repository Settings → Pages, set Source to **GitHub Actions**. The `pages.yml` workflow validates the site, stages only public site content, and deploys it after a push to `main` or a manual workflow run. This replaces an unused Next.js template that required a nonexistent package.json.

The workflow excludes submission notes and private account materials. App Store submission materials live in the KimDrop app repository under `app-store/1.0/`, not on this public site. No credentials or review phone numbers belong here.

After publishing, verify all six KimDrop URLs in a signed-out browser before using them in App Store Connect. Adding files locally does not publish them.

Former `/filebridge/` URLs redirect to the corresponding `/kimdrop/` pages, including support, privacy and English localizations.
