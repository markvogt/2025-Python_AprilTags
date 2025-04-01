import numpy as np
import pygame

def generate_tone(frequency, duration):
    """
    Generates a tone of specified frequency and duration on Raspberry Pi.

    Args:
        frequency (float): Frequency of the tone in Hz.
        duration (float): Duration of the tone in seconds.
    """
    sample_rate = 44100  # Sampling frequency in Hz
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # Generate sine wave
    wave = (wave * 32767).astype(np.int16)  # Convert to 16-bit PCM format

    pygame.mixer.init(frequency=sample_rate, size=-16, channels=1)
    sound = pygame.sndarray.make_sound(wave)
    sound.play(-1)
    pygame.time.wait(int(duration * 1000))
    sound.stop()

# Example usage
generate_tone(440, 2)  # Generate a 440 Hz tone for 2 seconds
generate_tone(880, 2)  # Generate a 440 Hz tone for 2 seconds
generate_tone(1760, 2)  # Generate a 440 Hz tone for 2 seconds
generate_tone(440, 2)  # Generate a 440 Hz tone for 2 seconds