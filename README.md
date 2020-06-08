# ![Exsprite Logo](/assets/title.png)
A CLI tool for extracting sprites from spritesheets!

## Setup
This will install all required packages and create the cli command for use
```
python setup.py install
```

## Example usage

If you want to group your sprite sheet by rows do

```
exsprite --filepath <path_to_sprite_sheet> save
```

The default grouping is by rows, however if you'd like to group your sprite sheet by columns, do

```
exsprite --filepath <path_to_sprite_sheet> --group col save
```
By default an output folder with your grouped sprite will be generated in the same dir as your spritesheet. If yopu'd like to control the name/location of the output folder path you can do
```
exsprite --filepath <path_to_sprite_sheet> --folderpath <path_to_output_folder> save
```
