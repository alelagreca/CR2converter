<p align = "center">
<img src = "cr2icon_256x256x32.png">
</p>

# CR2converter

Runs on mac only for now...

The program basically runs "sips" tool through an user-friendly graphical interface.

## Installation

It is probably best if you set a new environment, for example with conda.
Install PySimpleGUI module:

```bash
pip3 install PySimpleGUI
```

## Usage

You can lauch the gui in your terminal with:

```bash
python3 cr2converter.py
```

When it opens, you will need to provide input and output directories. CR2 files in input directory will be display so you may choose some of them. If none is selected, all listed files will be processed as input.

You may also change the default output format from jpg to any of tiff, png and more.

Hope it helps!!!

## Application

CR2converter was packaged as a portable mac application using pyinstaller (command below) for convenience (just launch with "double click")

```bash
pyinstaller --onefile --windowed --add-data "cr2icon_256x256x32.png:." --add-data "CR2toX:." --icon cr2icon.icns cr2converter.py
```

You can find the .app in the dist directory

* **Alejandro La Greca** | <ale.lagreca@gmail.com> |  [Github](https://github.com/alelagreca) | [Twitter](https://twitter.com/aled_lg)
