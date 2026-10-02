# GitHub profile design

## Direction

A developer portfolio built around real work: AI infrastructure, knowledge retrieval, identity, and automation. Midnight navy surfaces, periwinkle and cyan accents, precise typography, and an original glass architecture illustration create a coherent technical identity.

The banner introduces the person. Linked project cards establish evidence. Smaller focus cards summarize engineering experience. Detailed descriptions remain available as native, selectable text in expandable sections. Bilingual headings and a short Chinese introduction make the profile approachable in both languages.

## References and what we used

- [DenverCoder1](https://github.com/DenverCoder1): a recognizable introduction, consistent repository cards, and clear separation of projects, tools, and supporting details. We adopted the information hierarchy and linked cards, not the author's images or personal metrics.
- [lowlighter](https://github.com/lowlighter/lowlighter): engineering information presented as coherent visual modules. We applied this to the three areas of experience; the diagrams are conceptual, not live statistics.
- [Tw93](https://github.com/tw93): real projects and current work make a profile personal. We used verified public work instead of adding unsubstantiated achievements.

## Content verification

Checked the public DYL521 profile, public non-fork repository list, and repository content on 2026-09-30.

- [Jarvis Registry](https://github.com/ascending-llc/jarvis-registry): contributions verified through commits returned for GitHub author DYL521. The README identifies a contributor role, not sole ownership.
  - [Embedding reindexing](https://github.com/ascending-llc/jarvis-registry/commit/cfa8267b5f57471544bce4a7e8b3ffe9ed05fb44).
  - [Tool access controls](https://github.com/ascending-llc/jarvis-registry/commit/5ebe945115059765ab8d3da1b4422a62dbd15470).
- [Agentic Design Patterns CN](https://github.com/DYL521/Agentic-Design-Patterns-CN): public repository and bilingual project purpose verified from its README. Original book authorship is not attributed to DYL521.
- Original RAG, identity, and Jira / Confluence experience and technologies are retained from the original profile README.
- The personal website https://dyl521.github.io/ is linked in the top navigation and footer, as explicitly requested by the user. Contact email is retained from the original README.

No follower counts, star counts, performance numbers, or uptime claims are invented or hard-coded into the design.

## Assets

- `assets/profile-hero.png`: original hero generated using the built-in image generation tool. Final prompt: [hero-prompt.txt](hero-prompt.txt). Source was copied from the generated-images directory into this repository. The illustration is conceptual; it is not an architecture claim about a particular project.
- `assets/project-*.svg`: two linked repository cards.
- `assets/work-*.svg`: three engineering focus cards.
- `assets/link-*.svg`: local navigation buttons.
- `assets/contact.svg`: contact panel.

The SVGs are editable, static, and self-contained. All assets are local; no third-party image service is required. Every image has alternative text. Essential identity, project links, descriptions, and contact information also exist as native text. Cards wrap naturally; the hero scales to the available width.

## Branches

- Original master backup: `codex/backup-master-20260920`, pointing at `d32661b75f1bf5613b91b0cac30e51c762dd3d48`.
- Working branch: `codex/profile-redesign`.
- No master merge is part of this iteration.

## Validation

Local README previews were checked at desktop width (1100px) and narrow widths (390px and 320px), including light and dark backgrounds. Images loaded and no document-level horizontal overflow was detected. Project details expand correctly. All ten referenced local image assets exist, SVGs parse successfully, and both website links target the requested URL. `git diff --check` passes. Preview styling approximates GitHub; it does not replace checking the rendered branch on GitHub after a future push.

## Revision: engineering field notes

Replaced the generated technology hero with a self-contained SVG masthead: Chinese name, ink-black type, vermilion annotations, paper background and a functional connection diagram. Removed decorative skill cards and badge navigation from the README. Kept verified project links and a text-first account of the work. Prior assets remain available for comparison.

## Revision: DYL521 personal dev space

Based on the user's explicit preference for bold contrast, oversized typography and experimental layout. Uses the actual GitHub handle as the central visual identity, orange/ink contrast and a cobalt code mark. No invented hobbies or biography. Native text remains readable beneath the SVG masthead. Full-width project strips replace the generic card grid.

References checked 2026-10-01: https://github.com/antfu (personal navigation), https://github.com/tw93 (work and releases at the center), https://github.com/ryo-ma (project identity). These inform hierarchy, not copied graphics.

## Revision: anime night room

User approved a slice-of-life anime night computer room. Original built-in image generation saved in assets/anime-room.png; exact prompt in docs/anime-room-prompt.txt. Character and room are fictional atmosphere, not a claim about the user's appearance, possessions or hobbies. Replaced poster masthead and oversized project cards with a panoramic illustration and native Markdown project shelf. Warm lamp / midnight palette, quiet bilingual welcome and accessible website links. Previous assets retained for comparison.

Final polish: native text replaces the engineering table for narrow screens; collapsible notes and toolbox reduce visual density; a small self-contained pixel window/lamp footer echoes the banner. No custom CSS is required by the README.

## User-supplied artwork revision

Replaced the banner with assets/profile-artwork.jpg, copied unchanged from the user's attachment. Preserved artwork lettering and full aspect ratio. Palette: ink #080f0e, vermilion #f02e42, jade #64d6bd. Replaced room-specific copy and footer decoration. Preview CSS follows this palette; GitHub itself controls README page background, link and heading colors. The artwork is user-supplied, not generated or claimed as original.

## GitHub rendering correction

Removed custom preview-only palette CSS. Accent colors now live in self-contained SVG section headings and navigation, so they are part of the actual README assets. Body text, links and background use the reader's GitHub theme. Preserved the user's removal of backup instructions. Local preview remains an approximation, not a pixel-exact GitHub renderer.

## Composition refinement

Constrained original artwork to 680px without cropping, centered a compact personal masthead and 32px navigation. Two 280px chapter labels replace full-width bars. Condensed project metadata and engineering descriptions; removed duplicate English engineering detail blocks. Preserved full Chinese introduction and toolbox disclosures. Footer becomes one centered invitation to exchange ideas. Native GitHub layout attributes only.

## Screenshot-led spacing correction

User screenshot exposed disconnected colored labels and excessive vertical gaps. Removed image section labels and spacer breaks; grouped each project in a native blockquote with explicit line breaks, and consolidated engineering into a two-column table. Kept original illustration and navigation accents.
