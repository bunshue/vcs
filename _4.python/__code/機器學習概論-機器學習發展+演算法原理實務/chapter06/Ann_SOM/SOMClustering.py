from ImageContainer import ImageContainer
from ImageContainer import ImagePattern

from SOM import SOM

if __name__ == "__main__":
    imgContainer = ImageContainer()
    imgContainer.fromDirectory("/Users/alexander/Pictures/qwe/")
    # imgContainer.analyzeAll()
    som = SOM(3, 5, 5, None)
    som.clustering(imgContainer.images)

    for image in imgContainer.images:
        print(som.coordinates(image))
