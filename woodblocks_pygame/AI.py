import os
import re

from languages.asp.asp_mapper import ASPMapper
from languages.asp.asp_input_program import ASPInputProgram
from platforms.desktop.desktop_handler import DesktopHandler
from specializations.dlv2.desktop.dlv2_desktop_service import DLV2DesktopService

from matrixCellPredicate import *
from shapePredicate import *
from shapeAggregate import *
from shapeAggregateBlock import *
from inCellPredicate import InCellPredicate

# Get the current asolute path.
dirname = os.path.split(os.path.abspath(__file__))[0]

class AI:
	def __init__(self) -> None:
		# Instantiate the Handler.
		self.handler = DesktopHandler(DLV2DesktopService(os.path.join(dirname, "dlv2.exe")))

		# Register input facts to provide to DLV2.
		ASPMapper.get_instance().register_class(MatrixCellPredicate)
		ASPMapper.get_instance().register_class(ShapePredicate)
		ASPMapper.get_instance().register_class(InCellPredicate)

	def instantiateProgram(self) -> None:
		# Instantiate the ASP program.
		self.inputProgram = ASPInputProgram()

		# Define the program's rules.
		logicProgram = open(os.path.join(dirname, "newShapeRules.lp"), "r")
		self.rules = logicProgram.read()
		logicProgram.close()

		# Add rules to the program
		self._addRules()

	def getOptimalPlace(self, matrix: list, shapes: list):
		self.instantiateProgram()

		matrixPredicates = []
		for i in range(len(matrix)):
			for j in range(len(matrix)):
				if (matrix[i][j]):
					matrixPredicates.append(MatrixCellPredicate(i, j))

		shapePredicate = ShapePredicate(0, shapes[0])

		#DEBUG
		#self.printArray(matrixPredicates)
		#self.printArray(shapePredicate)

		# Add predicates to the program
		self.inputProgram.add_objects_input(matrixPredicates)
		self.inputProgram.add_object_input(shapePredicate)

		# Add program to the handler
		self.handler.add_program(self.inputProgram)

		print(self.inputProgram)

		# Spawn DLV synchronously and get the output
		output = self.handler.start_sync()

		optimalPlacement = []

		optimalAnswerSets = output.get_optimal_answer_sets()
		#print(len(optimalAnswerSets))

		for answerSet in output.get_optimal_answer_sets():
			#print(answerSet.get_weights())
			for atom in answerSet.get_atoms():
				# Filter out inCellPredicates. The answer set contains facts, outCellPredicates etc. We are only interested in inCellPredicates.
				if isinstance(atom, InCellPredicate):
					optimalPlacement.append((atom.get_index(), atom.get_coordX(), atom.get_coordY()))

		self.inputProgram.clear_all()
		self.handler.remove_all()

		return optimalPlacement

	def getOptimalPlacement(self, matrix: list, shapes: list):
		"""
		Returns the optimal placement for a single `ShapeAggregate`, given the input matrix status.
		Returns `None` if the AS is empty (no solution).
		"""

		# Instantiate program.
		self.instantiateProgram()

		matrixPredicates = []
		for i in range(len(matrix)):
			for j in range(len(matrix)):
				if (matrix[i][j]):
					matrixPredicates.append(MatrixCellPredicate(i, j))

		shapePredicate = []
		for x in range(len(shapes)):
			shapePredicate.append(ShapePredicate(x, shapes[x][0]))

		#self.printArray(matrixPredicates)
		#self.printArray(shapePredicate)

		# Add predicates to the program
		self.inputProgram.add_objects_input(matrixPredicates)
		self.inputProgram.add_objects_input(shapePredicate)

		# Add program to the handler
		self.handler.add_program(self.inputProgram)
		print(self.inputProgram)

		# Spawn DLV synchronously and get the output
		output = self.handler.start_sync()

		optimalPlacement = []

		optimalAnswerSets = output.get_optimal_answer_sets()

		for answerSet in output.get_optimal_answer_sets():
			#print(answerSet.get_weights())
			for atom in answerSet.get_atoms():
				# Filter out inCellPredicates. The answer set contains facts, outCellPredicates etc. We are only interested in inCellPredicates.
				if isinstance(atom, InCellPredicate):
					optimalPlacement.append((atom.get_index(), atom.get_coordX(), atom.get_coordY()))

		self.inputProgram.clear_all()
		self.handler.remove_all()

		return optimalPlacement

	def getOptimalPlacements(self, matrix, shapeAggregates):
		pass

	def _addRules(self) -> None:
		self.rules = re.sub(r'\s?\n\t+', '', self.rules)
		self.inputProgram.add_program(self.rules)

	def _reset(self) -> None:
		# Remove the program from the handler
		self.handler.remove_all()
		# Remove rules and facts from the program
		self.inputProgram.clear_all()

		# Add rules back
		self._addRules()

	def printArray(self, arr: list) -> None:
		for el in arr:
			print(el)