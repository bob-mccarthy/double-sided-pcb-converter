#Double Sided PCB Converter

Takes pngs of your pcbs taken from gerber2img and processes them so that you can mill your
double sided designs

The program looks for two folders in the main directory which are input and output. In the input
directory you want to place 3 files and have them labeled accordingly: the outline of your board ('outline.png'), the traces on the front copper ('front-copper.png'), and the traces of the back-copper ('back-copper.png'). Once done processing it will place your processed images into the outputs folder of your directory. It will produce a 'front-copper.png', 'front-outline.png', 'back-copper.png', and 'back-outline.png' and you will want to start by milling the front pngs before flipping and milling the back pngs