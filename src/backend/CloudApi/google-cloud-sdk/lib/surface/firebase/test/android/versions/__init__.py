# -*- coding: utf-8 -*- #
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The 'gcloud firebase test android versions' command group."""

from __future__ import absolute_import
from __future__ import unicode_literals
from googlecloudsdk.calliope import base


class Versions(base.Group):
  """Explore Android versions available for testing."""

  detailed_help = {
      'EXAMPLES': """\
          To list information about all versions of the Android OS available
          for running tests, including details such as OS code name and
          release date, run:

            $ {command} list

          To view information about a specific Android OS version, run:

            $ {command} describe VERSION_ID
          """,
  }

  @staticmethod
  def Args(parser):
    """Method called by Calliope to register flags common to this sub-group.

    Args:
      parser: An argparse parser used to add arguments that immediately follow
          this group in the CLI. Positional arguments are allowed.
    """
