#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import *

def duplicate_selected_layer(image, drawable):
    # Get the active layer
    active_layer = pdb.gimp_image_get_active_layer(image)

    # Duplicate the active layer
    duplicated_layer = pdb.gimp_layer_copy(active_layer, True)
    pdb.gimp_image_insert_layer(image, duplicated_layer, None, 1)

    # Update the layer's name
    pdb.gimp_item_set_name(duplicated_layer, active_layer.name + "_copy")

    # Refresh the image
    pdb.gimp_displays_flush()

    # Alpha select the duplicated layer
    pdb.gimp_selection_layer_alpha(duplicated_layer)

    # Grow the selection by a specific amount (e.g., 10 pixels)
    grow_amount = 10
    pdb.gimp_selection_grow(image, grow_amount)

    # Set the color for filling the selection (e.g., red)
    fill_color = (255, 0, 0)  # RGB color values (red, green, blue)

    # Fill the selection with the chosen color
    pdb.gimp_edit_bucket_fill(duplicated_layer, 0, 0, 100, 0, False, 0, 0)

register(
    "python_fu_duplicate_selected_layer",
    "Duplicate Selected Layer with Alpha Selection, Grow, and Color Fill",
    "Duplicates the selected layer, performs an alpha selection, grows the selection, and fills it with a chosen color",
    "Harrou",
    "Abdelrrahmane",
    "2023",
    "<Image>/Filters/Layer/Duplicate Selected Layer with Alpha Selection, Grow, and Color Fill",
    "*",
    [],
    [],
    duplicate_selected_layer)

main()
