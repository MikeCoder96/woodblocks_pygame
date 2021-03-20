import os
from languages.asp.asp_mapper import ASPMapper
from languages.asp.asp_input_program import ASPInputProgram
from platforms.desktop.desktop_handler import DesktopHandler
from specializations.dlv2.desktop.dlv2_desktop_service import DLV2DesktopService

from matrixCellPredicate import *
from shapePredicate import *
from shapeAggregate import *
from shapeAggregateBlock import *

# Get the current asolute path.
dirname = os.path.split(os.path.abspath(__file__))[0]

class AI:
	def __init__(self) -> None:
		# Instantiate the Handler.
		self.handler = DesktopHandler(DLV2DesktopService(os.path.join(dirname, "dlv.exe")))

		# Register input facts to provide to DLV2.
		ASPMapper.get_instance().register_class(MatrixCellPredicate)
		ASPMapper.get_instance().register_class(ShapePredicate)

		# Instantiate the ASP program.
		self.inputProgram = ASPInputProgram()

		# Define the program's rules.
		self.rules = "test(X) :- X = 2."

		# Add rules to the program
		self._addRules()

	def getOptimalPlacement(self, matrix: list, shapeAggregate: ShapeAggregate):
		"""
		Returns the optimal placement for a single `ShapeAggregate`, given the input matrix status.
		"""

		matrixPredicates = []

		for i in range(len(matrix)):
			for j in range(len(matrix)):
				if (matrix[i][j]):
					matrixPredicates.append(MatrixCellPredicate(i, j))

		# Create the Shape predicates
		shapePredicates = []
		
		for shapeAggregateBlock in shapeAggregate.get_blocks():
			shapePredicates.append(ShapePredicate(
				shapeAggregate.get_index(), 
				shapeAggregateBlock.get_componentX(), 
				shapeAggregateBlock.get_componentY()
			))

		# Add predicates to the program
		self.inputProgram.add_objects_input(matrixPredicates)
		self.inputProgram.add_objects_input(shapePredicates)

		# Add programr to the handler
		self.handler.add_program(self.inputProgram)

		# Spawn DLV synchronously and get the output
		output = self.handler.start_sync()

		return output.get_output()

	def getOptimalPlacements(self, matrix, shapeAggregates):
		pass

	def _addRules(self) -> None:
		self.inputProgram.add_program(self.rules)

	def _reset(self) -> None:
		# Remove the program from the handler
		self.handler.remove_all()
		# Remove rules and facts from the program
		self.inputProgram.clear_all()

		# Add rules back
		self._addRules()