# Solution 1
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    if fastest:
        redShirtSpeeds.sort(reverse=True)
    else:
        redShirtSpeeds.sort()

    blueShirtSpeeds.sort()

    totalSpeed = 0

    for i, x in enumerate(redShirtSpeeds):
        max = (
            redShirtSpeeds[i]
            if redShirtSpeeds[i] > blueShirtSpeeds[i]
            else blueShirtSpeeds[i]
        )
        totalSpeed += max

    return totalSpeed
