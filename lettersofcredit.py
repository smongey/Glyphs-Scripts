#MenuTitle: Letters of Credit
# -*- coding: utf-8 -*-
__doc__="""
Apply the spacing approach from Letters of Credit as outlined on briem.net to your current active typeface. Space n, o, v, H, O, V first.
"""

import GlyphsApp

Glyphs.clearLog() 
l = Glyphs.font.selectedLayers

hasKeyGlyphs = True
glyphs = Glyphs.font.glyphs

for g in glyphs:
	#filter by master glyphs
	n = g.name
	if (n == "H") or (n == "O") or (n == "n") or (n == "o") or (n == "v") or (n == "V"):
		paths = g.layers[0].paths[0]
		comps = g.layers[0].components[0]
		if (paths == None) and (comps == None):
			print "Draw and space ", n, " please"
			hasKeyGlyphs = False


if (hasKeyGlyphs == True):
	print "Add Metric Keys"
	for g in glyphs:
		
		if ("_part" in g.name) or ("_tail" in g.name) or ("accent" in g.name):
			continue
	
		white = 9223372036854775807
		highlight = 5  # dark green
	
		
		# color master spacing glyphs
		if (g.name == "n") or (g.name == "o") or (g.name == "v") or (g.name == "H") or (g.name == "O"):
			g.color = highlight
	
		# left and right = 'n'
		if (g.name == "m"):
			g.leftMetricsKey = "n"
			g.rightMetricsKey = "n"
			
		# left = 'n'
		if (g.name == "r") or (g.name == "b") or (g.name == "j") or (g.name == "u"):
			g.leftMetricsKey = "n"
	
		# right = 'n'
		if (g.name == "h") or (g.name == "u"):
			g.rightMetricsKey = "n"
	
		# left slightly wider 'n'
		if (g.name == "h") or (g.name == "i") or (g.name == "k") or (g.name == "l") or (g.name == "p"):
			g.leftMetricsKey = "=n+7"
	
		# right same as left 'n'
		if (g.name == "d") or (g.name == "i") or (g.name == "j") or (g.name == "l") or (g.name == "q"):
			g.rightMetricsKey = "=|n"
	
		# left = 'o'
		if (g.name == "c") or (g.name == "d") or (g.name == "e") or (g.name == "q"):
			g.leftMetricsKey = "o"
	
		# right = 'o'
		if (g.name == "b") or (g.name == "p"):
			g.rightMetricsKey = "o"
	
		# right key slight wider than 'o'
		if (g.name == "c") or (g.name == "e"):
			g.rightMetricsKey = "=o+5"
	
		# left and right = 'v'
		if (g.name == "w") or (g.name == "x") or (g.name == "x") or (g.name == "y"):
			g.rightMetricsKey = "v"
			g.leftMetricsKey = "v"
		
		# right = 'v'
		if (g.name == "k") or (g.name == "r"):
			g.rightMetricsKey = "v"
		
		# left = 'H'
		if (g.name == "B") or (g.name == "D") or (g.name == "E") or (g.name == "F") or (g.name == "I") or (g.name == "K") or (g.name == "L") or (g.name == "P") or (g.name == "R") or (g.name == "U"):
			g.leftMetricsKey = "H"

		# right = 'H'
		if (g.name == "I") or (g.name == "J") or (g.name == "M"):
			g.rightMetricsKey = "H"		

		# n narrower than 'H'
		if (g.name == "N"):
			g.rightMetricsKey = "=H-5"
			
		if (g.name == "M"):
			g.leftMetricsKey = "N"

		if (g.name == "G") or (g.name == "U"):
			g.rightMetricsKey = "N"		

		# both sides = 'H/2'
		if (g.name == "Z"):
			g.leftMetricsKey = "=H/2"
			g.rightMetricsKey = "=H/2"
		
		# right = 'H/2'
		if (g.name == "B") or (g.name == "C") or (g.name == "C") or (g.name == "E") or (g.name == "F"):
			g.rightMetricsKey = "=H/2"
		
		# left = 'O'
		if (g.name == "C") or (g.name == "G"):
			g.leftMetricsKey = "O"
		
		# right = 'O'
		if (g.name == "D") or (g.name == "P"):
			g.rightMetricsKey = "O"

		# both sides = 'V'
		if (g.name == "A") or (g.name == "T") or (g.name == "W") or (g.name == "X") or (g.name == "Y"):
			g.leftMetricsKey = "V"
			g.rightMetricsKey = "V"

		if (g.name == "J"):
			g.leftMetricsKey = "V"

		if (g.name == "K") or (g.name == "L") or (g.name == "R"):
			g.rightMetricsKey = "V"

		if(g.name == "S") or (g.name == "a") or (g.name == "f") or (g.name == "g") or (g.name == "s") or (g.name == "t") or (g.name == "z"):
			g.color = 7
			print "now space ", g.name;
		

if (hasKeyGlyphs == True):
	for g in glyphs:
	
		# update metrics
		g.layers[0].syncMetrics()
		
		# print the values
		if g.leftMetricsKey:
				leftB = g.leftMetricsKey 
		else:
			leftB = str(int(g.layers[0].LSB))
		
		if g.rightMetricsKey:
				rightB = g.rightMetricsKey 
		else:
			rightB = str(int(g.layers[0].RSB))
		
		# output metrics to log
		print leftB + "\t\t" + g.name + "\t\t" + rightB
		print " "

