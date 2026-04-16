# credits_public

- Public version of Frums - Credits animation repository.
- Should be multiplatform. Feel free to raise an issue if it isn't. Feel free to raise an issue for anything.
- Tested on clean Python 3.6 (Windows 10) with minimal modules installed.

# media credits

- All animation work done by me (plaaosert)
- Renderer used is an in-progress command line rendering library for which a separate repository will be created... eventually.
- Song credit: Frums - Credits EX https://soundcloud.com/frums/credits-ex
- Song is not included in this repository. Read /media/README.txt.

# how to see

- https://youtu.be/o3cKQzrtFgQ

# how to run

 Run credits.py. Required libraries:

- just-playback https://github.com/cheofusi/just_playback

- keyboard https://github.com/boppreh/keyboard

- colorama https://github.com/tartley/colorama -
  the version of colorama used is also included inside this repository.
  You can install all required libraries by running:
  
  ```
  pip install -r requirements.txt
  ```

# play control

The player supports keyboard shortcuts for playback control during video/audio playback. All shortcuts are only active when playback is enabled (`need_update = True`):

| Key                 | Function                                                                |
| ------------------- | ----------------------------------------------------------------------- |
| `P`                 | Toggle **play/pause** (resume playback when paused, pause when playing) |
| `,` (Comma)         | Small fast forward: skip forward by `3 × beat delay` (3/8 beat)         |
| `.` (Period)        | Medium fast forward: skip forward by `7 × beat delay` (7/8 beat)        |
| `/` (Forward Slash) | Large fast forward: skip forward by `15 × beat delay` (15/8 beats)      |

### Notes

* The `delay` value is calculated based on musical tempo (BPM): `60.0/179.0/8.0`, which corresponds to the duration of 1/8 beat at 179 BPM (i.e. the BPM of Credits EX).
* All fast-forward operations jump forward relative to the current playback position.

# skipping

Press numeric keys **1 - 6** to instantly skip to predefined named sections during playback for quick scene navigation:

* `1`: Skip to **Start** (default)
* `2`: Skip to **Title** scene
* `3`: Skip to **Funding** scene
* `4`: Skip to **Loading** scene
* `5`: Skip to **Break** scene
* `6`: Skip to **Final** scene

All skip operations will immediately confirm the jump and exit the skip selection menu.


