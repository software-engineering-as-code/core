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

from swe_as_code.db.layout import setup_database

from ._args import BuildArgs, CheckArgs, FormatArgs, InitArgs


def initialize_workspace(args: InitArgs) -> None:
    print(f"Initialize software engineering database in: {args.workspace_dir}")
    setup_database(args.workspace_dir)


def build_workspace(args: BuildArgs) -> None:
    ...


def check_workspace(args: CheckArgs) -> None:
    ...


def format_workspace(args: FormatArgs) -> None:
    ...
