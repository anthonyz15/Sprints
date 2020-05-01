import re
import math

def map_converter(map_filename):
    map_file = open(map_filename)
    map_filename = map_filename[:-4]
    map3d_file = open(map_filename+ ".wrl", "w")
    result=("#VRML V2.0 utf8\n"
            "NavigationInfo {\n"
                "\theadlight TRUE\n"
                "\tavatarSize [0.3 1.6 0.5]\n"
            "}\n"
            "Viewpoint {\n"
	            "\tposition -402 5 270\n"	
                "\torientation 0 1 0 -1.50\n"	
                "\tdescription \"front\"\n"
            "}\n")
    for line in map_file:
        if line.startswith("Wall"):
            values = re.split("Wall:x1=|, y1=|, x2=|, y2=|, Height=|, Texture: ", line)
            x1 = int(values[1])
            y1 = int(values[2])
            x2 = int(values[3])
            y2 = int(values[4])
            height = int(values[5])
            texture = "\"" + values[6].strip("\n") + "\""
            #Translation
            translation_x = ((x1-683) + (x2-683))/2
            translation_y = height / 2
            translation_z = -((350-y1) + (350-y2))/2 
            #Size
            a = x2 - x1
            b = y2 - y1
            size_x = math.sqrt(a**2 + b**2)
            size_y = height
            size_z = 0.1
            #Rotation
            if a==0:
                angle=1.571
            else:
                angle = -math.atan(b/a)
            result += ("Transform {\n"
	                        "\ttranslation " + str(translation_x) + " " + str(translation_y) + " " + str(translation_z) + "\n"
                            "\trotation 0 1 0 " + str(angle) + "\n"
	                        "\tchildren [\n"
		                        "\t\tShape {\n"
			                        "\t\t\tappearance Appearance {\n"
				                        "\t\t\t\tmaterial Material {\n"
					                        "\t\t\t\t\tdiffuseColor 0 0 0\n"
					                        "\t\t\t\t\temissiveColor 0 0 0\n"
				                        "\t\t\t\t}\n"
				                        "\t\t\t\ttexture ImageTexture {\n"
					                        "\t\t\t\t\turl " + texture + "\n"
				                        "\t\t\t\t}\n"
				                        "\t\t\t\ttextureTransform TextureTransform {\n"
					                        "\t\t\t\t\tscale 1 1\n"
					                        "\t\t\t\t\trotation 0\n"
				                        "\t\t\t\t}\n"
			                        "\t\t\t}\n"
			                        "\t\t\tgeometry Box {\n"
			                            "\t\t\t\tsize " + str(size_x) + " " + str(size_y) + " " + str(size_z) + "\n"
			                        "\t\t\t}\n"
		                        "\t\t}\n"
	                        "\t]\n"
                        "}\n")

        if line.startswith("Background"):
            value = line.split("Background:")
            background = "\"" + value[1].strip("\n") + "\""
            result += ("Transform {\n"
	                        "\ttranslation 0 0 0\n"
	                        "\tchildren [\n"
		                        "\t\tShape {\n"
			                        "\t\t\tappearance Appearance {\n"
				                        "\t\t\t\tmaterial Material {\n"
					                        "\t\t\t\t\tdiffuseColor 0 0 0\n"
					                        "\t\t\t\t\temissiveColor 0 0 0\n"
				                        "\t\t\t\t}\n"
				                        "\t\t\t\ttexture ImageTexture {\n"
					                        "\t\t\t\t\turl " + background + "\n"
				                        "\t\t\t\t}\n"
				                        "\t\t\t\ttextureTransform TextureTransform {\n"
					                        "\t\t\t\t\tscale 1 1\n"
					                        "\t\t\t\t\trotation 0\n"
				                        "\t\t\t\t}\n"
			                        "\t\t\t}\n"
			                        "\t\t\tgeometry Box {\n"
			                            "\t\t\t\tsize 1366 0.1 700\n"
			                        "\t\t\t}\n"
		                        "\t\t}\n"
	                        "\t]\n"
                        "}\n")

        if line.startswith("TreeType"):
            tree_values = re.split("TreeType:|, location\(|,|\)", line) 
            tree = ""
            x = int(tree_values[2])
            y = int(tree_values[3])
            if tree_values[1] == "Tree 1":
                tree = "\"tree1.png\"" 
            elif tree_values[1] == "Tree 2":
                tree = "\"tree2.png\"" 
            elif tree_values[1] == "Tree 3":
                tree = "\"tree3.png\"" 
            tree_translation_x = x - 683
            tree_translation_z = -(350 - y)
            result += ("Transform {\n"
                        "\ttranslation " + str(tree_translation_x) + " 2 " + str(tree_translation_z) + "\n"
                        "\tchildren [\n"
                            "\t\tBillboard {\n"
                                "\t\t\tchildren [\n"
                                    "\t\t\t\tShape {\n"
                                        "\t\t\t\t\tappearance Appearance {\n"
                                            "\t\t\t\t\t\ttexture ImageTexture {\n"
                                                "\t\t\t\t\t\t\turl " + tree + "\n"
                                            "\t\t\t\t\t\t}\n"
                                        "\t\t\t\t\t}\n"
                                        "\t\t\t\t\tgeometry Box {\n"
                                            "\t\t\t\t\t\tsize 5 4 0.0001\n"
                                        "\t\t\t\t\t}\n"
                                    "\t\t\t}\n"
                                "\t\t\t]\n"
                            "\t\t}\n"
                        "\t]\n"
                    "}\n")

    map3d_file.write(result)
    map_file.close()
    map3d_file.close()