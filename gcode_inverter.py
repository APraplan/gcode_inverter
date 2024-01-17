import sys

def invert_gcode(gcode, axis):
    
    lines = gcode.split("\n")
    
    max_value = None
    min_value = None
    
    for line in lines:
        
        if line.startswith("G1"):
            
            if axis in line:
                index = line.index(axis)
                end_index = line.find(" ", index)
                
                if end_index == -1:
                    end_index = len(line)
                
                value = line[index + 1:end_index]
                
                if max_value is None:
                    max_value = float(value)
                else:
                    max_value = max(max_value, float(value))
                
                if min_value is None:
                    min_value = float(value)
                else:
                    min_value = min(min_value, float(value))
    
    offset = max_value + min_value

    for i in range(len(lines)):
        line = lines[i]
        
        if line.startswith("G1"):

            if axis in line:
                index = line.index(axis)
                end_index = line.find(" ", index)
                
                if end_index == -1:
                    end_index = len(line)
                
                value = line[index + 1:end_index]
                inverted = round(-float(value) + offset, 3)
                lines[i] = line[:index + 1] + str(inverted) + line[end_index:]
            
    modified_gcode = "\n".join(lines)
    
    return modified_gcode

if __name__ == "__main__":
    
    if len(sys.argv) < 3:
        print("Not enough arguments provided.")
        print("Usage: python gcode_inverter.py <gcode_file_path> <axis> <offset>")
        sys.exit()
    elif len(sys.argv) > 3:
        print("Too many arguments provided.")
        print("Usage: python gcode_inverter.py <gcode_file_path> <axis> <offset>")
        sys.exit()
    else:
        
        gcode_file_path = sys.argv[1]
        try:
            with open(gcode_file_path, "r") as file:
                gcode = file.read()
        except FileNotFoundError:
            print("File not found.")
            print("Usage: python gcode_inverter.py <gcode_file_path> <axis> <offset>")
            sys.exit()
        
        axis = sys.argv[2]
        if axis not in ["X", "Y", "Z"]:
            print("Invalid axis provided.")
            print("Usage: python gcode_inverter.py <gcode_file_path> <axis> <offset>")
            sys.exit()
    
    modified_gcode = invert_gcode(gcode, axis)

    new_file_path = gcode_file_path.replace(".gcode", "_inverted_" + axis + ".gcode")

    with open(new_file_path, "w") as file:
        file.write(modified_gcode)
