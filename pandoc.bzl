PANDOC_EXTENSIONS = {
    "asciidoc": "adoc",
    "beamer": "tex",
    "commonmark": "md",
    "context": "tex",
    "docbook": "xml",
    "docbook4": "xml",
    "docbook5": "xml",
    "docx": "docx",
    "dokuwiki": "txt",
    "dzslides": "html",
    "epub": "epub",
    "epub2": "epub",
    "epub3": "epub",
    "fb2": "fb",
    "haddock": "txt",
    "html": "html",
    "html4": "html",
    "html5": "html",
    "icml": "icml",
    "jats": "xml",
    "json": "json",
    "latex": "tex",
    "man": "1",
    "markdown": "md",
    "markdown_github": "md",
    "markdown_mmd": "md",
    "markdown_phpextra": "md",
    "markdown_strict": "md",
    "mediawiki": "txt",
    "ms": "1",
    "muse": "txt",
    "native": "txt",
    "odt": "odt",
    "opendocument": "odt",
    "opml": "openml",
    "org": "txt",
    "plain": "txt",
    "pptx": "pptx",
    "revealjs": "html",
    "rst": "rst",
    "rtf": "rtf",
    "s5": "html",
    "slideous": "html",
    "slidy": "html",
    "tei": "html",
    "texinfo": "texi",
    "textile": "textile",
    "zimwiki": "txt",
}

def _pandoc_impl(ctx):
    toolchain = ctx.toolchains["@bazel_pandoc//:pandoc_toolchain_type"]
    cli_args = []
    cli_args.extend(ctx.attr.options)
    if ctx.attr.from_format:
        cli_args.extend(["--from", ctx.attr.from_format])
    if ctx.attr.to_format:
        cli_args.extend(["--to", ctx.attr.to_format])
    if ctx.attr.defaults_file:
        cli_args.extend(["--defaults", ctx.file.defaults_file.path])
    cli_args.extend(["-o", ctx.outputs.output.path])
    cli_args.extend(["--data-dir", "handbook"])

    files = []
    files.extend(ctx.files.srcs)
    files.append(ctx.file.defaults_file)
    ctx.actions.run(
        mnemonic = "Pandoc",
        executable = toolchain.pandoc.files.to_list()[0].path,
        arguments = cli_args,
        inputs = depset(
            direct = files,
            transitive = [toolchain.pandoc.files],
        ),
        outputs = [ctx.outputs.output],
        progress_message = "Running: %s" % cli_args,
    )

_pandoc = rule(
    attrs = {
        "from_format": attr.string(),
        "options": attr.string_list(),
        "srcs": attr.label_list(mandatory = True, allow_files = True),
        "to_format": attr.string(),
        "output": attr.output(mandatory = True),
        "defaults_file": attr.label(allow_single_file = True),
    },
    toolchains = ["@bazel_pandoc//:pandoc_toolchain_type"],
    implementation = _pandoc_impl,
)

def pandoc(**kwargs):
    _pandoc(**kwargs)
