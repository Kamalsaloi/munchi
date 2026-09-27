# Munshi landing page

Landing page for Munshi, a service that turns customer orders from WhatsApp, email, phone calls and handwritten parchis into TallyPrime entries for Indian distributors.

It's a single static file: open `index.html` in a browser. No build step.

## Before going live

Search `index.html` for `TODO` and replace the placeholders:

- WhatsApp number `91XXXXXXXXXX` (4 links) and phone `+91XXXXXXXXXX`
- Company name, email, founder name and reply time
- Pilot price
- `https://munshi.example` in the `og:url` and `og:image` tags: set the real domain
- `assets/parchi-sample.jpg` is a staged stand-in rendered from a handwriting font. Replace it with a real photo of a handwritten order slip (with the customer's permission, names changed) before launch

Have a native speaker review the Hinglish lines. All order data on the page is a labelled sample.

## Files

- `index.html`: the page
- `og-image.png`: link-preview image for WhatsApp and social shares
- `assets/`: images used on the page
- `PRODUCT.md`: product facts used for design decisions
- `DESIGN.md`: the design system (tokens, rules, components)
- `.impeccable/`: design critique and direction notes from the Impeccable skill
