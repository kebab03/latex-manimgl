from manimlib import *

class st(Scene):
	def construct(self):
		#tex = Tex(r'\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}').scale(3)
		tex1 = Tex(r"\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}")
		self.add(tex1)