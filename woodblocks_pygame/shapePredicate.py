from languages import predicate

class ShapePredicate(predicate.Predicate):
	predicate_name: str = "shape"

	def __init__(self, coordX: int, coordY: int, shapeIndex: int) -> None:
		super().__init__(self, [(coordX),(coordY)])
		self.predicate_name += str(shapeIndex + 1) # yields: "shape1", "shape2", "shape3"
		self.coordX = coordX
		self.coordY = coordY
