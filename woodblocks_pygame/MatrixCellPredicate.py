from languages import predicate

class MatrixCellPredicate(predicate.Predicate):
	predicate_name: str = "matrixCell"

	def __init__(self, coordX: int, coordY: int) -> None:
		super().__init__([("coordX"),("coordY")])
		self.coordX = coordX
		self.coordY = coordY

	def get_coordX(self) -> int:
		return self.coordX

	def get_coordY(self) -> int:
		return self.coordY