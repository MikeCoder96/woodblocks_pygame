from languages import predicate

class MatrixCellPredicate(predicate.Predicate):
	predicate_name: str = "matrixCell"

	def __init__(self, coordX: int = None, coordY: int = None) -> None:
		super().__init__([("coordX"),("coordY")])
		self.coordX = coordX
		self.coordY = coordY

	def get_coordX(self) -> int:
		return self.coordX

	def get_coordY(self) -> int:
		return self.coordY

	def set_coordX(self, coordX: int):
		self.coordX = coordX

	def set_coordY(self, coordY: int):
		self.coordY = coordY