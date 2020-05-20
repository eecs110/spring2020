# For some reason, this file is displaying linter errors, but it works.
# Frustrating.
import unittest
from test_authentication import TestAuthentication
from test_yelp import TestYelp
from test_spotify import TestSpotify


if __name__ == '__main__':
    unittest.main()

# Note: to run on command line: 
# $ tests.py -v
# $ tests.py TestAuthentication -v
# $ tests.py TestYelp -v
# $ tests.py TestSpotify -v
