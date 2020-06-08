# ![Exsprite Logo](/assets/title.png)
A CLI tool for extracting sprites from spritesheets!

## Setup
#### Dependencies
```
- numpy
- scikit-image
- scipy
- fire
- matplotlib
```

#### Installation
The following will install all dependencies and create the CLI command
```
python setup.py install
```

## Usage

#### Grouping by rows
![Row Example](/assets/row_group_image.png)
```
exsprite save --filepath <path_to_sprite_sheet>
```

#### Grouping by columns
![Column Example](/assets/column_group_image.png)
```
exsprite save --filepath <path_to_sprite_sheet> --group col
```

#### Custom output folder
By default an output folder with your grouped sprite will be generated in the same dir as your spritesheet. If you'd like to control the name/location of the output folder path you can do
```
exsprite save --filepath <path_to_sprite_sheet> --folderpath <path_to_output_folder>
```
