# gcode_inverter
GI is a small Python script that allows you to invert one axis in a Gcode file. This script can be used to change the direction of rotations of the perimeter, an option not available in most slicers.
Inverting the rotation of the printing of your perimeters can be useful to avoid some artifacts on the print, or simply because you want to.

## Procedure to Invert the Rotation Direction of Perimeters
The procedure consists of first creating a symmetry on one axis of your model to print. The second step is to use your favorite slicer to generate the Gcode of your symmetrical piece. The last step is to use GI to invert back your axis and enjoy a piece with a perimeter and all internal structures printed in the opposite direction.

## Using GI
To use GI, no packages are needed. Simply run the script with Python and provide two input arguments. The first one is the path to your Gcode file to invert, and the second argument corresponds to the axis to invert. GI will produce a new file with the prefix "inverted" for your convenience to discern the new Gcode.



