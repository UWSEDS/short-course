"""
A multiline doc string begins with a single line summary (<72 chars).

The summary line may be used by automatic indexing tools; it is
important that it fits on one line and is separated from the rest of
the docstring by a blank line.
"""

import sys



Good

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# More indentation included to distinguish this from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)


Bad

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)

What to do here?

if (this_is_one_thing and
    that_is_another_thing):
    do_something()


# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting.
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()




What about here?

my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
# Versus
my_list = [
    1, 2, 3,
    4, 5, 6,
]

Pick one and be consistent!


Imports:

import os
import sys
# Versus
import os, sys



spam(ham[1], {eggs: 2})
spam( ham[ 1 ], { eggs: 2 } )


if x == 4: print x, y; x, y = y, x
if x == 4 : print x , y ; x , y = y , x


i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)


i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)



def complex(real, imag=0.0):
    return magic(r=real, i=imag)


def complex(real, imag = 0.0):
    return magic(r = real, i = imag)



if foo == 'blah': do_blah_thing()
else: do_non_blah_thing()

try: something()
finally: cleanup()

do_one(); do_two(); do_three(long, argument,
                             list, like, this)

if foo == 'blah': one(); two(); three()


list_of_prime = [...]
primes = [...]
list_of_primes = [...]
prime_list = [...]


def foo(x):
    if x >= 0:
        return math.sqrt(x)

def bar(x):
    if x < 0:
        return
    return math.sqrt(x)



def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)


if filename.endswith('zip'):

if filename[3:] == 'zip':


if not seq:
if seq:

if len(seq)
if not len(seq)


EXPECTED_RECORD_LENGTH = 5
TAXONOMY_FIELD = 4
EXPECTED_TAXONOMY_LENGTH = 8
TAXONOMY_HIERARCHY = [
    "kingdom", "phylum", "class", "order",
    "family", "genus", "species", "strain"
]
PHYLODIST_HEADER = [
    "locus_tag", "subject_locus", "subject_locus_tag", "pident"
]
IMG_DATA_DIRECTORY_NAME = "IMG_Data"
PHYLODIST_FILE_SUFFIX = "phylodist"


x = x + 1 # Increment x

    # Unit test for the sweepFiles function to test bounds
    # checking on metadata parameters.
    def test_sweepFiles_metadataType(self):
        with self.assertRaises(TypeError):
            io.sweepFiles('examples', metadata=41)

import math

# Find the square of the 3D distance.
distance_squared = (x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2
# Compute the square root of the square of the distance.
distance = math.sqrt(distance_squared);
# Make sure the distance is less than 3.5 Angstroms or error.
if distance < 3.5:
        raise Exception('distance violation',
                        'interatomic distance is less than 3.5 Angstroms')
else:
        # Add the distance to the list of distances.
        distances.append(distance)

# Find the square of the 3D distance and compute the sqrt,
#       then compare the distance to our cutoff (defined elsewhere)
#       and throw an error if the distance is too small
#       otherwise add the distance to our vector of distances.
distance_squared = (x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2
distance = math.sqrt(distance_squared);
if distance < DISTANCE_CUTOFF:
        raise Exception('distance violation',
                        'interatomic distance is less than %.2f Angstroms'
                        % DISTANCE_CUTOFF)
else:
        distances.append(distance)


def kos_root():
    """Return the pathname of the KOS root directory."""
    global _kos_root
    if _kos_root: return _kos_root


"""
CSV to TSV converter: convert CSV to Tab Separated Value format.

Usage:
    csv2tsv.py (-h | --help)
    csv2tsv.py <CSV input filename> <TSV output filename>
    csv2tsv.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

"""
Usage: my_program.py [-hso FILE] [--quiet | --verbose] [INPUT ...]

-h --help    show this
-s --sorted  sorted output
-o FILE      specify output file [default: ./test.txt]
--quiet      print less text
--verbose    print more text

"""


def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex_zero


