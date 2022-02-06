import asyncio
import importlib
import inspect
import types
import typing
import os
import signal
import sys

from interop_template import config
from interop_template import interop


def signint_handler(p0, p1):
    interop.publisher.stop()
    interop.subscriber.stop()

    sys.exit(0)


async def main():
    await interop.init_app(app=config)
    await interop()


if __name__ == "__main__":

    app_module: typing.Optional[types.ModuleType] = None
    import_name: str = os.getenv("IMPORT_NAME", "")
    app_module = importlib.import_module(import_name)

    if app_module:
        dirs: typing.Iterable[str] = os.path.join(
            os.path.dirname(inspect.getfile(app_module)),
            "publishers"
        ), os.path.join(
            os.path.dirname(inspect.getfile(app_module)),
            "subscribers"
        )

        for dir in dirs:
            if os.path.isdir(dir):
                for file in os.listdir(dir):
                    dirfile: str = os.path.join(dir, file)
                    if os.path.isfile(dirfile) and dirfile.endswith(".py"):
                        importlib.import_module(
                            f"interop_template.{dir.split('/')[-1]}.{file[:-3]}"
                        )

    signal.signal(signal.SIGINT, signint_handler)
    asyncio.run(main(), debug=True)
