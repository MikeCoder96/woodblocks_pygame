class ShapeAggregateBlock():
	def __init__(self, componentX: int, componentY: int, blockSize: int) -> None:
		self.componentX = int(componentX / blockSize)
		self.componentY = int(componentY / blockSize)

	def __init__(self, rawBlocks: list, blockSize: int) -> None:
		self.componentX = int(rawBlocks[0] / blockSize)
		self.componentY = int(rawBlocks[1] / blockSize)

	def get_componentX(self) -> int:
		"""
		Returns x-position of the single block, blockSize-agnostic.
		"""
		return self.componentX

	def get_componentY(self) -> int:
		"""
		Returns y-position of the single block, blockSize-agnostic.
		"""
		return self.componentY

	def set_componentX(self, x: int):
		self.componentX = x

	def set_componentY(self, y: int):
		self.componentY = y