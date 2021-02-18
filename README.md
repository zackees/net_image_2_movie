# Brief

fetch_png.py: Repeatedly fetches an image (png) every X seconds.
make_movie.py: Stitches those png files together into a movie.


# Example:
  * `python3 fetch_png.py --url http://www.ercot.com/content/cdr/main/currentDayForecastSystemLoad.png --sample 10`
  * `python3 make_movie.py`
  * Movie will be produced under `out/out.mp4`

# TODO:
  * Add support for other file formats besides png.