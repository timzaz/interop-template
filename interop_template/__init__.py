import dotenv
import os
import typing

from interop import Interop

#: Set the environment variables
env_dir = None
path = dotenv.find_dotenv(".env.local", usecwd=True)

if path and env_dir is None:
    env_dir = os.path.dirname(path)
    dotenv.load_dotenv(path)

#: The remainder of the code should be run from the .env.local directory
if env_dir and os.getcwd() != env_dir:
    os.chdir(env_dir)

#: populate accordingly
#: whatever is set here is passed to every publisher and can be accessed by every
#: subscriber
config: typing.Dict[str, typing.Any] = dict()
interop = Interop(
    os.getenv("IMPORT_NAME", "interop_template"),
    os.getenv("RMQ_BROKER_URI", "")
)