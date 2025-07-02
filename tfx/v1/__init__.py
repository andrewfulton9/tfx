# Copyright 2021 Google LLC. All Rights Reserved.
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
"""Public modules for TFX."""

# pylint: disable=g-statement-before-imports,g-import-not-at-top

try:
  # These modules may not be available in some environments.
  from tfx.v1 import components, extensions, orchestration
except ImportError as e:
  # 'tfx.v1' is needed for the error during the circular dependency resolution.
  if e.name not in ['tfx.v1', 'components', 'extensions', 'orchestration']:
    raise

from tfx.v1 import dsl, proto, testing, types, utils

# Import version string.
from tfx.version import __version__
