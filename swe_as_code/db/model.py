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

from enum import Enum
from typing import Dict, List

from pydantic import BaseModel


class DatabaseConfig(BaseModel):
    version: int


EntityId = str


class RequirementSource(Enum):
    Internal = "internal"
    Stakeholder = "stakeholder"


class RequirementState(Enum):
    New = "new"
    Confirmed = "confirmed"
    Accepted = "accepted"


class RequirementData(BaseModel):
    component: str
    source: RequirementSource
    state: RequirementState
    description: str
    requirement: str
    contained_in: List[str]
    derived_from: List[str]


class Requirements(BaseModel):
    __root__: Dict[EntityId, RequirementData]
