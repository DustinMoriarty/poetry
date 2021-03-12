from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from poetry.core.packages import Package


class BaseInstaller:
    def install(self, package: "Package") -> None:
        raise NotImplementedError

    def update(self, source: "Package", target: "Package") -> None:
        raise NotImplementedError

    def remove(self, package: "Package") -> None:
        raise NotImplementedError
