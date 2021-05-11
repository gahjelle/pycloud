"""Basic smoke tests of the pycloud package"""

# PyCloud imports
import pycloud


def test_pycloud_can_be_imported():
    """Test that pycloud is properly installed and can be accessed"""
    pycloud.__version__
