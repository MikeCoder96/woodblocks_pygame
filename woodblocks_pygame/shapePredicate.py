from languages import predicate

class ShapePredicate(predicate.Predicate):
	predicate_name = "shape"

	def __init__(self, shapeIndex: int, coordX: int, coordY: int) -> None:
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
