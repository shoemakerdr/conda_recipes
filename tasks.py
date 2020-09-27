from pathlib import Path

from colorama import init, Fore, Style
from halo import Halo
from invoke import task, exceptions
import conda_build.api as conda_build_api
from conda_build.cli.main_build import execute as conda_build_execute
from conda_build.config import Config as CondaConfig

# colorama init
init(autoreset=True)


@task
def build(c, recipe, conda_build_args=""):
    conda_build_args = conda_build_args.split(" ") if conda_build_args else []
    print(f"building {recipe} with the following conda build args: {conda_build_args}")
    conda_build_execute([recipe, *conda_build_args])


@task
def publish(c, recipe):
    config = CondaConfig()
    config.verbose = False
    config.debug = False
    spinner = Halo(
        text=f"Deriving conda build package paths for `{recipe}` recipe...",
        spinner="dots",
    )
    spinner.start()
    package_paths = conda_build_api.get_output_file_paths(recipe, config=config)
    spinner.succeed(f"Derived the following paths: {package_paths}")

    for p in package_paths:
        if not Path(p).exists():
            raise exceptions.Exit(
                f"{Fore.RED}ERROR:{Style.RESET_ALL} Conda package path `{p}` does not exist! Please run "
                f"`$ inv build {recipe}` to build this package.",
                code=1,
            )

    packages = " ".join(package_paths)
    c.run(f"anaconda upload {packages}")
    print(f"{Fore.CYAN}Publish done!")
