import math

def time_dilation(time_spaceship, velocity):
    """
    Calculate the time experienced on Earth based on the time experienced on a spaceship
    and its velocity relative to Earth.

    :param time_spaceship: Time experienced on the spaceship (in seconds, minutes, hours, etc.).
    :param velocity: Velocity of the spaceship relative to Earth (in meters per second).
    :return: Time experienced on Earth (in the same unit as time_spaceship).
    """
    c = 299792458  # Speed of light in meters per second
    time_earth = time_spaceship / math.sqrt(1 - (velocity**2 / c**2))
    return time_earth

# You can test the function with specific values for time_spaceship and velocity
# Example:

velocity = int(input("Enter Spaceship Speed ? "))
time_spaceship = int(input("Enter Time passed on the Spaceship ? "))


print ("-"*80)

print(time_dilation(time_spaceship, velocity))



