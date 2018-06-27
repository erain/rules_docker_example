package(default_visibility = ["//visibility:public"])

licenses(["notice"])  # Apache 2.0

load("@examples_grpc//:requirements.bzl", "requirement")
load("@io_bazel_rules_docker//python:image.bzl", "py_image")

py_binary(
    name = "server",
    srcs = [
        "server.py",
    ],
    deps = [
        requirement("grpcio"),
        "//hello_grpc/proto:py",
    ],
)
