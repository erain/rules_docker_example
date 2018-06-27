load("@io_bazel_rules_go//go:def.bzl", "go_binary", "go_library")
load("@io_bazel_rules_docker//go:image.bzl", "go_image")
load("@io_bazel_rules_docker//docker:docker.bzl", "docker_push")

go_library(
    name = "go_default_library",
    srcs = ["main.go"],
    importpath = "github.com/example/platform/src/app",
    visibility = ["//visibility:private"],
    deps = ["//app/library:go_default_library"],
)

go_binary(
    name = "app",
    embed = [":go_default_library"],
    visibility = ["//visibility:public"],
    x_defs = {
        "github.com/example/platform/src/app/internal/helper.version": "{VERSION}",
    },
)

go_image(
    name = "app_image",
    binary = ":app",
    embed = [":go_default_library"],
    goarch = "amd64",
    goos = "linux",
    visibility = ["//visibility:public"],
)

docker_push(
    name = "push_app_image",
    image = ":app_image",
    registry = "<account-number>.dkr.ecr.us-east-1.amazonaws.com",
    repository = "app",
    stamp = True,
    tag = "{VERSION}",
)
