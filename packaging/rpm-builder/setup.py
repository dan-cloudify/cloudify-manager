########
# Copyright (c) 2018 Cloudify Platform Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

from setuptools import setup

setup(
    name='cloudify-rpm-builder',
    version='4.3.dev1',
    author='Cloudify Platform Ltd',
    author_email='cosmo-admin@cloudify.co',
    license='Apache License, Version 2.0',
    description='RPM build utils used by Cloudify',
    py_modules=['build_rpm.py', 'fetch_rpms.py'],
    zip_safe=False,
    install_requires=['requests'],
)