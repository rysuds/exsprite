# ![Exsprite Logo](/assets/title.png)
A CLI tool for extracting sprites from spritesheets!

## Setup
This will install all required packages and create the cli command for use
```
python setup.py install
```

## Example usage

#### Grouping by rows
![Row Example](/assets/row_group_image.png)
```
exsprite --filepath <path_to_sprite_sheet> save
```

#### Grouping by columns
![Column Example](/assets/column_group_image.png)
```
exsprite --filepath <path_to_sprite_sheet> --group col save
```

#### Custom output folder
By default an output folder with your grouped sprite will be generated in the same dir as your spritesheet. If you'd like to control the name/location of the output folder path you can do
```
exsprite --filepath <path_to_sprite_sheet> --folderpath <path_to_output_folder> save
```
