resolved = [
     {
          "original_rule_class": "bind",
          "original_attributes": {
               "name": "android/crosstool",
               "actual": "@bazel_tools//tools/cpp:toolchain"
          },
          "native": "bind(name = \"android/crosstool\", actual = \"@bazel_tools//tools/cpp:toolchain\")"
     },
     {
          "original_rule_class": "bind",
          "original_attributes": {
               "name": "android/d8_jar_import",
               "actual": "@bazel_tools//tools/android:no_android_sdk_repository_error"
          },
          "native": "bind(name = \"android/d8_jar_import\", actual = \"@bazel_tools//tools/android:no_android_sdk_repository_error\")"
     },
     {
          "original_rule_class": "bind",
          "original_attributes": {
               "name": "android/dx_jar_import",
               "actual": "@bazel_tools//tools/android:no_android_sdk_repository_error"
          },
          "native": "bind(name = \"android/dx_jar_import\", actual = \"@bazel_tools//tools/android:no_android_sdk_repository_error\")"
     },
     {
          "original_rule_class": "bind",
          "original_attributes": {
               "name": "android/sdk",
               "actual": "@bazel_tools//tools/android:poison_pill_android_sdk"
          },
          "native": "bind(name = \"android/sdk\", actual = \"@bazel_tools//tools/android:poison_pill_android_sdk\")"
     },
     {
          "original_rule_class": "bind",
          "original_attributes": {
               "name": "android_ndk_for_testing",
               "actual": "@bazel_tools//tools/android:empty"
          },
          "native": "bind(name = \"android_ndk_for_testing\", actual = \"@bazel_tools//tools/android:empty\")"
     },
     {
          "original_rule_class": "bind",
          "original_attributes": {
               "name": "android_sdk_for_testing",
               "actual": "@bazel_tools//tools/android:empty"
          },
          "native": "bind(name = \"android_sdk_for_testing\", actual = \"@bazel_tools//tools/android:empty\")"
     },
     {
          "original_rule_class": "local_repository",
          "original_attributes": {
               "name": "bazel_pandoc",
               "path": "../"
          },
          "native": "local_repository(name = \"bazel_pandoc\", path = \"../\")"
     },
     {
          "original_rule_class": "local_repository",
          "original_attributes": {
               "name": "bazel_tools",
               "path": "/var/tmp/_bazel_mtl/install/730b09b9d9f2bfd30b4c0a074ba23835/embedded_tools"
          },
          "native": "local_repository(name = \"bazel_tools\", path = __embedded_dir__ + \"/\" + \"embedded_tools\")"
     },
     {
          "original_rule_class": "bind",
          "original_attributes": {
               "name": "cc_toolchain",
               "actual": "@local_config_cc//:toolchain"
          },
          "native": "bind(name = \"cc_toolchain\", actual = \"@local_config_cc//:toolchain\")"
     },
     {
          "original_rule_class": "bind",
          "original_attributes": {
               "name": "databinding_annotation_processor",
               "actual": "@bazel_tools//tools/android:empty"
          },
          "native": "bind(name = \"databinding_annotation_processor\", actual = \"@bazel_tools//tools/android:empty\")"
     },
     {
          "original_rule_class": "bind",
          "original_attributes": {
               "name": "has_androidsdk",
               "actual": "@bazel_tools//tools/android:always_false"
          },
          "native": "bind(name = \"has_androidsdk\", actual = \"@bazel_tools//tools/android:always_false\")"
     },
     {
          "original_rule_class": "local_repository",
          "original_attributes": {
               "name": "pandoc_tests",
               "path": "."
          },
          "native": "local_repository(name = \"pandoc_tests\", path = \".\")"
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pandoc_bin_linux-x86_64 instantiated at:\n  /Users/mtl/Development/bazel-pandoc/tests/WORKSPACE:10:20: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_pandoc/repositories.bzl:20:17: in pandoc_repositories\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pandoc_bin_linux-x86_64",
               "generator_name": "pandoc_bin_linux-x86_64",
               "generator_function": "pandoc_repositories",
               "generator_location": None,
               "url": "https://github.com/jgm/pandoc/releases/download/2.19.2/pandoc-2.19.2-linux-amd64.tar.gz",
               "sha256": "9d55c7afb6a244e8a615451ed9cb02e6a6f187ad4d169c6d5a123fa74adb4830",
               "strip_prefix": "pandoc-2.19.2",
               "build_file_content": "\nfilegroup(\n    name = \"pandoc\",\n    srcs = [\"bin/pandoc\"],\n    visibility = [\"//visibility:public\"],\n)"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/jgm/pandoc/releases/download/2.19.2/pandoc-2.19.2-linux-amd64.tar.gz",
                         "urls": [],
                         "sha256": "9d55c7afb6a244e8a615451ed9cb02e6a6f187ad4d169c6d5a123fa74adb4830",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "pandoc-2.19.2",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "\nfilegroup(\n    name = \"pandoc\",\n    srcs = [\"bin/pandoc\"],\n    visibility = [\"//visibility:public\"],\n)",
                         "workspace_file_content": "",
                         "name": "pandoc_bin_linux-x86_64"
                    },
                    "output_tree_hash": "5f6675a7cc4f9a9065157c400f7d8a4ad6292e0df4563bbb9c41ca38100f508c"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pandoc_bin_macOS instantiated at:\n  /Users/mtl/Development/bazel-pandoc/tests/WORKSPACE:10:20: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_pandoc/repositories.bzl:28:17: in pandoc_repositories\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pandoc_bin_macOS",
               "generator_name": "pandoc_bin_macOS",
               "generator_function": "pandoc_repositories",
               "generator_location": None,
               "url": "https://github.com/jgm/pandoc/releases/download/2.19.2/pandoc-2.19.2-macOS.zip",
               "sha256": "af0cda69e31e42f01ba6adc0aa779d3e5853e6c092beeb420a4fc22712d2110b",
               "strip_prefix": "pandoc-2.19.2",
               "build_file_content": "\nfilegroup(\n    name = \"pandoc\",\n    srcs = [\"bin/pandoc\"],\n    visibility = [\"//visibility:public\"],\n)"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/jgm/pandoc/releases/download/2.19.2/pandoc-2.19.2-macOS.zip",
                         "urls": [],
                         "sha256": "af0cda69e31e42f01ba6adc0aa779d3e5853e6c092beeb420a4fc22712d2110b",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "pandoc-2.19.2",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "\nfilegroup(\n    name = \"pandoc\",\n    srcs = [\"bin/pandoc\"],\n    visibility = [\"//visibility:public\"],\n)",
                         "workspace_file_content": "",
                         "name": "pandoc_bin_macOS"
                    },
                    "output_tree_hash": "dae2a98c10ab39eb61ee3340cf8ea0d3fca37bd8eccc59cc76ed51c5ac76dbcf"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pandoc_bin_osx-arm instantiated at:\n  /Users/mtl/Development/bazel-pandoc/tests/WORKSPACE:10:20: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_pandoc/repositories.bzl:36:17: in pandoc_repositories\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pandoc_bin_osx-arm",
               "generator_name": "pandoc_bin_osx-arm",
               "generator_function": "pandoc_repositories",
               "generator_location": None,
               "url": "https://github.com/mtl-wgtwo/bazel-pandoc/releases/download/pandoc-2.19.2/pandoc-2.19.2-osx-arm.zip",
               "sha256": "9da7061f84eb09a4f21a50844bd89c74dea9c00c3c8923612e0124795c626b80",
               "strip_prefix": "pandoc-2.19.2",
               "build_file_content": "\nfilegroup(\n    name = \"pandoc\",\n    srcs = [\"bin/pandoc\"],\n    visibility = [\"//visibility:public\"],\n)"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/mtl-wgtwo/bazel-pandoc/releases/download/pandoc-2.19.2/pandoc-2.19.2-osx-arm.zip",
                         "urls": [],
                         "sha256": "9da7061f84eb09a4f21a50844bd89c74dea9c00c3c8923612e0124795c626b80",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "pandoc-2.19.2",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "\nfilegroup(\n    name = \"pandoc\",\n    srcs = [\"bin/pandoc\"],\n    visibility = [\"//visibility:public\"],\n)",
                         "workspace_file_content": "",
                         "name": "pandoc_bin_osx-arm"
                    },
                    "output_tree_hash": "c88d76b081a83e19bfcd6400039ed3b20bfa9532e1354d3408d57a00c5266771"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remote_coverage_tools instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:4:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_coverage_tools",
               "generator_name": "remote_coverage_tools",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/bazel_coverage_output_generator/releases/coverage_output_generator-v2.6.zip"
               ],
               "sha256": "7006375f6756819b7013ca875eab70a541cf7d89142d9c511ed78ea4fefa38af"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/bazel_coverage_output_generator/releases/coverage_output_generator-v2.6.zip"
                         ],
                         "sha256": "7006375f6756819b7013ca875eab70a541cf7d89142d9c511ed78ea4fefa38af",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remote_coverage_tools"
                    },
                    "output_tree_hash": "57d60737c04d254ee04aadf408f7df77c4fe893357e74dc049c7319224e141c7"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:local_java_repository.bzl%_local_java_repository_rule",
          "definition_information": "Repository local_jdk instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:31:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/local_java_repository.bzl:223:32: in local_java_repository\nRepository rule _local_java_repository_rule defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/local_java_repository.bzl:194:46: in <toplevel>\n",
          "original_attributes": {
               "name": "local_jdk",
               "generator_name": "local_jdk",
               "generator_function": "maybe",
               "generator_location": None,
               "java_home": "/Library/Java/JavaVirtualMachines/jdk-18.jdk/Contents/Home",
               "version": "",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:local_java_repository.bzl%_local_java_repository_rule",
                    "attributes": {
                         "name": "local_jdk",
                         "generator_name": "local_jdk",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "java_home": "/Library/Java/JavaVirtualMachines/jdk-18.jdk/Contents/Home",
                         "version": "",
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
                    },
                    "output_tree_hash": "649a5043af419ed765ab78d134fe4b0cb3d2c52c03718589d9b64271cc24187d"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remote_java_tools instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:363:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_java_tools",
               "generator_name": "remote_java_tools",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/bazel_java_tools/releases/java/v11.9/java_tools-v11.9.zip",
                    "https://github.com/bazelbuild/java_tools/releases/download/java_v11.9/java_tools-v11.9.zip"
               ],
               "sha256": "5cd59ea6bf938a1efc1e11ea562d37b39c82f76781211b7cd941a2346ea8484d"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/bazel_java_tools/releases/java/v11.9/java_tools-v11.9.zip",
                              "https://github.com/bazelbuild/java_tools/releases/download/java_v11.9/java_tools-v11.9.zip"
                         ],
                         "sha256": "5cd59ea6bf938a1efc1e11ea562d37b39c82f76781211b7cd941a2346ea8484d",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remote_java_tools"
                    },
                    "output_tree_hash": "1115931c413c6e769c94c09c05fc63b580d28c399ab5507ba7267852d1eb082d"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remote_java_tools_darwin instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:393:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_java_tools_darwin",
               "generator_name": "remote_java_tools_darwin",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/bazel_java_tools/releases/java/v11.9/java_tools_darwin-v11.9.zip",
                    "https://github.com/bazelbuild/java_tools/releases/download/java_v11.9/java_tools_darwin-v11.9.zip"
               ],
               "sha256": "b9e962c6a836ba1d7573f2473fab3a897c6370d4c2724bde4017b40932ff4fe4"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/bazel_java_tools/releases/java/v11.9/java_tools_darwin-v11.9.zip",
                              "https://github.com/bazelbuild/java_tools/releases/download/java_v11.9/java_tools_darwin-v11.9.zip"
                         ],
                         "sha256": "b9e962c6a836ba1d7573f2473fab3a897c6370d4c2724bde4017b40932ff4fe4",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remote_java_tools_darwin"
                    },
                    "output_tree_hash": "9c569cfb3af9ae614ee97cbe132ac190398a07d9b6423aa1cd3a036e01a48aed"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remote_java_tools_linux instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:373:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_java_tools_linux",
               "generator_name": "remote_java_tools_linux",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/bazel_java_tools/releases/java/v11.9/java_tools_linux-v11.9.zip",
                    "https://github.com/bazelbuild/java_tools/releases/download/java_v11.9/java_tools_linux-v11.9.zip"
               ],
               "sha256": "512582cac5b7ea7974a77b0da4581b21f546c9478f206eedf54687eeac035989"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/bazel_java_tools/releases/java/v11.9/java_tools_linux-v11.9.zip",
                              "https://github.com/bazelbuild/java_tools/releases/download/java_v11.9/java_tools_linux-v11.9.zip"
                         ],
                         "sha256": "512582cac5b7ea7974a77b0da4581b21f546c9478f206eedf54687eeac035989",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remote_java_tools_linux"
                    },
                    "output_tree_hash": "4f9efcd897d73b088fa5de3c64657a0270bf177fc48c24e562503e7089a32c15"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remote_java_tools_windows instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:383:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_java_tools_windows",
               "generator_name": "remote_java_tools_windows",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/bazel_java_tools/releases/java/v11.9/java_tools_windows-v11.9.zip",
                    "https://github.com/bazelbuild/java_tools/releases/download/java_v11.9/java_tools_windows-v11.9.zip"
               ],
               "sha256": "677ab910046205020fd715489147c2bcfad8a35d9f5d94fdc998d217545bd87a"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/bazel_java_tools/releases/java/v11.9/java_tools_windows-v11.9.zip",
                              "https://github.com/bazelbuild/java_tools/releases/download/java_v11.9/java_tools_windows-v11.9.zip"
                         ],
                         "sha256": "677ab910046205020fd715489147c2bcfad8a35d9f5d94fdc998d217545bd87a",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remote_java_tools_windows"
                    },
                    "output_tree_hash": "87b3c75ee461ea6c90fc44e8f17da04f6f3f020af3a254ff52abcfd7e0154d04"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk11_linux instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:45:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux",
               "generator_name": "remotejdk11_linux",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-linux_x64.tar.gz",
                    "https://cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-linux_x64.tar.gz"
               ],
               "sha256": "e064b61d93304012351242bf0823c6a2e41d9e28add7ea7f05378b7243d34247",
               "strip_prefix": "zulu11.56.19-ca-jdk11.0.15-linux_x64",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-linux_x64.tar.gz",
                              "https://cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-linux_x64.tar.gz"
                         ],
                         "sha256": "e064b61d93304012351242bf0823c6a2e41d9e28add7ea7f05378b7243d34247",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu11.56.19-ca-jdk11.0.15-linux_x64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk11_linux"
                    },
                    "output_tree_hash": "31a3ef62c67176122d2b57b153234dfd210fe77c94934da8b847d305f1cdd5c4"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk11_linux_aarch64 instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:61:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_aarch64",
               "generator_name": "remotejdk11_linux_aarch64",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/cdn.azul.com/zulu-embedded/bin/zulu11.56.19-ca-jdk11.0.15-linux_aarch64.tar.gz",
                    "https://cdn.azul.com/zulu-embedded/bin/zulu11.56.19-ca-jdk11.0.15-linux_aarch64.tar.gz"
               ],
               "sha256": "fc7c41a0005180d4ca471c90d01e049469e0614cf774566d4cf383caa29d1a97",
               "strip_prefix": "zulu11.56.19-ca-jdk11.0.15-linux_aarch64",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/cdn.azul.com/zulu-embedded/bin/zulu11.56.19-ca-jdk11.0.15-linux_aarch64.tar.gz",
                              "https://cdn.azul.com/zulu-embedded/bin/zulu11.56.19-ca-jdk11.0.15-linux_aarch64.tar.gz"
                         ],
                         "sha256": "fc7c41a0005180d4ca471c90d01e049469e0614cf774566d4cf383caa29d1a97",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu11.56.19-ca-jdk11.0.15-linux_aarch64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk11_linux_aarch64"
                    },
                    "output_tree_hash": "0963f22389d0c9318d8687853fe1d415bf4256537dac2b85522035647575096c"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:61:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "f817d64408c5484cf564d5fdc24f11c3f601835818645f6de7ab4c56eaf4056f"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk11_linux_ppc64le instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:77:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_ppc64le",
               "generator_name": "remotejdk11_linux_ppc64le",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.15+10/OpenJDK11U-jdk_ppc64le_linux_hotspot_11.0.15_10.tar.gz",
                    "https://github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.15+10/OpenJDK11U-jdk_ppc64le_linux_hotspot_11.0.15_10.tar.gz"
               ],
               "sha256": "a8fba686f6eb8ae1d1a9566821dbd5a85a1108b96ad857fdbac5c1e4649fc56f",
               "strip_prefix": "jdk-11.0.15+10",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.15+10/OpenJDK11U-jdk_ppc64le_linux_hotspot_11.0.15_10.tar.gz",
                              "https://github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.15+10/OpenJDK11U-jdk_ppc64le_linux_hotspot_11.0.15_10.tar.gz"
                         ],
                         "sha256": "a8fba686f6eb8ae1d1a9566821dbd5a85a1108b96ad857fdbac5c1e4649fc56f",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "jdk-11.0.15+10",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk11_linux_ppc64le"
                    },
                    "output_tree_hash": "cb966d2c1f4374b581792eeea90c32200a312175b9a3e7c61a95df371e6bffa3"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_ppc64le_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:77:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "b5938368c9f92a6f5045ffca11214afb8ec9256686bec9245714376aa66b67d1"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk11_linux_s390x instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_s390x",
               "generator_name": "remotejdk11_linux_s390x",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.15+10/OpenJDK11U-jdk_s390x_linux_hotspot_11.0.15_10.tar.gz",
                    "https://github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.15+10/OpenJDK11U-jdk_s390x_linux_hotspot_11.0.15_10.tar.gz"
               ],
               "sha256": "a58fc0361966af0a5d5a31a2d8a208e3c9bb0f54f345596fd80b99ea9a39788b",
               "strip_prefix": "jdk-11.0.15+10",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.15+10/OpenJDK11U-jdk_s390x_linux_hotspot_11.0.15_10.tar.gz",
                              "https://github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.15+10/OpenJDK11U-jdk_s390x_linux_hotspot_11.0.15_10.tar.gz"
                         ],
                         "sha256": "a58fc0361966af0a5d5a31a2d8a208e3c9bb0f54f345596fd80b99ea9a39788b",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "jdk-11.0.15+10",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk11_linux_s390x"
                    },
                    "output_tree_hash": "6173908f761f4561b6f89e7b01f9c2f2f3efb7bd59200b924d0b2eda50f863a1"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_s390x_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_s390x_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_s390x_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_s390x_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_s390x_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "10df692cd4259131687761221fcb989c660f1c6e9376feba066b4fdc80bdc048"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:45:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "8e1033ec85367ff2067aa4aa175c76d9cab0f81b9d0d4f10b7743e953331b892"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk11_macos instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:109:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_macos",
               "generator_name": "remotejdk11_macos",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-macosx_x64.tar.gz",
                    "https://cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-macosx_x64.tar.gz"
               ],
               "sha256": "2614e5c5de8e989d4d81759de4c333aa5b867b17ab9ee78754309ba65c7f6f55",
               "strip_prefix": "zulu11.56.19-ca-jdk11.0.15-macosx_x64",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-macosx_x64.tar.gz",
                              "https://cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-macosx_x64.tar.gz"
                         ],
                         "sha256": "2614e5c5de8e989d4d81759de4c333aa5b867b17ab9ee78754309ba65c7f6f55",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu11.56.19-ca-jdk11.0.15-macosx_x64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk11_macos"
                    },
                    "output_tree_hash": "f7d4b757b94681b27656b9e7f2b189ed647f3cff205a59389c24aee1624b9eb7"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk11_macos_aarch64 instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:125:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_macos_aarch64",
               "generator_name": "remotejdk11_macos_aarch64",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-macosx_aarch64.tar.gz",
                    "https://cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-macosx_aarch64.tar.gz"
               ],
               "sha256": "6bb0d2c6e8a29dcd9c577bbb2986352ba12481a9549ac2c0bcfd00ed60e538d2",
               "strip_prefix": "zulu11.56.19-ca-jdk11.0.15-macosx_aarch64",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-macosx_aarch64.tar.gz",
                              "https://cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-macosx_aarch64.tar.gz"
                         ],
                         "sha256": "6bb0d2c6e8a29dcd9c577bbb2986352ba12481a9549ac2c0bcfd00ed60e538d2",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu11.56.19-ca-jdk11.0.15-macosx_aarch64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk11_macos_aarch64"
                    },
                    "output_tree_hash": "98a2e160e45c3c7a5e854952da5b40d9262a1f6cbbf19fe5b36989e0eb145ed2"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:125:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk11_macos_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk11_macos_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "a762e337f24b8b511c520c1101b81cc02082e3fd25e58140dfa47eb7342161ce"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:109:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_macos_toolchain_config_repo",
               "generator_name": "remotejdk11_macos_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_macos_toolchain_config_repo",
                         "generator_name": "remotejdk11_macos_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "4b40216fabc2f6c17810749b3bf713065a39e05ff547dac45c395be6391709af"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk11_win instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:141:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_win",
               "generator_name": "remotejdk11_win",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-win_x64.zip",
                    "https://cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-win_x64.zip"
               ],
               "sha256": "a106c77389a63b6bd963a087d5f01171bd32aa3ee7377ecef87531390dcb9050",
               "strip_prefix": "zulu11.56.19-ca-jdk11.0.15-win_x64",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-win_x64.zip",
                              "https://cdn.azul.com/zulu/bin/zulu11.56.19-ca-jdk11.0.15-win_x64.zip"
                         ],
                         "sha256": "a106c77389a63b6bd963a087d5f01171bd32aa3ee7377ecef87531390dcb9050",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu11.56.19-ca-jdk11.0.15-win_x64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk11_win"
                    },
                    "output_tree_hash": "542e25127f50335efd2e3dc0992c085593af01829a202fd1b5a17a86988322ae"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk11_win_arm64 instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:157:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_win_arm64",
               "generator_name": "remotejdk11_win_arm64",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/aka.ms/download-jdk/microsoft-jdk-11.0.13.8.1-windows-aarch64.zip"
               ],
               "sha256": "b8a28e6e767d90acf793ea6f5bed0bb595ba0ba5ebdf8b99f395266161e53ec2",
               "strip_prefix": "jdk-11.0.13+8",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/aka.ms/download-jdk/microsoft-jdk-11.0.13.8.1-windows-aarch64.zip"
                         ],
                         "sha256": "b8a28e6e767d90acf793ea6f5bed0bb595ba0ba5ebdf8b99f395266161e53ec2",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "jdk-11.0.13+8",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk11_win_arm64"
                    },
                    "output_tree_hash": "b2cedc1ddcba552ee316af0254dc50a35b9457d5b3ed91e3157845b722a0bf6f"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:157:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk11_win_arm64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk11_win_arm64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "383e78f7a5b828401c8b5a470bc3676797a189fe9641856f243c35e282e4384c"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:141:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_win_toolchain_config_repo",
               "generator_name": "remotejdk11_win_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_win_toolchain_config_repo",
                         "generator_name": "remotejdk11_win_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "f6c7a48666a77c098017285e46d511074ce3de7ff4e9808bc592fd49228681b2"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk17_linux instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:173:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux",
               "generator_name": "remotejdk17_linux",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-linux_x64.tar.gz",
                    "https://cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-linux_x64.tar.gz"
               ],
               "sha256": "73d5c4bae20325ca41b606f7eae64669db3aac638c5b3ead4a975055846ad6de",
               "strip_prefix": "zulu17.32.13-ca-jdk17.0.2-linux_x64",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-linux_x64.tar.gz",
                              "https://cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-linux_x64.tar.gz"
                         ],
                         "sha256": "73d5c4bae20325ca41b606f7eae64669db3aac638c5b3ead4a975055846ad6de",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu17.32.13-ca-jdk17.0.2-linux_x64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk17_linux"
                    },
                    "output_tree_hash": "cba9fbf237e05b5cb295953824783f837b713d7d3a6912442d50a29baeeed159"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk17_linux_aarch64 instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:189:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_aarch64",
               "generator_name": "remotejdk17_linux_aarch64",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-linux_aarch64.tar.gz",
                    "https://cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-linux_aarch64.tar.gz"
               ],
               "sha256": "2b8066bbdbc5cff422bb6b6db1b8f8d362b576340cce8492f1255502af632b06",
               "strip_prefix": "zulu17.32.13-ca-jdk17.0.2-linux_aarch64",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-linux_aarch64.tar.gz",
                              "https://cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-linux_aarch64.tar.gz"
                         ],
                         "sha256": "2b8066bbdbc5cff422bb6b6db1b8f8d362b576340cce8492f1255502af632b06",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu17.32.13-ca-jdk17.0.2-linux_aarch64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk17_linux_aarch64"
                    },
                    "output_tree_hash": "296806f53babc4d1113c78952ead3cd6a989284ede228dc2e195357990b6ce05"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:189:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "57763b4c6342c2729b70ccf1676a75726a4775a6e6468c86462f7247c968ecd7"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:173:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "9cd805ebc7702094002f5373bee54fb0b9bba1ece881b83ff48c0586ddaa10d5"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk17_macos instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:205:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_macos",
               "generator_name": "remotejdk17_macos",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-macosx_x64.tar.gz",
                    "https://cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-macosx_x64.tar.gz"
               ],
               "sha256": "89d04b2d99b05dcb25114178e65f6a1c5ca742e125cab0a63d87e7e42f3fcb80",
               "strip_prefix": "zulu17.32.13-ca-jdk17.0.2-macosx_x64",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-macosx_x64.tar.gz",
                              "https://cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-macosx_x64.tar.gz"
                         ],
                         "sha256": "89d04b2d99b05dcb25114178e65f6a1c5ca742e125cab0a63d87e7e42f3fcb80",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu17.32.13-ca-jdk17.0.2-macosx_x64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk17_macos"
                    },
                    "output_tree_hash": "ce3f1df2b92c12d38a1169163dc9c861c926bb9739bf53c5c830b2e9ed23e753"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk17_macos_aarch64 instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:221:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_macos_aarch64",
               "generator_name": "remotejdk17_macos_aarch64",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-macosx_aarch64.tar.gz",
                    "https://cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-macosx_aarch64.tar.gz"
               ],
               "sha256": "54247dde248ffbcd3c048675504b1c503b81daf2dc0d64a79e353c48d383c977",
               "strip_prefix": "zulu17.32.13-ca-jdk17.0.2-macosx_aarch64",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-macosx_aarch64.tar.gz",
                              "https://cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-macosx_aarch64.tar.gz"
                         ],
                         "sha256": "54247dde248ffbcd3c048675504b1c503b81daf2dc0d64a79e353c48d383c977",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu17.32.13-ca-jdk17.0.2-macosx_aarch64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk17_macos_aarch64"
                    },
                    "output_tree_hash": "a5d84bb66c16f32a04325efd86bf90cb43f0076b72f6f3358dcbe4b187a9d90e"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:221:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk17_macos_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk17_macos_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "f698cb98820064a11248ba634c70c6df5b57382ee5f8a1b589007e5b73bfc6f8"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:205:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_macos_toolchain_config_repo",
               "generator_name": "remotejdk17_macos_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_macos_toolchain_config_repo",
                         "generator_name": "remotejdk17_macos_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "8fc6087c6e654d2ff8ce626db7d0902fcf08d111f3c9f737ab19355b67d59c80"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk17_win instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:237:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_win",
               "generator_name": "remotejdk17_win",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-win_x64.zip",
                    "https://cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-win_x64.zip"
               ],
               "sha256": "e965aa0ea7a0661a3446cf8f10ee00684b851f883b803315289f26b4aa907fdb",
               "strip_prefix": "zulu17.32.13-ca-jdk17.0.2-win_x64",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-win_x64.zip",
                              "https://cdn.azul.com/zulu/bin/zulu17.32.13-ca-jdk17.0.2-win_x64.zip"
                         ],
                         "sha256": "e965aa0ea7a0661a3446cf8f10ee00684b851f883b803315289f26b4aa907fdb",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu17.32.13-ca-jdk17.0.2-win_x64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk17_win"
                    },
                    "output_tree_hash": "55802834cd35a78dc3bfd3b1a581be7ee184d1aa1faae55b2aed3f678dfc7b68"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk17_win_arm64 instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:252:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_win_arm64",
               "generator_name": "remotejdk17_win_arm64",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu17.30.15-ca-jdk17.0.1-win_aarch64.zip",
                    "https://cdn.azul.com/zulu/bin/zulu17.30.15-ca-jdk17.0.1-win_aarch64.zip"
               ],
               "sha256": "811d7e7591bac4f081dfb00ba6bd15b6fc5969e1f89f0f327ef75147027c3877",
               "strip_prefix": "zulu17.30.15-ca-jdk17.0.1-win_aarch64",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu17.30.15-ca-jdk17.0.1-win_aarch64.zip",
                              "https://cdn.azul.com/zulu/bin/zulu17.30.15-ca-jdk17.0.1-win_aarch64.zip"
                         ],
                         "sha256": "811d7e7591bac4f081dfb00ba6bd15b6fc5969e1f89f0f327ef75147027c3877",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu17.30.15-ca-jdk17.0.1-win_aarch64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk17_win_arm64"
                    },
                    "output_tree_hash": "024ad1288f60a842f66b6bc2190dc9af23f48b16ef5ed113f66f48e55a4cca3a"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:252:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk17_win_arm64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk17_win_arm64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "78dfb0f7dab651cbc675d9dfe42e28b363ec26c3e5dc9a57b94833852f91deda"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:237:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_win_toolchain_config_repo",
               "generator_name": "remotejdk17_win_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_win_toolchain_config_repo",
                         "generator_name": "remotejdk17_win_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "224a8c9f9e2f5e5cbb9efff01aa2555019675d3e1c9b93a7b4a83dfd7f5b69d5"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk18_linux instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:268:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_linux",
               "generator_name": "remotejdk18_linux",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-linux_x64.tar.gz",
                    "https://cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-linux_x64.tar.gz"
               ],
               "sha256": "959a94ca4097dcaabc7886784cec10dfdf2b0a3bff890ea8943cc09c5fff29cb",
               "strip_prefix": "zulu18.28.13-ca-jdk18.0.0-linux_x64",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-linux_x64.tar.gz",
                              "https://cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-linux_x64.tar.gz"
                         ],
                         "sha256": "959a94ca4097dcaabc7886784cec10dfdf2b0a3bff890ea8943cc09c5fff29cb",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu18.28.13-ca-jdk18.0.0-linux_x64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk18_linux"
                    },
                    "output_tree_hash": "d1cf20a2182ae94a5334fd0af7fd01fdbafdd45c4120cabfb221eaeb4adcfcfc"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk18_linux_aarch64 instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:284:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_linux_aarch64",
               "generator_name": "remotejdk18_linux_aarch64",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-linux_aarch64.tar.gz",
                    "https://cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-linux_aarch64.tar.gz"
               ],
               "sha256": "a1d5f78172f32f819d08e9043b0f82fa7af738b37c55c6ca8d6092c61d204d53",
               "strip_prefix": "zulu18.28.13-ca-jdk18.0.0-linux_aarch64",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-linux_aarch64.tar.gz",
                              "https://cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-linux_aarch64.tar.gz"
                         ],
                         "sha256": "a1d5f78172f32f819d08e9043b0f82fa7af738b37c55c6ca8d6092c61d204d53",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu18.28.13-ca-jdk18.0.0-linux_aarch64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk18_linux_aarch64"
                    },
                    "output_tree_hash": "e7146a465f3ae55f943ad4594a1d578cd3c259526c34d7d1db986c645c5d42e0"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:284:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk18_linux_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk18_linux_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "0492adccec49cb7fafa99a8da0a43c1ecf77d62d15c2213ced41f7dd06d2a40f"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:268:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_linux_toolchain_config_repo",
               "generator_name": "remotejdk18_linux_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_linux_toolchain_config_repo",
                         "generator_name": "remotejdk18_linux_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "7b4e118acc67f0ab2e764a34c9081459f46ecf83ede0abcb03fdbe4959b9033e"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk18_macos instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:300:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_macos",
               "generator_name": "remotejdk18_macos",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-macosx_x64.tar.gz",
                    "https://cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-macosx_x64.tar.gz"
               ],
               "sha256": "780a9aa4bda95a6793bf41d13f837c59ef915e9bfd0e0c5fd4c70e4cdaa88541",
               "strip_prefix": "zulu18.28.13-ca-jdk18.0.0-macosx_x64",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-macosx_x64.tar.gz",
                              "https://cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-macosx_x64.tar.gz"
                         ],
                         "sha256": "780a9aa4bda95a6793bf41d13f837c59ef915e9bfd0e0c5fd4c70e4cdaa88541",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu18.28.13-ca-jdk18.0.0-macosx_x64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk18_macos"
                    },
                    "output_tree_hash": "9fd71fb700b8f808b6d458e7f0867ad5bb6927f86a70829a2e1ea85a6e0b3c0c"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk18_macos_aarch64 instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:316:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_macos_aarch64",
               "generator_name": "remotejdk18_macos_aarch64",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-macosx_aarch64.tar.gz",
                    "https://cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-macosx_aarch64.tar.gz"
               ],
               "sha256": "9595e001451e201fdf33c1952777968a3ac18fe37273bdeaea5b5ed2c4950432",
               "strip_prefix": "zulu18.28.13-ca-jdk18.0.0-macosx_aarch64",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-macosx_aarch64.tar.gz",
                              "https://cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-macosx_aarch64.tar.gz"
                         ],
                         "sha256": "9595e001451e201fdf33c1952777968a3ac18fe37273bdeaea5b5ed2c4950432",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu18.28.13-ca-jdk18.0.0-macosx_aarch64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk18_macos_aarch64"
                    },
                    "output_tree_hash": "7c3b6aa25364200e555b7d0112452c6ed3d7a3f20902070a8746e8b248505785"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:316:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk18_macos_aarch64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk18_macos_aarch64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "d088fdffd2f9c3a6cdefd249980df8b6b1ac0240cb5a1e7c67655ed2f181d0fb"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:300:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_macos_toolchain_config_repo",
               "generator_name": "remotejdk18_macos_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_macos_toolchain_config_repo",
                         "generator_name": "remotejdk18_macos_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "195ddef2a390e6ceebe003a0f2ede89a2962723d5e89c88fc6f1203d84eec1c5"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk18_win instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:332:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_win",
               "generator_name": "remotejdk18_win",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-win_x64.zip",
                    "https://cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-win_x64.zip"
               ],
               "sha256": "6c75498163b047595386fdb909cb6d4e04282c3a81799743c5e1f9316391fe16",
               "strip_prefix": "zulu18.28.13-ca-jdk18.0.0-win_x64",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-win_x64.zip",
                              "https://cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-win_x64.zip"
                         ],
                         "sha256": "6c75498163b047595386fdb909cb6d4e04282c3a81799743c5e1f9316391fe16",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu18.28.13-ca-jdk18.0.0-win_x64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk18_win"
                    },
                    "output_tree_hash": "31b87e2fda9c590f8db6524a2517b611d21cb876e7e8d40f1471b4b18eb1238d"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository remotejdk18_win_arm64 instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:348:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:48:17: in remote_java_repository\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_win_arm64",
               "generator_name": "remotejdk18_win_arm64",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-win_aarch64.zip",
                    "https://cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-win_aarch64.zip"
               ],
               "sha256": "9b52b259516e4140ee56b91f77750667bffbc543e78ad8c39082449d4c377b54",
               "strip_prefix": "zulu18.28.13-ca-jdk18.0.0-win_aarch64",
               "build_file": "@bazel_tools//tools/jdk:jdk.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-win_aarch64.zip",
                              "https://cdn.azul.com/zulu/bin/zulu18.28.13-ca-jdk18.0.0-win_aarch64.zip"
                         ],
                         "sha256": "9b52b259516e4140ee56b91f77750667bffbc543e78ad8c39082449d4c377b54",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zulu18.28.13-ca-jdk18.0.0-win_aarch64",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@bazel_tools//tools/jdk:jdk.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "remotejdk18_win_arm64"
                    },
                    "output_tree_hash": "93ca5b7069de3517ca09c6203f5e88a286a2864509c865c9e8f3a01cfe0b1939"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:348:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk18_win_arm64_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk18_win_arm64_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "bb8b23eb4ea8b42cec8fd2e3752c459811f8944d1b9c66b71d53f693f71c52c7"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk18_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:332:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:53:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/jdk/remote_java_repository.bzl:26:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk18_win_toolchain_config_repo",
               "generator_name": "remotejdk18_win_toolchain_config_repo",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/jdk:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk18_win_toolchain_config_repo",
                         "generator_name": "remotejdk18_win_toolchain_config_repo",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_18\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"18\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk18_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "0fbe406ef93edfa2dd63ecbec5eb91b55150360ebda0981365494b89015f6d4e"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_cc instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:414:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_cc",
               "generator_name": "rules_cc",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_cc/releases/download/0.0.2/rules_cc-0.0.2.tar.gz"
               ],
               "sha256": "58bff40957ace85c2de21ebfc72e53ed3a0d33af8cc20abd0ceec55c63be7de2"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_cc/releases/download/0.0.2/rules_cc-0.0.2.tar.gz"
                         ],
                         "sha256": "58bff40957ace85c2de21ebfc72e53ed3a0d33af8cc20abd0ceec55c63be7de2",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_cc"
                    },
                    "output_tree_hash": "d1aae5466714ed8166cc876175f2ed95ce245b5318420f9ecba8201cbb68ff26"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_java instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:403:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java",
               "generator_name": "rules_java",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/github.com/bazelbuild/rules_java/archive/7cf3cefd652008d0a64a419c34c13bdca6c8f178.zip",
                    "https://github.com/bazelbuild/rules_java/archive/7cf3cefd652008d0a64a419c34c13bdca6c8f178.zip"
               ],
               "sha256": "bc81f1ba47ef5cc68ad32225c3d0e70b8c6f6077663835438da8d5733f917598",
               "strip_prefix": "rules_java-7cf3cefd652008d0a64a419c34c13bdca6c8f178"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/github.com/bazelbuild/rules_java/archive/7cf3cefd652008d0a64a419c34c13bdca6c8f178.zip",
                              "https://github.com/bazelbuild/rules_java/archive/7cf3cefd652008d0a64a419c34c13bdca6c8f178.zip"
                         ],
                         "sha256": "bc81f1ba47ef5cc68ad32225c3d0e70b8c6f6077663835438da8d5733f917598",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_java-7cf3cefd652008d0a64a419c34c13bdca6c8f178",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_java"
                    },
                    "output_tree_hash": "00a0f1231dacff0b0cea3886200e0158c67a3600068275da14120f5434f83b5e"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_proto instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:425:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_proto",
               "generator_name": "rules_proto",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/github.com/bazelbuild/rules_proto/archive/7e4afce6fe62dbff0a4a03450143146f9f2d7488.tar.gz",
                    "https://github.com/bazelbuild/rules_proto/archive/7e4afce6fe62dbff0a4a03450143146f9f2d7488.tar.gz"
               ],
               "sha256": "8e7d59a5b12b233be5652e3d29f42fba01c7cbab09f6b3a8d0a57ed6d1e9a0da",
               "strip_prefix": "rules_proto-7e4afce6fe62dbff0a4a03450143146f9f2d7488"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/github.com/bazelbuild/rules_proto/archive/7e4afce6fe62dbff0a4a03450143146f9f2d7488.tar.gz",
                              "https://github.com/bazelbuild/rules_proto/archive/7e4afce6fe62dbff0a4a03450143146f9f2d7488.tar.gz"
                         ],
                         "sha256": "8e7d59a5b12b233be5652e3d29f42fba01c7cbab09f6b3a8d0a57ed6d1e9a0da",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_proto-7e4afce6fe62dbff0a4a03450143146f9f2d7488",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_proto"
                    },
                    "output_tree_hash": "949d4de46aa6da1c096c0c7d833e9495fa4775950870c8d844b7dba6e0e03a97"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
          "definition_information": "Repository android_gmaven_r8 instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:460:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_jar defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:530:27: in <toplevel>\n",
          "original_attributes": {
               "name": "android_gmaven_r8",
               "generator_name": "android_gmaven_r8",
               "generator_function": "maybe",
               "generator_location": None,
               "sha256": "8626ca32fb47aba7fddd2c897615e2e8ffcdb4d4b213572a2aefb3f838f01972",
               "url": "https://maven.google.com/com/android/tools/r8/3.3.28/r8-3.3.28.jar"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_jar",
                    "attributes": {
                         "sha256": "8626ca32fb47aba7fddd2c897615e2e8ffcdb4d4b213572a2aefb3f838f01972",
                         "integrity": "",
                         "canonical_id": "",
                         "url": "https://maven.google.com/com/android/tools/r8/3.3.28/r8-3.3.28.jar",
                         "urls": [],
                         "netrc": "",
                         "auth_patterns": {},
                         "downloaded_file_name": "downloaded.jar",
                         "name": "android_gmaven_r8"
                    },
                    "output_tree_hash": "18e5699d659b2f5327c36de75ad058b272bf03c0aba76c9ea268b23072cfaaca"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository android_tools instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:452:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "android_tools",
               "generator_name": "android_tools",
               "generator_function": "maybe",
               "generator_location": None,
               "url": "https://mirror.bazel.build/bazel_android_tools/android_tools_pkg-0.27.0.tar.gz",
               "sha256": "1afa4b7e13c82523c8b69e87f8d598c891ec7e2baa41d9e24e08becd723edb4d"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://mirror.bazel.build/bazel_android_tools/android_tools_pkg-0.27.0.tar.gz",
                         "urls": [],
                         "sha256": "1afa4b7e13c82523c8b69e87f8d598c891ec7e2baa41d9e24e08becd723edb4d",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "android_tools"
                    },
                    "output_tree_hash": "a09be6903a9f114110b0f0b227b3438aeb9db5f947816eff25e298a8098d7201"
               }
          ]
     },
     {
          "original_rule_class": "local_config_platform",
          "original_attributes": {
               "name": "local_config_platform"
          },
          "native": "local_config_platform(name = 'local_config_platform')"
     },
     {
          "original_rule_class": "local_repository",
          "original_attributes": {
               "name": "platforms",
               "path": "/var/tmp/_bazel_mtl/install/730b09b9d9f2bfd30b4c0a074ba23835/platforms"
          },
          "native": "local_repository(name = \"platforms\", path = __embedded_dir__ + \"/\" + \"platforms\")"
     },
     {
          "original_rule_class": "@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf",
          "definition_information": "Repository local_config_cc instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:509:13: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/cpp/cc_configure.bzl:183:16: in cc_configure\nRepository rule cc_autoconf defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/cpp/cc_configure.bzl:143:30: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_cc",
               "generator_name": "local_config_cc",
               "generator_function": "cc_configure",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf",
                    "attributes": {
                         "name": "local_config_cc",
                         "generator_name": "local_config_cc",
                         "generator_function": "cc_configure",
                         "generator_location": None
                    },
                    "output_tree_hash": "bdf770e47c6afbf1c2f6cc356cc38ac6861bdfba527cc6c7ba5b150b53cc1f04"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf_toolchains",
          "definition_information": "Repository local_config_cc_toolchains instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:509:13: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/cpp/cc_configure.bzl:182:27: in cc_configure\nRepository rule cc_autoconf_toolchains defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/cpp/cc_configure.bzl:77:41: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_cc_toolchains",
               "generator_name": "local_config_cc_toolchains",
               "generator_function": "cc_configure",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/cpp:cc_configure.bzl%cc_autoconf_toolchains",
                    "attributes": {
                         "name": "local_config_cc_toolchains",
                         "generator_name": "local_config_cc_toolchains",
                         "generator_function": "cc_configure",
                         "generator_location": None
                    },
                    "output_tree_hash": "b05d8a0101f0e1512043c05f894fd15e91f3e215f83d77704ff85f484562595a"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/osx:xcode_configure.bzl%xcode_autoconf",
          "definition_information": "Repository local_config_xcode instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:512:16: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/osx/xcode_configure.bzl:293:19: in xcode_configure\nRepository rule xcode_autoconf defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/osx/xcode_configure.bzl:282:33: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_xcode",
               "generator_name": "local_config_xcode",
               "generator_function": "xcode_configure",
               "generator_location": None,
               "xcode_locator": "@bazel_tools//tools/osx:xcode_locator.m"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/osx:xcode_configure.bzl%xcode_autoconf",
                    "attributes": {
                         "name": "local_config_xcode",
                         "generator_name": "local_config_xcode",
                         "generator_function": "xcode_configure",
                         "generator_location": None,
                         "xcode_locator": "@bazel_tools//tools/osx:xcode_locator.m"
                    },
                    "output_tree_hash": "44775ff7711abb96b4e6294d26ce9a2218d6613992a7324d67b03d5cc4484b2c"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/sh:sh_configure.bzl%sh_config",
          "definition_information": "Repository local_config_sh instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:515:13: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/sh/sh_configure.bzl:83:14: in sh_configure\nRepository rule sh_config defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/sh/sh_configure.bzl:72:28: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_sh",
               "generator_name": "local_config_sh",
               "generator_function": "sh_configure",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/sh:sh_configure.bzl%sh_config",
                    "attributes": {
                         "name": "local_config_sh",
                         "generator_name": "local_config_sh",
                         "generator_function": "sh_configure",
                         "generator_location": None
                    },
                    "output_tree_hash": "e36855460b514225eac75f4abe2cb992c5455b7077a9028d213d269d11490744"
               }
          ]
     },
     {
          "original_rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_license instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:519:6: in <toplevel>\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/utils.bzl:233:18: in maybe\nRepository rule http_archive defined at:\n  /private/var/tmp/_bazel_mtl/52e62a7b7d4b09bf466f60e23d604bb7/external/bazel_tools/tools/build_defs/repo/http.bzl:372:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_license",
               "generator_name": "rules_license",
               "generator_function": "maybe",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/github.com/bazelbuild/rules_license/releases/download/0.0.3/rules_license-0.0.3.tar.gz",
                    "https://github.com/bazelbuild/rules_license/releases/download/0.0.3/rules_license-0.0.3.tar.gz"
               ],
               "sha256": "00ccc0df21312c127ac4b12880ab0f9a26c1cff99442dc6c5a331750360de3c3"
          },
          "repositories": [
               {
                    "rule_class": "@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/github.com/bazelbuild/rules_license/releases/download/0.0.3/rules_license-0.0.3.tar.gz",
                              "https://github.com/bazelbuild/rules_license/releases/download/0.0.3/rules_license-0.0.3.tar.gz"
                         ],
                         "sha256": "00ccc0df21312c127ac4b12880ab0f9a26c1cff99442dc6c5a331750360de3c3",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_license"
                    },
                    "output_tree_hash": "5dd374b45b4d89eef1fa4b5a00de823fa9666f84e7466c1714cea49102e2f1cd"
               }
          ]
     },
     {
          "original_rule_class": "register_toolchains",
          "original_attributes": {
               "name": "//external/register_toolchains",
               "*args": [
                    "@bazel_pandoc//:pandoc_toolchain_linux-x86_64",
                    "@bazel_pandoc//:pandoc_toolchain_macOS",
                    "@bazel_pandoc//:pandoc_toolchain_osx-arm",
                    "@local_jdk//:runtime_toolchain_definition",
                    "@remotejdk11_linux_toolchain_config_repo//:toolchain",
                    "@remotejdk11_linux_aarch64_toolchain_config_repo//:toolchain",
                    "@remotejdk11_linux_ppc64le_toolchain_config_repo//:toolchain",
                    "@remotejdk11_linux_s390x_toolchain_config_repo//:toolchain",
                    "@remotejdk11_macos_toolchain_config_repo//:toolchain",
                    "@remotejdk11_macos_aarch64_toolchain_config_repo//:toolchain",
                    "@remotejdk11_win_toolchain_config_repo//:toolchain",
                    "@remotejdk11_win_arm64_toolchain_config_repo//:toolchain",
                    "@remotejdk17_linux_toolchain_config_repo//:toolchain",
                    "@remotejdk17_linux_aarch64_toolchain_config_repo//:toolchain",
                    "@remotejdk17_macos_toolchain_config_repo//:toolchain",
                    "@remotejdk17_macos_aarch64_toolchain_config_repo//:toolchain",
                    "@remotejdk17_win_toolchain_config_repo//:toolchain",
                    "@remotejdk17_win_arm64_toolchain_config_repo//:toolchain",
                    "@remotejdk18_linux_toolchain_config_repo//:toolchain",
                    "@remotejdk18_linux_aarch64_toolchain_config_repo//:toolchain",
                    "@remotejdk18_macos_toolchain_config_repo//:toolchain",
                    "@remotejdk18_macos_aarch64_toolchain_config_repo//:toolchain",
                    "@remotejdk18_win_toolchain_config_repo//:toolchain",
                    "@remotejdk18_win_arm64_toolchain_config_repo//:toolchain",
                    "@bazel_tools//tools/jdk:all",
                    "@bazel_tools//tools/python:autodetecting_toolchain",
                    "@local_config_cc_toolchains//:all",
                    "@local_config_sh//:local_sh_toolchain"
               ]
          },
          "native": "register_toolchains(\"@bazel_pandoc//:pandoc_toolchain_linux-x86_64\", \"@bazel_pandoc//:pandoc_toolchain_macOS\", \"@bazel_pandoc//:pandoc_toolchain_osx-arm\", \"@local_jdk//:runtime_toolchain_definition\", \"@remotejdk11_linux_toolchain_config_repo//:toolchain\", \"@remotejdk11_linux_aarch64_toolchain_config_repo//:toolchain\", \"@remotejdk11_linux_ppc64le_toolchain_config_repo//:toolchain\", \"@remotejdk11_linux_s390x_toolchain_config_repo//:toolchain\", \"@remotejdk11_macos_toolchain_config_repo//:toolchain\", \"@remotejdk11_macos_aarch64_toolchain_config_repo//:toolchain\", \"@remotejdk11_win_toolchain_config_repo//:toolchain\", \"@remotejdk11_win_arm64_toolchain_config_repo//:toolchain\", \"@remotejdk17_linux_toolchain_config_repo//:toolchain\", \"@remotejdk17_linux_aarch64_toolchain_config_repo//:toolchain\", \"@remotejdk17_macos_toolchain_config_repo//:toolchain\", \"@remotejdk17_macos_aarch64_toolchain_config_repo//:toolchain\", \"@remotejdk17_win_toolchain_config_repo//:toolchain\", \"@remotejdk17_win_arm64_toolchain_config_repo//:toolchain\", \"@remotejdk18_linux_toolchain_config_repo//:toolchain\", \"@remotejdk18_linux_aarch64_toolchain_config_repo//:toolchain\", \"@remotejdk18_macos_toolchain_config_repo//:toolchain\", \"@remotejdk18_macos_aarch64_toolchain_config_repo//:toolchain\", \"@remotejdk18_win_toolchain_config_repo//:toolchain\", \"@remotejdk18_win_arm64_toolchain_config_repo//:toolchain\", \"@bazel_tools//tools/jdk:all\", \"@bazel_tools//tools/python:autodetecting_toolchain\", \"@local_config_cc_toolchains//:all\", \"@local_config_sh//:local_sh_toolchain\")"
     },
     {
          "original_rule_class": "register_execution_platforms",
          "original_attributes": {
               "name": "//external/register_execution_platforms",
               "*args": []
          },
          "native": "register_execution_platforms()"
     }
]