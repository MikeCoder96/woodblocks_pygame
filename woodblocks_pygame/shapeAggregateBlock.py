class ShapeAggregateBlock():
	def __init__(self, componentX: int, componentY: int, blockSize: int) -> None:
		self.componentX = int(componentX / blockSize)
		self.componentY = int(componentY / blockSize)

	def __init__(self, rawBlocks: list, blockSize: int) -> None:
		print(rawBlocks)
		self.componentX = int(rawBlocks[0] / blockSize)
		self.componentY = int(rawBlocks[1] / blockSize)

	def get_componentX(self) -> int:
		return self.componentX

	def get_componentY(self) -> int:
		return self.componentY