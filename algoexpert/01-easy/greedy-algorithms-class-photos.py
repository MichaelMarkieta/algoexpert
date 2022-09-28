# Solution 1
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    redTaller = True if redShirtHeights[0] > blueShirtHeights[0] else False

    if redTaller:
        for i, x in enumerate(redShirtHeights):
            if x <= blueShirtHeights[i]:
                return False
    else:
        for i, x in enumerate(blueShirtHeights):
            if x <= redShirtHeights[i]:
                return False

    return True
