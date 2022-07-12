from manimlib import *

class st(Scene):
	def construct(self):
		tex = Tex(r'\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}').scale(3)
		self.add(tex)