import os
from languages.asp.asp_mapper import ASPMapper
from languages.asp.asp_input_program import ASPInputProgram
from platforms.desktop.desktop_handler import DesktopHandler
from specializations.dlv2.desktop.dlv2_desktop_service import DLV2DesktopService

from matrixCellPredicate import MatrixCellPredicate
from shapePredicate import ShapePredicate

# This is a test program.

# Get the current asolute path.
dirname = os.path.split(os.path.abspath(__file__))[0]

# Instantiate the Handler.
handler = DesktopHandler(DLV2DesktopService(os.path.join(dirname, "dlv.exe")))

# Register input facts to provide to DLV2.
ASPMapper.get_instance().register_class(MatrixCellPredicate)
ASPMapper.get_instance().register_class(ShapePredicate)

# Instantiate the ASP program.
inputProgram = ASPInputProgram()

# Add rules.
rules = "test(X) :- X = 2."

# Add rules to the program.
inputProgram.add_program(rules)

# Add the program to the DesktopHander.
handler.add_program(inputProgram)

# Process answer sets and get the output.
output = handler.start_sync()

# Print the output in string format.
print(output.get_output())