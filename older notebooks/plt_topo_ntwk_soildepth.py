"""
Created on Sun Aug 4 
@author: YLiHD

Plot topography, channel network over topography and soil depth

### To do: write comments (input, output, ...)

"""
import copy
import matplotlib.pyplot as plt  # For plotting results; optional
import matplotlib as mpl
from landlab import imshow_grid, imshowhs_grid  # For plotting results; optional

def plt_landscape_evo(profiler,mg):

    # Set the size of the canvas
    plt.figure(figsize=(13,4))
    
    # Show topography with channel network
    cmap_terrain = copy.copy(mpl.colormaps["terrain"])
    plt.subplot(1,2,1)
    profiler.plot_profiles_in_map_view(cmap = cmap_terrain)
    
    # Show Soil thickness
    cmap_pink = copy.copy(mpl.colormaps["pink"])
    plt.subplot(1,2,2)
    imshow_grid(
        mg,
        mg.at_node["soil__depth"],
        colorbar_label="Soil depth (m) ",
        cmap=cmap_pink,
    )
    
    # Plot figure
    plt.show()