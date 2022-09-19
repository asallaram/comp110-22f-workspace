"""Example implementing a list utility function."""

# Function name: contains
# We will have 2 parameters: needle (str), haystack (list[str])
# Return type bool
# Gameplan:
# 1. Start with the first index
# 2. Loop through every index
#   2.A Test if item at indez equal to needle
#       2.A.True Return True! We found it!
# 3. False


def contains(haystack: list[str], needle: str) -> bool:
    """This function will search a list of integers for a certain integer value and return a boolean based on that."""
    i: int = 0
    track: bool = False
    while i < len(haystack) and not track:
        if haystack[i] == needle:
            track = True
        else:
            track = False
            i += 1
    return track 

print(contains(["h", "sas", "h"], "sas" ))