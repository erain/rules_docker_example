load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive", "http_file")

# Download the rules_docker repository at release v0.7.0
http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "aed1c249d4ec8f703edddf35cbe9dfaca0b5f5ea6e4cd9e83e99f3b0d1136c3d",
    strip_prefix = "rules_docker-0.7.0",
    urls = ["https://github.com/bazelbuild/rules_docker/archive/v0.7.0.tar.gz"],
)

load(
    "@io_bazel_rules_docker//repositories:repositories.bzl",
    container_repositories = "repositories",
)
container_repositories()

load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_pull",
)

# Pulling image
container_pull(
    name = "ubuntu1604",
    registry = "index.docker.io",
    repository = "library/ubuntu",
    digest = "sha256:e4a134999bea4abb4a27bc437e6118fdddfb172e1b9d683129b74d254af51675",
)

# Pulling image
container_pull(
    name = "go-alpine",
    registry = "index.docker.io",
    repository = "library/golang",
    tag = "alpine",
)

# cc_image
load(
    "@io_bazel_rules_docker//cc:image.bzl",
    _cc_image_repos = "repositories",
)

_cc_image_repos()


# For our go_image test.
http_archive(
    name = "io_bazel_rules_go",
    sha256 = "62ec3496a00445889a843062de9930c228b770218c735eca89c67949cd967c3f",
    url = "https://github.com/bazelbuild/rules_go/releases/download/0.16.4/rules_go-0.16.4.tar.gz",
)

load("@io_bazel_rules_go//go:def.bzl", "go_register_toolchains", "go_rules_dependencies")

go_rules_dependencies()

go_register_toolchains()

# go_image
load(
    "@io_bazel_rules_docker//go:image.bzl",
    _go_image_repos = "repositories",
)

_go_image_repos()
