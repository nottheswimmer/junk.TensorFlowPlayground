def disable_avx2_warning():
    """Disables annoying warning message about unused CPU instructions.

    https://stackoverflow.com/questions/47068709/your-cpu-supports-ins
    tructions-that-this-tensorflow-binary-was-not-compiled-to-u
    """
    from os import environ
    environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
