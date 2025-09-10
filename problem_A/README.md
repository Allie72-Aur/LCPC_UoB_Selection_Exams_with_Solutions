# Guide to the Contents of this Folder

problem_A
├── markdown.md
├── product_Z
│  ├── c_code
│  ├── LaTeX
│  │  ├── latex.tex
│  │  └── Product_Z.pdf
│  ├── markdown
│  │  ├── markdown.html
│  │  └── markdown.md
│  └── python
│     ├── calc_product_z.py
│     ├── test_calc_product_z.py
│     └── test_calc_product_z.sh
├── README.md
├── series_A
│  ├── c_code
│  ├── LaTeX
│  │  ├── latex.tex
│  │  └── SeriesA.pdf
│  ├── markdown
│  │  ├── Calculate_Series_A.md
│  │  ├── markdown.html
│  │  ├── markdown.md
│  │  └── mathjax.md
│  └── python
│     ├── calc_series_a.py
│     ├── test_series_a.py
│     └── test_series_a.sh
├── series_Y
│  ├── LaTeX
│  │  ├── latex.tex
│  │  └── Series_Y.pdf
│  ├── markdown
│  │  ├── markdown.html
│  │  └── markdown.md
│  └── python
│     ├── calc_series_y.py
│     ├── test_calc_series_y.py
│     └── test_calc_series_y.sh
├── solutions_to_Problem_A.html
└── solutions_to_Problem_A.pdf

## Main Documents

The `solutions_to_Problem_A.html` and `solutions_to_Problem_A.pdf` files contain
the final, polished explanations and pseudocode for all sub-problems. These
documents are compiled from the various source files in the sub-folders to
present a cohesive solution guide.

The `README.md` file, which you are reading now, provides a high-level overview
of the entire project structure.

the HTML file is compiled from `markdown.md`, subsequently; the PDF is a print
of the HTML document.

## The Sub-Folders

.
├── product_Z
├── series_A
└── series_Y

Each sub-problem (product_Z, series_A, series_Y) has its own folder, which is
further divided into dedicated sub-folders for code, documentation, etc.

### Markdown (`markdown/`)

This folder contains the Markdown source files (`.md`) that serve as the main
documentation. They include explanations, pseudocode, and mathematical formulas
rendered using MathJax. The `markdown.html` file is a compiled version of this
content.

### LaTeX (`LaTeX/`)

Mostly, their contents are the same as the markdown files, the PDF files in the
sub-direcories (`Product_Z.pdf`, `SeriesA.pdf`, etc.) are produced from those
`tex` files.

After experimenting with them for a while; I figured markdown is much more
convenient to work with, since you can embed LaTeX into them to render
basic mathematical equations, this makes writing a whole LaTeX document
just to get that one feature so overkill.

### Python (`python/`)

This is where all the Python-based source code is stored.

* **Implementation Files**: Files like `calc_product_z.py` contain the core logic
  for the solution.

* **Unit Test Suites**: The `test_*.py` files contain the unit tests, written
  using the standard unittest framework, to verify that the solution code is
  working correctly.

* **Shell Scripts**: The `test_*.sh` scripts are simple utilities designed to run
  the corresponding unit tests with a single command.

### C Code (`c_code/`)

This folder is a placeholder for future implementations of the solutions in
the C programming language. Its presence indicates a plan for expanding the
solutions to include multiple languages.
