from pathlib import Path
import shutil

closet = Path(".")/'closet'


def put_closets_away(path_to_garments):
    for garment in path_to_garments.iterdir():
        category = garment.parts[1].rpartition(" ")[2].replace('.json', '')
        closet_section = path_to_garments / category
        closet_section.mkdir(exist_ok=True)
        hanger = closet_section / garment.parts[1]
        shutil.move(garment, hanger)

put_closets_away(closet)