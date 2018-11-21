# Copyright 2018, The TensorFlow Federated Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for value_utils.py."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Dependency imports
import tensorflow as tf

import unittest

from tensorflow_federated.python.core.api import computations
from tensorflow_federated.python.core.api import value_base

from tensorflow_federated.python.core.impl import computation_building_context


class ComputationBuildingContextTest(unittest.TestCase):

  def test_something(self):
    context = computation_building_context.ComputationBuildingContext()
    comp = computations.tf_computation(lambda: tf.constant(10))
    result = context.invoke(comp, None)
    self.assertIsInstance(result, value_base.Value)
    self.assertEqual(str(result.type_signature), 'int32')


if __name__ == '__main__':
  unittest.main()
