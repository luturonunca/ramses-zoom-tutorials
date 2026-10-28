# Cosmological zoom-in tutorials

From a parent box to a hydrodynamical zoom-in of a Milky-Way-mass halo, with MUSIC2, RAMSES and hast. The notebooks follow the style of [ramses-tutorials](https://ramses-tutorials.readthedocs.io/en/latest/); go through its Cosmological-Volume tutorial first.

| Part | Notebook | Steps |
|---|---|---|
| 1 | [`1_parent_box_and_selection.ipynb`](Cosmological-Zoom/1_parent_box_and_selection.ipynb) | MUSIC2 parent box, RAMSES dark-matter-only run with the clump finder, hast halo selection |
| 2 | [`2_dm_zoom_and_decontamination.ipynb`](Cosmological-Zoom/2_dm_zoom_and_decontamination.ipynb) | MUSIC2 zoom ICs, RAMSES dark-matter-only zoom, hast decontamination |
| 3 | [`3_hydro_zoom.ipynb`](Cosmological-Zoom/3_hydro_zoom.ipynb) | MUSIC2 zoom ICs with baryons, RAMSES hydrodynamical zoom |

The zooms use `levelmax = 9` (effective $512^3$) so that they run on a laptop; each part ends with production settings.

## Codes

- [RAMSES](https://github.com/ramses-organisation/ramses), installed as in the Cosmological-Volume tutorial (`RAMSESPATH`).
- [MUSIC2, luturonunca fork](https://github.com/luturonunca/MUSIC2) (`MUSICPATH`): fixes an empty convex-hull refinement region with upstream MUSIC2.
- [hast3](https://github.com/luturonunca/hast3) (`HASTPATH`), plus `seaborn` and `scikit-learn`.

See section 0 of Part 1 for the installation.

## Layout

- `Cosmological-Zoom/MyFirstZoom/`: all MUSIC, RAMSES and hast configuration files used in the notebooks. Snapshots and IC binaries are not tracked.
- `Cosmological-Zoom/figures/`: figures shown in the notebooks.
- `doc/source/`: Sphinx sources to build the notebooks as HTML.
