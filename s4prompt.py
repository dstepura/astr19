class red_panda:
	def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
		self.arm_length = arm_length
		self.leg_length = leg_length
		self.num_eyes = num_eyes
		self.has_tail = has_tail
		self.is_furry = is_furry

	def describe(self):
		print("These are a red panda's physical traits:")
		print(f"Arm length: {self.arm_length} inches")
		print(f"Leg length: {self.leg_length} inches")
		print(f"Number of eyes: {self.num_eyes}")
		print(f"Has a tail: {self.has_tail}")
		print(f"Is furry: {self.is_furry}")


def main():
	my_animal  = red_panda(
		arm_length = 11,
		leg_length = 11,
		num_eyes = 2,
		has_tail = True,
		is_furry = True
		)
	my_animal.describe()

main()