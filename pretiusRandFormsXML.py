import argparse
import os
import glob
import xml.etree.ElementTree as ET
import random
import re
import string
import hashlib

# create an ArgumentParser object to handle command line arguments
parser = argparse.ArgumentParser(description='Replace XML attribute values with random values')
parser.add_argument('input_pattern', type=str, help='Path to input XML file or a pattern matching multiple files')
parser.add_argument('--randomize-filenames', action='store_true', help='Randomize the output filenames')

# parse the command line arguments
args = parser.parse_args()

# get a list of input files matching the specified pattern
input_files = glob.glob(args.input_pattern)

print('Pretius Oracle Forms XML randomizer');

# replace http://www.example.com with the namespace URI you want to remove
ET.register_namespace('', 'http://xmlns.oracle.com/Forms') 

# iterate through all the input files
for input_file in input_files:
    # open the input XML file and parse it
    tree = ET.parse(input_file)
    root = tree.getroot()

    # create an output folder if it doesn't exist
    output_folder = 'output'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # regular expression pattern to match any character except '&amp;#10;'
    # pattern = '[^&](&[^#]|[^a])|[^&]'

    # iterate through all the elements in the XML tree
    for elem in root.iter():
        # iterate through all the attributes of the current element
        for attr in elem.attrib:
            # if the attribute name contains "name", replace its value with an MD5 hash as this is used in the Forms tool
            if "Name" in attr:
                attr_value = elem.get(attr)
                md5 = hashlib.md5(attr_value.encode())
                replaced_value = md5.hexdigest()
            else:
                # replace all characters in the attribute value except '&amp;#10;'
                attr_value = elem.get(attr)

                s = attr_value
                segments = s.split(r'&#10;')
                result = ""
                for i, segment in enumerate(segments):
                    if i == len(segments) - 1:
                        result += ''.join(random.choices(string.digits, k=len(segment)))
                    else:
                        result += ''.join(random.choices(string.digits, k=len(segment))) + r'&#10;'

                replaced_value = result
            
            elem.set(attr, replaced_value)

    # write the modified XML tree to the output folder
    if args.randomize_filenames:
        # generate a random filename using uppercase letters and digits
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        output_path = os.path.join(output_folder, filename + '.xml')
    else:
        # use the same filename as the input file
        output_path = os.path.join(output_folder, os.path.basename(input_file))

    # tree.write(output_path)
    tree.write(output_path, xml_declaration=True, encoding='utf-8', method='xml', default_namespace='')


    print(f'Modified XML file written to {output_path}')
