class CryptoWarning(Warning): ...
class CryptoDeprecationWarning(DeprecationWarning, CryptoWarning): ...
class CryptoRuntimeWarning(RuntimeWarning, CryptoWarning): ...
class RandomPool_DeprecationWarning(CryptoDeprecationWarning): ...
class ClockRewindWarning(CryptoRuntimeWarning): ...
class GetRandomNumber_DeprecationWarning(CryptoDeprecationWarning): ...
class PowmInsecureWarning(CryptoRuntimeWarning): ...
