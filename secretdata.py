from IPython.display import Image
from skimage.io import imread
from skimage.color import gray2rgb

secret = gray2rgb(imread('images/dreamy.jpg'))
appropriate_response = Image(url='http://www.reactiongifs.com/wp-content/uploads/2012/12/friday-damn.gif');
