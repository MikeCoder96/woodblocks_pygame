from shapeAggregateBlock import *

class ShapeAggregate:
	def __init__(self, rawShape: list, availableShapesIndex: int, blockSize: int) -> None:
		self.shapeAggregateBlocks = []

		for rawBlocks in rawShape:
			self.shapeAggregateBlocks.append(ShapeAggregateBlock(rawBlocks, blockSize))

		self.index = availableShapesIndex + 1 if availableShapesIndex else 1

	def get_blocks(self):
		return self.shapeAggregateBlocks

	def get_index(self):
		return self.index