---
name: Munshi
description: Customer orders from WhatsApp, calls and handwritten parchis, turned into TallyPrime entries.
colors:
  screen-ground: "#f3f6f7"
  panel: "#ffffff"
  line: "#d3dde1"
  line-soft: "#e5ecef"
  ledger-teal: "#0f5566"
  ledger-teal-deep: "#0b4452"
  teal-tint: "#e2eef1"
  selection-yellow: "#ffd94d"
  selection-yellow-soft: "#fff2bd"
  ink: "#1a1e21"
  ink-soft: "#3b464c"
  pencil: "#56626a"
  action-red: "#b8321f"
  action-red-deep: "#962817"
  action-red-tint: "#fbe6e2"
  wa-header: "#008069"
  wa-wallpaper: "#efeae2"
  wa-bubble-in: "#ffffff"
  wa-bubble-out: "#d9fdd3"
  wa-text: "#111b21"
  wa-meta: "#667781"
  wa-tick: "#53bdeb"
typography:
  display:
    fontFamily: "Anek Latin, system-ui, sans-serif"
    fontSize: "clamp(2.5rem, 5.4vw, 4.6rem)"
    fontWeight: 800
    lineHeight: 0.98
    letterSpacing: "-0.02em"
    fontVariation: "\"wdth\" 82"
  headline:
    fontFamily: "Anek Latin, system-ui, sans-serif"
    fontSize: "clamp(2rem, 4vw, 3.3rem)"
    fontWeight: 800
    lineHeight: 1.02
    letterSpacing: "-0.015em"
    fontVariation: "\"wdth\" 84"
  title:
    fontFamily: "Anek Latin, system-ui, sans-serif"
    fontSize: "1.3rem"
    fontWeight: 700
    lineHeight: 1.25
    fontVariation: "\"wdth\" 92"
  body:
    fontFamily: "Anek Latin, system-ui, sans-serif"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "Anek Latin, system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 600
    lineHeight: 1.3
  wa-ui:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.4
  mono:
    fontFamily: "Spline Sans Mono, ui-monospace, Consolas, monospace"
    fontSize: "14px"
    fontWeight: 600
    lineHeight: 1.4
rounded:
  label: "3px"
  key: "4px"
  control: "6px"
  frame: "8px"
  bubble: "7.5px"
  screen: "10px"
spacing:
  xs: "8px"
  sm: "12px"
  md: "16px"
  lg: "24px"
  xl: "56px"
  section: "96px"
components:
  button-whatsapp:
    backgroundColor: "{colors.wa-header}"
    textColor: "{colors.panel}"
    rounded: "{rounded.control}"
    padding: "12px 22px"
    height: "54px"
  button-whatsapp-hover:
    backgroundColor: "#006e5a"
  key:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "10px"
  key-action:
    backgroundColor: "{colors.action-red}"
    textColor: "{colors.panel}"
    rounded: "{rounded.control}"
    padding: "10px"
  screen-bar:
    backgroundColor: "{colors.ledger-teal}"
    textColor: "{colors.panel}"
    padding: "10px 16px"
  tab-active:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.ink}"
    height: "48px"
---

# Design System: Munshi

## Overview

**Creative North Star: "The Voucher Screen"**

Munshi's pages are drawn in the grammar of the order-entry screen that distributor staff look at all day: a light screen ground, white panels with a teal title bar, rows that a yellow selection bar reads down, and a rail of key-capped actions. Proof is shown by the screen doing its job (a messy order becoming a draft, a person approving it, the lines turning to ink), not by claims.

The system is calm and sparse. Most of the page is ink on white or on the cool screen ground; colour is reserved for state. Each block carries one idea, and a line earns its place only if a non-technical owner needs it. The voice is plain English with a little Hinglish, written in Latin letters.

**Key Characteristics:**
- Cool light ground, never warm cream.
- One working screen in the first viewport; the rest of the page stays quiet.
- Draft is pencil grey, approved is ink black: one visible line between them.
- Green opens WhatsApp; red marks what a person must act on in the voucher.
- Labels are real words in the sans face; no eyebrows or kickers.

## Colors

A restrained screen palette: cool neutrals, one teal for structure, yellow for selection, red for action.

