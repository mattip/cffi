import cffi.verifier
from .test_verify import *


def setup_module():
    cffi.verifier.local._FORCE_GENERIC_ENGINE = True
    # Runs all tests with _FORCE_GENERIC_ENGINE = True, to make sure we
    # also test vengine_gen.py.

def teardown_module():
    cffi.verifier.local._FORCE_GENERIC_ENGINE = False
