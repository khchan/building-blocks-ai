# building-blocks-ai

## Setup
1. Create a virtual environment called `venv` - this should create a folder called `venv` where project-specific dependencies will live:
```
python -m venv venv
```
2. Activate the virtual environment by name:
```
source venv/bin/activate
```
3. Install dependencies:
```
pip install -r requirements.txt
```

## Development
Run jupyter lab to bring up an interactive environment:
```
jupyter lab
```

## Live Reloading Notebook Slideshow
jupyter can export a notebook into a slideshow format, and to do live reloads you can install `fswatch` to build the html whenever the notebook changes:
```
brew install fswatch
```

Then to watch the notebook and open the slideshow run:
```
./watch.sh
```