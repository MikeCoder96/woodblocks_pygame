from languages import predicate

class ShapePredicate(predicate.Predicate):
	predicate_name = "shape"

	def __init__(self, shapeIndex: int = None, shapeType: int = None) -> None:
		super().__init__([("index"),("type")])
		self.index = shapeIndex
		self.type = shapeType

	def get_index(self) -> int:
		return self.index

	def get_type(self) -> int:
		return self.type

	def set_index(self, index: int):
		self.index = index

	def set_type(self, type: int):
		self.type = type

	def __str__(self) -> str:
		return "(" + str(self.index) + ", " + str(self.type) + ")"
