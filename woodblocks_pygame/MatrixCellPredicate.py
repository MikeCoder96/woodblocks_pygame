from languages import predicate

class MatrixCellPredicate(predicate.Predicate):
	predicate_name: str = "matrixCell"

	def __init__(self, coordX: int, coordY: int) -> None:
		super().__init__(self, [(coordX),(coordY)])
		self.coordX = coordX
		self.coordY = coordY