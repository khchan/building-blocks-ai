#!/bin/bash

fswatch -0 notebook.ipynb | xargs -0 -n 1 -I {} jupyter nbconvert notebook.ipynb --to slides --SlidesExporter.reveal_scroll=True &

python -m http.server 9001