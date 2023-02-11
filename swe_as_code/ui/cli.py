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

from ._args import BuildArgs, CheckArgs, FormatArgs, InitArgs
from ._commands import build_workspace, check_workspace, format_workspace, initialize_workspace

def main() -> None:
    tap.Parser(
        tap.SubParserGroup(
            tap.SubParser(
                "build",
                BuildArgs,
                help="Build the workspace into viewable artifacts.",
            ),
            tap.SubParser(
                "check",
                CheckArgs,
                help="Check the workspace for correctness and consistency.",
            ),
            tap.SubParser(
                "format",
                FormatArgs,
                help="Format the workspace to a uniform representation.",
            ),
            tap.SubParser(
                "init",
                InitArgs,
                help="Initialize a new workspace.",
            ),
        )
    ).bind(
        build_workspace,
        check_workspace,
        format_workspace,
        initialize_workspace,
    ).run()