### Primary
- **Ledger Teal** (#0f5566): screen title bars, active tab underline, arrows, link icons. The structural colour of the screen.
- **WhatsApp Green** (#008069): every button that opens WhatsApp (nav, hero, close, mobile dock). It matches the channel the owner already uses.
- **Action Red** (#b8321f): inside the voucher only: the Approve key and the out-of-stock note. Nothing decorative is ever red.

### Secondary
- **Selection Yellow** (#ffd94d): the moving row highlight, the approval line in the timeline, text selection, and the ENTERED label. Always means "this is the line being read or committed".

### WhatsApp chat (quoted UI)
- **WhatsApp Header** (#008069), **Wallpaper** (#efeae2), **Incoming** (#ffffff), **Outgoing** (#d9fdd3), **Text** (#111b21), **Meta** (#667781), **Read ticks** (#53bdeb): used only inside drawings of a WhatsApp chat, so the order looks like it arrived where it really arrives. Never used for Munshi's own UI.

### Neutral
- **Screen Ground** (#f3f6f7): page background and the tab strip.
- **Panel White** (#ffffff): screens, bands and tables.
- **Ink** (#1a1e21): headings, approved entries, primary text.
- **Ink Soft** (#3b464c): body copy.
- **Pencil** (#56626a): draft lines, meta text, captions (5.9:1 on white).
- **Line** (#d3dde1) and **Line Soft** (#e5ecef): borders and row rules.

### Named Rules
**The Hand-Up Rule.** Inside the voucher, red is used only where a person acts: the Approve key and a flagged line.

**The Channel Rule.** Anything that opens WhatsApp is WhatsApp green with white text. The bright #25D366 is never used behind white text (about 2:1 contrast).

**The Pencil-to-Ink Rule.** Unapproved content is pencil grey; approved content is ink. The change between them is the product's promise and happens in view.

## Typography

**Display and Body Font:** Anek Latin (variable width), with system-ui fallback.
**Label/Mono Font:** Spline Sans Mono, for key caps, clock times and the draft/entered label only.
**Quoted WhatsApp UI:** the platform system stack (Segoe UI, Roboto, Helvetica), only inside WhatsApp chat drawings.

**Character:** A sturdy Indian-designed grotesque that condenses for headlines and opens up for reading.

### Hierarchy
- **Display** (800, clamp 2.5–4.6rem, 0.98, wdth 82): the hero headline only.
- **Headline** (800, clamp 2–3.3rem, 1.02, wdth 84): section headings, max ~18em.
- **Title** (700, 1.3rem, 1.25): timeline and step headings.
- **Body** (400, 18px, 1.55; 17px under 560px): copy, max ~38em.
- **Label** (600, 14px): notes, table meta, status line. 14px is the floor on mobile.
- **Mono** (600, 12–16px): key caps (`Ctrl A`, `C`), timeline times, the DRAFT/ENTERED label.

### Named Rules
**The No-Costume Mono Rule.** Monospace is for keys, times and machine labels. Ordinary words are never set in mono.

## Layout

Single column of full-width bands inside a 1240px container with 24px gutters (16px under 560px). The hero is a two-column grid (0.9fr copy, 1.1fr screen) that stacks under 1040px. Bands alternate screen ground and white, with 96px vertical padding (64px under 720px). The close is marked by a 3px ink rule. Inside the screen, the key rail is a 112px right column that becomes a row under the table below 640px. Under 900px a WhatsApp action dock appears at the bottom once the hero CTA scrolls away.

## Elevation & Depth

Flat by default. Surfaces are separated by 1px lines and tonal bands, not shadows. The only raised object is the Approve key cap (a 2px offset in Action Red Deep), because a key is a physical thing.

## Shapes

Small, square-ish radii: 4px for key caps and labels, 6px for buttons and keys, 10px for screens. Row rules are 1px and solid; totals sit over a 3px double rule; the approval gate in the filmstrip is a 3px ink rule with a yellow label.

## Components

- **Voucher screen:** a teal "Sales Order Creation" bar with a DRAFT/ENTERED label, input tabs (Parchi photo, WhatsApp, Phone call), then the voucher itself as one bordered group: a grey header strip (Party A/c name · Order no. · Date), a teal-tinted column-header row (Name of Item · Qty · Rate · Amount), item names in 600 weight, right-aligned tabular figures, a total over a 3px double rule, and a narration line. A key rail and a one-line status bar sit outside the group. Only a flagged line carries a note.
- **Keys:** white with a line border and a mono key cap; the action key is red. Approve is `Ctrl A` and asks "Accept? Yes / No" before inking.
- **WhatsApp chat drawing:** green header with back arrow, avatar and contact name; beige wallpaper; white incoming and green outgoing bubbles with a tail on the first bubble of a run, time inside the bubble, blue read ticks on outgoing.
- **Filmstrip:** a row of equal frames on a time axis (dot + mono time + dashed line), each frame a picture of the step (photo, match arrows, stock slots, chat, mini voucher) with a caption of three or four words. Draft frames are dashed on the screen ground; the yellow approval gate is a vertical label on a 3px ink rule; frames after it are solid ink on white. Below 1040px the strip scrolls sideways with scroll-snap.
- **Alias rows:** what the customer wrote (pencil italic) → teal arrow → the item as a teal-tint pill, inside a panel with a teal bar and one footnote.
- **WhatsApp button:** WhatsApp green, 54px tall, WhatsApp glyph, full width on phones.

## Do's and Don'ts

- **Do** show the screen working instead of listing features.
- **Do** keep one note per flagged line and none on normal lines.
- **Do** label sample data as sample.
- **Don't** add eyebrows, kickers, numbered badges or labels stacked above headings.
- **Don't** add chips or status pills to every row.
- **Don't** explain a step in a paragraph when a small drawing of it can show it; captions stay under five words.
- **Don't** use warm cream grounds or decorative shadows.
- **Don't** use red for anything a person doesn't have to act on, and don't make WhatsApp buttons any colour but WhatsApp green.
- **Don't** invent customers, metrics, prices or testimonials.
- **Don't** use Devanagari script; Hinglish is written in Latin letters.
