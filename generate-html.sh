#!/bin/bash

jupyter nbconvert notebook.ipynb --to slides --SlidesExporter.reveal_scroll=True
