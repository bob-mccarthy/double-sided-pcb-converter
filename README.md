# Double Sided PCB Converter

## Turns your [gerber2img](https://quentinbolsee.pages.cba.mit.edu/gerber2img/) board images, and processes the images to allow for double sided pcb milling

Automating the process for milling double sided pcbs described [here](https://sibusaman.fabcloud.io/doublepcb/)

## How to Run 

Install the dependencies

```
pip3 install -r requirements.txt
```

Place your photos into a folder called input in the top directory. The program looks for three files in the input directory: the outline of your board ('outline.png'), the traces on the front copper ('front-copper.png'), and the traces of the back-copper ('back-copper.png'). All of these images must be the same size 

then run

```
pip3 install main.py
```

It will then place four files in the output folder front-copper.png, front-outline.png, 
back-copper.png, back-outline.png. First mill front-copper.png and front-outline.png. Then flip the pcb inside of the stock and mill back-copper.png and back-outline.png.
