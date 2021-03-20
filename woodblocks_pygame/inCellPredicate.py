from languages.predicate import Predicate

class InCellPredicate(Predicate):
	predicate_name = "inCell"

	def __init__(self, shapeIndex: int = None, coordX: int = None, coordY: int = None) -> None:
		super().__init__([("index"),("coordX"),("coordY")])
		self.index = shapeIndex
		self.coordX = coordX
		self.coordY = coordY

	def get_index(self) -> int:
		return self.index

	def get_coordX(self) -> int:
		return self.coordX

	def get_coordY(self) -> int:
		return self.coordY

	def set_index(self, index: int):
		self.index = index

	def set_coordX(self, coordX: int):
		self.coordX = coordX

	def set_coordY(self, coordY: int):
		self.coordY = coordY
