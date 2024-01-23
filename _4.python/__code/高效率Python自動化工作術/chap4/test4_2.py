from pathlib import Path

p = Path(".")
p = p.joinpath("newfolder")
p.mkdir(exist_ok=True)
