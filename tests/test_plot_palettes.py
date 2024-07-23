import idpalette as idp
import matplotlib.colors as mpc
import matplotlib.pyplot as plt


def test_plot_palette():
    out_file = 'palettes.png'
    palette_names = idp._palettes().keys()
    nrows = len(palette_names)

    # Create a figure with a subplot for each palette.
    fig_width = 6
    fig_height = 4
    fig, axs = plt.subplots(nrows=nrows, figsize=(fig_width, fig_height))
    fig.set_layout_engine('tight')

    # Plot the colours in each palette.
    for ax, name in zip(axs, palette_names):
        colours = idp.idpalette(name)
        n = len(colours)
        xs = range(n)
        # Convert the hex strings into RGBA tuples for matplotlib.
        rgba = [mpc.to_rgba(c) for c in colours]
        cmap = mpc.LinearSegmentedColormap.from_list(name, rgba, N=n)
        # Show each colour in order (left to right).
        ax.imshow([xs], aspect='auto', cmap=cmap)
        # Label each subplot with the palette name.
        ax.text(
            -0.01,
            0.5,
            name,
            va='center',
            ha='right',
            fontsize=10,
            transform=ax.transAxes,
        )
        # Hide axis lines, ticks, and labels.
        ax.set_axis_off()

    fig.savefig(
        out_file,
        dpi=150,
        pil_kwargs={
            'exif': None,
            'pnginfo': None,
        },
    )
