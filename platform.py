from platformio.managers.platform import PlatformBase
from platformio.util import get_systype


class H18Platform(PlatformBase):

    @property
    def packages(self):
        packages = PlatformBase.packages.fget(self)
        if (get_systype() == "H18" and
                "toolchain-gcclinux64" in packages):
            del packages['toolchain-gcclinux64']
        return packages
