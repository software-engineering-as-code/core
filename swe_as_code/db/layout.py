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

from swe_as_code.db.model import DatabaseConfig, Requirements, RequirementData, RequirementSource, RequirementState
from swe_as_code.db.utils import write_yaml

DATABASE_VERSION = 1

def get_config_path (workspace_dir: Path) -> Path:
    return workspace_dir / "config.yaml"


def get_requirements_dir (workspace_dir: Path) -> Path:
    return workspace_dir / "requirements"


def get_test_specifications_dir (workspace_dir: Path) -> Path:
    return workspace_dir / "test_specifications"


def _create_database_config(workspace_dir: Path) -> None:
    config_file = get_config_path(workspace_dir)
    db_config = DatabaseConfig(version=DATABASE_VERSION)
    write_yaml(config_file, db_config.dict())


def _create_requirements(workspace_dir: Path) -> None:
    requirements_dir = get_requirements_dir(workspace_dir)
    requirements_dir.mkdir(parents=True, exist_ok=True)

    requirements_file_main = requirements_dir / "main.yaml"
    main_requirements = Requirements(requirements={"a": RequirementData(component="comp", source=RequirementSource.Stakeholder, state=RequirementState.New, description="", requirement="abc", contained_in=[], derived_from=[])})
    write_yaml(requirements_file_main, main_requirements.dict())

def setup_database(workspace_dir: Path) -> None:
    workspace_dir.mkdir(parents=True, exist_ok=True)
    _create_database_config(workspace_dir)
    _create_requirements(workspace_dir)
