# Copyright 2023 Google LLC
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
"""Batch tests."""

import unittest

from clusterfuzz._internal.bot.tasks.utasks import fuzz_task
from clusterfuzz._internal.bot.tasks.utasks import regression_task
from clusterfuzz._internal.datastore import data_types
from clusterfuzz._internal.google_cloud_utils import batch
from clusterfuzz._internal.tests.test_libs import test_utils


@test_utils.with_cloud_emulators('datastore')
class GetSpecTest(unittest.TestCase):
  """Tests for get_spec."""

  def setUp(self):
    self.maxDiff = None

  def test_nonpreemptible_get_spec(self):
    """Tests that get_spec works for non-preemptibles as expected."""
    job = data_types.Job(name='libfuzzer_chrome_asan', platform='LINUX')
    job.put()
    spec = batch.get_spec(regression_task.__name__, job.name)
    expected_spec = batch.BatchJobSpec(
        docker_image='gcr.io/clusterfuzz-images/base:a2f4dd6-202202070654',
        user_data='file://linux-init.yaml',
        disk_size_gb=110,
        disk_type='pd-standard',
        service_account_email='test-clusterfuzz-service-account-email',
        subnetwork=None,
        gce_zone='gce-zone',
        project='test-clusterfuzz',
        preemptible=False,
        machine_type='n1-standard-1')

    self.assertCountEqual(spec, expected_spec)

  def test_preemptible_get_spec(self):
    """Tests that get_spec works for preemptibles as expected."""
    job = data_types.Job(name='libfuzzer_chrome_asan', platform='LINUX')
    job.put()
    spec = batch.get_spec(fuzz_task.__name__, job.name)
    expected_spec = batch.BatchJobSpec(
        docker_image='gcr.io/clusterfuzz-images/base:a2f4dd6-202202070654',
        user_data='file://linux-init.yaml',
        disk_size_gb=75,
        disk_type='pd-standard',
        service_account_email='test-clusterfuzz-service-account-email',
        subnetwork=None,
        gce_zone='gce-zone',
        project='test-clusterfuzz',
        preemptible=True,
        machine_type='n1-standard-1')

    self.assertCountEqual(spec, expected_spec)
