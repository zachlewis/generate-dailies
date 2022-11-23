name = "daily"

version = "22.11.23.01"

description = "Daily is a tool to convert scene-linear openexr images into display-referred quicktime movies."

authors = ["Jed Smith", "Thomas Hollier", "Zach Lewis"]

requires = [
  "OpenImageIO-2.2+<3",
  "OpenColorIO-2.2+<3",
  "timecode",
  "pyseq",
  "PyYAML-5+",
  "Pillow-7+",
  "ffmpeg-4.4+<6",
  "numpy-1.16+<2",
  "python-3"
]

def commands():
  env.PATH.prepend('{root}/bin')

build_command = """
mkdir -p {install_path}/{{bin,data,config}}
cp -a {root}/bin {install_path}/.
cp -a {root}/data {install_path}/.
cp -a {root}/config {install_path}/.
"""


