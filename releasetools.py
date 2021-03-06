# Copyright (C) 2012 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Custom OTA commands for msm8974-common"""

def FullOTA_InstallEnd(info):
    info.script.AppendExtra('ui_print("...Removing AudioFX...");')
    info.script.AppendExtra('run_program("/sbin/busybox", "mount", "/system");')
    info.script.AppendExtra('delete_recursive("/system/priv-app/AudioFX");')
    info.script.AppendExtra('delete_recursive("/system/app/AudioFX");')
    info.script.AppendExtra('ui_print("...Modifying build.prop...");')
    info.script.AppendExtra('run_program("/sbin/busybox", "sed", "-i -e", "s/ro.product.device=baconcaf/ro.product.device=bacon/g", "/system/build.prop");')
    info.script.AppendExtra('unmount("/system");')

