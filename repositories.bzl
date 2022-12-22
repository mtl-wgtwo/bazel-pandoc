load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

PANDOC_VERSION = "2.19.2"

BUILD_CONTENT_UNIX = """
filegroup(
    name = "pandoc",
    srcs = ["bin/pandoc"],
    visibility = ["//visibility:public"],
)"""

BUILD_CONTENT_WINDOWS = """
filegroup(
    name = "pandoc",
    srcs = ["pandoc.exe"],
    visibility = ["//visibility:public"],
)"""

def pandoc_repositories():
    http_archive(
        name = "pandoc_bin_linux-x86_64",
        build_file_content = BUILD_CONTENT_UNIX,
        sha256 = "9d55c7afb6a244e8a615451ed9cb02e6a6f187ad4d169c6d5a123fa74adb4830",
        strip_prefix = "pandoc-{v}".format(v = PANDOC_VERSION),
        url = "https://github.com/jgm/pandoc/releases/download/{v}/pandoc-{v}-linux-amd64.tar.gz".format(v = PANDOC_VERSION),
    )

    http_archive(
        name = "pandoc_bin_macOS",
        build_file_content = BUILD_CONTENT_UNIX,
        sha256 = "af0cda69e31e42f01ba6adc0aa779d3e5853e6c092beeb420a4fc22712d2110b",
        strip_prefix = "pandoc-{v}".format(v = PANDOC_VERSION),
        url = "https://github.com/jgm/pandoc/releases/download/{v}/pandoc-{v}-macOS.zip".format(v = PANDOC_VERSION),
    )

    http_archive(
        name = "pandoc_bin_osx-arm",
        build_file_content = BUILD_CONTENT_UNIX,
        sha256 = "9da7061f84eb09a4f21a50844bd89c74dea9c00c3c8923612e0124795c626b80",
        strip_prefix = "pandoc-{v}".format(v = PANDOC_VERSION),
        url = "https://github.com/mtl-wgtwo/bazel-pandoc/releases/download/pandoc-{v}/pandoc-{v}-osx-arm.zip".format(v = PANDOC_VERSION),
    )

    native.register_toolchains(
        "@bazel_pandoc//:pandoc_toolchain_linux-x86_64",
        "@bazel_pandoc//:pandoc_toolchain_macOS",
        "@bazel_pandoc//:pandoc_toolchain_osx-arm",
    )
