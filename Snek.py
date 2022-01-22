import math
import time

beginTime = time.time()
timeElapsed= 0.0 # This can be moved into the main loop to clean up the global namespace
updateWaitTime = 1 # In milliseconds

waveFrequencyMultiplier = 5 # How fast the wave will move
waveAmplitude = 25 # Size of the wave
waveOffset = waveAmplitude + 5 # How far from 0 the wave will be // We need to add the amplitude otherwise any values below it will make not noticeable influence

blankSpaceChar = "-"
snakeEnd = "*"

while(True):
    timeElapsed = (beginTime - time.time()) # Calculate how much time has passed since the script started
    spacer = str(blankSpaceChar) * round(
        abs( # Rectify the sine wave so we don't have any funny business
            math.sin(waveFrequencyMultiplier*timeElapsed) * waveAmplitude + waveOffset
        )
    )
    print(spacer + snakeEnd)
    time.sleep(updateWaitTime/1000) # Wait n milliseconds // This is a must, otherwise we get some funky fast outputs
