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

from pathlib import Path
from typing import Any, Dict

from ruamel.yaml import YAML


def write_yaml(filename: Path, data: Dict[str, Any]) -> str:
    yaml = YAML()
    yaml.default_flow_style = False
    with filename.open("w") as stream:
        yaml.dump(data, stream)
