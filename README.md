# GitHub README for Minimal Random Quote Generator

This repository contains code for hosting a minimal quote generator website that displays a new quote every 5 seconds. The quotes are fetched from the [quotable API](https://api.quotable.io/). 

## Installation

To run this project locally, you will need Python 3 and Streamlit. You can install Streamlit using the following command:

```bash
pip install streamlit
```

You can then clone this repository using:

```bash
git clone https://github.com/{your-username}/minimal-random-quote-generator.git
```

Navigate to the repository directory and run the following command to start the Streamlit app:

```bash
streamlit run app.py
```

## Usage

Once the Streamlit app is running, a random quote will be displayed along with its author. The quote will change every 5 seconds. 

The app also features a background image, which can be customized by changing the image URL in the `main()` function.

## Demo

You can try out the live demo of this app at the following link: https://deepankarvarma-random-quote-generator-using-python-app-pko9mm.streamlit.app/

## Credits

This project uses the [quotable API](https://api.quotable.io/), which is a free, open-source API for quotes.
