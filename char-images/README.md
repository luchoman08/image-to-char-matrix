# Prerequisites
Python 3
[Virtual env](https://help.dreamhost.com/hc/es/articles/115000695551-Instalar-y-usar-virtualenv-con-Python-3)

# Enabling the virtual environment
```bash
source venv/bin/activate
```

# Installing dependencies

```bash
pip install -r requirements.txt
```

# Using the cli
## Usage examples

```bash
# That command will create a file named `output.jpg` where the char image was created.
python cli.py generate --input-file sample-images/gentoo.png --expected-width 72
```

```bash
python cli.py generate --input-file sample-images/gentoo.png --output-file gentoo-char-image.jpg --expected-width 72
```

```bash
python cli.py generate --input-file sample-images/gentoo.png --output-file gentoo-char-image.jpg --expected-width 72 --char '#'
```

## List of commands
## generate
### Arguments
```
--input-file is the unique required argument and should be the route relative or absolute to the file to be converted.

python cli.py generate --input-file sample-images/gentoo.png </br>
In that case an image with the original resolution will be created as output.jpg
```

```
--output-file is the route and file name where the result will be stored

By default is output.jpg in the same folder where the command was executed

python cli.py generate --input-file sample-images/gentoo.png --output gentoo-char.jpg </br>

In that case an image with the original resolution will be created as gentoo-char.jpg

--expected-width is the default quantity of horizontal chars

--black-threshold is the default value between 0 and 255 value to be assumed as black.

Before the char image conversion, the input image will be converted to gray scale, where each pixel is between 0 and 255, where 0 is white and 255 is black.

--char is the char to be used in the output, by default is X
```