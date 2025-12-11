# Publications Management

This directory contains scripts to help manage publications on your Hugo website.

## Using the BibTeX to Markdown Converter

### Quick Start

1. Prepare your BibTeX file (e.g., `papers.bib`)
2. Run the conversion script:
   ```bash
   python scripts/bib2md.py papers.bib
   ```
3. Add images for each publication to `static/img/publications/`
4. Preview with `hugo server`

### Usage

```bash
python scripts/bib2md.py <input.bib> [output_dir]
```

Arguments:
- `input.bib`: Path to your BibTeX file
- `output_dir`: (Optional) Output directory, defaults to `content/publications`

### Example

```bash
# Convert example.bib to markdown files
python scripts/bib2md.py scripts/example.bib

# Or specify a custom output directory
python scripts/bib2md.py my-papers.bib content/publications
```

### What the Script Does

The script will:
1. Parse your BibTeX file and extract publication information
2. Generate a markdown file for each entry with:
   - Title
   - Authors
   - Publication date
   - Venue (conference/journal)
   - Abstract/description
   - DOI/URL link
3. Create properly formatted frontmatter for Hugo
4. Print a list of needed images

### BibTeX Fields Supported

- `title`: Paper title
- `author`: Authors (supports "and" separator and "Last, First" format)
- `year`, `month`: Publication date
- `booktitle`, `journal`, `venue`: Publication venue
- `abstract`: Paper abstract/description
- `doi`, `url`: Link to paper
- Entry types: `@article`, `@inproceedings`, `@incollection`, `@techreport`, etc.

### Adding Publication Images

After running the script, you'll need to add images for each publication:

1. Create an image (screenshot, diagram, or key figure from your paper)
2. Save it to `static/img/publications/` with the filename shown in the script output
3. Recommended size: 500x300px or similar aspect ratio

### Manual Publication Entry

You can also manually create publication entries. Create a new `.md` file in `content/publications/`:

```markdown
---
title: "Your Paper Title"
date: 2024-01-01
pubtype: "Conference Paper"
featured: true
description: "Brief description or abstract"
authors: ["Author One", "Author Two"]
tags: ["tag1", "tag2"]
image: "/img/publications/your-image.png"
link: "https://doi.org/your-paper"
venue: "Conference/Journal Name"
weight: 500
---

Full abstract or detailed description goes here.
```

### Publication Types

- `Paper`: Journal article
- `Conference Paper`: Conference publication
- `Technical Report`: Tech report
- `PhD Thesis`: Doctoral dissertation
- `Master Thesis`: Master's thesis
- `Book`: Book publication
- `Talk`: Presentation/talk

### Tips

1. Set `featured: true` to show the publication on the homepage
2. Lower `weight` values appear first
3. Use relevant tags for filtering
4. Add high-quality images for better visual appeal
5. Keep descriptions concise for the summary view
