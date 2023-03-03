load("//:repositories.bzl", "pandoc_repositories")

# -- load statements -- #

def _non_module_deps_impl(ctx = None):
    pandoc_repositories()

# -- repo definitions -- #

non_module_deps = module_extension(implementation = _non_module_deps_impl)
