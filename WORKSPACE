load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "96424f67fbdb44e804c024c489f69980ef91cc1320367c66eafae4c030d75fe0",
    strip_prefix = "rules_docker-7401cb256222615c497c0dee5a4de5724a4f4cc7",
    urls = ["https://github.com/bazelbuild/rules_docker/archive/7401cb256222615c497c0dee5a4de5724a4f4cc7.tar.gz"],
)

load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_pull",
    container_repositories = "repositories",
)

# This is NOT needed when going through the language lang_image
# "repositories" function(s).
container_repositories()

# Pulling image
container_pull(
    name = "ubuntu16_04",
    digest = "sha256:c81e8f6bcbab8818fdbe2df6d367990ab55d85b4dab300931a53ba5d082f4296",
    registry = "gcr.io",
    repository = "cloud-marketplace/google/ubuntu16_04",
)

# Rules Protobuf
git_repository(
    name = "org_pubref_rules_protobuf",
    remote = "https://github.com/pubref/rules_protobuf.git",
    tag = "v0.8.2",
)

load("@org_pubref_rules_protobuf//python:rules.bzl", "py_proto_repositories")

py_proto_repositories()

# Rules Python
git_repository(
    name = "io_bazel_rules_python",
    commit = "8b5d0683a7d878b28fffe464779c8a53659fc645",
    remote = "https://github.com/bazelbuild/rules_python.git",
)

load("@io_bazel_rules_python//python:pip.bzl", "pip_import", "pip_repositories")

pip_repositories()

# Import for py grpc examples
pip_import(
    name = "examples_grpc",
    requirements = "//hello_grpc/py:requirements.txt",
)

load(
    "@examples_grpc//:requirements.bzl",
    _grpc_install = "pip_install",
)

_grpc_install()

# Rules Go
http_archive(
    name = "io_bazel_rules_go",
    sha256 = "1868ff68d6079e31b2f09b828b58d62e57ca8e9636edff699247c9108518570b",
    urls = ["https://github.com/bazelbuild/rules_go/releases/download/0.11.1/rules_go-0.11.1.tar.gz"],
)

http_archive(
    name = "bazel_gazelle",
    sha256 = "92a3c59734dad2ef85dc731dbcb2bc23c4568cded79d4b87ebccd787eb89e8d0",
    urls = ["https://github.com/bazelbuild/bazel-gazelle/releases/download/0.11.0/bazel-gazelle-0.11.0.tar.gz"],
)

load("@io_bazel_rules_go//go:def.bzl", "go_register_toolchains", "go_rules_dependencies")

go_rules_dependencies()

go_register_toolchains()

load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies")

gazelle_dependencies()

# Golang Binary
http_file(
    name = "golang_release",
    sha256 = "b5a64335f1490277b585832d1f6c7f8c6c11206cba5cd3f771dcb87b98ad1a33",
    urls = ["https://storage.googleapis.com/golang/go1.10.linux-amd64.tar.gz"],
)

# cc_image
load(
    "@io_bazel_rules_docker//cc:image.bzl",
    _cc_image_repos = "repositories",
)

_cc_image_repos()

# go_image
load(
    "@io_bazel_rules_docker//go:image.bzl",
    _go_image_repos = "repositories",
)

_go_image_repos()
