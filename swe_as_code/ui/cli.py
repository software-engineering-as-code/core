# Copyright 2023 Software-Engineering-as-Code
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import typed_argparse as tap

from pathlib import Path

class InitArgs(tap.TypedArgs):
    root_dir: Path = tap.arg(help="The directory to initialize.")

def initialize_workspace(args: InitArgs) -> None:
    print("Initialize")

def main() -> None:
    tap.Parser(
        tap.SubParserGroup(
            tap.SubParser(
                "init",
                InitArgs,
                help="Initialize a new workspace."
            ),
        )
    ).bind(
        initialize_workspace,
    ).run()